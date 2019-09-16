hour,minute = map(int,input().split())
minute = minute-45
if(minute < 0):
	minute = minute+60
	hour = hour-1
	if(hour == -1):
		hour = 23
print(hour,minute)