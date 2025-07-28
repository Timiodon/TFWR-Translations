# Expansion 2
Votre ferme s'est encore agrandie ! Maintenant, les cases ne sont plus dans une belle rangée, vous devez donc trouver un moyen de parcourir une grille carrée.

Avec la boucle `while`, ce n'est pas possible tant que vous n'avez pas débloqué les sens et les opérateurs.
Il est temps d'introduire la boucle `for`.

Vous pouvez tout lire sur la boucle `for` sur la page [Boucle For](docs/scripting/for.md), mais pour l'instant, vous n'en aurez besoin que pour répéter du code un nombre fixe de fois.

`#fait n flips
for i in range(5):
	do_a_flip()`

`range(n)` crée une plage de nombres de `0` à `n-1` qui contient `n` éléments. La boucle `for` exécute son corps de boucle une fois pour chaque élément de la séquence. Dans cet exemple, `do_a_flip()` sera appelé `5` fois.

La fonction `get_world_size()` est également disponible maintenant. Elle retourne la longueur du côté de votre ferme. De cette façon, vous pouvez écrire du code qui ne se cassera pas avec la prochaine amélioration d'expansion.

`for i in range(get_world_size()):
	harvest()
	move(North)`

Cet exemple récolte une colonne de la ferme pour n'importe quelle taille de ferme.

Si vous êtes bloqué en essayant de trouver comment déplacer le drone autour de la ferme, consultez l'indice ci-dessous.
<spoiler=montrer l'indice>Il y a, bien sûr, plusieurs façons de se déplacer dans la ferme.
Ce que nous cherchons, c'est un moyen de la parcourir de manière systématique qui ne se cassera pas lorsque la ferme grandira à nouveau.
Un moyen systématique d'atteindre chaque endroit de la ferme serait de répéter les 2 étapes suivantes à l'infini :

1.Se déplacer vers le `North` jusqu'à ce qu'il revienne au début.
2.Se déplacer vers l'`East`

`for i in range(get_world_size()):` peut être utile pour transformer cette idée en code.
</spoiler>
<spoiler=montrer la solution possible> Le parcours de base pourrait ressembler à ceci :

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		#fait un flip sur chaque case
		do_a_flip()
		move(North)
	move(East)`
</spoiler>