costumes = {}
finalist = []
iterations = int(input())

for i in range(0,iterations):
	costume = input()
	if costume not in list(costumes.keys()):
		costumes[costume] = 1
	else:
		costumes[costume]+=1
minimum = min(list(costumes.values()))
for i in list(costumes.keys()):
	if costumes[i] == minimum:
		finalist.append(i)
finalist.sort()
for i in finalist:
	print(i)