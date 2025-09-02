# Classement
Si tu es arrivé jusqu'ici, tu as surmonté de nombreux défis. Mais les as-tu résolus efficacement ?
Tu peux rivaliser avec d'autres joueurs sur divers classements pour les méthodes agricoles les plus efficaces.

Tu peux démarrer une course de classement en appelant `leaderboard_run(leaderboard, filename, speedup)`.
Cela lance une [simulation](docs/unlocks/simulation.md) similaire à `simulate()`, sauf que les conditions de départ sont fixes. Chaque catégorie de classement a des conditions de départ et de succès différentes.

La course de classement réussit si la condition de succès est `True` lorsque la simulation se termine. La simulation ne se terminera pas automatiquement lorsque l'objectif est atteint. Tu dois t'assurer que le programme se termine.
Si la course est réussie, ton temps sera ajouté au classement.

Pour réduire la variance, toutes les courses doivent durer au moins 2 heures (tu peux l'accélérer, donc ça ne prendra pas si longtemps). Si une course est terminée plus tôt, elle sera répétée jusqu'à ce qu'un temps total de 2 heures soit atteint. La moyenne de toutes les courses est ensuite téléchargée comme ton score.

Voici un exemple de configuration qui te placera dans le classement du foin.
![](LeaderboardSetup400)

## Réinitialisation la Plus Rapide
La réinitialisation la plus rapide est la catégorie la plus prestigieuse. Automatise entièrement le jeu depuis une seule parcelle de ferme jusqu'au déblocage à nouveau des classements.

Tu n'as pas besoin de tout débloquer, essaie simplement de débloquer `Unlocks.Leaderboard` aussi vite que possible.

N'oublie pas que tu peux utiliser `num_unlocked(unlock) > 0` pour vérifier si quelque chose est débloqué et tu peux utiliser `get_cost()` sur les déblocages pour voir ce qu'ils coûtent afin de pouvoir cultiver automatiquement les bons objets.

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
Commence avec tout débloqué et cultive `300000` or aussi vite que possible. C'est exactement la quantité d'or que tu gagneras en résolvant un labyrinthe `300` fois.

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
Commence avec tout débloqué et cultive `98010` os aussi vite que possible. C'est exactement le nombre d'os que tu obtiendras si tu remplis une zone de 10x10 avec la queue du dinosaure.

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

## Autres Classements de Ressources
Chaque plante a son propre classement pour cultiver cette plante particulière le plus rapidement possible. Tu commences avec tous les déblocages, les ressources dont tu as besoin pour faire pousser la plante, et beaucoup de puissance. L'objectif est de cultiver `100000` de la ressource produite par la plante.

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