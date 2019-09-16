mainlist = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_','.']
while True:
	try:
		uints = input().split()
		rotate = int(uints[0])
		string = uints[1]
		string = list(string[::-1])
		for i in range(0,len(string)):
			elint = mainlist.index(string[i])+rotate
			while(elint>=len(mainlist)):
				elint-=len(mainlist)
			string[i] = mainlist[elint]
		print(''.join(string))
	except:
		break