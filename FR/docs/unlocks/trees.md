# Arbres
Les [arbres](objects/tree) sont un meilleur moyen d'obtenir du bois que les buissons. Ils donnent 5 bois chacun. Comme les buissons, ils peuvent être plantés sur de l'herbe ou de la terre.

Les arbres aiment avoir de l'espace et les planter juste à côté les uns des autres ralentira leur croissance. Le temps de croissance est doublé pour chaque arbre qui se trouve sur une case directement au nord, à l'est, à l'ouest ou au sud de celui-ci. Donc si tu plantes des arbres sur chaque case, ils mettront `2*2*2*2 = 16` fois plus de temps à pousser.

<spoiler=montrer> L'opérateur `%` peut être utile ici. Rappelle-toi que l'opérateur `%` renvoie le reste de la division. Les nombres pairs divisés par `2` ont un reste de `0` et les nombres impairs divisés par `2` ont un reste de `1`.
Tu peux donc vérifier si un nombre est pair comme ceci :

`def is_even(n):
	return n % 2 == 0`

Cela renvoie `True` si n est pair et `False` sinon.
</spoiler>