try:
	while True:
		a = list(map(int,input().split()))
		for i in range(0,len(a)):
			if i == 0:
				if(sum(a[1:]) == a[0]):
					print(a[0])
					break
			if i == len(a):
				# print(i)
				if(sum(a[:i-1]) == a[i-1]):
					print(a[-1])
					break
			else:
				# print(sum(a[0:i],sum(a[i+1:len(a)])))
				if(sum(a[0:i])+sum(a[i+1:len(a)]) == a[i]):
					print(a[i])
					break
except:
	pass