try:
	while True:
		sentence = input()
		sentence = sentence.lower()
		success = 0
		for i in range(0,len(sentence)):
			if sentence[i] == 'p':
				if sentence[i:i+7] == "problem":
					success = 1
					break
		if(success == 1):
			print("yes")
		else:
			print("no")
except:
	pass