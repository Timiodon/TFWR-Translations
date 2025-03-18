# Arbres
[Trees](objects/tree) sont une meilleure façon d'obtenir du bois que les buissons. Ils donnent 5 bois chacun. Comme les buissons, ils peuvent être plantés sur de l'herbe ou du sol.

Les arbres aiment avoir un peu d'espace et les planter juste à côté ralentira leur croissance. Le temps de croissance est doublé pour chaque arbre qui est sur une case directement au nord, à l'est, à l'ouest ou au sud de lui. Donc si vous plantez des arbres sur chaque case, ils prendront `2*2*2*2 = 16` fois plus de temps à pousser.

<spoiler=show> L'opérateur `%` peut être utile ici. Rappelez-vous que l'opérateur `%` renvoie le reste de la division. Les nombres pairs divisés par `2` ont un reste de `0` et les nombres impairs divisés par `2` ont un reste de `1`.
Donc vous pouvez vérifier si un nombre est pair comme ceci :

`def is_even(n):
	return n % 2 == 0`

Cela renvoie `True` si n est pair et `False` s'il ne l'est pas.
</spoiler>