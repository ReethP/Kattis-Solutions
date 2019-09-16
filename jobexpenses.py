input()

holder = list(map(int,input().split()))

ans = 0
for i in holder:
	if i < 0:
		ans+= (i*-1)
print(ans)