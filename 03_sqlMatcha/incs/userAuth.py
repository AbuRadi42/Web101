import mysql.connector as mySQL
import basehash

from mysql.connector import errorcode
from flask import Flask, flash, redirect, render_template, session

# from Retrieve import sendVerificationText

credentials	= {}

credentials["host"]	= "127.0.0.1"
credentials["user"]	= "root"
credentials["pass"]	= "password"
credentials["DB"]	= "Matcha"

def db_connect(credentials):

	try:
		cnx = mySQL.connect(
			host		= credentials["host"],
			user		= credentials["user"],
			password	= credentials["pass"],
			database	= credentials["DB"],
			auth_plugin	= "mysql_native_password"
		)

	except Exception as e:

		if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print(" wrong username or password")
		elif e.errno == errorcode.ER_BAD_DB_ERROR:
			print(" database does not exist")
		else:
			print(e)

		cnx.close()

		return -1, -1

	try:

		# return cnx, cnx.cursor(prepared = True)

		return cnx, cnx.cursor()

	except mySQL.Error as e:

		print(e)

		cnx.close()

		return -1, -1

	return 0, 0

def userSignUp(userName, realName, password, e_mail, gender, Sexuality):

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
		errMsg = "password must include capital latter/s"
		flash(errMsg, "warning")
		return render_template("nwusrForm.html", e = errMsg)

	if lowerCFlag is False:
		errMsg = "password must include small latter/s"
		flash(errMsg, "warning")
		return render_template("nwusrForm.html", e = errMsg)

	if numberFlag is False:
		errMsg = "password must include number/s"
		flash(errMsg, "warning")
		return render_template("nwusrForm.html", e = errMsg)

	if len(password) < 8:
		errMsg = "password is too short"
		flash(errMsg, "warning")
		return render_template("nwusrForm.html", e = errMsg)

	encrypted = password

	hash_key = "42"

	# ---

	cnx, cursor = db_connect(credentials)

	# return str((cnx, cursor))

	if (cnx and cursor):

		q = """
				INSERT INTO `users` (
					userName,
					realName,
					password,
					hash_key,
					e_mail,
					active,
					likes,
					hates,
					fameR,
					gender,
					Sexuality
				) VALUES (
					"{}",
					"{}",
					"{}",
					"{}",
					"{}",
					0,
					0,
					0,
					0,
					{},
					"{}"
				)
			""".format(
				userName,
				realName,
				encrypted,
				hash_key,
				e_mail,
				gender,
				Sexuality
			)

		try:

			cursor.execute(q)

			cnx.commit()

			cnx.close()

			infoMsg = "sign up is successful, check your email"
			flash(infoMsg, "info")
			return render_template("loginForm.html", e = infoMsg)

		except mySQL.Error as e:

			print(e)

			cnx.close()

			return redirect("/nwusrForm/03")

	else:

		return redirect("/nwusrForm/03")

def userSignIn(userName, password):

	cnx, cursor = db_connect(credentials)

	# return str((cnx, cursor))

	if (cnx and cursor):

		q = """
				SELECT *
				FROM `users`
				WHERE userName = "{}"
				AND password = "{}"
			""".format(
				userName,
				password
			)

		try:

			cursor.execute(q)

			R = cursor.fetchall()

			if len(R) == 0:

				cnx.close()

				infoMsg = "incorrect credentials"
				flash(infoMsg, "warning_login")
				return render_template("loginForm.html", e = infoMsg)

			else:

				if R[0][7]:

					cnx.close()

					session["loggedIn"] = True
					session["userName"] = R[0][1]
					session["uId"] = R[0][0]

					return redirect("/")

				else:

					cnx.close()

					infoMsg = "account not activated yet"
					flash(infoMsg, "warning_login")
					return render_template("loginForm.html", e = infoMsg)

			return redirect("/")

		except mySQL.Error as e:

			print(e)

			cnx.close()

			infoMsg = "SQL failure..."
			flash(infoMsg, "warning_login")
			return render_template("loginForm.html", e = infoMsg)

	else:

		infoMsg = "SQL failure..."
		flash(infoMsg, "warning_login")
		return render_template("loginForm.html", e = infoMsg)

	# 		r.hset(session["userIdNo"], "Connection", ":  " * 9 + "Online" + "  :" * 9)
	# 		#---
	# 		cmd = "curl ipinfo.io/city"
	# 		status, output = commands.getstatusoutput(cmd)
	# 		r.hset(session["userIdNo"], "Location", output.splitlines()[-1])
	# 		#---
	# 		print("User No. [\033[1m", end = " ")
	# 		print(session["userIdNo"], end = " ")
	# 		print("\033[0m] just logged in")
	# 	else:
	# 		print("User No. [\033[1m", end = " ")
	# 		print(hashName, end = " ")
	# 		print("\033[0m] failed to log in; account isn"t activated yet.")
	# 		flash("not activated yet!")
	# else:
	# 	print("User No. [\033[1m", end = " ")
	# 	print(hashName, end = " ")
	# 	print("\033[0m] failed to log in; wrong password.")
	# 	flash("wrong password!")
	# if Home() == "<a href="#" class="noPicsHome">Home</a>":
	# 	return redirect("/profile")

def goneSince(userName, localtime):

	cnx, cursor = db_connect(credentials)

	# return str((cnx, cursor))

	if (cnx and cursor):

		q = """
				UPDATE `users`
				SET goneSince = "{}"
				WHERE userName = "{}"
			""".format(
				localtime,
				userName
			)

		try:

			cursor.execute(q)

			cnx.commit()

			cnx.close()

			return 1

		except mySQL.Error as e:

			print(e)

			cnx.close()

			infoMsg = "SQL failure..."
			flash(infoMsg, "warning_login")
			return render_template("loginForm.html", e = infoMsg)

	else:

		infoMsg = "SQL failure..."
		flash(infoMsg, "warning_login")
		return render_template("loginForm.html", e = infoMsg)
