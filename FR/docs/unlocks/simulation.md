# Simulation

Les simulations te permettent de tester rapidement du code sans changer l'état de la vraie ferme.
L'état de départ de la simulation peut être choisi librement, et lorsque la simulation se termine, la vraie ferme sera dans l'état exact où elle se trouvait avant le début de la simulation.

La fonction `simulate()` est utilisée pour démarrer une simulation.

le fichier dans lequel l'exécution doit commencer
`filename = "f1"`

commencer avec tout débloqué et amélioré au maximum
`sim_unlocks = Unlocks`

commencer avec 10000 carottes et 50 foin
`sim_items = {Items.Carrot : 10000, Items.Hay : 50}`

commencer avec une variable globale "a" ayant une valeur de 13
`sim_globals = {"a" : 13}`

utiliser une graine aléatoire fixe
`seed = 0`

accélérer la simulation d'un facteur 64
`speedup = 64`

lancer la simulation
`run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)`

La fonction `simulate()` renvoie le temps, en secondes, qu'il a fallu pour simuler le fichier de départ donné.

### Nom du fichier
Le premier argument de la fonction `simulate` est le nom du fichier. C'est le nom qui est affiché en haut de la fenêtre de code. La simulation exécutera le fichier spécifié comme si tu avais cliqué sur le bouton Exécuter.

### Déblocages de départ
Toutes les fonctionnalités de programmation comme les boucles, les instructions if, les listes, les dictionnaires,... resteront toujours débloquées.

Le deuxième argument te permet de spécifier avec quels déblocages/améliorations la simulation doit commencer en plus des fonctionnalités de programmation. Cela doit être une séquence de déblocages. La simulation commencera avec tous les déblocages de la séquence améliorés à leur niveau maximum.

Si tu veux spécifier un niveau d'amélioration autre que le maximum, tu peux passer un dictionnaire qui associe les déblocages aux niveaux de déblocage. Dans ce cas, les valeurs négatives correspondent au niveau de déblocage maximum.

### Objets de départ
Le troisième argument te permet de passer un dictionnaire qui associe des objets à des nombres. Il spécifie les objets avec lesquels commencer la simulation.

### Globales de départ
Parce que la simulation démarre une exécution de programme complètement nouvelle, tu ne peux pas accéder aux variables du programme qui lance la simulation.
Cependant, il est possible de passer des valeurs à la simulation en utilisant le quatrième argument. C'est un dict qui associe des noms de variables sous forme de chaînes de caractères à des valeurs. Ces variables sont ensuite ajoutées à la portée globale de l'exécution à l'intérieur de la simulation.

Note que cela copie toutes les valeurs, donc les modifier à l'intérieur de la simulation n'affectera pas les valeurs originales à l'extérieur. Il n'est pas possible de renvoyer des valeurs de la simulation autres que le temps d'exécution.

### Graine aléatoire
Le cinquième argument te permet de spécifier la graine aléatoire utilisée dans la simulation. Ce doit être un entier positif. Les valeurs négatives utiliseront une graine aléatoire.

La graine aléatoire affecte tout, des temps de croissance des plantes à la disposition des labyrinthes en passant par les temps de dégradation de l'eau. Si tu lances la même simulation plusieurs fois avec la même graine aléatoire et les mêmes conditions de départ, le résultat devrait toujours être le même.

### Accélération
Le sixième argument est l'accélération de départ de la simulation. Cela te permet de tester les choses rapidement. Si le jeu n'arrive pas à suivre la vitesse définie, il ralentira automatiquement.

L'accélération n'affecte en rien le résultat de la simulation. Elle n'existe que pour réduire le temps d'attente.