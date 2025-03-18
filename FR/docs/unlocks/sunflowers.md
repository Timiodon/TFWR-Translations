# Tournesols
[Tournesols](objects/sunflower) collectent l'énergie du soleil. Tu peux récolter cette énergie.

Les planter fonctionne exactement comme planter des carottes ou des citrouilles.

Récolter un tournesol mature te rapporte de l'énergie.
S'il y a au moins 10 tournesols dans la ferme et que tu récoltes celui avec le plus grand nombre de pétales, tu obtiens `5` fois plus d'énergie !

`measure()` retourne le nombre de pétales du tournesol sous le drone.
Les tournesols ont au moins `7` et au plus `15` pétales.
Ils peuvent déjà être mesurés avant d'être complètement mûrs.

Plusieurs tournesols peuvent avoir le même nombre de pétales, donc il peut également y avoir plusieurs tournesols avec le plus grand nombre de pétales. Dans ce cas, peu importe lequel tu récoltes.

Tant que tu as de l'énergie, le drone l'utilisera pour aller deux fois plus vite.
Il consomme 1 énergie toutes les 30 actions (comme se déplacer, récolter, planter...)
Exécuter d'autres instructions de code peut aussi consommer de l'énergie, mais beaucoup moins que les actions du drone.

En général, tout ce qui est accéléré par les améliorations de vitesse est aussi accéléré par l'énergie.
Tout ce qui est accéléré par l'énergie utilise également de l'énergie proportionnellement au temps qu'il faut pour l'exécuter, en ignorant les améliorations de vitesse.