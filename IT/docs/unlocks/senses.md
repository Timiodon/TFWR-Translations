# Sensori
Il drone ora può vedere!

Le funzioni `get_pos_x()` e `get_pos_y()` restituiscono la posizione x e y corrente del drone. Alla posizione di partenza sono entrambe `0`. La posizione x aumenta di `1` per ogni casella verso `East` e la posizione y aumenta di `1` per ogni casella verso `North`.

`num_items(item)` restituisce quanti item di un certo tipo possiedi.
Ad esempio `num_items(Items.Hay)` restituisce quanto fieno hai.

`get_entity_type()` e `get_ground_type()` restituiscono il tipo di entity o di terreno che si trova sotto il drone.

Fai un flip se ti trovi sopra un cespuglio:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

La parola chiave `None` è ora sbloccata! `None` è un valore che rappresenta l'assenza di un valore.
Ad esempio, una funzione che non ha un'istruzione `return` restituirà effettivamente `None`.

`get_entity_type()` restituisce `None` se non c'è nessuna entity sotto il drone.
