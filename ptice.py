adrian = ['A','B','C']
bruno = ['B','A','B','C']
goran = ['C','C','A','A','B','B']
right = [0,0,0]
input()
sequence = input()
for i in range(len(sequence)):
	if(sequence[i] == bruno[i%4]):
		right[1]+=1
	if(sequence[i] == adrian[i%3]):
		right[0]+=1
	if(sequence[i] == goran[i%6]):
		right[2]+=1
largest = max(right)
print(largest)
for i in range(3):
	if(right[i] == largest):
		if(i==0):
			print("Adrian")
		if(i==1):
			print("Bruno")
		if(i==2):
			print("Goran")