import mysql.connector as mySQL

from userAuth import db_connect, credentials
from mysql.connector import errorcode

from flask import session
# from displayUsers import TheyLikeThem

def Notifs():

	cnx, cursor = db_connect(credentials)

	if (cnx and cursor):

		q = """
				SELECT *
				FROM `notifs`
				WHERE username = '{}'
			""".format(
				str(session['userName'])
			)

		try:

			cursor.execute(q)

			R = cursor.fetchall()

			cnx.close()

			if len(R) != 0:

				for i in R:

					if i[3] is 0:

						return '<span style="color: red;"> %s</span>' % u'•'

				return '<span style="color: #333;"> %s</span>' % u'•'

			else:

				return '<span style="color: #333;"> %s</span>' % u'•'

		except mySQL.Error as e:

			print(e)

			cnx.close()

			return redirect('/')

	return redirect('/')

#---
def common_interest(x, y):
	if TheyLikeThem(x, y) and TheyLikeThem(y, x):
		return True
	else:
		return False
#---
def notifList(realName):

	pass

	# cnx, cursor = db_connect(credentials)

	# if (cnx and cursor):

	# 	q = """
	# 			SELECT *
	# 			FROM `notifs`
	# 			WHERE username = '{}'

	# 			ORDER BY notifId DESC
	# 		""".format(
	# 			str(session['userName'])
	# 		)

	# 	try:

	# 		cursor.execute(q)

	# 		R = cursor.fetchall()

	# 		cnx.close()

	# 		rStr = ''

	# 		if len(R) != 0:

	# 			for i in R:

	# 			if i[3] == 1:
	# 				rstr += ''.join((
	# 					'<div style="color: %s;">' % 'gray',
	# 						'<h5 style="font-size: 13.5px">',
	# 							u' • '
	# 							+ '%s, ' % note[5:29]
	# 							+ '%s %s' % (
	# 								realName,
	# 								# note[36:]
	# 							)
	# 							+ ('... <a href="/%schatingTo%s">reply</a>' % (
	# 								session['userIdNo'],
	# 								# note[31:35]
	# 							) if note[2] == 'm' else ('. <a href="/%sLikesNo%s">like them back</a>' % (
	# 								session['userIdNo'],
	# 								# note[31:35]
	# 							) if not common_interest(
	# 								session['userIdNo'],
	# 								# note[31:35]
	# 							) else '.')),
	# 						'</h5>',
	# 					'</div>',
	# 					'<hr>'
	# 				))
	# 			else:
	# 				rstr += ''.join((
	# 					'<div style="color: %s;">' % '#303030',
	# 						'<h5 style="font-size: 13.5px">',
	# 							u' • '
	# 							+ '%s, ' % note[4:28]
	# 							+ '%s %s' % (
	# 								realName,
	# 								note[35:]
	# 							)
	# 							+ ('... <a href="/%schatingTo%s">reply</a>' % (
	# 								session['userIdNo'],
	# 								# note[30:34]
	# 							) if note[1] == 'm' else ('. <a href="/%sLikesNo%s">like them back</a>' % (
	# 								session['userIdNo'],
	# 								# note[30:34]
	# 							) if not common_interest(
	# 								session['userIdNo'],
	# 								# note[30:34]
	# 							) else '.')),
	# 						'</h5>',
	# 					'</div>',
	# 					'<hr>'
	# 				))

	# 				pass

	# 		else:

	# 			rStr += ''.join((
	# 				'<div style="text-align: center; color: gray;">',
	# 					'<h5>',
	# 						'you don\'t have any notifications yet',
	# 					'</h5>',
	# 				'</div>'
	# 			))

	# 			return rStr

	# 	except mySQL.Error as e:

	# 		print(e)

	# 		cnx.close()

	# 		return redirect('/')

	# return redirect('/')

	# rstr = ''

	# if bool(notifs) is False:
	# 	rstr += ''.join((
	# 		'<div style="text-align: center; color: gray;">',
	# 			'<h5>',
	# 				'you don\'t have any notifications yet',
	# 			'</h5>',
	# 		'</div>'
	# 	))
	# 	return rstr
	# else:


	# 			r.hset('notifsOf%s' % session['userIdNo'], time, '#' + note) # <- marking seen notifs
	# 	return rstr
