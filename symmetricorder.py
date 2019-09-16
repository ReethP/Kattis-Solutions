uinput = 1
setnum = 1
while(uinput != 0):
	uinput = int(input())
	if(uinput == 0):
		break
	namelist1 = []
	namelist2 = []
	for i in range(2,uinput+2):
		name = input()
		if(i%2==0):
			namelist1.append(name)
		else:
			namelist2.append(name)
	namelist2 = namelist2[::-1]
	print("SET",setnum)
	for k in namelist1:
		print(k)
	for j in namelist2:
		print(j)
	setnum+=1
