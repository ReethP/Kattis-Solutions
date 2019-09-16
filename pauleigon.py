uint = list(map(int,input().split()))
consec = uint[0]
score1 = uint[1]
score2 = uint[2]
counter = 0
if ((score1+score2)//consec)%2 == 0:
	print("paul")
else:
	print("opponent")