iterations = int(input())
days = []
for i in range(0,iterations):
	day1, day2 = map(int,input().split())
	for j in range(day1,day2+1):
		if j not in days:
			days.append(j)
print(len(days))