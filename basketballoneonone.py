game = input()
apoint = 0
bpoint = 0
for i in range((len(game)-1)):
	if(game[i] == 'A'):
		apoint+=int(game[i+1])
	elif(game[i] == 'B'):
		bpoint+=int(game[i+1])
	else:
		continue
if(apoint>bpoint):
	print("A")
else:
	print("B")


