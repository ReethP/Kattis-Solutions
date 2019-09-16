list1 = list(map(int,input().split()))
num1 = list1[0]
num2 = list1[1]
num3 = list1[2]

if((num1+num2)==num3):
	print(num1,"+",num2,"=",num3,sep='')
elif((num1-num2)==num3):
	print(num1,"-",num2,"=",num3,sep='')
elif((num1*num2)==num3):
	print(num1,"*",num2,"=",num3,sep='')
elif((num1/num2)==num3):
	print(num1,"/",num2,"=",num3,sep='')
elif(num1==(num2+num3)):
	print(num1,"=",num2,"+",num3,sep='')
elif(num1==(num2-num3)):
	print(num1,"=",num2,"-",num3,sep='')
elif(num1==(num2*num3)):
	print(num1,"=",num2,"*",num3,sep='')
elif(num1==(num2/num3)):
	print(num1,"=",num2,"/",num3,sep='')
else:
	print("")