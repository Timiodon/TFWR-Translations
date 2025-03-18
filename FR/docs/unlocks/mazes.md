# Labyrinthes
`Items.Weird_Substance`, qui est obtenue en [fertilisant](docs/unlocks/fertilizer.md) des plantes, a un effet étrange sur les buissons. Si le drone est au-dessus d'un buisson et que tu appelles `use_item(Items.Weird_Substance, amount)`, le buisson se transformera en un labyrinthe de haies. La taille du labyrinthe dépend de la quantité d'`Items.Weird_Substance` utilisée (le deuxième argument de l'appel `use_item()`). Sans améliorations pour le labyrinthe, utiliser `n` `Items.Weird_Substance` donnera un labyrinthe de `n`x`n`. Pour chaque niveau d'amélioration du labyrinthe, tu dois utiliser `n` `Items.Weird_Substance` supplémentaire pour obtenir le même effet. Ainsi, pour faire un labyrinthe couvrant tout le champ :

`plant(Entities.Bush)
n_substance = get_world_size() * num_unlocked(Unlocks.Mazes)
use_item(Items.Weird_Substance, n_substance)`

Pour une raison quelconque, le drone ne peut pas voler au-dessus des haies, même si elles ne semblent pas si hautes.

Il y a un trésor caché quelque part dans les haies. Utilise `harvest()` sur le trésor pour recevoir de l'or égal à la superficie du labyrinthe. (Par exemple, un labyrinthe de 5x5 donnera 25 pièces d'or.)

Si tu utilises `harvest()` ailleurs, le labyrinthe disparaîtra simplement.

`get_entity_type()` est égal à `Entities.Treasure` si le drone est au-dessus du trésor et à `Entities.Hedge` ailleurs dans le labyrinthe.

Les labyrinthes ne contiennent pas de boucles à moins que tu ne réutilises le labyrinthe (voir ci-dessous comment réutiliser un labyrinthe). Donc, il n'y a pas de moyen pour que le drone revienne à la même position sans revenir en arrière.

Tu peux vérifier s'il y a un mur en essayant de passer à travers. 
`move()` renvoie `True` s'il a réussi et `False` sinon.

Si tu n'as aucune idée de comment atteindre le trésor, prends un coup d'œil à l'Astuce 1. Elle te montre comment aborder un problème comme celui-ci.

Pour un défi supplémentaire, tu peux aussi réutiliser le labyrinthe en utilisant la même quantité d'`Items.Weird_Substance` sur le trésor à nouveau. Cela augmentera la quantité d'or dans le trésor d'un labyrinthe entier et le déplacera à une position aléatoire dans le labyrinthe.

Utiliser `measure()` sur un trésor renvoie la position à laquelle il se déplacera, sous forme de tuple.
`next_x, next_y = measure()`

Chaque fois que le trésor est déplacé, un mur aléatoire peut être retiré du labyrinthe. Donc, les labyrinthes réutilisés peuvent contenir des boucles.

Note que les boucles dans le labyrinthe rendent les choses beaucoup plus difficiles car cela signifie que tu peux revenir au même endroit sans retourner en arrière. Réutiliser un labyrinthe ne te donne pas plus d'or que de simplement le récolter et générer un nouveau labyrinthe. C'est entièrement un défi supplémentaire que tu peux ignorer. Ça ne vaut le coup que si les informations supplémentaires et les raccourcis t'aident à résoudre le labyrinthe plus rapidement.

Le même labyrinthe peut être résolu au maximum 300 fois. Cela correspond à 299 relocalisations. Après cela, utiliser la substance étrange sur le trésor n'augmentera plus l'or dedans et `measure()` renverra `None`.

<spoiler=voir astuce 1>Voici une approche générale pour résoudre le problème :

Crée un labyrinthe et imagine que tu es le drone.

Réfléchis à la façon dont tu essaierais de trouver le trésor si tu étais dans le labyrinthe.

Écris ta stratégie étape par étape pour que quelqu'un d'autre puisse la suivre sans réfléchir.

Maintenant, essaie de traduire tes étapes en code.
</spoiler>
<spoiler=voir astuce 2>Aussi longtemps qu'il n'y a pas de boucles : Tous les murs ne forment qu'un seul grand mur connecté. Si tu suis le mur, il te guidera à travers tout le labyrinthe. Cette approche ne nécessite très peu de code et tu n'as pas besoin de garder une trace des endroits où tu es déjà passé. Une dizaine de lignes de code suffisent.</spoiler>
<spoiler=voir astuce 3>Au lieu de déplacer le drone dans des directions absolues comme est ou ouest, il peut être très utile de déplacer le drone dans des directions relatives comme "tourner à droite" ou "tourner à gauche". Pour cela, tu dois suivre la direction dans laquelle le drone va actuellement. Le drone ne tourne jamais réellement, mais tu peux garder une "rotation virtuelle" en code. 

L'astuce d'index suivante est utile pour cela :

`directions = [North, East, South, West]
index = 0`

Utilise `% 4` pour lui permettre de "tourner en rond", de sorte qu'après `West` il revienne à `North`.
`# tourner à droite
index = (index + 1) % 4`

`# tourner à gauche
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=voir astuce 4>Si tu ne peux pas le résoudre, tu peux toujours te faciliter la tâche et le faire de manière moins efficace. 
Résoudre un labyrinthe de `1`x`1` est trivial.</spoiler>