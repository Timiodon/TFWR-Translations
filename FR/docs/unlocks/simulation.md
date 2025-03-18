# Simulation

Les simulations vous permettent de tester rapidement le code sans modifier l'état réel de la ferme.  
L'état de départ de la simulation peut être choisi librement, et lorsque la simulation se termine, la ferme réelle sera exactement dans l'état où elle était avant le début de la simulation.

La fonction `simulate()` est utilisée pour démarrer une simulation.

le fichier dans lequel l'exécution doit commencer  
`filename = "f1"`

commencez avec tout débloqué et entièrement amélioré  
`sim_unlocks = Unlocks`

commencez avec 10000 carottes et 50 foin  
`sim_items = {Items.Carrot : 10000, Items.Hay : 50}`

commencez avec une variable globale "a" avec une valeur de 13  
`sim_globals = {"a" : 13}`

utilisez une graine aléatoire fixe  
`seed = 0`

accélérez la simulation par un facteur de 64  
`speedup = 64`

exécutez la simulation  
`run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)`

La fonction `simulate()` renvoie le temps, en secondes, qu'il a fallu pour simuler le fichier de départ donné.

### Nom du Fichier
Le premier argument de la fonction simulate est le nom de fichier. C'est le nom qui s'affiche en haut de la fenêtre de code. La simulation exécutera le fichier spécifié comme si vous aviez cliqué sur le bouton Exécuter dessus.

### Déblocages de Départ
Toutes les fonctionnalités de programmation telles que les boucles, les instructions if, les listes, les dicts,... resteront toujours débloquées.

Le deuxième argument vous permet de spécifier avec quels déblocages/ améliorations la simulation doit commencer en plus des fonctionnalités de programmation. Cela devrait être une séquence de déblocages. La simulation commencera avec tous les déblocages de la séquence améliorés à leur niveau maximum.

Si vous souhaitez spécifier un niveau d'amélioration autre que le maximum, vous pouvez passer un dictionnaire qui associe les déblocages aux niveaux de déblocage. Dans ce cas, les valeurs négatives correspondent au niveau de déblocage maximum.

### Objets de Départ
Le troisième argument vous permet de passer un dictionnaire qui associe des objets à des nombres. Il spécifie les objets avec lesquels commencer la simulation.

### Variables Globales de Départ
Étant donné que la simulation commence une nouvelle exécution de programme complètement, vous ne pouvez pas accéder aux variables du programme qui démarre la simulation.  
Cependant, il est possible de passer des valeurs à la simulation en utilisant le quatrième argument. Il s'agit d'un dict qui associe des noms de variables sous forme de chaînes à des valeurs. Ces variables sont ensuite ajoutées à la portée globale de l'exécution à l'intérieur de la simulation.

Notez que cela copie toutes les valeurs, donc les modifier à l'intérieur de la simulation n'affectera pas les valeurs originales à l'extérieur de la simulation. Il n'est pas possible de renvoyer des valeurs de la simulation autres que le temps qu'il a fallu pour s'exécuter.

### Graine Aléatoire
Le cinquième argument vous permet de spécifier la graine aléatoire utilisée dans la simulation. Cela doit être un entier positif. Les valeurs négatives entraîneront l'utilisation d'une graine aléatoire.

La graine aléatoire affecte tout, des temps de croissance des plantes aux agencements de labyrinthes en passant par les temps de décroissance de l'eau. Si vous commencez plusieurs fois la même simulation avec la même graine aléatoire et les mêmes conditions initiales, le résultat devrait toujours être le même.

### Accélération
Le sixième argument est l'accélération initiale de la simulation. Cela vous permet de tester les choses rapidement. Si le jeu ne peut pas suivre la vitesse définie, il ralentira automatiquement.

L'accélération n'affecte en rien le résultat de la simulation. Elle existe uniquement pour réduire le temps d'attente.