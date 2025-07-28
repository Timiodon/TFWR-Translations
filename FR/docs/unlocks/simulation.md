# Simulation

Les simulations te permettent de tester rapidement du code sans changer l'état de la ferme réelle.
L'état de départ de la simulation peut être choisi librement, et lorsque la simulation se termine, la ferme réelle sera dans l'état exact où elle se trouvait avant le début de la simulation.

La fonction `simulate()` est utilisée pour démarrer une simulation.

le fichier dans lequel l'exécution doit commencer
`filename = "f1"`

commence avec tout débloqué et entièrement amélioré
`sim_unlocks = Unlocks`

commence avec 10000 carottes et 50 foin
`sim_items = {Items.Carrot : 10000, Items.Hay : 50}`

commence avec une variable globale "a" avec une valeur de 13
`sim_globals = {"a" : 13}`

utilise une graine aléatoire fixe
`seed = 0`

accélère la simulation par un facteur 64
`speedup = 64`

lance la simulation
`run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)`

La fonction `simulate()` retourne le temps, en secondes, qu'a pris la simulation du fichier de départ donné.

### Nom de fichier
Le premier argument de la fonction simulate est le nom de fichier (filename). C'est le nom qui est affiché en haut de la fenêtre de code. La simulation exécutera le fichier spécifié comme si tu avais cliqué sur le bouton Exécuter.

### Déblocages de départ
Toutes les fonctionnalités de programmation comme les boucles, les instructions if, les listes, les dicts,... resteront toujours débloquées.

Le deuxième argument te permet de spécifier avec quels déblocages/améliorations la simulation doit commencer en plus des fonctionnalités de programmation. Ce doit être une séquence de déblocages. La simulation commencera avec tous les déblocages de la séquence améliorés à leur niveau maximum.

Si tu veux spécifier un niveau d'amélioration autre que le maximum, tu peux passer un dictionnaire qui mappe les déblocages aux niveaux de déblocage. Dans ce cas, les valeurs négatives correspondent au niveau de déblocage maximum.

### Objets de départ
Le troisième argument te permet de passer un dictionnaire qui mappe des objets à des nombres. Il spécifie les objets avec lesquels commencer la simulation.

### Globales de départ
Parce que la simulation démarre une exécution de programme complètement nouvelle, tu ne peux pas accéder aux variables du programme qui lance la simulation.
Cependant, il est possible de passer des valeurs à la simulation en utilisant le quatrième argument. C'est un dict qui mappe des noms de variables sous forme de chaînes de caractères à des valeurs. Ces variables sont ensuite ajoutées au scope global de l'exécution à l'intérieur de la simulation.

Note que cela copie toutes les valeurs, donc les modifier à l'intérieur de la simulation n'affectera pas les valeurs originales à l'extérieur de la simulation. Il n'est pas possible de retourner des valeurs de la simulation autres que le temps qu'elle a pris pour s'exécuter.

### Graine Aléatoire
Le cinquième argument te permet de spécifier la graine aléatoire (random seed) utilisée dans la simulation. Ce doit être un entier positif. Les valeurs négatives utiliseront une graine aléatoire.

La graine aléatoire affecte tout, des temps de croissance des plantes aux tracés des labyrinthes en passant par les temps de décomposition de l'eau. Si tu démarres la même simulation plusieurs fois avec la même graine aléatoire et les mêmes conditions de départ, le résultat devrait toujours être le même.

### Speedup
Le sixième argument est le speedup de départ de la simulation. Cela te permet de tester les choses rapidement. Si le jeu n'est pas en mesure de suivre la vitesse définie, il ralentira automatiquement.

Le speedup n'affecte en rien le résultat de la simulation. Il n'existe que pour réduire le temps d'attente.