import mysql.connector as mySQL

from mysql.connector import errorcode

# <- assigning default credentials

credentials	= {}

credentials['host']	= '127.0.0.1'
credentials['user']	= 'root'
credentials['pass']	= 'password'
credentials['DB']	= 'Matcha'

# ---

def	DB_Setup(credentials):

	try:
		cnx = mySQL.connect(
			host		= credentials['host'],
			user		= credentials['user'],
			password	= credentials['pass'],
			auth_plugin	= 'mysql_native_password'
		)

	except mySQL.Error as e:

		if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print(' wrong username or password')
		else:
			print(e)

		cnx.close()
		return 0

	try:
		cursor = cnx.cursor()
		cursor.execute(
			"""
				CREATE DATABASE if not exists
				{}
				DEFAULT CHARACTER SET 'utf8'
			""".format(credentials['DB'])
		)

		cnx.commit()
		cursor.close()
		cnx.close()

	except mySQL.Error as e:
		print(' failed to create the database')

		cursor.close()
		cnx.close()
		return 0

	try:
		cnx = mySQL.connect(
			host		= credentials['host'],
			user		= credentials['user'],
			password	= credentials['pass'],
			database	= credentials['DB'],
			auth_plugin	= 'mysql_native_password'
		)

	except Exception as e:

		if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print(' wrong username or password')
		elif e.errno == errorcode.ER_BAD_DB_ERROR:
			print(' database does not exist')
		else:
			print(e)

		cnx.close()
		return 0

	try:
		cursor = cnx.cursor()
		cursor.execute(
			"""
				CREATE TABLE if not exists `users` (
					`uId`		int NOT NULL AUTO_INCREMENT,
					`userName`	varchar(255),
					`realName`	varchar(255),
					`password`	varchar(2048),
					`hash_key`	varchar(2048),
					`e_mail`	varchar(255),
					`pic`		TEXT,
					`active`	bool,
					`gender`	tinyint(1),
					`Sexuality`	varchar(16),
					`Biography`	varchar(1024),
					`Interests`	varchar(1024),
					`likes`		varchar(4096),
					`hates`		varchar(4096),
					`fameR`		int,
					`goneSince`	varchar(255),
					`timedate`	TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
					primary key (uId)
				)
			"""
		)

		cnx.commit()

	except mySQL.Error as e:

		print(e)

		cursor.close()
		cnx.close()
		return 1

	finally:

		cursor.close()
		cnx.close()
		return 1

DB_Setup(credentials)
