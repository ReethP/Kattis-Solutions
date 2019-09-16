periods = int(input())

tqaly = 0
for i in range(0,periods):
	qal, years = input().split()
	qal = float(qal)
	years = float(years)
	tqaly = (qal*years)+tqaly

print(tqaly)
