# Expansion 2
Ta ferme s'est encore agrandie ! Maintenant, les cases ne sont plus en une belle rangée, tu dois donc trouver un moyen de parcourir une grille carrée.

Avec la boucle `while`, ce n'est pas possible tant que tu n'as pas débloqué les sens et les opérateurs.
Il est temps d'introduire la boucle `for`.

Tu peux tout lire sur la boucle `for` sur la page [Boucle For](docs/scripting/for.md), mais pour l'instant tu n'en auras besoin que pour répéter du code un nombre fixe de fois.

`#faire n loopings
for i in range(5):
	do_a_flip()`

`range(n)` crée une plage de nombres de `0` à `n-1`, qui contient `n` éléments. La boucle `for` exécute son corps de boucle une fois pour chaque élément de la séquence. Dans cet exemple, `do_a_flip()` sera appelé `5` fois.

La fonction `get_world_size()` est également disponible maintenant. Elle renvoie la longueur d'un côté de ta ferme. De cette façon, tu peux écrire du code qui ne se cassera pas avec la prochaine amélioration d'expansion.

`for i in range(get_world_size()):
	harvest()
	move(North)`

Cet exemple récolte une colonne de la ferme pour n'importe quelle taille de ferme.

Si tu es bloqué en essayant de comprendre comment déplacer le drone autour de la ferme, regarde l'indice ci-dessous.
<spoiler=montrer l'indice>Il y a, bien sûr, plusieurs façons de se déplacer dans la ferme.
Ce que nous cherchons, c'est un moyen de la parcourir de manière systématique qui ne se cassera pas lorsque la ferme s'agrandira à nouveau.
Un moyen systématique d'atteindre chaque endroit de la ferme serait de répéter les 2 étapes suivantes à l'infini :

1. Se déplacer vers le `North` jusqu'à revenir au point de départ.
2. Se déplacer vers l'`East`

`for i in range(get_world_size()):` peut être utile pour transformer cette idée en code.
</spoiler>
<spoiler=voir une solution possible> Le parcours de base pourrait ressembler à ceci :

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		#faire un looping sur chaque case
		do_a_flip()
		move(North)
	move(East)`
</spoiler>