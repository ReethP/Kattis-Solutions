newalphabet = {"a":"@", "b":"8","c":"(","d":"|)",
				"e":"3","f":"#","g":"6","h":"[-]"
				,"i":"|","j":"_|","k":"|<","l":"1"
				,"m":"[]\/[]","n":"[]\[]","o":"0","p":"|D"
				,"q":"(,)","r":"|Z","s":"$","t":"']['"
				,"u":"|_|","v":"\/","w":"\/\/","x":"}{"
				,"y":"`/","z":"2"," ":" "}

userinput = input()
userinput = userinput.lower()



newstring = []
for i in userinput:
	if i in newalphabet.keys():
		newstring.append(newalphabet[i])
	else:
		newstring.append(i)

for q in newstring:
	print(q, end = "")
print()