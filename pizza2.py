import math
r,c = input().split()
r = int(r)
c = int(c)
pi = math.pi
circum1 = pi*r*r
circum2 = pi*(r-c)*(r-c)
print((circum2/circum1)*100)