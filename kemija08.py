vowels = ['a','e','i','o','u']
sentence = input()
word = []
i = 0
while i < len(sentence):
	if(sentence[i] in vowels):
		word.append(sentence[i])
		i+=3
	else:
		word.append(sentence[i])
		i+=1
print(''.join(word))
