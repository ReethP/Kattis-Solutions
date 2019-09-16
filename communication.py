def oppxor(og, shifted):
	# print(og,shifted)
	newnum = ['0','b']
	for j in range(0,len(shifted)):
		if(og[j] == shifted[j]):
			newnum.append('1')
		else:
			newnum.append('0')
	print(int(''.join(newnum),2))
input()
inputs = list(map(int,input().split()))
for el in inputs:
	el2 =[]
	holder2 = []
	holder = el
	el = el>>1
	holder = bin(holder)
	el = bin(el)
	for i in holder:
		holder2.append(i)
	for j in el:
		el2.append(j)
	el2.insert(2,'0')
	el2 = el2[2:]
	holder2 = holder2[2:]
	# print(holder2)
	# print(el2)
	oppxor(holder2,el2)
