# Classement
Si tu es arrivé jusqu'ici, tu as surmonté de nombreux défis. Mais les as-tu résolus efficacement ? 
Tu peux te mesurer à d'autres joueurs sur divers classements pour les méthodes agricoles les plus efficaces.

Tu peux lancer une tentative de classement en appelant `leaderboard_run(leaderboard, filename, speedup)`.
Cela démarre une [simulation](docs/unlocks/simulation.md) similaire à `simulate()` sauf que les conditions de départ sont fixes. Chaque catégorie de classement a des conditions de départ et de réussite différentes.

La tentative de classement réussit si la condition de réussite est `True` lorsque la simulation se termine. La simulation ne se terminera pas automatiquement quand l'objectif est atteint. Tu dois t'assurer que le programme se termine.
Si la tentative est réussie, ton temps sera ajouté au classement.

Pour réduire la variance, toutes les tentatives doivent durer au moins 2 heures (tu peux accélérer le processus, donc ça ne prendra pas autant de temps). Si une tentative est terminée plus tôt, elle sera répétée jusqu'à ce qu'un temps total de 2 heures soit atteint. La moyenne de toutes les tentatives est ensuite téléchargée comme ton score.

Voici un exemple de configuration qui te permettra de te placer sur le classement du foin.
![](LeaderboardSetup400)

## Réinitialisation la plus rapide
La réinitialisation la plus rapide est la catégorie la plus prestigieuse. Automatiser complètement le jeu à partir d'une seule parcelle de ferme pour débloquer à nouveau les classements.

Tu n'as pas besoin de tout débloquer, essaie juste de débloquer `Unlocks.Leaderboard` aussi vite que possible.

Rappelle-toi que tu peux utiliser `num_unlocked(unlock) > 0` pour vérifier si quelque chose est débloqué et tu peux utiliser `get_cost()` sur les déblocages pour voir combien ils coûtent afin que tu puisses automatiquement récolter les bons objets.

Appel de Fonction :
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Simulation Équivalente :
`unlocks = {}
items = {}
globals = {}
#une valeur de seed négative signifie un seed aléatoire
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condition de Réussite :
`num_unlocked(Unlocks.Leaderboard) > 0`

## Labyrinthe
Commence avec tout débloqué et récolte `300000` or aussi vite que possible. C'est exactement la quantité d'or que tu gagneras en résolvant un labyrinthe `300` fois.

Appel de Fonction :
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Simulation Équivalente :
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condition de Réussite :
`num_items(Items.Gold) >= 300000`

## Dinosaure
Commence avec tout débloqué et récolte `98010` os aussi vite que possible. C'est exactement le nombre d'os que tu obtiendras si tu remplis une zone de 10x10 avec la queue du dinosaure.

Appel de Fonction :
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Simulation Équivalente :
`unlocks = Unlocks
items = {Items.Pumpkin : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condition de Réussite :
`num_items(Items.Bone) >= 98010`

## Autres Classements de Ressources
Chaque plante a son propre classement pour la culture de cette plante aussi rapidement que possible. Tu commences avec tous les déblocages, les ressources nécessaires pour faire pousser la plante, et beaucoup d'énergie. L'objectif est de cultiver `100000` de la ressource produite par la plante.

Appel de Fonctions :
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
`leaderboard_run(Leaderboards.Polyculture, filename, speedup)`

Condition de Réussite :
`num_items(resource) >= 100000`

`Leaderboards.Polyculture` nécessite de cultiver `100000` de chacune des trois ressources de polyculture.