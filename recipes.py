recipes = int(input())
for i in range(0,recipes):
	ingreddetails = []
	numlist = list(map(int,input().split()))
	ingredients = numlist[0]
	ogservings = numlist[1]
	desiredservings = numlist[2]
	scalingfactor = desiredservings/ogservings
	scaledWeightMainIng = 0
	for j in range(0,ingredients):
		ing = input().split()
		ing[1] = float(ing[1])
		ing[2] = float(ing[2])
		if(ing[2]) == 100:
			scaledWeightMainIng = ing[1]*scalingfactor
		for k in ing:
			ingreddetails.append(k)
	print("Recipe #",i+1)
	for k in range(0,len(ingreddetails),3):
		print(ingreddetails[k],(ingreddetails[k+2]*scaledWeightMainIng)/100)
	print("----------------------------------------")

