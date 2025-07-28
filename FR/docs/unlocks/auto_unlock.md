# Déblocages automatiques
Pour automatiser complètement le jeu, vous pouvez utiliser la fonction `unlock()` pour débloquer automatiquement des fonctionnalités.
Par exemple, vous pouvez utiliser `unlock(Unlocks.Speed)` et `unlock(Unlocks.Expand)` pour débloquer les fonctionnalités de vitesse et d'expansion.

Pour déterminer le coût d'un déblocage, utilisez simplement la fonction `get_cost()` comme vous le feriez pour une plante ou un objet.
Exemple :
`get_cost(Unlocks.Loops)`
retourne `{Items.Hay:5}`

Si vous voulez savoir combien d'un déblocage particulier vous avez, utilisez la fonction `num_unlocked(unlock)`.

Par exemple, `num_unlocked(Unlocks.Speed)` retournera le nombre d'améliorations de vitesse que vous avez.

`num_unlocked(Unlocks.Senses)` retournera `1` si les sens sont débloqués et `0` s'ils ne le sont pas.

Vous pouvez également utiliser `num_unlocked()` sur les Items, Entities ou Grounds. Cela retournera `1` s'il est débloqué, sinon `0`.

Attention, `num_unlocked(Unlocks.Carrots)` retournera le nombre de fois qu'il a été débloqué/amélioré.
`num_unlocked(Items.Carrot)` ne retournera que `0` ou `1`. (Idem pour les autres plantes)