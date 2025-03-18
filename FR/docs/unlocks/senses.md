# Sens

Le drone peut voir maintenant !

Les fonctions `get_pos_x()` et `get_pos_y()` renvoient la position x et y actuelle du drone. À la position de départ, elles sont toutes les deux `0`. La position x augmente de `1` chaque tuile vers `East` et la position y augmente de `1` chaque tuile vers `North`.

`num_items(item)` renvoie combien d’un objet vous avez.
Par exemple `num_items(Items.Hay)` indique combien de foin vous avez.

`get_entity_type()` et `get_ground_type()` renvoient le type d'entity ou de sol qui est sous le drone.

Fais une figure si tu es au-dessus d'un buisson :
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

Le mot-clé `None` est aussi débloqué maintenant ! `None` est une valeur qui représente l'absence de valeur.
Par exemple, une fonction qui n’a pas d'instruction `return` retournera en fait `None`.

`get_entity_type()` renvoie `None` s'il n'y a pas d'entity sous le drone.