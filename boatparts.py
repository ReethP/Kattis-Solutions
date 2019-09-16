nums = list(map(int,input().split()))
parts = nums[0]
days = nums[1]
counter = 0
partslist = []
success = 0

for i in range(0,days):
	part = input()
	if part not in partslist:
		partslist.append(part)
		counter = i+1
if len(partslist) == parts:
	print(counter)
else:
	print("paradox avoided")
