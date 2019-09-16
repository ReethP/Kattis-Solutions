input()
mainlist = list(map(int,input().split()))
smallest = mainlist[0]
for k in mainlist:
	if k<smallest:
		smallest = k
print(mainlist.index(smallest))