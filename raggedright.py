paragraph = []
try:
	while True:
		line = input()
		paragraph.append(line)
except:
	longest = 0
	raggscore = 0
	for i in paragraph:
		length = len(i)
		if length > longest:
			longest = length
	for i in range(0,len(paragraph)-1):
		lengthofpar = len(paragraph[i])
		if(lengthofpar != longest):
			raggscore = raggscore + (longest-lengthofpar)**2
	print(raggscore)