# Sens
Le drone peut voir maintenant !

Les fonctions `get_pos_x()` et `get_pos_y()` retournent la position x et y actuelle du drone. À la position de départ, elles sont toutes les deux à `0`. La position x augmente de `1` pour chaque case vers `East` et la position y augmente de `1` pour chaque case vers `North`.

`num_items(item)` retourne la quantité d'un objet que tu possèdes.
Par exemple, `num_items(Items.Hay)` retourne la quantité de foin que tu as.

`get_entity_type()` et `get_ground_type()` retournent le type d'entité ou de sol qui se trouve sous le drone.

Fais un flip si tu es au-dessus d'un buisson :
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

Le mot-clé `None` est aussi débloqué maintenant ! `None` est une valeur qui représente l'absence de valeur.
Par exemple, une fonction sans instruction `return` retournera en fait `None`.

`get_entity_type()` retourne `None` s'il n'y a pas d'entité sous le drone.


Si tu veux savoir combien de fois un déblocage particulier a été obtenu, utilise la fonction `num_unlocked(unlock)`.

Par exemple, `num_unlocked(Unlocks.Speed)` retournera le nombre d'améliorations de vitesse que tu as.

`num_unlocked(Unlocks.Senses)` retournera `1` si les sens sont débloqués et `0` sinon.

Tu peux aussi utiliser `num_unlocked()` sur des objets (Items), des entités (Entities) ou des sols (Grounds). Cela retournera `1` s'ils sont débloqués, sinon `0`.

Attention, `num_unlocked(Unlocks.Carrots)` retournera le nombre de fois où il a été débloqué/amélioré.
`num_unlocked(Items.Carrot)` ne retournera que `0` ou `1`. (Pareil pour les autres plantes)