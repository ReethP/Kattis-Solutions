userinputs = input()
h, w, nbricks = userinputs.split()
h = int(h)
w = int(w)
nbricks = int(nbricks)

bricklist = []

bricks = input()
for x in bricks.split():
	bricklist.append(int(x))

walllist = []

for i in range(0,h):
	walllist.append(w)

iterator = 0

for j in bricklist:
	walllist[iterator] = walllist[iterator] - j
	if(walllist[iterator] == 0):
		if((walllist[iterator] == 0) and (iterator == (h-1))):
			print("YES")
			break
		else:
			iterator = iterator+1
			continue
	elif(walllist[iterator] < 0):
		print("NO")
		break