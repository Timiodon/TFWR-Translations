# Mesure du Temps
Si tu veux vraiment optimiser tes méthodes, tu dois comprendre comment le temps est mesuré dans ce jeu. Ce déblocage est entièrement consacré à ça.

## Nouvelles Fonctions
Il y a deux fonctions utiles pour mesurer combien de temps les choses prennent :

`get_time()` renvoie le temps en secondes depuis le début du jeu.

`get_tick_count()` renvoie le nombre de ticks effectués depuis le début de l'exécution.

Ces deux fonctions, ainsi que `quick_print()`, sont entièrement gratuites. Même l'opération d'appel est gratuite pour elles.

## Détails d'Exécution

### Attention
Ce n'est pas comme ça que la performance fonctionne dans le monde réel. Ce sont juste des règles inventées pour ce jeu afin d'avoir un modèle de temps cohérent et compréhensible.
Tu ne t'en soucieras probablement que si tu veux hyper-optimiser ton code.


L'unité de temps de base pour l'exécution du code est appelée un "tick". Sans améliorations de vitesse et sans puissance, l'exécution se déroule à une vitesse de `400` ticks par seconde.

En général, les opérations qui combinent deux valeurs comme `+, -, *, /, //, %, and, or, ...` prennent un tick pour s'exécuter.
Les opérations sur une seule valeur `-` et `not` sont gratuites.
Un branchement `if` prend aussi un tick pour s'exécuter (en plus du temps nécessaire pour évaluer l'expression de la condition).
Les appels de fonction et les lectures et écritures de variables sont gratuits, mais les définitions de fonction prennent 1 tick.
Les instructions `import` sont gratuites.
Accéder à un module importé avec l'opérateur `.` est gratuit.
Si une fonction ou un module a été passé via des arguments ou des affectations de variables, l'utiliser coûtera 1 tick au lieu de 0.
Les boucles `for` et `while` prennent un tick pour démarrer, mais les itérations sont gratuites (sans compter le temps d'évaluation des expressions de condition/séquence).
`return`, `break` et `continue` sont tous gratuits.
`pass` prend un tick, il peut donc être utilisé pour créer des délais précis.
L'indexation dans une structure de données prend un tick pour l'opérateur d'index et, dans le cas d'un dictionnaire ou d'un set, des ticks supplémentaires en fonction de la taille de la clé.

Le nombre de ticks que les fonctions intégrées prennent pour s'exécuter est documenté individuellement dans la documentation de chaque fonction.