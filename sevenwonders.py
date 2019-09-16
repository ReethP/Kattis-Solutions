userint = input()
t = 0
c = 0
g = 0
for k in userint:
	if k == "T":
		t+=1
	elif k == "C":
		c+=1
	else:
		g+=1
# print(t,c,g)
points = (t**2)+(c**2)+(g**2)
while(t>0 and c>0 and g>0):
	t-=1
	c-=1
	g-=1
	points+=7
print(points)