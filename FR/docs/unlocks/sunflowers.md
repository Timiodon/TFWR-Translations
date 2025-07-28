# Tournesols
Les [tournesols](objects/sunflower) collectent l'énergie du soleil. Tu peux récolter cette énergie.

Les planter fonctionne exactement comme planter des carottes ou des citrouilles.

Récolter un tournesol adulte rapporte de l'énergie.
S'il y a au moins 10 tournesols sur la ferme et que tu récoltes celui avec le plus grand nombre de pétales, tu obtiens `5` fois plus d'énergie !

`measure()` retourne le nombre de pétales du tournesol sous le drone.
Les tournesols ont au moins `7` et au plus `15` pétales.
Ils peuvent déjà être mesurés avant d'être complètement développés.

Plusieurs tournesols peuvent avoir le même nombre de pétales, il peut donc y avoir plusieurs tournesols avec le plus grand nombre de pétales. Dans ce cas, peu importe lequel tu récoltes.

Tant que tu as de l'énergie, le drone l'utilisera pour aller deux fois plus vite.
Il consomme 1 d'énergie toutes les 30 actions (comme les déplacements, les récoltes, les plantations...)
L'exécution d'autres instructions de code peut aussi consommer de l'énergie, mais beaucoup moins que les actions du drone.

En général, tout ce qui est accéléré par les améliorations de vitesse est aussi accéléré par l'énergie.
Tout ce qui est accéléré par l'énergie consomme aussi de l'énergie proportionnellement au temps nécessaire à son exécution, en ignorant les améliorations de vitesse.