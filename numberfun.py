iters = int(input())
for i in range(iters):
	nums = list(map(int,input().split()))
	if(nums[0] + nums[1] == nums[2]):
		print("Possible")
		continue
	if(nums[0] - nums[1] == nums[2]):
		print("Possible")
		continue
	if(nums[1] - nums[0] == nums[2]):
		print("Possible")
		continue
	if(nums[0] * nums[1] == nums[2]):
		print("Possible")
		continue
	if(nums[0] / nums[1] == nums[2]):
		print("Possible")
		continue
	if(nums[1] / nums[0] == nums[2]):
		print("Possible")
		continue
	print("Impossible")

