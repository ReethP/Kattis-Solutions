import math

iterations, l, w = map(int,input().split())
matches = []
for i in range(0,iterations):
	match = int(input())
	matches.append(match)

longest = math.sqrt(l*l+w*w)
for k in matches:
	if k>longest:
		print("NE")
	else:
		print("DA")