# -*- coding: utf-8 -*-

import redis

from flask import session, flash
from binascii import hexlify
from simplecrypt import encrypt
from validate_email import validate_email

r = redis.Redis()

def handleUserInfoChange(
	POST_USERNAME,
	POST_GENDER,
	POST_REALNAME,
	POST_E_MAIL,
	POST_PASSWORD,
	POST_CONFIRM,
	Biography,
	Interests,
	POST_SEXUALITY
):
	ChangeFlag = False

	uInfo = r.hgetall(session['userIdNo'])

	Crnt_USERNAME = uInfo['userName']
	Crnt_GENDER = uInfo['gender']
	Crnt_REALNAME = uInfo['realName']
	Crnt_E_MAIL = uInfo['e_mail']
	# Crnt_Biography = uInfo['Biography']
	# Crnt_Interests = uInfo['Interests']
	Crnt_SEXUALITY = uInfo['Sexuality']

	if POST_USERNAME <> '' and POST_USERNAME <> Crnt_USERNAME:
		# userNameChng = 1
		# for hashName in r.keys('0*'):
		# 	userName1 = r.hget(hashName, 'userName')
		# 	if userName1 == POST_USERNAME:
		# 		# flash('userName already exists')
		# 		print "failed to change; userName already exists" 
		# 		userNameChng = -1
		# 		break
		# if userNameChng > 0:
		# 	if len(POST_USERNAME) < (5 + 1):
		# 		print "failed to change; userName is shorter than six characters"
		# 	else:
		# 		r.hset(session['userIdNo'], 'userName', POST_USERNAME)
		# 		ChangeFlag = True
		# 		print "changed userName successfully"
		print "userName isn't allowed to be changed yet"

	if POST_GENDER <> Crnt_GENDER:
		r.hset(session['userIdNo'], 'gender', POST_GENDER)
		ChangeFlag = True
		print "changed gender successfully"

	if POST_REALNAME <> '' and POST_REALNAME <> Crnt_REALNAME:
		testName = POST_REALNAME.split()
		if len(testName) < 2:
			# flash('realName format: Name Surname')
			print "failed to change; Name & Surname are required"
		else:
			r.hset(session['userIdNo'], 'realName', POST_REALNAME)
			ChangeFlag = True
			print "changed realName successfully"

	if POST_E_MAIL <> '' and POST_E_MAIL <> Crnt_E_MAIL:
		if not validate_email(POST_E_MAIL):
			print "failed to change; email isn't valid"
		else:
			r.hset(session['userIdNo'], 'e_mail', POST_E_MAIL)
			ChangeFlag = True
			print "changed e_mail successfully"

	if POST_PASSWORD == '' and POST_CONFIRM <> '':
		print "failed to change password; unconfirmed password"
	if POST_PASSWORD <> '' and POST_CONFIRM == '':
		print "failed to change password; unconfirmed password"
	if POST_PASSWORD <> '' and POST_CONFIRM <> '':
		if POST_PASSWORD <> POST_CONFIRM:
			flash('unconfirmed password!')
			print "failed to change password; unconfirmed password"
		else:
			# password check
			passWordChng = 1

			upperCFlag = False
			lowerCFlag = False
			numberFlag = False
			for i in POST_PASSWORD:
				if i.isalpha():
					if i.isupper():
						upperCFlag = True
					elif i.islower():
						lowerCFlag = True
				elif i.isdigit():
					numberFlag = True
			if upperCFlag is False:
				# flash('your password needs to have at least on capital latter')
				print "failed to change password; password missing capital latter(s)"
			if lowerCFlag is False:
				# flash('your password needs to have at least on small latter')
				print "failed to change password; password missing small latter(s)"
			if numberFlag is False:
				# flash('your password needs to have at least on number')
				print "failed to change password; password missing number(s)"
			if upperCFlag is False or lowerCFlag is False or numberFlag is False:
				passWordChng = -1
			if len(POST_PASSWORD) < 10:
				print "failed to change password; password is too short"
				passWordChng = -1
			if passWordChng > 0:
				encrypted = hexlify(encrypt(Crnt_USERNAME[::-1], POST_PASSWORD))
				r.hset(session['userIdNo'], 'password', encrypted)
				ChangeFlag = True
				print "changed password successfully"

	if Biography <> '':
		r.hset(session['userIdNo'], 'Biography', Biography)
		ChangeFlag = True
		print "changed Biography successfully"

	if Interests <> '':
		r.hset(session['userIdNo'], 'Interests', Interests)
		ChangeFlag = True
		print "changed Interests successfully"

	if POST_SEXUALITY <> Crnt_SEXUALITY:
		r.hset(session['userIdNo'], 'Sexuality', POST_SEXUALITY)
		ChangeFlag = True
		print "changed Sexuality successfully"

	if ChangeFlag is False:
		print "failed to change; nothing to change"

def showBlocked():
	hates = r.hget(session['userIdNo'], 'hates')
	if hates is None:
		return ''
	hates = hates.split('_+_')

	rstr = ''
	index = 1
	while index < len(hates):
		line = hates[index].split('_Y_')
		rstr += ''.join((
			'<h5 class="blockedList">',
				u'•'
				+ ' [<a href="/unblockUserNo%s">unBlock</a>] ' % line[0]
				+ r.hget(line[0], 'realName')
				+ (', ' + line[1] if line[1] <> '#NoReason' else ''),
			'</h5>'
		))
		index += 1
	return rstr
