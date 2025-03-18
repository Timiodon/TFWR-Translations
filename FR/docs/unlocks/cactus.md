# Cactus
Comme les autres plantes, les [cactus](objects/cactus) peuvent être cultivés sur le sol et récoltés comme d'habitude.

Cependant, ils viennent en diverses tailles et ont un sens étrange de l'ordre.

Si vous récoltez un cactus complètement développé et que tous les cactus voisins sont en ordre trié, cela récoltera également tous les cactus voisins de manière récursive.

Un cactus est considéré en ordre trié si tous les cactus voisins au `North` et à l'`East` sont complètement développés et plus grands ou égaux en taille, et tous les cactus voisins au `South` et à l'`West` sont complètement développés et plus petits ou égaux en taille.

La récolte ne s'étendra que si tous les cactus adjacents sont complètement développés et en ordre trié. Cela signifie que si un carré de cactus développés est trié par taille et que vous en récoltez un, cela récoltera tout le carré.

Vous recevrez des cactus égaux au nombre de cactus récoltés au carré. Donc, si vous récoltez simultanément `n` cactus, vous recevrez `n**2` `Items.Cactus`.

La taille d'un cactus peut être mesurée avec `measure()`.
C'est toujours l'un de ces chiffres : `0,1,2,3,4,5,6,7,8,9`.

Vous pouvez aussi passer une direction dans `measure(direction)` pour mesurer la case voisine dans cette direction du drone.

Vous pouvez échanger un cactus avec son voisin dans n'importe quelle direction en utilisant la commande `swap()`.
`swap(direction)` échange l'objet sous le drone avec l'objet à une case dans la `direction` du drone.

## Exemples
Dans chacune de ces grilles, tous les cactus sont en ordre trié et la récolte se propagera sur tout le champ :
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

Dans cette grille, seul le cactus en bas à gauche est en ordre trié, ce qui n'est pas suffisant pour qu'il se propage :
`1 5 3
4 9 7
3 3 2`

<spoiler=afficher indice 1>
Si chaque colonne et chaque rangée du champ est triée, alors tout le champ est trié.
</spoiler>
<spoiler=afficher indice 2>
Si vous ne connaissez pas bien les algorithmes de tri, vous pourriez vouloir les rechercher en ligne et réfléchir à ceux qui pourraient être adaptés à ce problème.
</spoiler>