itera = int(input())
for i in range(0,itera):
	itera2 = int(input())
	cities = []
	for k in range(0,itera2):
		city = input()
		if city not in cities:
			cities.append(city)
	print(len(cities))