from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import redis
from simplecrypt import encrypt, decrypt
from binascii import hexlify, unhexlify

r = redis.Redis()

WebApp = Flask(__name__)

@WebApp.route('/')

def index():
	if not session.get('loggedIn'):
		return render_template('loginForm.html')
	else:
		return render_template('dashBoard.html')

@WebApp.route('/login', methods=['POST'])

def login():
	POST_USERNAME = str(request.form['username'])
	POST_PASSWORD = str(request.form['password'])
	
	for hashName in r.keys("0*"):
		userName = r.hget(hashName, "userName")
		if userName == POST_USERNAME:
			break
	passWord = r.hget(hashName, "password")
	decrypted = decrypt(POST_USERNAME[::-1], unhexlify(passWord))
	if decrypted == POST_PASSWORD:
		session['loggedIn'] = True
		session['userIdNo'] = hashName
		print "User No. [\033[1m",
		print session['userIdNo'],
		print "\033[0m] just logged in"
	else:
		print "User No. [\033[1m",
		print hashName,
		print "\033[0m] failed to log in; wrong password."
		flash('wrong password!')
	return index()

@WebApp.route('/logout')

def logout():
	print "User No. [\033[1m",
	print session['userIdNo'],
	print "\033[0m] just logged out"
	session['userIdNo'] = None
	session['loggedIn'] = False
	return index()

@WebApp.route('/signup', methods=['POST'])

def signup():
	POST_USERNAME = str(request.form['username'])
	POST_REALNAME = str(request.form['realname'])
	POST_PASSWORD = str(request.form['password'])
	POST_REPEAT = str(request.form['repeat'])
	POST_E_MAIL = str(request.form['e_mail'])
	POST_GENDER = int(request.form['gender'])
	POST_SEXUALITY = str(request.form['sexuality'])
	POST_BIOGRAPHY = str(request.form['biography'])
	POST_INTERESTS = str(request.form['interests'])
	Session = sessionmaker(bind=engine)

	return render_template('nwusrForm.html')

if __name__ == '__main__':
	WebApp.secret_key = os.urandom(12)
	WebApp.run(host='0.0.0.0', port=4000, debug=True)