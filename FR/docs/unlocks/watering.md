# Arrosage
Les plantes poussent plus vite lorsqu'elles sont arrosées. Le sol a un niveau d'eau allant de `0` à `1`.  
La fonction `get_water()` renvoie le niveau d'eau du sol qu'elle survole.

La vitesse de croissance d'une plante augmente linéairement de 1x à une vitesse de niveau d'eau 0 à 5x à un niveau d'eau 1.

Le sol s'assèche avec le temps : en moyenne, il perd 1 % de son eau actuelle par seconde, mais il y a une certaine variance aléatoire à cela. Maintenir un haut niveau d'eau consomme beaucoup plus d'eau que maintenir un bas niveau d'eau.

Vous pouvez utiliser de l'eau sur vos plantes. Un réservoir d'eau est automatiquement ajouté à votre inventaire toutes les 10 secondes.  
Améliorer `Unlocks.Watering` vous donnera un réservoir d'eau supplémentaire toutes les 10 secondes.

Un réservoir contient `0.25` d'eau.

Appelez `use_item(Items.Water)` sur n'importe quel sol pour l'arroser.