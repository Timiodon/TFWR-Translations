# Variabili
Le variabili possono essere pensate come dei contenitori con un nome che possono contenere un valore.
L'operatore `=` si usa per dichiarare una variabile e memorizzarvi un valore.

`variable_name = value`

La parte a sinistra dell'operatore è il nome della variabile. Puoi dargli il nome che vuoi.
La parte a destra è un'espressione il cui valore risultante sarà memorizzato nella variabile.

Dichiara una variabile chiamata `a` e memorizzaci il valore `5`:
`a = 5`
Dichiara una variabile chiamata `b` e memorizzaci il valore di ritorno di `can_harvest()`:
`b = can_harvest()`

Non confondere l'operatore `=` con l'operatore `==`. 
L'operatore `==` controlla se due valori sono uguali e restituisce `True` o `False`.
L'operatore `=` assegna il valore a destra al nome a sinistra.

Dopo che una variabile è stata assegnata, puoi usarla nel codice per recuperare il valore che contiene

`a = 5
for i in range(a):
	do_a_flip()`

Il ciclo qui sopra viene eseguito 5 volte perché `a` è impostato a `5`.
La `i` nel ciclo `for` è anche una variabile a cui viene automaticamente assegnato il valore corrente della sequenza ad ogni iterazione del ciclo. (Non deve per forza chiamarsi `i`, puoi darle qualsiasi nome di variabile valido.)

Le variabili ti permettono di fare la stessa cosa anche con un ciclo while:

`a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1`

Questo fa la stessa cosa del ciclo for di prima. Dobbiamo solo incrementare i manualmente.
Nota che per incrementare i, lo impostiamo al suo stesso valore più `1`. Cambiare il valore di una variabile basandosi sul suo valore precedente è una cosa molto comune. 
Si può abbreviare usando questi operatori: `+=, -=, *=, /=, %=`

`i = i + 1` è la stessa cosa di `i += 1`
`a = a / 3` è la stessa cosa di `a /= 3`
