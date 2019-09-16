pay = list(map(int,input().split()))
p1 = pay[0]
p2 = pay[1]
p3 = pay[2]

trucks = []
for i in range(0,3):
	a1,a2 = input().split()
	trucks.append(int(a1))
	trucks.append(int(a2))

minimum = min(trucks)
maximum = max(trucks)

counter = 0
pay = 0
while(minimum<maximum+1):
	if(minimum == trucks[0]):
		counter+=1
	if(minimum == trucks[1]):
		counter-=1
	if(minimum == trucks[2]):
		counter+=1
	if(minimum == trucks[3]):
		counter-=1
	if(minimum == trucks[4]):
		counter+=1
	if(minimum == trucks[5]):
		counter-=1
	if(counter == 1):
		pay = pay+(p1*counter)
	if(counter == 2):
		pay = pay+(p2*counter)
	if(counter == 3):
		pay = pay+(p3*counter)
	minimum+=1
print(pay)