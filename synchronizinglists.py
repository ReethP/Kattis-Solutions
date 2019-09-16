while True:
	firstint = int(input())
	if(firstint == 0):
		break
	else:
		list1 = []
		list2 = []
		list3 = []
		list4 = []
		list5 = []
		for i in range(0,firstint):
			uint = int(input())
			list1.append(uint)
			list2.append(uint)
		list2 = sorted(list2)
		for j in list2:
			a = list1.index(j)
			list3.append(a)
		# print(list3)
		for k in range(0,firstint):
			uint = int(input())
			list4.append(uint)
			list5.append(0)
		list4 = sorted(list4)
		for l in range(0,firstint):
			list5[list3[l]] = list4[l]
		for m in list5:
			print(m)