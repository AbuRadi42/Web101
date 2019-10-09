import redis

idNo = 1

Character = [
	[
		"Star69Fish", #5_Sided_Star
		"Patrick Star",
		"736300025fb247ee0070786c584aca7d94f43e7f23921471c0cad0b6c56e530a1247e9ddf02525673a9dd320aead571da50c5fdb75c62c0318b06dc17eed85695c6f24d2da25f92c2fa440bec4bcdd02",
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
		"Clarinetist", #12345Clarinet
		"Squidward Tentacles",
		"7363000210c1721d5c20e73a5123a69f4af52c5873f42143aa2023ea74036103d9a887e148bdd78bac2959fa1ad257f04c1c34ef8c7b5246d7880fabfda77df3371cd71573a4524414b9930a86ab6af7f8",
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
		"I'm a fictional character",
		"Clarinet, Monuments",
		""
	],
	[
		"BigBoy", #Money0rgasm
		"Mr. Krabs",
		"7363000226a3f086f4080cf47b443b13eb673acf363ff6dc31530413c435a99b6db9a8d0523e44a7d61dd6cd4d2600cf19459ceb2cda40c607e1a80f3c5dd51162c0165f6acfa626fb6b64081546dc",
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
		"Squirrel", #Science_42
		"Sandy Cheeks",
		"73630002d29e0686f26ce74e8975161c0c3a017784d9c2e6724816591c5bbdeaf326f425b9dd8baad7f8a797d980fe1bc724d83f70e825fa285871f752081bd834617f5107112a69e37e69483a17",
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
		"Junior", #JuniorSize1
		"Sheldon J. Plankton",
		"73630002cd4a30828c23af446ceb208202d868c0458aa4848884c2a57fbe724a5e5ef12c7dff6c5f2e36a69cda5c910e442427f21650d877073f7fa1e95abd94fd4207745fdca339f6ada2d096c49d",
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
		"Puffy", #PuffyStuff1
		"Mrs. Puff",
		"73630002b7884442d9244e5675b9ed0e889740af9c32a89ebe94c74e8a852a62f0dd28e2f8cba19e115723ccac73404652626f938a183c7f35fcb1a4f512aa3d41205a71fcf0dbfc1ee7b2d746ba72",
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
		"moneyKrabs", #dontTe11MyDad
		"Pearl Krabs",
		"73630002c59982959c234f167a6efc2d86751c8a3bd4f31b6a8f5c9b5ec06ac3e7007d4a7d443ba1be85fcc6649d9493ad81866cbb95e08b880d077b013e4799f779d9c57650349dd15be888667c8bb99f",
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
		"Screen", #OI01_getit?
		"Karen Plankton",
		"73630002778a20bbebcc649bb5fb2360516ca521e77f545363eba295ac3c2613dcac2fde249143e1eded04059e78505ff029ac57d61f9f83b8aa1b9029405aacaeb7f43b7050a05d4217d8a8b03aec",
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
		"SquarePants", #Soaked1and1Square
		"SpongeBob SquarePants",
		"736300027e532a4742c05e07f840210bfd9b1d5b90acacc6bd50c8d83d79c3e10a7903a80cda06d5085ad01f54c4d35be3a2585b9ca224cc34f815552512c5a791f2481c10defc469c67a0cd7a8fa0cd78da94e6c7",
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
