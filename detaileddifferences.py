itera = int(input())
for i in range(0,itera):
	a = input()
	b = input()
	checker = []
	for k in range(0,len(a)):
		if(a[k] == b[k]):
			checker.append(".")
		else:
			checker.append("*")
	print(a)
	print(b)
	print(''.join(checker))