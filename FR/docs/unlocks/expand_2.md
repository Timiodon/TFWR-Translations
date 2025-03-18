# Agrandir 2
Ta ferme s'est encore agrandie ! Maintenant, les tuiles ne sont plus alignées, donc tu dois trouver un moyen de traverser une grille carrée.

Avec la boucle `while`, ce n'est pas possible tant que tu n'as pas débloqué les capteurs et les opérateurs. Il est temps de découvrir la boucle `for`.

Tu peux lire tout sur la boucle `for` sur la page [For Loop](docs/scripting/for.md), mais pour l'instant, tu en auras seulement besoin pour répéter le code un nombre fixe de fois.

`#faire n figures
for i in range(5):
	do_a_flip()`

`range(n)` crée un intervalle de nombres de `0` à `n-1` qui contient `n` éléments. La boucle `for` exécute son corps une fois pour chaque élément dans la séquence. Dans cet exemple, `do_a_flip()` sera appelé `5` fois.

La fonction `get_world_size()` est aussi disponible maintenant. Elle renvoie la longueur du côté de ta ferme. Ainsi, tu peux écrire du code qui ne plantera pas lors de la prochaine mise à jour d'agrandissement.

`for i in range(get_world_size()):
	harvest()
	move(North)`

Cet exemple récolte une colonne de la ferme pour n'importe quelle taille de ferme.

Si tu es bloqué en essayant de comprendre comment déplacer le drone autour de la ferme, consulte l'indice ci-dessous.
<spoiler=montrer l'indice> Il y a, bien sûr, plusieurs façons de se déplacer à travers la ferme.
Ce que nous recherchons, c'est un moyen de la traverser de manière systématique qui ne se cassera pas lorsque la ferme s'agrandira de nouveau.
Une façon systématique d'atteindre chaque endroit de la ferme serait de répéter indéfiniment les 2 étapes suivantes :

1. Se déplacer vers le `North` jusqu'à ce qu'il revienne au début.
2. Se déplacer vers l'`East`.

`for i in range(get_world_size()):` peut être utile pour transformer cette idée en code.
</spoiler>
<spoiler=montrer une solution possible> Le parcours de base pourrait ressembler à ça :

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		#faire une figure sur chaque tuile
		do_a_flip()
		move(North)
	move(East)`
</spoiler>