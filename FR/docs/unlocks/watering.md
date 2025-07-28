# Arrosage
Les plantes poussent plus vite lorsqu'elles sont arrosées. Le sol a un niveau d'eau allant de `0` à `1`.
La fonction `get_water()` retourne le niveau d'eau du sol sur lequel il se trouve.

La vitesse de croissance d'une plante évolue linéairement de la vitesse 1x au niveau d'eau 0 à la vitesse 5x au niveau d'eau 1.

Le sol s'assèche avec le temps : en moyenne, il perd 1% de son eau actuelle par seconde, mais il y a une certaine variance aléatoire. Maintenir un niveau d'eau élevé consommera beaucoup plus d'eau que de maintenir un niveau d'eau bas.

Tu peux utiliser de l'eau sur tes plantes. Un réservoir d'eau est automatiquement ajouté à ton inventaire toutes les 10 secondes.
Améliorer `Unlocks.Watering` te donnera un réservoir d'eau supplémentaire toutes les 10 secondes.

Un réservoir contient `0.25` d'eau.

Appelle `use_item(Items.Water)` sur n'importe quel sol pour l'arroser.