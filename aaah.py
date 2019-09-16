jon = input()
doctor = input()
jonlen = 0
doclen = 0

for element in jon:
	if element == 'a':
		jonlen = jonlen+1

for element2 in doctor:
	if element2 == 'a':
		doclen = doclen+1

if jonlen>=doclen:
	print("go")
else:
	print("no")