
def unsearchedUsers(search):
	everyOne = []
	for key in r.scan_iter("0*"):
		if len(key) is 4:
			everyOne.append(key)

	search = search.split()
	for i in search:
		# embedded search / filter
		if ":" in i:
			if i.split(":")[0].lower() == "gender":
				if i.split(":")[1].lower() == "male":
					for j in everyOne:
						if r.hget(j, "gender") == "1":
							everyOne.remove(j) if j in everyOne else 0
				elif i.split(":")[1].lower() == "female":
					for j in everyOne:
						if r.hget(j, "gender") == "0":
							everyOne.remove(j) if j in everyOne else 0
				else:
					print "failed to filter gender; unrecognised gender"
			elif i.split(":")[0].lower() == "famerate":
				if unicode(i.split(":")[1]).isnumeric():
					for j in everyOne:
						if int(r.hget(j, "fameR")) is int(i.split(":")[1]):
							everyOne.remove(j) if j in everyOne else 0
				else:
					print "failed to filter fame; unnumeric rate"
		# normal search / filter
		else:
			for j in everyOne:
				if i in str(r.hget(j, "realName")).split():
					everyOne.remove(j) if j in everyOne else 0
				elif i in str(r.hget(j, "Location")).split():
					everyOne.remove(j) if j in everyOne else 0
				elif i in str(r.hget(j, "Interests")).split(", "):
					everyOne.remove(j) if j in everyOne else 0

	rtrnList = everyOne

	return rtrnList
