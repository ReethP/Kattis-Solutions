tasks, time = map(int,input().split())
inputs = list(map(int,input().split()))
inputs = inputs[::-1]
# print(inputs)
completed = 0
while True:
	if(len(inputs) > 0):
		newnum = inputs.pop()
		if(time-newnum>=0):
			time = time - newnum
			completed += 1
		else:
			break
	else:
		break
print(completed)
