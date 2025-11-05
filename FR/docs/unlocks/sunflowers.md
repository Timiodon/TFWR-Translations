# Tournesols
Les [tournesols](objects/sunflower) collectent la puissance du soleil. Tu peux récolter cette puissance.

Les planter fonctionne exactement de la même manière que pour les carottes ou les citrouilles.

Récolter un tournesol adulte rapporte de la puissance.
S'il y a au moins 10 tournesols dans la ferme et que tu récoltes celui avec le plus grand nombre de pétales, tu obtiens `8` fois plus de puissance !
Si tu récoltes un tournesol alors qu'un autre a plus de pétales, le prochain tournesol que tu récolteras ne te donnera que la quantité normale de puissance (pas le bonus de 8x).

`measure()` renvoie le nombre de pétales du tournesol sous le drone.
Les tournesols ont au moins `7` et au plus `15` pétales.
Ils peuvent être mesurés même avant d'être complètement adultes.

Plusieurs tournesols peuvent avoir le même nombre de pétales, il peut donc y avoir plusieurs tournesols avec le plus grand nombre de pétales. Dans ce cas, peu importe lequel tu récoltes.

Tant que tu as de la puissance, le drone l'utilisera pour fonctionner deux fois plus vite.
Il consomme 1 de puissance toutes les 30 actions (comme les déplacements, les récoltes, les plantations...)
Exécuter d'autres instructions de code peut aussi utiliser de la puissance, mais beaucoup moins que les actions du drone.

En général, tout ce qui est accéléré par les améliorations de vitesse est aussi accéléré par la puissance.
Tout ce qui est accéléré par la puissance utilise aussi de la puissance proportionnellement au temps que cela prend pour s'exécuter, sans tenir compte des améliorations de vitesse.