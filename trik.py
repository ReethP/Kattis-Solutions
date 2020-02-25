moves = [[1,2],[2,3],[1,3]]
location = 1
movelist = list(input())
for i in movelist:
	if(i == "A" and location in moves[0]):
		if(location == moves[0][0]):
			location = moves[0][1]
		else:
			location = moves[0][0]
	elif(i == "B" and location in moves[1]):
		if(location == moves[1][0]):
			location = moves[1][1]
		else:
			location = moves[1][0]
	elif(i == "C" and location in moves[2]):
		if(location == moves[2][0]):
			location = moves[2][1]
		else:
			location = moves[2][0]
	else:
		continue
print(location)