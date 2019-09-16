a = 0
m = int(input())
n = [i for i in input().split(" ")]
for i in n:
    b = int(i)
    if b < 0:
        a+=1
print(a)
