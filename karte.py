uint = input()
length = len(uint)
for i in range(0,length,3):
	if(i==0):
		continue
	else:
		holder = i-3
	print(uint[holder:i])
print(uint[length-3:length])