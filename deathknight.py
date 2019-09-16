iterations = int(input())
wins = 0
for i in range(0,iterations):
	battle = input()
	counter = 0
	for j in range(0,len(battle)-1):
		if(battle[j] == "C" and battle[j+1] == "D"):
			break
		counter+=1
	if(counter == len(battle)-1):
		wins+=1
print(wins)
