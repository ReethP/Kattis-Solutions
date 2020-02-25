nums = list(map(int,input().split()))
maximum = nums[0]
current = 0
reject = 0
for i in range(nums[1]):
	line = input().split()
	num = int(line[1])
	if(line[0] == "enter" and current+num <= maximum):
		current = current+num
	elif(line[0] == "enter"):
		reject+=1
	else:
		current-=num

print(reject)