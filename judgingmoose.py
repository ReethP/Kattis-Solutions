uin = list(map(int,input().split()))
a = uin[0]
b = uin[1]
if(a==0 and b==0):
	print("Not a moose")
elif(a==b):
	print("Even",a*2)
else:
	if(a>b):
		print("Odd", a*2)
	else:
		print("Odd", b*2)