from flask import Flask, flash, redirect, render_template, request, session, abort

import redis

from simplecrypt import encrypt, decrypt
from binascii import hexlify, unhexlify
from validate_email import validate_email

r = redis.Redis()

def userSignUp(userName0, realName, password, e_mail, gender, Sexuality):
	# userName check
	for hashName in r.keys("0*"):
		userName1 = r.hget(hashName, "userName")
		if userName1 == userName0:
			# flash('userName already exists')
			print "failed to sign up; userName already exists"
			return 0
	if userName0 == "":
		# flash('you need to enter a userName')
		print "failed to sign up; a userName is required"
		return 0
	# realName check
	testName = realName.split()
	if len(testName) < 2:
		# flash('realName format: Name Surname')
		print "failed to sign up; Name & Surname are required"
		return 0
	# password check
	upperCFlag = False
	lowerCFlag = False
	numberFlag = False
	for i in password:
		if i.isalpha():
			if i.isupper():
				upperCFlag = True
			elif i.islower():
				lowerCFlag = True
		elif i.isdigit():
			numberFlag = True
	if upperCFlag is False:
			# flash('your password needs to have at least on capital latter')
		print "failed to sign up; password missing capital latter"
	if lowerCFlag is False:
		# flash('your password needs to have at least on small latter')
		print "failed to sign up; password missing small latter"
	if numberFlag is False:
		# flash('your password needs to have at least on number')
		print "failed to sign up; password missing number"
	if upperCFlag is False or lowerCFlag is False or numberFlag is False:
		return 0
	if len(password) < 10:
		print "failed to sign up; password is too short"
		return 0
	encrypted = hexlify(encrypt(userName0[::-1], password))
	# print encrypted
	# decrypted = decrypt(userName0[::-1], unhexlify(encrypted))
	# print decrypted
	hash_key = userName0[::-1]
	# email check
	if not validate_email(e_mail):
		print "failed to sign up; email isn't valid"
		return 0

	# Redis data
	new_IdNo = str(0).zfill(4)
	for idNo in r.keys("0*"):
		if int(idNo, 10) > int(new_IdNo):
			new_IdNo = idNo
	new_IdNo = str(int(new_IdNo, 10) + 1).zfill(4)
	initUserInfo = {}
	initUserInfo['userName'] = userName0
	initUserInfo['realName'] = realName
	initUserInfo['password'] = encrypted
	initUserInfo['hash_key'] = hash_key

	initUserInfo['e_mail'] = e_mail
	initUserInfo['active'] = 0
	initUserInfo['gender'] = gender

	initUserInfo['Sexuality'] = Sexuality
	initUserInfo['Following'] = ""

	if r.hmset(new_IdNo, initUserInfo):
		print "User No. [\033[1m",
		print new_IdNo,
		print "\033[0m] just signed up"
		return new_IdNo

	# send a varification email

	# print initUserInfo['password']
