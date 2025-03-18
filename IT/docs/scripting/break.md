# Break
`break` consente di fermare un loop in anticipo. Quando l'istruzione `break` viene raggiunta, uscirà immediatamente dal loop più interno e inizierà a eseguire il codice dopo il loop.

`for i in range(10):
	break
print(i)`
Questo stampa `0` perché `i` è `0` nella prima iterazione del loop e poi l'istruzione break termina il loop.

Funziona anche nei loop `while`.

`while True:
	if can_harvest():
		break`

Questo codice esegue il loop `while` finché `can_harvest()` non è `True`.
Ha lo stesso effetto di

`while not can_harvest():
	pass`

Nei loop annidati, `break` esce sempre dal loop più interno.

`for i in range(10):
	for j in range(10):
		break
		print("this is never printed")
	print("this is printed 10 times")`