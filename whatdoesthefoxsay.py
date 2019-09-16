userint = ""
asound = []
fox = []

iterations = int(input())
for i in range(0,iterations):
	animalsounds = input()
	animalsounds = animalsounds.split()
	while(True):
		userint = input()
		if(userint == "what does the fox say?"):
			break
		else:
			parsed = userint.split()
			sound = parsed[2]
			asound.append(sound)
			parsed.clear()
	for a in animalsounds:
		if a not in asound:
			fox.append(a)
	for j in fox:
		print(j, end = " ")
	print()
	fox.clear()

"""

toot ba ba moo moo ma
a goes toot
b goes ba
c goes ma

list = toot ba ba moo ma
acc = toot ba ma



"""