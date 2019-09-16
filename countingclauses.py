clauses, num = input().split()
clauses = int(clauses)
num = int(num)

for i in range(0,clauses):
	f,s,t = input().split()
if(clauses < 8):
	print("unsatisfactory")
else:
	print("satisfactory")