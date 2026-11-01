# Classement souterrain
Le sous-sol réserve des défis encore plus grands. Prêt à optimiser tes programmes de minage et de culture ?
Ce déblocage te permet de rivaliser pour les méthodes les plus efficaces dans les profondeurs.

Tu peux lancer une tentative de classement souterrain en appelant `leaderboard_run(leaderboard, filename, speedup)`.
Cela lance une [simulation](docs/unlocks/simulation.md) similaire à `simulate()`, sauf que les conditions de départ sont fixes. Chaque catégorie de classement a des conditions de départ et de succès différentes.

La course de classement réussit si la condition de succès est `True` lorsque la simulation se termine. 

La simulation ne se terminera PAS automatiquement lorsque l'objectif est atteint. Tu dois t'assurer que le programme se termine.
Si la course est réussie, ton temps sera ajouté au classement.

Pour réduire la variance, toutes les courses doivent couvrir au moins 2 heures de temps simulé. Tu peux accélérer la simulation, cela ne prendra donc pas autant de temps réel. Si une course se termine plus tôt, elle est répétée jusqu’à atteindre 2 heures simulées au total. La moyenne de toutes les courses est alors envoyée comme score.

Voici un exemple de configuration pour entrer dans le classement `Leaderboards.Rice_Single`.

![|x400](UndergroundLeaderboardSetup)

## Réinitialisation souterraine la plus rapide
La réinitialisation souterraine est la catégorie la plus prestigieuse. Tu y automatises entièrement l’arbre minier, d’une seule case jusqu’au nouveau déblocage de `Unlocks.Underground_Leaderboard`.

Tu n’as pas à tout débloquer : essaie simplement de débloquer `Unlocks.Underground_Leaderboard` le plus vite possible.

Rappelle-toi que tu peux utiliser `num_unlocked(unlock) > 0` pour vérifier si quelque chose est débloqué et tu peux utiliser `get_cost()` sur les déblocages pour voir ce qu'ils coûtent afin de pouvoir cultiver automatiquement les bons objets.

`unlock()` ne tient pas compte des dépendances de l’arbre technologique. Il est par exemple possible de débloquer `Unlocks.Fertilizer` avant `Unlocks.Water`.

Appel de fonction :
`leaderboard_run(Leaderboards.Fastest_Underground_Reset, filename, speedup)`

Simulation équivalente :
`unlocks = {}
items = {}
globals = {}
#une valeur de graine négative signifie une graine aléatoire
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condition de succès :
`num_unlocked(Unlocks.Underground_Leaderboard) > 0`

## Minerais
Ce classement teste tes compétences dans la production de minerais, surtout le quartz. Il modifie la génération du sol pour fournir du charbon, puis du fer, puis du quartz, dans cet ordre.

Commence avec tout débloqué et produis `20000` de quartz le plus vite possible.

Appel de fonction :
`leaderboard_run(Leaderboards.Ores, filename, speedup)`

Simulation équivalente :
`unlocks = Unlocks
items = {Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condition de succès :
`num_items(Items.Quartz) >= 20000`

## Carte au trésor
Ce classement commence avec tout débloqué et beaucoup de puissance. Il modifie la génération du sol pour qu’il y ait beaucoup de cartes au trésor.

Il se déroule dans un monde de 8x8 avec un seul drone. L’objectif est de produire `115000` d’or le plus vite possible.

Appel de fonction :
`leaderboard_run(Leaderboards.Treasure_Map, filename, speedup)`

Simulation équivalente :
`unlocks = Unlocks
items = {Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condition de succès :
`num_items(Items.Gold) >= 115000`

## Classements de ressources
Ces classements consistent à produire des ressources précises le plus vite possible. Tu commences avec tout débloqué et beaucoup de puissance. Seule exception : le classement des pyramides, où tu dois produire ta puissance en restaurant des pyramides.

L’objectif est de produire une quantité définie de ressources.

Comme toujours, tu dois t'assurer que ton programme se termine lorsque tu atteins l'objectif. Une course n'est pas terminée tant que le programme n'est pas fini, même si l'objectif est atteint.

Ces classements modifient la génération du sol pour que la ressource recherchée apparaisse continuellement. Il n’est donc pas nécessaire d’utiliser `clear()`. Par exemple, le classement du riz ne contient que des couches d’argile.

### `Leaderboards.Rice`
`leaderboard_run(Leaderboards.Rice, filename, speedup)`
Condition de succès : `num_items(Items.Rice) >= 2000000`

### `Leaderboards.Bamboo`
Il est interdit de creuser dans le classement du bambou.

`leaderboard_run(Leaderboards.Bamboo, filename, speedup)`
Condition de succès : `num_items(Items.Bamboo) >= 500000000`

### `Leaderboards.Dynamite`
`leaderboard_run(Leaderboards.Dynamite, filename, speedup)`
Condition de succès : `num_items(Items.Dynamite) >= 10000000`

### `Leaderboards.Mushrooms`
`leaderboard_run(Leaderboards.Mushrooms, filename, speedup)`
Condition de succès : `num_items(Items.Mushroom) >= 240000`

### `Leaderboards.Pyramids`
`leaderboard_run(Leaderboards.Pyramids, filename, speedup)`
Condition de succès : `num_items(Items.Power) >= 150000`

## Classements souterrains à un drone
Il y a aussi des classements pour cultiver avec un seul drone. Tu n'as qu'un seul drone et une ferme de 8x8 et tu dois cultiver une certaine quantité de ressources aussi vite que possible.

### `Leaderboards.Rice_Single`
`leaderboard_run(Leaderboards.Rice_Single, filename, speedup)`
Condition de succès : `num_items(Items.Rice) >= 100000`

### `Leaderboards.Ores_Single`
`leaderboard_run(Leaderboards.Ores_Single, filename, speedup)`
Condition de succès : `num_items(Items.Quartz) >= 4000`

### `Leaderboards.Bamboo_Single`
`leaderboard_run(Leaderboards.Bamboo_Single, filename, speedup)`
Condition de succès : `num_items(Items.Bamboo) >= 25000000`

### `Leaderboards.Dynamite_Single`
`leaderboard_run(Leaderboards.Dynamite_Single, filename, speedup)`
Condition de succès : `num_items(Items.Dynamite) >= 100000`

### `Leaderboards.Mushrooms_Single`
`leaderboard_run(Leaderboards.Mushrooms_Single, filename, speedup)`
Condition de succès : `num_items(Items.Mushroom) >= 30000`

### `Leaderboards.Pyramids_Single`
`leaderboard_run(Leaderboards.Pyramids_Single, filename, speedup)`
Condition de succès : `num_items(Items.Power) >= 30000`

