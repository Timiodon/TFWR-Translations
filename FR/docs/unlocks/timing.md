# Chronométrage
Si tu veux vraiment optimiser tes méthodes, tu dois comprendre comment le temps est mesuré dans ce jeu. Ce déblocage porte sur ça.

## Nouvelles Fonctions
Il y a deux fonctions utiles pour mesurer la durée des opérations :

`get_time()` renvoie le temps en secondes depuis le début du jeu.

`get_tick_count()` renvoie le nombre de ticks effectués depuis le début de l'exécution.

Ces deux fonctions, ainsi que `quick_print()`, sont entièrement gratuites. Même l'opération d'appel est gratuite pour elles.

## Détails de l'Exécution

### Alerte
Ce n'est pas comme ça que la performance fonctionne dans la réalité. Ce sont juste des règles inventées pour avoir un modèle de chronométrage cohérent et compréhensible dans ce jeu.
Tu t'en soucieras probablement seulement si tu veux hyper-optimiser ton code.


L'unité de base du temps pour l'exécution du code s'appelle un "tick". Sans améliorations de vitesse ni de puissance, l'exécution se déroule à un rythme de `400` ticks par seconde.

En général, les opérations qui combinent deux valeurs comme `+, -, *, /, //, %, and, or, ...` prennent un tick pour s'exécuter.
La valeur unique `-` et `not` sont gratuites.
Une branche `if` prend aussi un tick pour s'exécuter (en plus du temps nécessaire pour évaluer l'expression de la condition).
Les appels de fonctions, lecture et écriture de variables sont gratuits mais les définitions de fonctions prennent 1 tick.
Les instructions `import` sont gratuites.
Accéder à un module importé avec l'opérateur `.` est gratuit.
Si une fonction ou un module a été passé via des arguments ou des affectations de variables, son utilisation coûtera 1 tick au lieu de 0.
Les boucles `for` et `while` prennent un tick pour démarrer, mais les itérations sont gratuites (sans compter le temps nécessaire pour évaluer les expressions de condition/séquence).
Les `return`, `break` et `continue` sont tous gratuits.
`pass` prend un tick, donc il peut être utilisé pour créer des délais précis.
L'indexation dans une structure de données prend un tick pour l'opérateur d'index, et, dans le cas d'un "dictionary" ou "set", des ticks supplémentaires en fonction de la taille de la clé.

Le nombre de ticks que prennent les fonctions intégrées pour s'exécuter est documenté dans la documentation de chaque fonction individuellement.