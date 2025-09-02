# Set
I set sono come i [dizionari](docs/scripting/dicts.md), ma senza valori. Sono solo un insieme non ordinato di chiavi.

Vengono creati come i dizionari, ma senza valori.
`set = {North, East, West}`

Usa `set()` per creare un set vuoto. Nota che `{}` crea un dizionario vuoto.

Usa `set.add(elem)` per aggiungere un nuovo elemento al set.

Usa `set.remove(elem)` per rimuovere un elemento da un set.

Usa `if elem in set:` per verificare se il set contiene un elemento.

Usa `for elem in set:` per iterare su tutti gli elementi del set.
Per set più grandi, l'operatore `in` è molto più veloce di quanto lo sarebbe su una lista.

Proprio come i dizionari, i set non sono ordinati, quindi non ci sono garanzie sull'ordine in cui gli elementi vengono iterati.

Inoltre, gli elementi nei set sono unici, quindi aggiungere un elemento che è già nel set non cambierà il set.