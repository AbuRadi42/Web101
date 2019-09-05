import redis

r = redis.Redis()

for hashName in r.keys("0*"):
	userName = r.hget(hashName, "userName")
	if userName == "BigBoy":
		break

print hashName
print userName

print r.hget(hashName, "password")
