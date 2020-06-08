import os
import sys
import base64
import mysql.connector as mySQL

from mysql.connector import errorcode
from flask import Flask, flash, request, redirect, render_template, session
from validate_email import validate_email
from time import time, ctime

# <- assigning default credentials

credentials	= {}

credentials['host']	= '127.0.0.1'
credentials['user']	= 'root'
credentials['pass']	= 'password'
credentials['DB']	= 'Matcha'

sys.path.insert(0, './incs')

from userAuth import db_connect, userSignUp, userSignIn, goneSince

# from simplecrypt import encrypt, decrypt
# from binascii import hexlify, unhexlify

# from Retrieve import sendEmail
# from displayUsers import Home, showUsers, unlike
# from handleChange import handleUserInfoChange, showBlocked
# from ShowMsgsBtwn import MsgsBtwn
# from Notifs import Notifs, notifList
# from Search import unsearchedUsers


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and \
	filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

WebApp = Flask(__name__)

@WebApp.route('/')

def index():
	if not session.get('loggedIn'):
		return render_template(
			'loginForm.html'
		)
	else:
		return render_template(
			'dashBoard.html'
			# Home = Home(),
			# Notifs = Notifs(),
			# cards = showUsers([])
		)

@WebApp.route('/login', methods = ['POST'])

def login():
	POST_USERNAME = str(request.form['username'])
	POST_PASSWORD = str(request.form['password'])

	return userSignIn(POST_USERNAME, POST_PASSWORD)

@WebApp.route('/logout')

def logout():

	if session.get('loggedIn'):

		localtime = 'gone since ' + ctime(time())

		goneSince(session.get('loggedIn'), localtime)

		session['userName'] = None
		session['loggedIn'] = False

		return index()
	else:
		return index()

#--- Password Retrieving Mechanism ;

# @WebApp.route('/passRetrieveForm')

# def passRetrieveFrom():
# 	return render_template('Retrieve.html')

# @WebApp.route('/passRetrieve', methods = ['POST'])

# def passRetrieve():
# 	POST_USERNAME = str(request.form['username'])
# 	if POST_USERNAME == "":
# 		print("\nfailed to get the userName; type it in the form\n")
# 	else:
# 		for hashName in r.keys("0*"):
# 			userName = r.hget(hashName, "userName")
# 			if userName == POST_USERNAME:
# 				break
# 		if userName <> POST_USERNAME:
# 			print("\nuserName \'\033[1m%s\033[0m\'" % POST_USERNAME, end = " ")
# 			print("isn't registered\n")
# 			flash('userName isn\'t registered')
# 			return index()
# 		else:
# 			e_mail = r.hget(hashName, 'e_mail')
# 			sendEmail(hashName, r.hget(hashName, "realName"), e_mail)
# 			print("\nan email was sent to %s\n" % e_mail)
# 	return index()

# @WebApp.route('/newPasswordForm_<y>')

# def newPasswordForm(y):
# 	return render_template(
# 		'newPasswordForm.html',
# 		y = y,
# 		realName = r.hget(y, "raelName")
# 	)

# @WebApp.route('/newPasswordSet_<y>', methods = ['POST'])

# def newPasswordSet(y):
# 	POST_PASSWORD = str(request.form['password'])
# 	POST_CONFRIM = str(request.form['confirm'])
# 	if POST_PASSWORD == "" or POST_CONFRIM == "":
# 		print("\nfailed to get the password; type it in the form\n")
# 	else:
# 		if POST_PASSWORD <> POST_CONFRIM:
# 			print("failed to change the password; unconfirmed password")
# 			return index()
# 		else:
# 			# password check
# 			password = POST_PASSWORD

# 			upperCFlag = False
# 			lowerCFlag = False
# 			numberFlag = False
# 			for i in password:
# 				if i.isalpha():
# 					if i.isupper():
# 						upperCFlag = True
# 					elif i.islower():
# 						lowerCFlag = True
# 				elif i.isdigit():
# 					numberFlag = True
# 			if upperCFlag is False:
# 				# flash('your password needs to have at least on capital latter')
# 				print("failed to sign up; password missing capital latter(s)")
# 			if lowerCFlag is False:
# 				# flash('your password needs to have at least on small latter')
# 				print("failed to sign up; password missing small latter(s)")
# 			if numberFlag is False:
# 				# flash('your password needs to have at least on number')
# 				print("failed to sign up; password missing number(s)")
# 			if upperCFlag is False or lowerCFlag is False or numberFlag is False:
# 				return index()
# 			if len(password) < 8:
# 				print("failed to sign up; password is too short")
# 				return index()
# 			encrypted = hexlify(encrypt(r.hget(y, 'userName')[::-1], password))
# 			r.hset(y, 'password', encrypted)
# 			print("changed password successfully")
# 	return index()

# @WebApp.route('/passResetFrom')

# def passResetFrom():
# 	return render_template('passResetFrom.html')

# @WebApp.route('/passReset', methods = ['POST'])

# def passReset():
# 	return index()

# #--- User Info Changing Mechanism ;

# @WebApp.route('/profile')

# def userProfile():
# 	userInfo = r.hgetall(session['userIdNo'])
# 	return render_template(
# 		'userProfile.html',
# 		Home = Home(),
# 		Notifs = Notifs(),
# 		userName = userInfo['userName'],
# 		realName = userInfo['realName'],
# 		e_mail = userInfo['e_mail'],
# 		pYDL = showBlocked()
# 	)

# @WebApp.route('/infoChange', methods = ['GET', 'POST'])

# def infoChange():
# 	POST_USERNAME = str(request.form['username'])
# 	# ---
# 	if request.method == 'POST':
# 		gender = request.form.getlist('gender')
# 		if len(gender) is 1:
# 			POST_GENDER = '0'
# 		else:
# 			POST_GENDER = '1'
# 	# ---
# 	POST_REALNAME = str(request.form['realname'])
# 	# ---
# 	POST_E_MAIL = str(request.form['e_mail'])
# 	# ---
# 	POST_PASSWORD = str(request.form['password'])
# 	POST_CONFIRM = str(request.form['confirm'])
# 	# ---
# 	Biography = str(request.form['biography'])
# 	Interests = str(request.form['interests'])
# 	# ---
# 	POST_SEXUALITY = str(request.form['sexuality'])
# 	# ---
# 	handleUserInfoChange(
# 		POST_USERNAME,
# 		POST_GENDER,
# 		POST_REALNAME,
# 		POST_E_MAIL,
# 		POST_PASSWORD,
# 		POST_CONFIRM,
# 		Biography,
# 		Interests,
# 		POST_SEXUALITY
# 	)

# 	if request.method == 'POST':
# 		if 'file' not in request.files:
# 			flash('No picture chosen')
# 			print('No picture chosen')
# 		else:
# 			file = request.files['file']
# 			if file.filename == '':
# 				flash('No file selected for uploading')
# 				print('No file selected for uploading')
# 			elif file and allowed_file(file.filename):
# 				inputStr = base64.b64encode(file.read())
# 				r.hset(session['userIdNo'], 'pic1', inputStr)
# 				flash('Picture successfully uploaded')
# 				print('Picture successfully uploaded')
# 			else:
# 				flash('Not a valied format')
# 				print('Not a valied format')
# 	return index()

# @WebApp.route('/deleteUserRoute')

# def deleteUserRoute():
# 	return render_template('deleteUser.html')

# @WebApp.route('/deleteUser')

# def deleteUser():
# 	r.delete(session['userIdNo'])
# 	print("User No. [\033[1m", end = " ")
# 	print(session['userIdNo'], end = " ")
# 	print("\033[0m] just deleted their account")
# 	session['userIdNo'] = None
# 	session['loggedIn'] = False
# 	return index()

# @WebApp.route('/<x>LikesNo<y>')

# def xLikesNoY(x, y):
# 	likes = r.hget(x, 'likes')
# 	if likes is None:
# 		likes = ''
# 	likesArray = likes.split()
# 	for i in likesArray:
# 		if i == y:
# 			unlike(x, y, likesArray)
# 			return index()
# 	# else ;
# 	likes += ' %s' % y
# 	r.hset(x, 'likes', likes)
# 	#---
# 	r.hset(
# 		y,
# 		'fameR',
# 		int(
# 			r.hget(
# 				y,
# 				'fameR'
# 			)
# 		) + 1
# 	)
# 	r.hset(
# 		'notifsOf%s' % y,
# 		str(time()),
# 		'(l)[%s] %s liked you' % (
# 			ctime(time()),
# 			session['userIdNo'],
# 		)
# 	)
# 	#---
# 	return index()

# @WebApp.route('/blockUserNo<y>')

# def blockUserNo(y):
# 	return render_template(
# 		'blockingForm.html',
# 		x = session['userIdNo'],
# 		y = y,
# 		N = r.hget(y, 'realName')
# 	)

# @WebApp.route('/<x>HatesNo<y>', methods = ['POST'])

# def xHatesNoY(x, y):
# 	POST_REASON = str(request.form['why'])
# 	if POST_REASON == '':
# 		POST_REASON = '#NoReason'

# 	hates = r.hget(x, 'hates')
# 	if hates is None:
# 		hates = ''
# 	hates += '_+_%s_Y_%s' % (y, POST_REASON)
# 	r.hset(x, 'hates', hates)
# 	return index()

# @WebApp.route('/unblockUserNo<y>')

# def unblockUserNo(y):
# 	x = session['userIdNo']

# 	hates = r.hget(x, 'hates')
# 	if hates is None:
# 		return index()
# 	hates = hates.split('_+_')
# 	for i in hates : hates.remove(i) if '%s_Y_' % y in i else 0
# 	h, j = '', 1
# 	while j < len(hates):
# 		h += '_+_' + hates[j]
# 		j += 1
# 	r.hset(x, 'hates', h)
# 	return index()

# #--- Chat & Notifications Mechanisms ;

# @WebApp.route('/notifs')

# def notifListRoute():
# 	return render_template(
# 		'notifList.html',
# 		Home = Home(),
# 		Notifs = Notifs(),
# 		notifList = notifList()
# 	)

# @WebApp.route('/<x>chatingTo<y>')

# def xChatingToY(x, y):
# 	return render_template(
# 		'xChatingToY.html',
# 		Home = Home(),
# 		Notifs = Notifs(),
# 		Msgs = MsgsBtwn(x, y),
# 		y = y
# 	)

# @WebApp.route('/sendMsgTo<y>', methods = ['POST'])

# def sendMsgToY(y):
# 	POST_MESSAGE = str(request.form['yourMsg'])

# 	r.hset(
# 		'%s_to_%s' % (
# 			session['userIdNo'],
# 			y
# 		),
# 		str(time()),
# 		session['userIdNo'] + '_|_' + POST_MESSAGE
# 	)

# 	r.hset(
# 		'notifsOf%s' % y,
# 		str(time()),
# 		'(m)[%s] %s sent you a message: %s' % (
# 			ctime(time()),
# 			session['userIdNo'],
# 			POST_MESSAGE[0:24]
# 		)
# 	)

# 	return redirect(
# 		'/%schatingTo%s' % (
# 			session['userIdNo'],
# 			y
# 		)
# 	)

# #--- New User Registration Mechanism ;

@WebApp.route('/nwusrForm/<e>')

def nwusrForm(e):
	errMsg = ""

	if e:
		if int(e) is 1:
			errMsg = "input is incomplete / invalid"
			flash(errMsg, "warning")

		elif int(e) is 2:
			errMsg = "username is already used"
			flash(errMsg, "warning")

		elif int(e) is 3:
			errMsg = "mySQL failure..."
			flash(errMsg, "warning")

		elif int(e) is 4:
			errMsg = "unconfirmed password"
			flash(errMsg, "warning")

		elif int(e) is 5:
			errMsg = "email isn't valid"
			flash(errMsg, "warning")

		elif int(e) is 9:
			# errMsg = "invalid password"
			# flash(errMsg, "warning")
			pass

	return render_template('nwusrForm.html', e = errMsg)

@WebApp.route('/signup', methods = ['POST'])

def signup():
	POST_USERNAME = str(request.form['username'])
	POST_REALNAME = str(request.form['realname'])
	POST_PASSWORD = str(request.form['password'])
	POST_REPEAT = str(request.form['repeat'])
	POST_E_MAIL = str(request.form['e_mail'])

	POST_SEXUALITY = str(request.form['sexuality'])

	if not (POST_USERNAME
	   and POST_REALNAME
	   and POST_PASSWORD
	   and POST_REPEAT
	   and POST_E_MAIL
	   and POST_SEXUALITY):

		return redirect('/nwusrForm/01')

	elif POST_USERNAME == "":

		return redirect('/nwusrForm/01')

	cnx, cursor = db_connect(credentials)

	# return str((cnx, cursor))

	if (cnx and cursor):

		q = """
				SELECT *
				FROM `users`
				WHERE username = '{}'
			""".format(
				str(POST_USERNAME)
			)

		try:

			cursor.execute(q)

			if len(cursor.fetchall()) != 0:

				return redirect('/nwusrForm/02')

			cnx.close()

		except mySQL.Error as e:

			print(e)

			cnx.close()

			return redirect('/nwusrForm/03')

	else:

		return redirect('/nwusrForm/03')

	# ---
	if POST_PASSWORD != POST_REPEAT:

		return redirect('/nwusrForm/04')
	# ---

	if not validate_email(POST_E_MAIL):

		return redirect('/nwusrForm/05')
	# ---
	if request.method == 'POST':
		gender = request.form.getlist('gender')
		if len(gender) is 1:
			POST_GENDER = '0'
		else:
			POST_GENDER = '1'
	# ---

	return userSignUp(
		POST_USERNAME,
		POST_REALNAME,
		POST_PASSWORD,
		POST_E_MAIL,
		POST_GENDER,
		POST_SEXUALITY
	)

# @WebApp.route('/verify<y>')

# def verify(y):
# 	crntStatus = r.hget(y, 'active')
# 	if crntStatus is None:
# 		print("failed to verify; user doesn't exist")
# 		return index()
# 	elif crntStatus == '1':
# 		print("failed to verify; user is already verified")
# 		return index()
# 	elif crntStatus == '0':
# 		r.hset(y, 'active', 1)
# 		print("verification of %s is successful" % y)
# 		return index()
# 	else:
# 		print("failed to verify; check your Redis connection")
# 		return index()

# #--- Search / Filter Mechanism ;

# @WebApp.route('/search', methods = ['POST'])

# def search():
# 	POST_SEARCH = str(request.form['searchTxt'])
# 	usersToLeave = unsearchedUsers(POST_SEARCH)
# 	return render_template(
# 		'dashBoard.html',
# 		Home = Home(),
# 		Notifs = Notifs(),
# 		cards = showUsers(usersToLeave)
# 	)

#--- MainFn

if __name__ == '__main__':
	WebApp.secret_key = os.urandom(12)
	WebApp.run(host = '0.0.0.0', port = 4000, debug = True)
