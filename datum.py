import datetime
a = list(map(int,input().split()))
x = datetime.datetime(2009,a[1],a[0])
print(x.strftime("%A"))