numbers = []
for i in range(0,10):
	number = int(input())
	number = number%42
	if number not in numbers:
		numbers.append(number)
print(len(numbers))