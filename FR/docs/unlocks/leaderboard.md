# Leaderboard
Si vous êtes arrivé jusqu'ici, vous avez surmonté de nombreux défis. Mais les avez-vous résolus efficacement ?
Vous pouvez rivaliser avec d'autres joueurs sur différents leaderboards pour les méthodes de culture les plus efficaces.

Vous pouvez démarrer une course de leaderboard en appelant `leaderboard_run(leaderboard, filename, speedup)`.
Cela démarre une [simulation](docs/unlocks/simulation.md) similaire à `simulate()` sauf que les conditions de départ sont fixes. Chaque catégorie de leaderboard a des conditions de départ et de succès différentes.

La course du leaderboard réussit si la condition de succès est `True` à la fin de la simulation. La simulation ne se terminera pas automatiquement lorsque l'objectif est atteint. Vous devez vous assurer que le programme se termine.
Si la course est réussie, votre temps sera ajouté au leaderboard.

Pour réduire la variance, toutes les courses doivent durer au moins 2 heures (vous pouvez l'accélérer, donc ça ne prendra pas si longtemps). Si une course est terminée plus tôt, elle sera répétée jusqu'à ce qu'un temps total de 2 heures soit atteint. La moyenne de toutes les courses est alors téléchargée comme votre score.

Voici un exemple de configuration qui vous placera sur le leaderboard du foin.
![](LeaderboardSetup400)

## Réinitialisation la plus rapide
La réinitialisation la plus rapide est la catégorie la plus prestigieuse. Automatisez complètement le jeu depuis une seule parcelle de ferme jusqu'au déblocage à nouveau des leaderboards.

Vous n'avez pas à tout débloquer, essayez simplement de débloquer `Unlocks.Leaderboard` le plus rapidement possible.

N'oubliez pas que vous pouvez utiliser `num_unlocked(unlock) > 0` pour vérifier si quelque chose est débloqué et vous pouvez utiliser `get_cost()` sur les déblocages pour voir ce qu'ils coûtent afin de pouvoir cultiver automatiquement les bons objets.

Appel de fonction :
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Simulation équivalente :
`unlocks = {}
items = {}
globals = {}
#une valeur de seed négative signifie une seed aléatoire
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condition de succès :
`num_unlocked(Unlocks.Leaderboard) > 0`

## Labyrinthe
Commencez avec tout de débloqué et cultivez `300000` or aussi vite que vous le pouvez. C'est exactement la quantité d'or que vous gagnerez en résolvant un labyrinthe `300` fois.

Appel de fonction :
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Simulation équivalente :
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condition de succès :
`num_items(Items.Gold) >= 300000`

## Dinosaure
Commencez avec tout de débloqué et cultivez `98010` os aussi vite que vous le pouvez. C'est exactement le nombre d'os que vous obtiendrez si vous remplissez une zone de 10x10 avec la queue du dinosaure.

Appel de fonction :
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Simulation équivalente :
`unlocks = Unlocks
items = {Items.Pumpkin : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condition de succès :
`num_items(Items.Bone) >= 98010`

## Autres Leaderboards de Ressources
Chaque plante a son propre leaderboard pour cultiver cette plante particulière le plus rapidement possible. Vous commencez avec tous les déblocages, les ressources dont vous avez besoin pour cultiver la plante, et beaucoup de puissance. L'objectif est de cultiver `100000` de la ressource produite par la plante.

Appels de fonction :
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
`leaderboard_run(Leaderboards.Polyculture, filename, speedup)`

Condition de succès :
`num_items(resource) >= 100000`

`Leaderboards.Polyculture` nécessite de cultiver `100000` des trois ressources de polyculture.