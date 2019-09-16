iterations = int(input())

if(iterations == 0):
	print(1,0)
elif(iterations == 1):
	print(0,1)
elif(iterations ==2):
	print(1,1)
else:
	loops = iterations-2
	acounter = 1
	bcounter = 1
	for i in range(0,loops):
		hold = acounter
		acounter = bcounter
		bcounter = bcounter+hold
	print(acounter,bcounter)