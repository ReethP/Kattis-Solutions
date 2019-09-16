player1 = input()
player2 = input()

letlist = []
for x in player1:
	if x not in letlist:
		letlist.append(x)
length = len(letlist)

wrongcounter = 0
rightcounter = 0
for y in player2:
	if y in letlist:
		rightcounter = rightcounter+1
	else:
		wrongcounter = wrongcounter+1
	if wrongcounter >=10:
		print("LOSE")
		break
	if rightcounter == length:
		print("WIN")
		break

