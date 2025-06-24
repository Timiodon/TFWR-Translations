# Labyrinthes
`Items.Weird_Substance`, qui est obtenue en [fertilisant](docs/unlocks/fertilizer.md) des plantes, a un effet étrange sur les buissons. Si le drone est au-dessus d'un buisson et que tu appelles `use_item(Items.Weird_Substance, amount)`, le buisson se transformera en un labyrinthe de haies. La taille du labyrinthe dépend de la quantité d'`Items.Weird_Substance` utilisée (le deuxième argument de l'appel `use_item()`). Sans améliorations pour le labyrinthe, utiliser `n` `Items.Weird_Substance` donnera un labyrinthe de `n`x`n`. Chaque niveau d'amélioration du labyrinthe double le trésor, mais il double aussi la quantité d'`Items.Weird_Substance` nécessaire.  
Donc pour faire un labyrinthe complet :

`plant(Entities.Bush)
n_substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, n_substance)`

Pour une raison quelconque, le drone ne peut pas voler au-dessus des haies, même si elles ne semblent pas si hautes.

Il y a un trésor caché quelque part dans la haie. Utilise `harvest()` sur le trésor pour recevoir de l'or égal à l'aire du labyrinthe. (Par exemple, un labyrinthe de 5x5 donnera 25 or.)

Si tu utilises `harvest()` ailleurs, le labyrinthe disparaîtra simplement.

`get_entity_type()` est égal à `Entities.Treasure` si le drone est au-dessus du trésor et à `Entities.Hedge` partout ailleurs dans le labyrinthe.

Les labyrinthes ne contiennent pas de boucles, à moins que tu ne réutilises le labyrinthe (voir ci-dessous comment réutiliser un labyrinthe). Ainsi, il n'y a aucun moyen pour le drone de revenir à la même position sans reculer.

Tu peux vérifier s'il y a un mur en essayant de le traverser. 
`move()` renvoie `True` si ça a réussi et `False` sinon.

Si tu n'as aucune idée de comment atteindre le trésor, consulte le Conseil 1. Il te montre comment aborder un problème comme celui-ci.

Pour un défi supplémentaire, tu peux aussi réutiliser le labyrinthe en utilisant à nouveau la même quantité d'`Items.Weird_Substance` sur le trésor.
Cela augmentera la quantité d'or dans le trésor d'un labyrinthe complet et le déplacera à une position aléatoire dans le labyrinthe.

Utiliser `measure()` sur un trésor renvoie la position où il se déplacera, sous la forme d'un tuple.
`next_x, next_y = measure()`

Chaque fois que le trésor est déplacé, un mur aléatoire peut être retiré du labyrinthe. Ainsi, les labyrinthes réutilisés peuvent contenir des boucles.

Note que les boucles dans le labyrinthe rendent cela beaucoup plus difficile, car cela signifie que tu peux revenir au même endroit sans reculer. 
Réutiliser un labyrinthe ne te donne pas plus d'or que de simplement récolter et créer un nouveau labyrinthe. C’est totalement un défi supplémentaire que tu peux simplement ignorer. Ce n'en vaut la peine que si les informations supplémentaires et les raccourcis te permettent de résoudre le labyrinthe plus rapidement.

Le même labyrinthe peut être résolu un maximum de 300 fois. Cela correspond à 299 déplacements. Après cela, utiliser la substance étrange sur le trésor n'augmentera plus l'or qu'il contient et `measure()` renverra `None`.

<spoiler=montrer le conseil 1>Voici une approche générale pour résoudre le problème :

Crée un labyrinthe et imagine que tu es le drone.

Réfléchis à comment tu essaierais de trouver le trésor si tu étais dans le labyrinthe.

Note ta stratégie étape par étape pour que quelqu'un d'autre puisse la suivre sans réfléchir.

Maintenant, essaie de traduire tes étapes en code.
</spoiler>
<spoiler=montrer le conseil 2>Tant qu'il n'y a pas de boucles : Tous les murs sont en fait un seul grand mur connecté. Si tu suis le mur, il te guidera à travers tout le labyrinthe. Cette approche nécessite très peu de code, et tu n'as pas besoin de suivre où tu es déjà allé. Une dizaine de lignes de code est tout ce dont tu as besoin.</spoiler>
<spoiler=montrer le conseil 3>Plutôt que de déplacer le drone dans des directions absolues comme est ou ouest, il peut être très utile de déplacer le drone dans des directions relatives comme "tourner à droite" ou "tourner à gauche". Pour ce faire, tu dois suivre la direction actuelle du drone. Le drone ne tourne jamais réellement, mais tu peux maintenir une rotation "virtuelle" dans le code. Le tour d'index suivant est utile pour cela :

`directions = [North, East, South, West]
index = 0`

Utilise `% 4` pour lui permettre de "tourner en rond", donc après `West` ça revient à `North`.
`# tourner à droite
index = (index + 1) % 4`

`# tourner à gauche
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=montrer le conseil 4>Si tu ne peux pas le résoudre, tu peux toujours te faciliter la vie et le faire de manière moins efficace. Résoudre un labyrinthe de `1`x`1` est trivial.</spoiler>