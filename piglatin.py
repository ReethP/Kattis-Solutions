try:
	vowels = ["a","e","i","o","u","y"]
	while True:
		sentence = input().split()
		newsentence = []
		for i in sentence:
			if i[0] not in vowels:
				newword = ""
				j = 0
				while i[j] not in vowels:
					j+=1
				newword =  i[j:]+i[0:j]+"ay"
			else:
				newword = i+"yay"
			newsentence.append(newword)
		print(' '.join(newsentence))
except:
	pass