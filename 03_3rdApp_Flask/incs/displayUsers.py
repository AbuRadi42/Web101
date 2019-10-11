import redis

from flask import session

r = redis.Redis()

def grabUsers():
	users = []
	for key in r.scan_iter("*"):
		if len(key) is 4:
			users.append(key)
	users.remove(session['userIdNo'])

	return users

def showUsers():
	users = grabUsers()

	Cards = '<div class="dashRow">'
	C = 0
	while C < len(users):
		uInfo = r.hgetall(users[C])
		# ---
		if C % 4 is 0:
			Cards += '</div><div class="dashRow">'
		# ---
		Cards += ''.join((
			'<div class="column">',
				'<div class="card">',
					'<img class="img_avatar" src="" alt="" style="padding: 2.5px; width: 99.99%">',
					'<div class="container">',
						'<h4><b>%s</b></h4>' % uInfo['realName'],
						'<p>%s</p>' % uInfo['Biography'] if uInfo['Biography'] is not None else None,
					'</div>',
				'</div>',
			'</div>'
		))
		# ---
		C += 1

	R = (4 - (len(users) % 4)) if (len(users) % 4) > 0 else 0

	while R > 0:
		Cards += ''.join((
			'<div class="column">',
				'<!-- Nothing.. -->',
			'</div>'
		))
		R -= 1

	return Cards
