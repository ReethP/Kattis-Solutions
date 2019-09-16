uint = list(map(int,input().split()))
empty = uint[0]
bottle = uint[1]
req = uint[2]
total = empty+bottle
drank = 0
drink = 0
while(total>=req):
	drink = total//req
	total = total%req
	total = total+drink
	drank = drank+drink
print(drank)