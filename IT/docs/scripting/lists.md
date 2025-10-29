# Liste
Le liste sono un modo semplice per memorizzare più valori in una singola variabile.
Puoi creare nuove liste in questo modo:

`some_list = [2, True, Items.Hay]`

La lista ora contiene i valori `2`, `True` e `Items.Hay`.
Una lista può anche essere vuota:

`empty_list = []`

Puoi accedere a un elemento di una lista tramite il suo indice. L'indice è `0` per il primo elemento, `1` per il secondo, `2` per il terzo...

pianta carote
`entities = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(entities[1])`

Puoi iterare su una lista usando un ciclo for. L'esempio seguente somma tutti gli elementi nella lista.

`numbers = [4, 7, 2, 5]
sum = 0
for number in numbers:
	sum += number`
`sum` è ora `18`

I seguenti metodi delle liste ti permettono di aggiungere e rimuovere elementi:

`elements.append(elem)` aggiunge un elemento alla fine della lista:

`numbers = [2, 6, 12]
numbers.append(7)`
`numbers` è ora `[2, 6, 12, 7]`

`elements.remove(elem)` rimuove la prima occorrenza di un elemento da una lista:

`numbers = [1, 2, 4, 2]
numbers.remove(2)`
`numbers` è ora `[1, 4, 2]`

`elements.insert(index, elem)` inserisce un elemento all'indice dato:

`some_list = [Entities.Tree, Items.Hay]
some_list.insert(1, Items.Wood)`
`some_list` è ora `[Entities.Tree, Items.Wood, Items.Hay]`

`elements.pop(index)` rimuove l'elemento all'indice specificato.
Se non viene specificato alcun indice, viene rimosso l'ultimo elemento.

`numbers = [3, 5, 8, 25]
numbers.pop()`
`numbers` è ora `[3, 5, 8]`
`numbers.pop(1)`
`numbers` è ora `[3, 8]`

La funzione `len()` restituisce la lunghezza della lista.
`numbers = [3, 2, 1]
x = len(numbers)`
`x` è ora `3`

Le liste hanno semantica per riferimento. Ciò significa che assegnare una lista a una variabile assegna lo stesso oggetto lista a quella variabile, invece di creare una copia della lista.
Se due variabili fanno riferimento alla stessa lista, le modifiche alla lista saranno visibili da entrambe.

`a = [1, 2]
b = a
b.pop()`
`a` e `b` sono ora entrambi `[1]`
