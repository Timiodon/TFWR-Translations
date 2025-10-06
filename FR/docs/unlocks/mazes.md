# Labyrinthes
`Items.Weird_Substance`, qui est obtenu en [fertilisant](docs/unlocks/fertilizer.md) les plantes, a un effet étrange sur les buissons. Si le drone est au-dessus d'un buisson et que tu appelles `use_item(Items.Weird_Substance, amount)`, le buisson se transformera en un labyrinthe de haies.
La taille du labyrinthe dépend de la quantité de `Items.Weird_Substance` utilisée (le deuxième argument de l'appel `use_item()`).
Sans améliorations de labyrinthe, utiliser `n` `Items.Weird_Substance` résultera en un labyrinthe de `n`x`n`. Chaque niveau d'amélioration de labyrinthe double le trésor, mais double aussi la quantité de `Items.Weird_Substance` nécessaire.
Donc, pour créer un labyrinthe de la taille du champ :

`plant(Entities.Bush)
substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)`


Pour une raison quelconque, le drone ne peut pas voler par-dessus les haies, même si elles n'ont pas l'air si hautes.

Il y a un trésor caché quelque part dans la haie. Utilise `harvest()` sur le trésor pour recevoir de l'or égal à la surface du labyrinthe. (Par exemple, un labyrinthe de 5x5 rapportera 25 or.)

Si tu utilises `harvest()` n'importe où ailleurs, le labyrinthe disparaîtra simplement.

`get_entity_type()` est égal à `Entities.Treasure` si le drone est sur le trésor et `Entities.Hedge` partout ailleurs dans le labyrinthe.

Les labyrinthes ne contiennent aucune boucle, sauf si tu réutilises le labyrinthe (voir ci-dessous comment réutiliser un labyrinthe). Il n'y a donc aucun moyen pour le drone de se retrouver à la même position sans revenir en arrière.

Tu peux vérifier s'il y a un mur en essayant de le traverser. 
`move()` renvoie `True` en cas de succès et `False` sinon.

`can_move()` peut être utilisé pour vérifier s'il y a un mur sans se déplacer.

Si tu n'as aucune idée de comment atteindre le trésor, jette un œil à l'Indice 1. Il te montre comment aborder un problème comme celui-ci.

Utiliser `measure()` n'importe où dans le labyrinthe renvoie la position du trésor.
`x, y = measure()`

Pour un défi supplémentaire, tu peux également réutiliser le labyrinthe en utilisant à nouveau la même quantité de `Items.Weird_Substance` sur le trésor.
Cela augmentera la quantité d'or dans le trésor d'un labyrinthe complet et le déplacera à une position aléatoire dans le labyrinthe.

Chaque fois que le trésor est déplacé, certaines des cloisons du labyrinthe peuvent être retirées aléatoirement. Les labyrinthes réutilisés peuvent donc contenir des boucles.

Note que les boucles dans le labyrinthe le rendent beaucoup plus difficile car cela signifie que tu peux revenir au même endroit sans reculer.
Réutiliser un labyrinthe ne te donne pas plus d'or que de simplement récolter et créer un nouveau labyrinthe.
C'est un défi 100% supplémentaire que tu peux simplement ignorer.
Cela ne vaut le coup que si les informations supplémentaires et les raccourcis t'aident à résoudre le labyrinthe plus rapidement.

Le trésor peut être déplacé jusqu'à 300 fois. Après cela, utiliser de la substance bizarre sur le trésor n'augmentera plus l'or qu'il contient et il ne se déplacera plus.

<spoiler=montrer l'indice 1>Voici une approche générale pour résoudre le problème :

Crée un labyrinthe et imagine que tu es le drone.

Pense à la façon dont tu essaierais de trouver le trésor si tu étais dans le labyrinthe.

Note ta stratégie étape par étape pour que quelqu'un d'autre puisse la suivre sans réfléchir.

Maintenant, essaie de traduire tes étapes en code.
</spoiler>
<spoiler=montrer l'indice 2>Tant qu'il n'y a pas de boucles : tous les murs ne sont en réalité qu'un seul grand mur connecté. Si tu suis le mur, il te mènera à travers tout le labyrinthe.
Cette approche nécessite très peu de code et tu n'as pas besoin de garder une trace des endroits où tu es déjà allé. Environ 10 lignes de code suffisent.</spoiler>
<spoiler=montrer l'indice 3>Au lieu de déplacer le drone dans des directions absolues comme l'est ou l'ouest, il peut être très utile de déplacer le drone dans des directions relatives comme "tourner à droite" ou "tourner à gauche". Pour ce faire, tu dois garder une trace de la direction dans laquelle le drone se déplace actuellement. Le drone ne tourne jamais réellement, mais tu peux toujours garder une rotation "virtuelle" dans le code.
L'astuce d'index suivante est utile pour cela :

`directions = [North, East, South, West]
index = 0`

Utilise `% 4` pour lui permettre de tourner "autour du cercle", de sorte qu'après `West`, il revienne à `North`.
`# tourner à droite
index = (index + 1) % 4`

`# tourner à gauche
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=montrer l'indice 4>Si tu n'arrives pas à le résoudre, tu peux toujours te simplifier la vie et le faire de manière moins efficace.
Résoudre un labyrinthe de `1`x`1` est trivial.</spoiler>