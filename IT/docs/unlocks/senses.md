# Sensori
Il drone può vedere ora!

Le funzioni `get_pos_x()` e `get_pos_y()` restituiscono la posizione attuale x e y del drone. All'inizio sono entrambi `0`. La posizione x aumenta di `1` per ogni piastrella verso `East` e la posizione y aumenta di `1` per ogni piastrella verso `North`.

`num_items(item)` restituisce quanti oggetti di un tipo hai.
Per esempio, `num_items(Items.Hay)` restituisce quanti fieni hai.

`get_entity_type()` e `get_ground_type()` restituiscono il tipo di entity o di terreno sotto il drone.

Fai una capriola se sei sopra un cespuglio:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

La parola chiave `None` è anche sbloccata ora! `None` è un valore che rappresenta l'assenza di valore.
Per esempio, una funzione che non ha una dichiarazione `return` restituirà effettivamente `None`.

`get_entity_type()` restituisce `None` se non c’è alcuna entity sotto il drone.