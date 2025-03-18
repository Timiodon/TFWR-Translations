# Continue
continue permette di interrompere l'iterazione corrente di un ciclo e saltare alla prossima iterazione del ciclo più interno.

`for i in range(10):
	continue
    print("this is never printed")`

Questo esegue tutte le `10` iterazioni del ciclo, ma l'istruzione `print` dopo il `continue` viene sempre saltata.

Funziona anche nei cicli `while`.

`while True:
	if not can_harvest():
		continue
    
    harvest()`

Questo codice chiama `harvest()` solo quando `can_harvest()` è `True`.
Ha lo stesso effetto di

`while True:
	if can_harvest():
		harvest()`

Nei cicli annidati, `continue` influenza sempre il ciclo più interno.

`for i in range(10):
	for j in range(10):
	    print("this is printed 100 times")
		continue
		print("this is never printed")
	print("this is printed 10 times")`