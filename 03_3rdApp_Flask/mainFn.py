from flask import Flask, flash, redirect, render_template, request, session, abort

import os
import redis
import sys

sys.path.insert(0, './incs')

from simplecrypt import encrypt, decrypt
from binascii import hexlify, unhexlify
from signUp import userSignUp
from Retrieve import sendEmail
from displayUsers import showUsers, unlike
from handleChange import handleUserInfoChange

r = redis.Redis()

WebApp = Flask(__name__)

@WebApp.route('/')

def index():
	if not session.get('loggedIn'):
		return render_template('loginForm.html')
	else:
		return render_template('dashBoard.html', cards = showUsers())

@WebApp.route('/login', methods=['POST'])

def login():
	POST_USERNAME = str(request.form['username'])
	POST_PASSWORD = str(request.form['password'])

	for hashName in r.keys("0*"):
		userName = r.hget(hashName, "userName")
		if userName == POST_USERNAME:
			break
	if userName <> POST_USERNAME:
		print "\nuserName \'\033[1m%s\033[0m\'" % POST_USERNAME,
		print "isn't registered\n"
		flash('userName isn\'t registered')
		return index()
	passWord = r.hget(hashName, "password")
	decrypted = decrypt(POST_USERNAME[::-1], unhexlify(passWord))
	if decrypted == POST_PASSWORD:
		if int(r.hget(hashName, "active")) is 1:
			session['loggedIn'] = True
			session['userIdNo'] = hashName
			print "User No. [\033[1m",
			print session['userIdNo'],
			print "\033[0m] just logged in"
		else:
			print "User No. [\033[1m",
			print hashName,
			print "\033[0m] failed to log in; account isn't activated yet."
			flash('not activated yet!')
	else:
		print "User No. [\033[1m",
		print hashName,
		print "\033[0m] failed to log in; wrong password."
		flash('wrong password!')
	return index()

@WebApp.route('/logout')

def logout():
	if session['userIdNo'] is not None:
		print "User No. [\033[1m",
		print session['userIdNo'],
		print "\033[0m] just logged out"
		session['userIdNo'] = None
		session['loggedIn'] = False
		return index()
	else:
		return index()

#--- Password Retrieving Mechanism ;

@WebApp.route('/passRetrieveForm')

def passRetrieveFrom():
	return render_template('Retrieve.html')

@WebApp.route('/passRetrieve', methods=['POST'])

def passRetrieve():
	POST_USERNAME = str(request.form['username'])
	if POST_USERNAME == "":
		print "\nfailed to get the userName; type it in the form\n"
	else:
		for hashName in r.keys("0*"):
			userName = r.hget(hashName, "userName")
			if userName == POST_USERNAME:
				break
		if userName <> POST_USERNAME:
			print "\nuserName \'\033[1m%s\033[0m\'" % POST_USERNAME,
			print "isn't registered\n"
			flash('userName isn\'t registered')
			return index()
		else:
			e_mail = r.hget(hashName, 'e_mail')
			sendEmail(hashName, e_mail)
			print "\nan email was sent to %s\n" % e_mail
	return index()

@WebApp.route('/passResetFrom')

def passResetFrom():
	return render_template('passResetFrom.html')

@WebApp.route('/passReset', methods=['POST'])

def passReset():
	return index()

#--- User Info Changing Mechanism ;

@WebApp.route('/profile')

def userProfile():
	userInfo = r.hgetall(session['userIdNo'])
	return render_template(
		'userProfile.html',
		userName=userInfo['userName'],
		realName=userInfo['realName'],
		e_mail=userInfo['e_mail']
	)

@WebApp.route('/infoChange', methods=['POST'])

def infoChange():
	POST_USERNAME = str(request.form['username'])
	# ---
	if request.method == 'POST':
		gender = request.form.getlist('gender')
		if len(gender) is 1:
			POST_GENDER = '0'
		else:
			POST_GENDER = '1'
	# ---
	POST_REALNAME = str(request.form['realname'])
	# ---
	POST_E_MAIL = str(request.form['e_mail'])
	# ---
	POST_PASSWORD = str(request.form['password'])
	POST_CONFIRM = str(request.form['confirm'])
	# ---
	Biography = str(request.form['biography'])
	Interests = str(request.form['interests'])
	# ---
	POST_SEXUALITY = str(request.form['sexuality'])
	# ---
	handleUserInfoChange(
		POST_USERNAME,
		POST_GENDER,
		POST_REALNAME,
		POST_E_MAIL,
		POST_PASSWORD,
		POST_CONFIRM,
		Biography,
		Interests,
		POST_SEXUALITY
	)
	return index()

@WebApp.route('/deleteUserRoute')

def deleteUserRoute():
	return render_template('deleteUser.html')

@WebApp.route('/deleteUser')

def deleteUser():
	r.delete(session['userIdNo'])
	print "User No. [\033[1m",
	print session['userIdNo'],
	print "\033[0m] just deleted their account"
	session['userIdNo'] = None
	session['loggedIn'] = False
	return index()

@WebApp.route('/<x>LikesNo<y>')

def xLikesNoY(x, y):
	likes = r.hget(x, 'likes')
	if likes is None:
		likes = ''
	likesArray = likes.split()
	for i in likesArray:
		if i == y:
			unlike(x, y, likesArray)
			return index()
	# else ;
	likes += ' %s' % y
	r.hset(session['userIdNo'], 'likes', likes)
	#---
	r.hset(
		y,
		'fameR',
		int(
			r.hget(
				y,
				'fameR'
			)
		) + 1
	)
	#---
	return index()

@WebApp.route('/<x>HatesNo<y>')

def xHatesNoY(x, y): # <- the fake thing is just going to be a part of 'why-blocked-them' string
	return index()

#--- New User Registration Mechanism ;

@WebApp.route('/nwusrForm')

def nwusrForm():
	return render_template('nwusrForm.html')

@WebApp.route('/signup', methods=['POST'])

def signup():
	POST_USERNAME = str(request.form['username'])
	POST_REALNAME = str(request.form['realname'])
	POST_PASSWORD = str(request.form['password'])
	POST_REPEAT = str(request.form['repeat'])
	# ---
	if POST_PASSWORD <> POST_REPEAT:
		flash('unconfirmed password!')
		print "failed to sign up; unconfirmed password"
		return index()
	# ---
	POST_E_MAIL = str(request.form['e_mail'])
	# ---
	if request.method == 'POST':
		gender = request.form.getlist('gender')
		if len(gender) is 1:
			POST_GENDER = '0'
		else:
			POST_GENDER = '1'
	# ---
	POST_SEXUALITY = str(request.form['sexuality'])

	Biography = '' 
	userSignUp(POST_USERNAME,
		POST_REALNAME,
		POST_PASSWORD,
		POST_E_MAIL,
		POST_GENDER,
		POST_SEXUALITY,
		Biography
	)
	return index()

#--- MainFn

if __name__ == '__main__':
	WebApp.secret_key = os.urandom(12)
	WebApp.run(host='0.0.0.0', port=4000, debug=True)
