# Liste
Le liste sono un modo semplice per memorizzare più valori in una singola variabile.
Puoi creare nuove liste in questo modo:

`list = [2, True, Items.Hay]`

La lista ora contiene i valori `2`, `True` e `Items.Hay`.
Una lista può anche essere vuota:

`empty_list = []`

Puoi accedere a un elemento di una lista tramite il suo indice. L'indice è `0` per il primo elemento, `1` per il secondo, `2` per il terzo...

pianta carote
`list = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(list[1])`

Puoi iterare su una lista usando un ciclo for. L'esempio seguente somma tutti gli elementi nella lista.

`list = [4, 7, 2, 5]
sum = 0
for number in list:
	sum += number`
`sum` è ora `18`

I seguenti metodi delle liste ti permettono di aggiungere e rimuovere elementi:

`list.append(elem)` aggiunge un elemento alla fine della lista:

`list = [2, 6, 12]
list.append(7)`
`list` è ora `[2, 6, 12, 7]`

`list.remove(elem)` rimuove la prima occorrenza di un elemento da una lista:

`list = [1, 2, 4, 2]
list.remove(2)`
`list` è ora `[1, 4, 2]`

`list.insert(index, elem)` inserisce un elemento all'indice dato:

`list = [Entities.Tree, Items.Hay]
list.insert(1, Items.Wood)`
`list` è ora `[Entities.Tree, Items.Wood, Items.Hay]`

`list.pop(index)` rimuove l'elemento all'indice specificato.
Se non viene specificato alcun indice, viene rimosso l'ultimo elemento.

`list = [3, 5, 8, 25]
list.pop()`
`list` è ora `[3, 5, 8]`
`list.pop(1)`
`list` è ora `[3, 8]`

La funzione `len()` restituisce la lunghezza della lista.
`list = [3, 2, 1]
x = len(list)`
`x` è ora `3`

Le liste hanno semantica per riferimento. Ciò significa che assegnare una lista a una variabile assegna lo stesso oggetto lista a quella variabile, invece di creare una copia della lista.
Se due variabili fanno riferimento alla stessa lista, le modifiche alla lista saranno visibili da entrambe.

`a = [1,2]
b = a
b.pop()`
`a` e `b` sono ora entrambi `[1]`
