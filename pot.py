iterations = int(input())

thesum = 0
for i in range(0,iterations):
	num = input()
	lastnum = int(num[len(num)-1])
	num = int(num[0:len(num)-1])
	thesum = thesum + (num**lastnum)
print(thesum)