iterations = int(input())
totalsecs = 0
totalmins = 0
for i in range(0,iterations):
	minu,secs = input().split()
	minu = int(minu)
	secs = int(secs)
	minu = minu*60
	totalsecs += secs
	totalmins += minu
ansholder = totalsecs/totalmins
if(ansholder<=1):
	print("measurement error")
else:
	print(ansholder)