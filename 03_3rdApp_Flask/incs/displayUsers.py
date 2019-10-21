# -*- coding: utf-8 -*-

import redis

from flask import session

r = redis.Redis()

# ---
def Home():
	userPics = r.hmget(session['userIdNo'], 'pic1', 'pic2', 'pic3', 'pic4', 'pic5')
	NoBs = 0
	for i in userPics : NoBs += (1 if i is not None else 0)
	if (NoBs > 0):
		return '<a href="/">Home</a>'
	else:
		return '<a href="#" class="noPicsHome">Home</a>'
# ---

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
	rstr += ('Interests: ' + uInfo['Interests'] + '&#13;') if uInfo.get('Interests') else ''
	rstr += ('Biography: ' + uInfo['Biography'] + '&#13;') if uInfo.get('Biography') else ''
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

	if NoBs > 1:
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
	else:
		htmlPics = ''.join((
			'<div class="w3-content w3-display-container" style="min-height:180px">',
				htmlImgs, # <- 1 pic
				'<div class="w3-center w3-container w3-section w3-large w3-text-white w3-display-bottommiddle"'
				+ 'style="width:99.99%">',
					'<div class="w3-left w3-hover-text-khaki" onclick="plusDivs(-1)">&#10094;</div>',
					'<div class="w3-right w3-hover-text-khaki" onclick="plusDivs(1)">&#10095;</div>',
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

#---
def common_interest(x, y):
	if TheyLikeThem(x, y) and TheyLikeThem(y, x):
		return '<i class="far fa-comment-dots"></i>' # <- &#xf4ad;
	else:
		return ''
#---

def showUsers():
	users = grabUsers()

	for i in users : users.remove(i) if xPicsIn1Card(i) is None else 0

	for i in users : users.remove(i) if r.hget(i, 'active') == '0' else 0

	# pulling out the C mode since other method didn't work to do this:
	hates = r.hget(session['userIdNo'], 'hates')
	if hates is None:
		hates = ''
	hates = hates.split('_+_')
	hates.remove('')
	j = 0
	while j < len(hates):
		hates[j] = hates[j].split('_Y_')[0]
		j += 1
	k = 0
	while k < len(hates):
		if hates[k] in users:
			users.remove(
				hates[k]
			)
		k += 1
	# removing the users who blocked you on their side from [dashBoard]
	l = 0
	while l < len(users):
		uhates = r.hget(users[l], 'hates')
		if uhates is None:
			l += 1
			continue
		uhates = uhates.split('_+_')
		uhates.remove('')
		m = 0
		while m < len(uhates):
			uhates[m] = uhates[m].split('_Y_')[0]
			m += 1
		n = 0
		while n < len(uhates):
			if session['userIdNo'] in uhates:
				users.remove(users[l])
				break
			n += 1
		l += 1

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
						'<a href="/blockUserNo%s" class="blockBtn">' % users[C],
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
						'<h4><b>%s <a href="%schatingTo%s" class="chatBtn">%s</a></b></h4>' % (
							uInfo['realName'],
							session['userIdNo'],
							users[C],
							common_interest(session['userIdNo'], users[C])
						),
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
