def checker(lista):
	for i in range(0,len(lista)-1):
		if(lista[i] == lista[i+1]):
			return "no"
	return "yes"
mainin = list(input().split())
mainin.sort()
print(checker(mainin))