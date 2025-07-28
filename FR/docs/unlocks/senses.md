# Sens
Le drone peut voir maintenant !

Les fonctions `get_pos_x()` et `get_pos_y()` retournent la position x et y actuelle du drone. À la position de départ, elles sont toutes les deux `0`. La position x augmente de `1` pour chaque case vers l'`East` et la position y augmente de `1` pour chaque case vers le `North`.

`num_items(item)` retourne combien d'un objet vous avez.
Par exemple `num_items(Items.Hay)` retourne combien de foin vous avez.

`get_entity_type()` et `get_ground_type()` retournent le type d'entité ou de sol qui se trouve sous le drone.

Fais un flip si tu es sur un buisson :
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

Le mot-clé `None` est également débloqué maintenant ! `None` est une valeur qui représente l'absence de valeur.
Par exemple, une fonction qui n'a pas d'instruction `return` retournera en fait `None`.

`get_entity_type()` retourne `None` s'il n'y a pas d'entité sous le drone.