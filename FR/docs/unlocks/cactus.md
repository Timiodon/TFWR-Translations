# Cactus
Comme les autres plantes, les [cactus](objects/cactus) peuvent être cultivés sur du sol et récoltés comme d'habitude.

Cependant, ils existent en différentes tailles et ont un étrange sens de l'ordre.

Si tu récoltes un cactus adulte et que tous les cactus voisins sont triés, il récoltera aussi récursivement tous les cactus voisins.

Un cactus est considéré comme trié si tous les cactus voisins au `North` et à l'`East` sont adultes et de taille supérieure ou égale, et tous les cactus voisins au `South` et à l'`West` sont adultes et de taille inférieure ou égale.

La récolte ne se propagera que si tous les cactus adjacents sont adultes et triés.
Cela signifie que si un carré de cactus adultes est trié par taille et que tu récoltes un cactus, il récoltera le carré entier.

Un cactus adulte apparaîtra marron s'il n'est pas trié. Une fois trié, il redeviendra vert.

Tu recevras un nombre de cactus égal au carré du nombre de cactus récoltés. Donc si tu récoltes `n` cactus simultanément, tu recevras `n**2` `Items.Cactus`.

La taille d'un cactus peut être mesurée avec `measure()`.
C'est toujours l'un de ces nombres : `0,1,2,3,4,5,6,7,8,9`.

Tu peux aussi passer une direction à `measure(direction)` pour mesurer la case voisine dans cette direction du drone.

Tu peux échanger un cactus avec son voisin dans n'importe quelle direction en utilisant la commande `swap()`.
`swap(direction)` échange l'objet sous le drone avec l'objet situé à une case dans la `direction` du drone.

## Exemples
Dans chacune de ces grilles, tous les cactus sont triés et la récolte se propagera sur tout le champ :
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

Dans cette grille, seul le cactus en bas à gauche est trié, ce qui n'est pas suffisant pour que la récolte se propage :
`1 5 3
4 9 7
3 3 2`

<spoiler=montrer l'indice 1>
Si les lignes sont déjà triées, trier les colonnes ne détriera pas les lignes.
</spoiler>
<spoiler=montrer l'indice 2>
Si tu n'es pas familier avec les algorithmes de tri, tu devrais peut-être les rechercher en ligne et réfléchir à ceux qui pourraient être adaptés à ce problème. Garde à l'esprit que tous ne fonctionnent pas car tu ne peux échanger que des cactus voisins.
</spoiler>