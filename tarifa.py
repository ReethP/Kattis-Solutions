a = int(input()) #Number of megabytes allowed per month
b = int(input()) #N months using plan
d = []
for c in range (0,b):
    e = int(input())
    d.append(e)
f = sum(d)
g = a*b
h = g-f
print(h+a)
