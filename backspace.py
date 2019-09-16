stack = []

userint = input()

for i in userint:
	if i == "<":
		stack.pop()
	else:
		stack.append(i)

if(len(stack) != 0):
	for j in stack:
		print(j, end = "")
	print()