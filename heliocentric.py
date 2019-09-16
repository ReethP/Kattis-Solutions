while True:
	try:
		for i in range(0,10):
			earth, mars = input().split()
			earth = int(earth)
			mars = int(mars)

			totaldays = 0

			while(earth != mars):
				earth = earth+1
				mars = mars+1
				totaldays = totaldays+1
				if(earth == 365):
					earth = 0
				if(mars == 687):
					mars = 0

			print("Case",i+1,end="")
			print(":", totaldays)

	except:
		break