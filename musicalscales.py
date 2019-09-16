scale = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

scaling = []

song = []

numscale = [2,2,1,2,2,2,1]
possiblescales = []
numnotes = int(input())

notes = input()
notes = notes.split()

for i in notes:
	if i not in song:
		song.append(i)

indexing = 0
inscale = 1
for j in range(0,len(scale)):
	for k in numscale:
		indexing = indexing+k
		if indexing+j > 11:
			indexing = indexing-12
		scaling.append(scale[indexing+j])
	indexing = 0
	for element in song:
		if element not in scaling:
			inscale = 0
	if inscale == 1:
		possiblescales.append(scale[j])
	inscale = 1
	scaling.clear()

if(len(possiblescales)!= 0):
	for p in possiblescales:
		print(p, end = " ")
	print()
else:
	print("none")