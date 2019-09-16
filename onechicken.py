a,b = input().split()
a = int(a)
b = int(b)
# print(a-b)
if(b-a>0 and (b-a)!=1):
	print("Dr. Chaz will have",b-a,"pieces of chicken left over!")
elif((b-a)==1):
	print("Dr. Chaz will have",b-a,"piece of chicken left over!")
elif((a-b)==1):
	print("Dr. Chaz needs",a-b,"more piece of chicken!")
else:
	print("Dr. Chaz needs",a-b,"more pieces of chicken!")