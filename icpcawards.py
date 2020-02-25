winners = []
origins = []
iters = int(input())
totalw = 0
for i in range(iters):
	team = input()
	origin = team.split()[0]
	if origin not in origins:
		origins.append(origin)
		winners.append(team)
for i in range(len(winners)):
	if(i==12):
		break
	print(winners[i])