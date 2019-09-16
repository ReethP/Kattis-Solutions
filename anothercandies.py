iterations = int(input())
candies = []

for i in range(0,iterations):
	input()
	children = int(input())
	candies.clear()
	for j in range(0,children):
		userinp = int(input())
		candies.append(userinp)

	kids = len(candies)
	totalcandies = 0
	for candy in candies:
		totalcandies = totalcandies + candy
	possible = totalcandies%kids
	if(possible == 0):
		print("YES")
	else:
		print("NO")