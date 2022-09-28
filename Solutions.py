a = int(input("Veuillez entrer A : "))
b = int(input("Veuillez entrer B : "))

if b != 0:
    if a != 0:
	    print("L'équation admet une solution unique, cette solution est ","-",b,"/",a,"=",(-b/a))
    else:
	    print("L'équation n'admet pas de solution")
else:
    if a != 0:
    	print("L'équation admet 0 pour solution, S = 0")
    else:
    	print("L'équation admet une infinité de solution")
