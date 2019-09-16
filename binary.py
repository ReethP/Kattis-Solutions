def binsearch(jack,lenjack,cdjill):
	lower = 0
	upper = lenjack-1
	while(lower <= upper):
		middle = (lower+upper)//2;
		if cdjill>jack[middle]:
			lower = middle+1
		elif cdjill < jack[middle]:
			upper = middle-1
		else:
			return 1

jack = [0,1,2,3,4,5,6]
lenjack = 7
cdjill = 9
print(binsearch(jack,lenjack,cdjill))