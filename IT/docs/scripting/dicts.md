# Dizionari
I dizionari sono una struttura dati che ti permette di mappare chiavi a valori, allo stesso modo in cui un vero dizionario mappa parole alle loro definizioni, e puoi cercarle molto velocemente.

Un dizionario può essere creato così:
`right_of = {North:East, East:South, South:West, West:North}`

L'espressione prima dei due punti è la chiave e l'espressione dopo i due punti è il valore a cui la chiave mappa.
Il dizionario sopra mappa ogni direzione alla direzione alla sua destra.

Eccone un altro che mappa la posizione del drone all'entità su cui si trova.
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

Accedere al valore mappato a una chiave è simile ad accedere a un elemento in una lista:
`value = dict[key]`

Esempio:
`orientation = right_of[South]`
Questo imposta `orientation` a `West`.

Puoi aggiungere una nuova coppia chiave-valore a un dizionario in questo modo:
`dict[key] = value`

Esempio:
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
Questo aggiorna l'entità memorizzata per la posizione corrente.

Le chiavi sono uniche, quindi aggiungere una chiave che esiste già nel dizionario sovrascriverà il valore precedente.

Usa `dict.pop(key)` per rimuovere una coppia chiave-valore da `dict`.

`key in dict` restituisce `True` se `key` è una chiave nel `dict` e `False` altrimenti.
Quindi puoi usare `if key in dict:` per verificare se `dict` contiene la chiave.

Mettere un dizionario in un ciclo for ti permette di iterare su tutte le chiavi:
`for key in dict:
	value = dict[key]`

Non ci sono garanzie sull'ordine in cui le chiavi vengono iterate.

Vedi anche [Set](docs/scripting/sets.md)