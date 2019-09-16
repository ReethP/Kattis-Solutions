numads = int(input())
for j in range(0,numads):
	adventure = input()
	checker = 0
	counter = len(adventure)
	money = 0
	incense = 0
	gem = 0
	item = 0
	bag = []
	succ = 1
	for i in adventure:
		checker +=1
		if(i == "$"):
			bag.append("$")
		elif(i == "|"):
			bag.append("I")
		elif(i == "*"):
			bag.append("G")
		elif(i == "t"):
			if(len(bag) == 0):
				succ = 0
				break
			item = bag.pop()
			if(item != "I"):
				succ = 0
				break
		elif(i == "j"):
			if(len(bag) == 0):
				succ = 0
				break
			item = bag.pop()
			if(item != "G"):
				succ = 0
				break
		elif(i == "b"):
			if(len(bag) == 0):
				succ = 0
				break
			item = bag.pop()
			if(item != "$"):
				succ = 0
				break
		else:
			continue

	if(len(bag) == 0 and checker == counter and succ == 1):
		print("YES")
	else:
		print("NO")