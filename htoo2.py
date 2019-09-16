elements = {}
elements2 = {}
numlist = ['1','2','3','4','5','6','7','8','9','0']
element, number = input().split()
number = int(number)
start = 0
end = 0
i = 0
while(i<len(element)):
	#Case that last element is a letter
	if(i == len(element)-1):
		if(element[i] not in elements):
			elements[element[i]] = 1
		else:
			elements[element[i]] = elements[element[i]]+1
	#Case when single new atom pa lang
	elif(element[i] not in elements and element[i+1] not in numlist):
		elements[element[i]] = 1
	#Case when single old atom
	elif(element[i] in elements and element[i+1] not in numlist):
		elements[element[i]] = elements[element[i]]+1
	#Case when new atom
	elif(element[i] not in elements and element[i+1] in numlist):
		elkey = element[i]
		
		i = i+1
		start = i
		if(i == len(element)-1):
			newint = int(element[i])
		else:
			while(i != len(element)-1 and element[i+1] in numlist):
				i+=1
			newint = int(element[start:i+1])
		elements[elkey] = newint
	#Case when old atom
	elif(element[i] in elements and element[i+1] in numlist):
		elkey = element[i]
		i = i+1
		start = i
		if(i == len(element)-1):
			newint = int(element[i])
		else:
			while(i != len(element)-1 and element[i+1] in numlist):
				i+=1
			newint = int(element[start:i+1])
		elements[elkey] = elements[elkey]+newint
	else:
		if(element[i+1] not in numlist):
			elements[element[i]] = 1
	i+=1


i = 0
element2 = input()

while(i<len(element2)):
	#Case that last element is a letter
	if(i == len(element2)-1):
		if(element2[i] not in elements2):
			elements2[element2[i]] = 1
		else:
			elements2[element2[i]] = elements2[element2[i]]+1
	#Case when single new atom pa lang
	elif(element2[i] not in elements2 and element2[i+1] not in numlist):
		elements2[element2[i]] = 1
	#Case when single old atom
	elif(element2[i] in elements2 and element2[i+1] not in numlist):
		elements2[element2[i]] = elements2[element2[i]]+1
	#Case when new atom
	elif(element2[i] not in elements2 and element2[i+1] in numlist):
		elkey = element2[i]
		
		i = i+1
		start = i
		if(i == len(element2)-1):
			newint = int(element2[i])
		else:
			while(i != len(element2)-1 and element2[i+1] in numlist):
				i+=1
			newint = int(element2[start:i+1])
		elements2[elkey] = newint
	#Case when old atom
	elif(element2[i] in elements2 and element2[i+1] in numlist):
		elkey = element2[i]
		i = i+1
		start = i
		if(i == len(element2)-1):
			newint = int(element2[i])
		else:
			while(i != len(element2)-1 and element2[i+1] in numlist):
				i+=1
			newint = int(element2[start:i+1])
		elements2[elkey] = elements2[elkey]+newint
	else:
		if(element2[i+1] not in numlist):
			elements2[element2[i]] = 1
	i+=1

for l,o in elements.items():
	elements[l] = elements[l]*number

run = 1
#check for elements currently not existing in the other
for p in elements2.keys():
	if p not in elements.keys():
		run = 0
allc=0
if(run == 1):
	stop = 0
	while(stop!=1):
		for d in elements.keys():
			if d in elements2.keys():
				if(elements[d]-elements2[d]>=0):
					elements[d] = elements[d]-elements2[d]
				else:
					stop = 1
		allc = allc+1


if(run == 1):
	print(allc-1)
else:
	print(0)