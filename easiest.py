while(True):
	num = input()
	number = int(num)
	inp = list(map(int,num))
	if(inp[0] == 0 and len(inp) == 1):
		break
	total = -1
	iterator = 11
	while(total!=sum(inp)):
		newnumber = number*iterator
		total = sum(map(int,list(str(newnumber))))
		iterator+=1
	iterator-=1
	print(iterator)

