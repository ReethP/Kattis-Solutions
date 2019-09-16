fulllist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
spechars = ['?','.',"'",'"',',','!']
numberlist = ['0','9','8','7','6','5','4','3','2','1']
iterations = int(input())
for i in range(0,iterations):
	letterlist = []
	uint = input()
	uint = uint.lower()
	for j in uint:
		if j not in letterlist and j not in spechars and j != ' ' and j not in numberlist:
			letterlist.append(j)
	if(len(letterlist) == 26):
		print("pangram")
	else:
		missinglist = []
		for k in fulllist:
			if k not in letterlist:
				missinglist.append(k)
		missing = ''.join(missinglist)
		print("missing", missing)