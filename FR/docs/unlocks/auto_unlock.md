# Déblocage Automatique
Pour automatiser complètement le jeu, tu peux utiliser la fonction `unlock()` pour débloquer automatiquement des fonctionnalités.  
Par exemple, tu peux utiliser `unlock(Unlocks.Speed)` et `unlock(Unlocks.Expand)` pour débloquer les fonctionnalités de vitesse et d'expansion.

Pour déterminer le coût d'un déblocage, utilise simplement la fonction `get_cost()` comme tu le ferais pour une plante ou un objet.  
Exemple :  
`get_cost(Unlocks.Loops)`  
renvoie `{Items.Hay:5}`

Si tu veux savoir combien de fois un déblocage particulier a été effectué, utilise la fonction `num_unlocked(unlock)`.

Par exemple, `num_unlocked(Unlocks.Speed)` renverra le nombre de mises à niveau de vitesse que tu possèdes.

`num_unlocked(Unlocks.Senses)` retournera `1` si les sens sont débloqués et `0` s'ils ne le sont pas.

Tu peux aussi utiliser `num_unlocked()` sur Items, Entities ou Grounds. Cela retournera `1` si c'est débloqué sinon `0`.

Attention `num_unlocked(Unlocks.Carrots)` renverra le nombre de fois où ça a été débloqué/amélioré.  
`num_unlocked(Items.Carrot)` ne retournera que `0` ou `1`. (Pareil pour les autres plantes)