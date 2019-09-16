gold, silver, copper = input().split()
gold = int(gold)
silver = int(silver)
copper = int(copper)
buyingpower = gold*3+silver*2+copper*1

victory = ""
treasure = ""
if(buyingpower >= 6):
	treasure = "Gold"
elif(buyingpower >=3):
	treasure = "Silver"
elif(buyingpower >=0):
	treasure = "Copper"
else:
	treasure =""

if(buyingpower >= 8):
	victory = "Province"
elif(buyingpower >=5):
	victory = "Duchy"
elif(buyingpower >=2):
	victory = "Estate"
else:
	victory = ""

if(treasure != ""):
	if(victory != ""):
		print(victory,"or",treasure)
	else:
		print(treasure)
else:
	if(victory!= ""):
		print(victory)
	else:
		print(treasure)