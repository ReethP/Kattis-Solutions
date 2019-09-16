def reversi(bina):
	newnum = ['0','b']
	bina = bina[::-1]
	for j in bina:
		newnum.append(j)
	finalnum = ''.join(newnum)
	print(int(finalnum,2))
inputs = int(input())
userint = bin(inputs)
reversi(userint[2:])