# -*- coding: utf-8 -*-

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

def getSexuality(gender, Sexuality):
	if Sexuality == '1':
		return u'⚤'
	elif Sexuality == '0':
		return u'⚥'
	elif Sexuality == '-1':
		if gender == '1':
			return u'⚣'
		else:
			return u'⚢'

def moreUserInfo(userId):
	uInfo = r.hgetall(userId)

	rstr = uInfo['Connection'] + ('&#13;' * 2)
	rstr += 'Location: ' + uInfo['Location'] + '&#13;'

	rstr += 'Gender: ' + (u'♂' if uInfo['gender'] == '1' else u'♀') + ', '
	rstr += 'Sexuality: ' + getSexuality(uInfo['gender'], uInfo['Sexuality']) + '&#13;'
	rstr += 'Interests: ' + uInfo['Interests'] + '&#13;'
	rstr += 'Biography: ' + uInfo['Biography'] + '&#13;'
	return rstr

#---
def xPicsIn1Card(userId):
	userPics = r.hmget(userId, 'pic1', 'pic2', 'pic3', 'pic4', 'pic5')

	# grabing the userPics to turn them into htmlImgs & counting the NoBs
	htmlImgs = ''
	NoBs = 0
	for i in userPics:
		if i is not None:
			htmlImgs += ''.join((
				'<img class="img_avatar mySlides" src="" style="image: url(\'{}\');" '.format(
					'data:image/jpeg;base64,' + i # <- find a way to encrypt pictures
				)
				+ 'style="padding: 2.5px; width: 100%">'
			))
			NoBs += 1

	htmlBdgs = ''
	CoCD = 1
	while CoCD <= NoBs:
		htmlBdgs += ''.join((
			'<span class="w3-badge demo w3-border w3-transparent w3-hover-white"'
			+ 'onclick="currentDiv({})"></span>'.format(str(CoCD))
		))
		CoCD += 1

	htmlPics = ''.join((
		'<div class="w3-content w3-display-container" style="min-height:180px">',
			htmlImgs,
			'<div class="w3-center w3-container w3-section w3-large w3-text-white w3-display-bottommiddle"'
			+ 'style="width:99.99%">',
				'<div class="w3-left w3-hover-text-khaki" onclick="plusDivs(-1)">&#10094;</div>',
				'<div class="w3-right w3-hover-text-khaki" onclick="plusDivs(1)">&#10095;</div>',
				htmlBdgs,
			'</div>',
		'</div>'
	))

	return None if NoBs is 0 else htmlPics
#---

def TheyLikeThem(x, y):
	likes = r.hget(x, 'likes')
	if likes is None:
		likes = ''
	likesArray = likes.split()
	for i in likesArray:
		if i == y:
			return True
	# else ;
	return False

def showUsers():
	users = grabUsers()

	for i in users : users.remove(i) if xPicsIn1Card(i) is None else 0

	Cards = '<div class="dashRow">'
	C = 0
	while C < len(users):
		# ---
		uInfo = r.hgetall(users[C])
		# ---
		if C % 4 is 0:
			Cards += '</div><div class="dashRow">'
		# ---
		Cards += ''.join((
			'<div class="column">',
				'<div class="card" title="%s">' % moreUserInfo(users[C]),
					xPicsIn1Card(users[C]),
					'<div class="blockBtn">',
						'<a href="/%sHatesNo%s" class="blockBtn">' % (
							session['userIdNo'],
							users[C]
						),
							u'✘',
						'</a>',
					'</div>',
					'<div class="likeBtn">',
						'<a href="/%sLikesNo%s" class="likeBtn" style="color: %s">' % (
							session['userIdNo'],
							users[C],
							'indianred' if TheyLikeThem(session['userIdNo'], users[C]) else 'lightgray'
						),
							u'♥',
						'</a>',
					'</div>',
					'<h2 class="fameR">%s</h2>' % uInfo['fameR'],
					'<div class="container">',
						'<h4><b>%s</b></h4>' % uInfo['realName'],
						'<p>%s</p>' % uInfo['Biography'] if uInfo['Biography'] is not None else '_',
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

#---

def unlike(x, y, likesArray):
	likesArray.remove(y)

	likes = ''
	for i in likesArray:
		likes += ' %s' % i

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
		) - 1
	)
	#---
