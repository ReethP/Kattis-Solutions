try:
	userinput = 0
	while(userinput != ''):
		userinput = input()
		a,b = userinput.split()
		a = int(a)
		b = int(b)
		c = a-b
		if(c<0):
			c = c*(-1)
		print(c)
except:
	pass