answers = []
iterations = int(input())
for i in range(iterations):
	inp = input().split()
	try:
		num = int(inp[0])/2
		color = inp[1]
	except:
		num = int(inp[1])
		color = inp[0]
	answers.append([num,color])
answers.sort(key = lambda answers:answers[0])
for i in answers:
	print(i[1])