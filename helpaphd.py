n = int(input())
if n >=1 and n<=1000:
    for i in range (0,n):
        b = str(input())
        if b == "P=NP":
            print("skipped")
        else:
            x,y = b.split("+")
            print(int(x)+int(y))

