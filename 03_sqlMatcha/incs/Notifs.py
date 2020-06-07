# -*- coding: utf-8 -*-

import redis

from flask import session
from displayUsers import TheyLikeThem

r = redis.Redis()

def Notifs():
	notifs = r.hgetall('notifsOf%s' % session['userIdNo'])

	if bool(notifs) is False:
		return '<span style="color: #333;"> %s</span>' % u'•'
	else:
		nF = 0
		for i, j in notifs.items():
			if j[0] <> '#':
				nF = 1
		if nF is 0:
			return '<span style="color: #333;"> %s</span>' % u'•'
		else:
			return '<span style="color: red;"> %s</span>' % u'•'

#---
def common_interest(x, y):
	if TheyLikeThem(x, y) and TheyLikeThem(y, x):
		return True
	else:
		return False
#---
def notifList():
	notifs = r.hgetall('notifsOf%s' % session['userIdNo'])

	rstr = ''

	if bool(notifs) is False:
		rstr += ''.join((
			'<div style="text-align: center; color: gray;">',
				'<h5>',
					'you don\'t have any notifications yet',
				'</h5>',
			'</div>'
		))
		return rstr
	else:
		sortedNotifs = list(reversed(sorted(notifs.iteritems()))) # sorted by timestamp & reversed

		for c in sortedNotifs:
			time, note = c
			if note[0] == '#':
				rstr += ''.join((
					'<div style="color: %s;">' % 'gray',
						'<h5 style="font-size: 13.5px">',
							u' • '
							+ '%s, ' % note[5:29]
							+ '%s %s' % (
								r.hget(note[31:35], 'realName'),
								note[36:]
							)
							+ ('... <a href="/%schatingTo%s">reply</a>' % (
								session['userIdNo'],
								note[31:35]
							) if note[2] == 'm' else ('. <a href="/%sLikesNo%s">like them back</a>' % (
								session['userIdNo'],
								note[31:35]
							) if not common_interest(
								session['userIdNo'],
								note[31:35]
							) else '.')),
						'</h5>',
					'</div>',
					'<hr>'
				))
			else:
				rstr += ''.join((
					'<div style="color: %s;">' % '#303030',
						'<h5 style="font-size: 13.5px">',
							u' • '
							+ '%s, ' % note[4:28]
							+ '%s %s' % (
								r.hget(note[30:34], 'realName'),
								note[35:]
							)
							+ ('... <a href="/%schatingTo%s">reply</a>' % (
								session['userIdNo'],
								note[30:34]
							) if note[1] == 'm' else ('. <a href="/%sLikesNo%s">like them back</a>' % (
								session['userIdNo'],
								note[30:34]
							) if not common_interest(
								session['userIdNo'],
								note[30:34]
							) else '.')),
						'</h5>',
					'</div>',
					'<hr>'
				))
				r.hset('notifsOf%s' % session['userIdNo'], time, '#' + note) # <- marking seen notifs
		return rstr
