dotype, uint = input().split()
if(dotype == "E"):
	holder = ''
	counter = 1
	for i in range(0,len(uint)):
		if(i != len(uint)-1 and uint[i] == uint[i+1]):
			counter+=1
		else:
			holder = holder+uint[i]+str(counter)
			counter = 1
	print(holder)
else:
	holder = ''
	for i in range(0,len(uint)):
		try:
			num = int(uint[i])
			letter = uint[i-1]
			for i in range(0,num):
				holder = holder+letter
		except:
			continue
	print(holder)
