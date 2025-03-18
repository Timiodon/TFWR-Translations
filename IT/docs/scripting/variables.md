# Variabili
Le variabili possono essere pensate come contenitori nominati che possono contenere un valore. L'operatore `=` è usato per dichiarare una variabile e memorizzare un valore al suo interno.

`variable_name = value`

Il lato sinistro dell'operatore è il nome della variabile. Puoi dargli qualsiasi nome tu voglia. Il lato destro è un'espressione il cui valore risultante verrà memorizzato nella variabile.

Dichiara una variabile chiamata `a` e memorizza il valore `5` in essa: `a = 5`  
Dichiara una variabile chiamata `b` e memorizza il valore di ritorno di `can_harvest()` in essa: `b = can_harvest()`

Non confondere l'operatore `=` con l'operatore `==`. L'operatore `==` verifica se due valori sono uguali e restituisce `True` o `False`. L'operatore `=` assegna il valore a destra al nome a sinistra.

Dopo che una variabile è stata assegnata, puoi usarla nel codice per recuperare il valore che contiene.

`a = 5
for i in range(a):
	do_a_flip()`

Il ciclo sopra viene eseguito 5 volte perché `a` è impostato su `5`. La `i` nel ciclo `for` è anche una variabile che viene automaticamente assegnata al valore corrente della sequenza a ogni iterazione del ciclo. (Non deve essere chiamata `i`, puoi darle qualsiasi nome di variabile valido.)

Le variabili ti permettono di fare la stessa cosa con un ciclo while:

`a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1`

Questo fa la stessa cosa del ciclo for sopra. Dobbiamo solo incrementare i manualmente. Nota che per incrementare i, lo impostiamo sul suo valore precedente più `1`. Cambiare il valore di una variabile basato sul suo valore precedente è qualcosa di molto comune. Può essere abbreviato usando questi operatori: `+=, -=, *=, /=, %=`

`i = i + 1` è lo stesso di `i += 1`  
`a = a / 3` è lo stesso di `a /= 3`