# Classement
Si tu es arrivé jusqu'ici, tu as surmonté de nombreux défis. Mais les as-tu résolus efficacement ? 
Tu peux rivaliser avec d'autres joueurs sur divers classements pour les méthodes agricoles les plus efficaces.

Tu peux démarrer une course de classement en appelant `leaderboard_run(leaderboard, filename, speedup)`.
Cela lance une [simulation](docs/unlocks/simulation.md) similaire à `simulate()`, sauf que les conditions de départ sont fixes. Chaque catégorie de classement a des conditions de départ et de succès différentes.

La course de classement réussit si la condition de succès est `True` lorsque la simulation se termine. 

La simulation ne se terminera PAS automatiquement lorsque l'objectif est atteint. Tu dois t'assurer que le programme se termine.
Si la course est réussie, ton temps sera ajouté au classement.

Pour réduire la variance, toutes les courses doivent durer au moins 2 heures (tu peux l'accélérer, donc ça ne prendra pas si longtemps). Si une course est terminée plus tôt, elle sera répétée jusqu'à ce qu'un temps total de 2 heures soit atteint. La moyenne de toutes les courses est ensuite téléchargée comme ton score.

Voici un exemple de configuration qui te placera dans le classement du foin.
![](LeaderboardSetup400)

## Réinitialisation la Plus Rapide
La réinitialisation la plus rapide est la catégorie la plus prestigieuse. Automatise complètement le jeu, d'une seule parcelle de ferme jusqu'au déblocage à nouveau des classements.

Tu n'as pas à tout débloquer, essaie juste de débloquer `Unlocks.Leaderboard` aussi vite que possible.

Rappelle-toi que tu peux utiliser `num_unlocked(unlock) > 0` pour vérifier si quelque chose est débloqué et tu peux utiliser `get_cost()` sur les déblocages pour voir ce qu'ils coûtent afin de pouvoir cultiver automatiquement les bons objets.

Appel de fonction :
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Simulation équivalente :
`unlocks = {}
items = {}
globals = {}
#une valeur de graine négative signifie une graine aléatoire
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condition de succès :
`num_unlocked(Unlocks.Leaderboard) > 0`

## Labyrinthe
Commence avec tout débloqué et cultive `9863168` or aussi vite que tu peux. C'est exactement la quantité d'or que tu gagneras en réutilisant un labyrinthe de 32x32 `300` fois.

Appel de fonction :
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Simulation équivalente :
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condition de succès :
`num_items(Items.Gold) >= 9863168`

## Dinosaure
Commence avec tout débloqué et cultive `33488928` os aussi vite que tu peux. C'est exactement le nombre d'os que tu obtiendras si tu remplis une zone de 32x32 avec la queue du dinosaure.

Appel de fonction :
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Simulation équivalente :
`unlocks = Unlocks
items = {Items.Cactus : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condition de succès :
`num_items(Items.Bone) >= 33488928`

## Autres Classements de Ressources
Chaque plante a son propre classement pour la cultiver le plus rapidement possible. Tu commences avec tous les déblocages, les ressources nécessaires pour faire pousser la plante, et beaucoup de puissance. L'objectif est de cultiver une quantité définie de la ressource produite par la plante.

Comme toujours, tu dois t'assurer que ton programme se termine lorsque tu atteins l'objectif. Une course n'est pas terminée tant que le programme n'est pas fini, même si l'objectif est atteint.

### `Leaderboards.Cactus`
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
Condition de succès : `num_items(Items.Cactus) >= 33554432`

### `Leaderboards.Sunflowers`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
Condition de succès : `num_items(Items.Power) >= 100000`

### `Leaderboards.Pumpkins`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
Condition de succès : `num_items(Items.Pumpkin) >= 200000000`

### `Leaderboards.Wood`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
Condition de succès : `num_items(Items.Wood) >= 10000000000`

### `Leaderboards.Carrots`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
Condition de succès : `num_items(Items.Carrot) >= 2000000000`

### `Leaderboards.Hay`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
Condition de succès : `num_items(Items.Hay) >= 2000000000`

## Classements avec un seul drone
Il y a aussi des classements pour cultiver avec un seul drone. Tu n'as qu'un seul drone et une ferme de 8x8 et tu dois cultiver une certaine quantité de ressources aussi vite que possible.

### `Leaderboards.Maze_Single`
`leaderboard_run(Leaderboards.Maze_Single, filename, speedup)`
Condition de succès : `num_items(Items.Gold) >= 616448`

### `Leaderboards.Cactus_Single`
`leaderboard_run(Leaderboards.Cactus_Single, filename, speedup)`
Condition de succès : `num_items(Items.Cactus) >= 131072`

### `Leaderboards.Sunflowers_Single`
`leaderboard_run(Leaderboards.Sunflowers_Single, filename, speedup)`
Condition de succès : `num_items(Items.Power) >= 10000`

### `Leaderboards.Pumpkins_Single`
`leaderboard_run(Leaderboards.Pumpkins_Single, filename, speedup)`
Condition de succès : `num_items(Items.Pumpkin) >= 10000000`

### `Leaderboards.Wood_Single`
`leaderboard_run(Leaderboards.Wood_Single, filename, speedup)`
Condition de succès : `num_items(Items.Wood) >= 500000000`

### `Leaderboards.Carrots_Single`
`leaderboard_run(Leaderboards.Carrots_Single, filename, speedup)`
Condition de succès : `num_items(Items.Carrot) >= 100000000`

### `Leaderboards.Hay_Single`
`leaderboard_run(Leaderboards.Hay_Single, filename, speedup)`
Condition de succès : `num_items(Items.Hay) >= 100000000`