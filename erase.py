passes = int(input())
firsthold = input()
second = input()
first = []
for p in range(0,len(firsthold)):
	first.append(firsthold[p])

for j in range(0,passes):
	for i in range(0,len(first)):
		if(first[i] == "1"):
			first[i] = "0"
		else:
			first[i] = "1"

first = "".join(first)
if(first == second):
	print("Deletion succeeded")
else:
	print("Deletion failed")