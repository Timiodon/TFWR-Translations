# Sens
Le drone peut voir maintenant !

Les fonctions `get_pos_x()` et `get_pos_y()` renvoient les positions x et y actuelles du drone. À la position de départ, elles sont toutes les deux à `0`. La position x augmente de `1` à chaque case vers l'`East` et la position y augmente de `1` à chaque case vers le `North`.

`num_items(item)` renvoie le nombre d'un objet que tu possèdes.
Par exemple, `num_items(Items.Hay)` renvoie la quantité de foin que tu as.

`get_entity_type()` et `get_ground_type()` renvoient le type d'entité ou de sol qui se trouve sous le drone.

Fais un looping si tu es sur un buisson :
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

Le mot-clé `None` est également débloqué maintenant ! `None` est une valeur qui représente l'absence de valeur.
Par exemple, une fonction qui n'a pas d'instruction `return` renverra en fait `None`.

`get_entity_type()` renvoie `None` s'il n'y a pas d'entité sous le drone.


Si tu veux savoir combien de déblocages d'un certain type tu as, utilise la fonction `num_unlocked(unlock)`.

Par exemple, `num_unlocked(Unlocks.Speed)` renverra le nombre d'améliorations de vitesse que tu as.

`num_unlocked(Unlocks.Senses)` renverra `1` si les sens sont débloqués et `0` sinon.

Tu peux aussi utiliser `num_unlocked()` sur les Objets, Entités ou Sols. Cela renverra `1` si c'est débloqué, sinon `0`.

Attention, `num_unlocked(Unlocks.Carrots)` renverra le nombre de fois où il a été débloqué/amélioré.
`num_unlocked(Items.Carrot)` ne renverra que `0` ou `1`. (Pareil pour les autres plantes)