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
	"e_mail":		"1Redis@Flask.py",
	"pic1":			"1",
	"pic2":			"2",
	"pic3":			"3",
	"pic4":			"4",
	"pic5":			"5",
	"active":		"0",
	"gender":		"maleFemaleEmail",
	"Sexuality":	"_Hetero_Homo_Bi",
	"Biography":	"Blah!Blah!Blah!",
	"Interests":	"Blah!Blah!Blah!",
	"likes":		" 0001 0005 0009",
	"hates":		" 0002 0004 0008",
	"fameR":		"0",
}
