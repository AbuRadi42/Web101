# -*- coding: utf-8 -*-

import redis

from collections import OrderedDict
from time import ctime

r = redis.Redis()

def timeWise(A):
	x, y = A
	return x

def MsgsBtwn(x, y):
	fromXtoY = r.hgetall('%s_to_%s' % (x, y))
	fromYtoX = r.hgetall('%s_to_%s' % (y, x))

	rstr = ''

	if bool(fromXtoY) is False and bool(fromYtoX) is False:
		rstr += ''.join((
			'<div style="text-align: center; color: gray;">',
				'<h5>',
					'you didn\'t start a conversation with %s yet.' % r.hget(y, 'realName'),
				'</h5>',
			'</div>'
		))
		return rstr
	else:
		if bool(fromXtoY) and bool(fromYtoX):
			From_X = sorted(fromXtoY.iteritems())
			From_Y = sorted(fromYtoX.iteritems())

			From_A = sorted(From_X + From_Y, key = timeWise)
		elif bool(fromXtoY) and not bool(fromYtoX):
			From_A = sorted(fromXtoY.iteritems())
		elif not bool(fromXtoY) and bool(fromYtoX):
			From_A = sorted(fromYtoX.iteritems())

	for c in From_A:
		time, note = c
		if len(note) is 0:
			continue
		rstr += ''.join((
			'<div class="Msgs">',
				'<h5 style="font-size: 13.5px">',
					'%s : ' % r.hget(note.split('_|_')[0], 'realName')
					+ note.split('_|_')[1]
					+ '<br><br><span style="color: gray; float: left;">%s</span>' % (
						str(ctime(float(time)))
					),
				'</h5>',
			'</div>',
			'<hr>'
		))

	return rstr
