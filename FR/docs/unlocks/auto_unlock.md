# Déblocages Auto
Pour automatiser entièrement le jeu, tu peux utiliser la fonction `unlock()` pour débloquer automatiquement des fonctionnalités.
Par exemple, tu peux utiliser `unlock(Unlocks.Speed)` et `unlock(Unlocks.Expand)` pour débloquer les fonctionnalités de vitesse et d'expansion.

Pour déterminer le coût d'un déblocage, utilise simplement la fonction `get_cost()` comme tu le ferais pour une plante ou un objet.
Exemple :
`get_cost(Unlocks.Loops)`
renvoie `{Items.Hay:5}`