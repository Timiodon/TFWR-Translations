# Continue
`continue` permette di interrompere l'iterazione corrente di un ciclo e saltare alla successiva iterazione del ciclo più interno.

`for i in range(10):
	continue
    print("questo non viene mai stampato")`

Questo esegue tutte le `10` iterazioni del ciclo, ma l'istruzione `print` dopo `continue` viene sempre saltata.

Funziona anche con i cicli `while`.

`while True:
	if not can_harvest():
		continue
    
    harvest()`

Questo codice chiama `harvest()` solo quando `can_harvest()` è `True`.
Ha lo stesso effetto di

`while True:
	if can_harvest():
		harvest()`

Nei cicli annidati, `continue` influisce sempre sul ciclo più interno.

`for i in range(10):
	for j in range(10):
	    print("questo viene stampato 100 volte")
		continue
		print("questo non viene mai stampato")
	print("questo viene stampato 10 volte")`