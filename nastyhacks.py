itera = int(input())
for i in range(0,itera):
	inp = list(map(int,input().split()))
	r = inp[0]
	e = inp[1]
	c = inp[2]
	total1 = r+c
	check = e-total1
	if(check == 0):
		print("does not matter")
	elif(check>0):
		print("advertise")
	else:
		print("do not advertise")