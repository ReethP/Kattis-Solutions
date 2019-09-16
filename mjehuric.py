def swap(alist, index):
	temp = alist[index+1]
	alist[index+1] = alist[index]
	alist[index] = temp

def sorter(alist):
	c = [1,2,3,4,5]
	while(not(alist == c)):
		for i in range(0,4):
			if(alist[i] > alist[i+1]):
				swap(alist, i)
				for a in alist:
					print(a, end = " ")
				print()
userinput = input()
alist = []
for j in userinput.split():
	alist.append(int(j))
sorter(alist)

