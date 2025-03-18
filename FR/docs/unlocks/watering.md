# Arrosage
Les plantes poussent plus vite lorsqu'elles sont arrosées. Le sol a un niveau d'eau allant de `0` à `1`.
La fonction `get_water()` renvoie le niveau d'eau du sol au-dessus duquel elle se trouve.

La vitesse de croissance d'une plante augmente linéairement, de 1x à un niveau d'eau de 0 à 5x à un niveau d'eau de 1.

Le sol s'assèche avec le temps : en moyenne, il perd 1 % de son eau actuelle par seconde, mais il y a de la variance aléatoire à cela. Maintenir un niveau d'eau élevé consommera beaucoup plus d'eau que de maintenir un niveau d'eau bas.

Vous pouvez utiliser des réservoirs d'eau pour arroser vos plantes. Un réservoir d'eau est automatiquement ajouté à votre inventaire toutes les 10 secondes.
Améliorer `Unlocks.Watering` vous donnera un réservoir d'eau supplémentaire toutes les 10 secondes.

Un réservoir contient `0.25` d'eau.

Appelez `use_item(Items.Water)` sur n'importe quel sol pour arroser le sol.