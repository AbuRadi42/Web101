import redis

idNo = 1

Character = [
	[
		"Star69Fish",
		"Patrick Star",
		"7363000229d9063ded8467772db7aff2d9ef78c7e43ac0249ab0832ffe75329ee29555423628cc77263332e4578a2755a0eef7e9547409772528e50352925665d711f7251124e15849ecca7a4491e31a", #5_sided_star
		"?",
		"Patrick@Star.com",
		"1",
		"2",
		"3",
		"4",
		"5",
		1,
		1,
		-1,
		"I live under a rock",
		"Food",
		""
	],
	[
		"Clarinetist",
		"Squidward Tentacles",
		"73630002d0ed38dbb368bb5747ff0d7984fe2ea3c16aec2d4af3e2dab988d9872fe98b973df9a0e7b86116a2b3486a447f38eac534739307e37eca0ab8bc4241223aeafd55f9acc76b7f613b9b1657de1b", #12345Clarinet
		"?",
		"Clarinetist@gmail.com",
		"1",
		"2",
		"3",
		"4",
		"5",
		1,
		1,
		0,
		"I'm a fictional character[idNo - 1]",
		"Clarinet, Monuments",
		""
	],
	[
		"BigBoy",
		"Mr. Krabs",
		"73630002bb27afeeb7dfe0e4f7084aa3cc2a930b94e725a44f6606275d32d3245833aba6572b302b65f5dcd422bda8714647489805f5fa850128fcc99a3deb148a93ae5936c55f6b7377eff1230a9d", #Money0rgasm
		"?",
		"Money@Money.com",
		"1",
		"2",
		"3",
		"4",
		"5",
		1,
		1,
		0,
		"Money is what makes it worth it",
		"KrabbyPattys, Food",
		""
	],
	[
		"Squirrel",
		"Sandy Cheeks",
		"736300023c8a1534972a5bbd187b582c09bf2d3e6ecc04ddd25bd4beb20593b68cb0f78cfba6115b7d867d4df231b1e0dd37f269383f66d67cc433c3cfa545154b0608578bea0e140cf27541a429", #Science_42
		"?",
		"squirrel@aquanauts.com",
		"1",
		"2",
		"3",
		"4",
		"5",
		1,
		0,
		0,
		"I'm an alien",
		"Ocean",
		""
	],
	[
		"Junior",
		"Sheldon J. Plankton",
		"73630002fd668e2a556dcebe75cc5b77b9d0d4f0f4a266311bd47ec5d3fd4feb2989898db899adbd9eaa7b4a79efb39f99bc295cf50e89657992d42b287a6890db71df2e542f37ee91cb1b23dab7c9", #JuniorSize1
		"?",
		"Plankton@1942.com",
		"1",
		"2",
		"3",
		"4",
		"5",
		1,
		1,
		-1,
		"Shhh, looking for KrabbyPattys the krabby patties recipe",
		"KrabbyPattys",
		""
	],
	[
		"Puffy",
		"Mrs. Puff",
		"7363000292f9ff57663eb348a046c6553d0b2a16687f4ba9018b975eed47773639628f81c71c2a16644280c67c94a858228da3bbc287f38b80152dbfcc5dae8f7651880f730d4332375bac5f1d2231", #PuffyStuff1
		"?",
		"Mrs@Puff.com",
		"1",
		"2",
		"3",
		"4",
		"5",
		1,
		0,
		1,
		"I'm mrs. puffy, I like it roughy",
		"Food",
		""
	],
	[
		"Pearl Krabs",
		"Patrick Star",
		"7363000284ede6d0f144c8f3031ada435fa2c86b324d2421c676ffcc616777d4603792e554a0ecb58f3fa6167b1ce695131a1dece0a8c96e240be3fa96c018026dd28e58a65093ccf2ae9c4166240dbd12", #dontTe11MyDad
		"?",
		"Pearl@Money.com",
		"1",
		"2",
		"3",
		"4",
		"5",
		1,
		0,
		1,
		"I live under a rock",
		"Food",
		""
	],
	[
		"Karen Plankton",
		"Patrick Star",
		"73630002939983d74475b729d49341e4c88d5efc6ec7cd371c3012e1f67f73e24c312630bc4b3c57d308f2ca7cd00d0a0a705dd9e900949bbfe882ef5ed7a33e139bed9a7b0cc35a9b696c8e232d4e", #OI01_getit?
		"?",
		"Karen@1984.com",
		"1",
		"2",
		"3",
		"4",
		"5",
		1,
		0,
		1,
		"I am the only true binary here, talk to me before Junior gets home",
		"Food",
		""
	],
	[
		"SquarePants",
		"SpongeBob SquarePants",
		"7363000250bd18a0d821e406e182c066751d0f9fd28b034d8faae199d0a72f933d4e24294d0a59f57195946ec0d4788aa57532ad31849d296e0ddb3fc5c120593e6bce9ab86d7319675cc55c1a5fa2030fd550884e", #Soaked1and1Square
		"?",
		"Square@Pants.com",
		"1",
		"2",
		"3",
		"4",
		"5",
		1,
		1,
		1,
		"I live live in a pineapple under the sea",
		"Food, Snails, squirrels",
		""
	]
]

dumbUserInfo = {
	"userName":		"",
	"realName":		"",
	"password":		"",
	"hash_key":		"",
	"e_mail":		"",
	"pics#1":		"",
	"pics#2":		"",
	"pics#3":		"",
	"pics#4":		"",
	"pics#5":		"",
	"active":		0,
	"gender":		"",
	"Sexuality":	"",
	"Biography":	"",
	"Interests":	"",
	"Following":	"",
}

r = redis.Redis()

while idNo < 10:
	dumbUserInfo['userName'] = Character[idNo - 1][0]
	dumbUserInfo['realName'] = Character[idNo - 1][1]
	dumbUserInfo['password'] = Character[idNo - 1][2]
	dumbUserInfo['hash_key'] = Character[idNo - 1][3]

	dumbUserInfo['e_mail'] = Character[idNo - 1][4]
	dumbUserInfo['pics#1'] = Character[idNo - 1][5]
	dumbUserInfo['pics#2'] = Character[idNo - 1][6]
	dumbUserInfo['pics#3'] = Character[idNo - 1][7]
	dumbUserInfo['pics#4'] = Character[idNo - 1][8]
	dumbUserInfo['pics#5'] = Character[idNo - 1][9]
	dumbUserInfo['active'] = Character[idNo - 1][10]
	dumbUserInfo['gender'] = Character[idNo - 1][11]

	dumbUserInfo['Sexuality'] = Character[idNo - 1][12]
	dumbUserInfo['Biography'] = Character[idNo - 1][13]
	dumbUserInfo['Interests'] = Character[idNo - 1][14]
	dumbUserInfo['Following'] = Character[idNo - 1][15]

	r.hmset(str(idNo).zfill(4), dumbUserInfo)

	print dumbUserInfo['realName'],
	print "is added to [\033[1m",
	print str(idNo).zfill(4),
	print "\033[0m]"

	idNo += 1
