import commands
import redis

def runRedisServer_IfNotAlready():
	cmd = "pgrep redis-server"
	status, output = commands.getstatusoutput(cmd)
	if status is 0 and output <> "":
		print "Redis-Server is \033[1mAlready\033[0m Running @ pid; %s" % output
	else:
		runCmd = "redis-server /etc/redis/6379.config"
		# cmd = "redis-server /6379.config"
		status, output = commands.getstatusoutput(runCmd)
		output = output.split()
		if status is 0:
			print "Redis-Server is Running @ pid; %i" % (
				int(output[22][5 - 1:10 - 1], 10) + 1
			)

runRedisServer_IfNotAlready()

r = redis.Redis()

initUserInfo = {
	"userName":		"somethingUnique",
	"realName":		"anyNameGoesHere",
	"password":		"123456789ABCDEF",
	"hash_key":		"FEDCBA987654321",
	"e_mail":		"1Redis@Flask.py",
	"pics#1":		"1",
	"pics#2":		"2",
	"pics#3":		"3",
	"pics#4":		"4",
	"pics#5":		"5",
	"active":		"0",
	"gender":		"maleFemaleEmail",
	"Sexuality":	"_Hetero_Homo_Bi",
	"Biography":	"Blah!Blah!Blah!",
	"Interests":	"Blah!Blah!Blah!",
	"Following":	"1 2 3 4 5 6 7 8",
}
