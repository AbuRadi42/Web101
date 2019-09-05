import commands

def runRedisServer_IfNotAlready():
	cmd = "pgrep redis-server"
	status, output = commands.getstatusoutput(cmd)
	if status is 0 and output <> "":
		print "Redis-Server is Running @ pid; %s" % output
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
