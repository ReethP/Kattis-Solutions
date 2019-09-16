def factorial(a):
	if a==0:
		return 1
	else:
		return a * factorial(a-1)
itera = int(input())
for i in range(0,itera):
	a = int(input())
	a = factorial(a)
	a = str(a)
	a = a[-1]
	print(a)