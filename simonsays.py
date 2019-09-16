iterations = int(input())
for i in range(0,iterations):
	simon = input()
	if(len(simon) >= 12):
		if(simon[0:10] == "Simon says"):
			print(simon[11:])