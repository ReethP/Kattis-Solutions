iterations = int(input())
steps = 0
for i in range(0,iterations):
	userint = []
	rawint = map(int,input().split())
	for a in rawint:
		userint.append(a)
	userint.pop(0)
	# userint = userint[::-1]
	# print(userint)
	run = 1
	top = len(userint)-1
	counter = top
	c3 = 1
	while(run):
		c1 = 0
		c2 = 1
		while(c1!=top):
			while(c2!=top):
				while(userint[counter-c1]<userint[counter-c2]):
						temp = userint[counter-c1]
						userint[counter-c1] = userint[counter-c2]
						userint[counter-c2] = temp
						counter-=1
						steps+=1
						c1 = c1+1
						c2 = c2+1
						if(counter == -1):
							break
		if(userint[counter-c1]<userint[counter-c2]):
			counter = top
		else:
			counter = top-c3
			c3 = c3+1
			print(c3,counter)
		if(c3 == top or c3 == 30):
			break

print(userint)
print(steps)