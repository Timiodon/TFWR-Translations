# Break
`break` permette di interrompere un ciclo in anticipo. Quando viene raggiunta l'istruzione `break`, uscirà immediatamente dal ciclo più interno e inizierà a eseguire il codice dopo il ciclo.

`for i in range(10):
	break
print(i)`
Questo stampa `0` perché `i` è `0` nella prima iterazione del ciclo e poi l'istruzione break termina il ciclo.

Funziona anche con i cicli `while`.

`while True:
	if can_harvest():
		break`

Questo codice esegue il ciclo `while` finché `can_harvest()` non è `True`.
Ha lo stesso effetto di

`while not can_harvest():
	pass`

Nei cicli annidati `break` esce sempre dal ciclo più interno.

`for i in range(10):
	for j in range(10):
		break
		print("questo non viene mai stampato")
	print("questo viene stampato 10 volte")`