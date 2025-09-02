# Sensori
Il drone ora può vedere! 

Le funzioni `get_pos_x()` e `get_pos_y()` restituiscono la posizione x e y corrente del drone. Alla posizione di partenza sono entrambe `0`. La posizione x aumenta di `1` per ogni casella verso `Est` e la posizione y aumenta di `1` per ogni casella verso `Nord`.

`num_items(item)` restituisce quanti esemplari di un oggetto possiedi.
Ad esempio `num_items(Items.Hay)` restituisce quanto fieno hai.

`get_entity_type()` e `get_ground_type()` restituiscono il tipo di entità o terreno che si trova sotto il drone.

Fai una capriola se ti trovi su un cespuglio:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

La parola chiave `None` è ora sbloccata! `None` è un valore che rappresenta l'assenza di un valore.
Ad esempio, una funzione che non ha un'istruzione `return` restituirà effettivamente `None`.

`get_entity_type()` restituisce `None` se non c'è alcuna entità sotto il drone.


Se vuoi scoprire quanti esemplari di un particolare sblocco possiedi, usa la funzione `num_unlocked(unlock)`.

Ad esempio, `num_unlocked(Unlocks.Speed)` restituirà il numero di potenziamenti di velocità che hai.

`num_unlocked(Unlocks.Senses)` restituirà `1` se i sensori sono sbloccati e `0` se non lo sono.

Puoi anche usare `num_unlocked()` su Items, Entities o Grounds. Questo restituirà `1` se è sbloccato, altrimenti `0`.

Fai attenzione, `num_unlocked(Unlocks.Carrots)` restituirà il numero di volte che è stato sbloccato/potenziato.
`num_unlocked(Items.Carrot)` restituirà solo `0` o `1`. (Lo stesso vale per le altre piante)
