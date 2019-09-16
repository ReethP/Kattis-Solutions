elements = {}
elements2 = {}
numlist = ['1','2','3','4','5','6','7','8','9','0']
element, number = input().split()
number = int(number)
elements = []
elements2 = []
numbers = []
numbers2 =[]
start = 0
end = 0
i = 0
while(i<len(element)):
	#Case that last element is a letter
	if(i == len(element)-1):
		if(element[i] not in elements):
			elements.append(element[i])
			numbers.append(1)
		else:
			a = elements.index(element[i])
			numbers[a] = numbers[a]+1
	#Case when single new atom pa lang
	elif(element[i] not in elements and element[i+1] not in numlist):
		elements.append(element[i])
		numbers.append(1)
	#Case when single old atom
	elif(element[i] in elements and element[i+1] not in numlist):
		a = elements.index(element[i])
		numbers[a] = numbers[a]+1
	#Case when new atom
	elif(element[i] not in elements and element[i+1] in numlist):
		elements.append(element[i])
		
		i = i+1
		start = i
		if(i == len(element)-1):
			newint = element[i]
		else:
			while(element[i+1] in numlist):
				i+=1
			newint = int(element[start:i+1])
		
		numbers.append(newint)
	#Case when old atom
	elif(element[i] in elements and element[i+1] in numlist):
		a = elements.index(element[i])
		i = i+1
		start = i
		if(i == len(element)-1):
			newint = element[i]
		else:
			while(element[i+1] in numlist):
				i+=1
			newint = int(element[start:i+1])
		numbers[a] = numbers[a]+ newint
	else:
		
		if(element[i+1] not in numlist):
			elements.append(element[i])
			numbers.append(1)
	i+=1


i = 0
element2 = input()
while(i<len(element2)):
	if(i == len(element2)-1):
		if(element2[i] not in elements2):
			elements2.append(element2[i])
			numbers2.append(1)
		else:
			a = elements2.index(element2[i])
			numbers2[a] = numbers2[a]+1
	#Case when single new atom pa lang
	elif(element2[i] not in elements2 and element2[i+1] not in numlist):
		elements2.append(element2[i])
		numbers2.append(1)
	#Case when single old atom
	elif(element2[i] in elements2 and element2[i+1] not in numlist):
		a = elements2.index(element2[i])
		numbers2[a] = numbers2[a]+1
	#Case when new atom
	elif(element2[i] not in elements2 and element2[i+1] in numlist):
		elements2.append(element2[i])
		i = i+1
		start = i
		if(i == len(element2)-1):
			newint = element2[i]
		else:
			while(element2[i+1] in numlist):
				i+=1
			newint = int(element2[start:i+1])
		numbers2.append(newint)
	#Case when old atom
	elif(element2[i] in elements2 and element2[i+1] in numlist):
		a = elements2.index(element2[i])
		i = i+1
		start = i
		if(i == len(element2)-1):
			newint = element2[i]
		else:
			while(element2[i+1] in numlist):
				i+=1
			newint = int(element2[start:i+1])
		numbers2[a] = numbers2[a]+ newint
	else:
		
		if(element2[i+1] not in numlist):
			elements2.append(element2[i])
			numbers2.append(1)
	i+=1

for l in range(0,len(numbers)):
	numbers[l] = int(numbers[l])*number

for y in range(0,len(numbers2)):
	numbers2[l] = int(numbers2[l])

run = 1
#check for elements currently not existing in the other
for q in elements2:
	if q not in elements:
		run = 0

allcounters = []
if(run == 1):
	for r in range(0,len(numbers)):
		copies = 0
		while(numbers[r] - numbers2[r])>=0:
			numbers[r] = numbers[r] - numbers2[r]
			copies+=1
		allcounters.append(copies)
allcounters = sorted(allcounters)
		# for s in range(0,len(numbers2)):
		# 	print(numbers)
		# 	print(numbers2)
		# 	numbers[r] = numbers[r]-numbers2[s]
		# counter = 0
		# for t in numbers:
		# 	if t<0:
		# 		continue
		# 	counter+=1
		# if counter == len(numbers)-1:
		# 	copies+=1
if(run == 1):
	print(allcounters[0])
else:
	print(0)