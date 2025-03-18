# Dictionaries
I dizionari sono una struttura dati che ti permette di mappare chiavi a valori allo stesso modo in cui un vero dizionario mappa le parole alle loro definizioni e puoi cercarle in modo molto rapido.

Un dictionary può essere creato così:
`rotation = {North:East, East:South, South:West, West:North}`

L'espressione prima dei due punti è la chiave e l'espressione dopo i due punti è il valore a cui la chiave è associata.
Il dictionary sopra associa ogni direzione alla direzione alla sua destra.

Eccone un altro che mappa la posizione del drone all'entity sopra cui si trova.
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

Accedere al valore associato a una chiave è simile ad accedere a un elemento in una lista:
`value = dict[key]`

Esempio:
`orientation = rotation[South]`
Questo imposta `orientation` su `West`.

Puoi aggiungere un nuovo paio chiave-valore a un dictionary così:
`dict[key] = value`

Esempio:
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
Questo aggiorna l'entity memorizzata per la posizione corrente.

Le chiavi sono uniche, quindi aggiungere una chiave che esiste già nel dictionary sovrascriverà il valore precedente.

Usa `dict.pop(key)` per rimuovere un paio chiave-valore dal `dict`.

`key in dict` restituisce `True` se `key` è una chiave nel `dict` e `False` altrimenti.
Quindi puoi usare `if key in dict:` per verificare se il `dict` contiene la chiave.

Mettere un dictionary in un ciclo for ti permette di iterare attraverso tutte le chiavi:
`for key in dict:
	value = dict[key]`

Non ci sono garanzie sull'ordine in cui le chiavi sono iterate.

Guarda anche [Sets](docs/scripting/sets.md)