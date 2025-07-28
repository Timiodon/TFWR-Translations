# Cactus
Comme les autres plantes, les [cactus](objects/cactus) peuvent être cultivés sur de la terre et récoltés comme d'habitude.

Cependant, ils existent en différentes tailles et ont un étrange sens de l'ordre.

Si vous récoltez un cactus entièrement développé et que tous les cactus voisins sont triés, il récoltera également tous les cactus voisins de manière récursive.

Un cactus est considéré comme trié si tous les cactus voisins au `North` et `East` sont entièrement développés et de taille supérieure ou égale et tous les cactus voisins au `South` et `West` sont entièrement développés et de taille inférieure ou égale.

La récolte ne se propagera que si tous les cactus adjacents sont entièrement développés et triés.
Cela signifie que si un carré de cactus cultivés est trié par taille et que vous récoltez un cactus, il récoltera tout le carré.

Un cactus entièrement développé apparaîtra brun s'il n'est pas trié. Une fois trié, il redeviendra vert.

Vous recevrez un nombre de cactus égal au carré du nombre de cactus récoltés. Donc si vous récoltez `n` cactus simultanément vous recevrez `n**2` `Items.Cactus`.

La taille d'un cactus peut être mesurée avec `measure()`.
C'est toujours l'un de ces nombres : `0,1,2,3,4,5,6,7,8,9`.

Vous pouvez également passer une direction dans `measure(direction)` pour mesurer la case voisine dans cette direction du drone.

Vous pouvez échanger un cactus avec son voisin dans n'importe quelle direction en utilisant la commande `swap()`.
`swap(direction)` échange l'objet sous le drone avec l'objet une case dans la `direction` du drone.

## Exemples
Dans chacune de ces grilles, tous les cactus sont triés et la récolte se propagera sur tout le champ :
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

Dans cette grille, seul le cactus en bas à gauche est trié, ce qui n'est pas suffisant pour qu'il se propage :
`1 5 3
4 9 7
3 3 2`

<spoiler=montrer l'indice 1>
Si les lignes sont déjà triées, trier les colonnes ne détruira pas le tri des lignes.
</spoiler>
<spoiler=montrer l'indice 2>
Si vous n'êtes pas familier avec les algorithmes de tri, vous pourriez vouloir les rechercher en ligne et réfléchir à ceux qui pourraient être adaptés à ce problème. Gardez à l'esprit que tous ne fonctionnent pas car vous ne pouvez échanger que des cactus voisins.
</spoiler>