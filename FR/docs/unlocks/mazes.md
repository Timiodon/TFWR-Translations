[<- Engrais](docs/unlocks/fertilizer.md) <right>[Mégaferme ->](docs/unlocks/megafarm.md)
---
# Labyrinthes
`Items.Weird_Substance` a un effet étrange sur les buissons. Si le drone est au-dessus d'un buisson et que tu appelles `use_item(Items.Weird_Substance, amount)`, le buisson se transformera en un labyrinthe de haies.
La taille du labyrinthe dépend de la quantité de `Items.Weird_Substance` utilisée (le deuxième argument de l'appel `use_item()`).
Sans améliorations de labyrinthe, utiliser `n` `Items.Weird_Substance` résultera en un labyrinthe de `n`x`n`. Chaque niveau d'amélioration de labyrinthe double le trésor, mais double aussi la quantité de `Items.Weird_Substance` nécessaire. 
Donc, pour créer un labyrinthe de la taille du champ :

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": -1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
}}


Pour une raison quelconque, le drone ne peut pas voler par-dessus les haies, même si elles n'ont pas l'air si hautes.

Il y a un trésor caché quelque part dans le labyrinthe. Utilise `harvest()` sur le trésor pour recevoir de l'or égal à la surface du labyrinthe. (Par exemple, un labyrinthe de 5x5 rapportera 25 or.)

Si tu utilises `harvest()` n'importe où ailleurs, le labyrinthe disparaîtra simplement.

`get_entity_type()` est égal à `Entities.Treasure` si le drone est sur le trésor et `Entities.Hedge` partout ailleurs dans le labyrinthe.

Les labyrinthes ne contiennent aucune boucle, sauf si tu réutilises le labyrinthe (voir ci-dessous comment réutiliser un labyrinthe). Il n'y a donc aucun moyen pour le drone de se retrouver à la même position sans revenir en arrière.

Tu peux vérifier s'il y a un mur en essayant de le traverser. 
`move()` renvoie `True` en cas de succès et `False` sinon.

`can_move()` peut être utilisé pour vérifier s'il y a un mur sans se déplacer.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(East)
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
#CODE
quick_print(
    can_move(North), 
    can_move(East), 
    can_move(South), 
    can_move(West)
)
if move(North) and get_entity_type() == Entities.Treasure:
    harvest()
}}

Si tu n'as aucune idée de comment atteindre le trésor, jette un œil à l'Indice 1. Il te montre comment aborder un problème comme celui-ci.

Utiliser `measure()` n'importe où dans le labyrinthe renvoie la position du trésor.
`x, y = measure()`

Pour un défi supplémentaire, tu peux également réutiliser le labyrinthe en utilisant à nouveau la même quantité de `Items.Weird_Substance` sur le trésor. 
Cela permet de récolter le trésor et le déplace à une nouvelle position aléatoire dans le labyrinthe.

Chaque fois que le trésor est déplacé, certaines des cloisons du labyrinthe peuvent être retirées aléatoirement. Les labyrinthes réutilisés peuvent donc contenir des boucles.

Note que les boucles dans le labyrinthe le rendent beaucoup plus difficile car cela signifie que tu peux revenir au même endroit sans reculer.
Réutiliser un labyrinthe ne te donne pas plus d'or que de simplement récolter et créer un nouveau labyrinthe.
C'est un défi 100% supplémentaire que tu peux simplement ignorer.
Cela ne vaut le coup que si les informations supplémentaires et les raccourcis t'aident à résoudre le labyrinthe plus rapidement.

Le trésor peut être déplacé jusqu'à 300 fois. Après cela, utiliser de la Substance Étrange sur le trésor ne te donnera plus d'or et ne déplacera plus le trésor.

<spoiler=montrer l'indice 1>
Voici une approche générale pour résoudre le problème :

Crée un labyrinthe et imagine que tu es le drone.

Pense à la façon dont tu essaierais de trouver le trésor si tu étais dans le labyrinthe.

Note ta stratégie étape par étape pour que quelqu'un d'autre puisse la suivre sans réfléchir.

Essaie maintenant de traduire ces étapes en code.
</spoiler>
<spoiler=afficher l’indice 2>
Tant qu’il n’y a pas de boucle, tous les murs forment un seul grand mur connecté. Pose ta main gauche dessus et suis-le : il te guidera dans tout le labyrinthe.
Cette méthode demande très peu de code et ne nécessite pas de mémoriser les endroits déjà visités. Une dizaine de lignes suffit.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": true,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": -1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
#CODE
directions = [North, East, South, West]
index = 0
while get_entity_type() != Entities.Treasure:
    index = (index - 1) % 4
    for _ in range(4):
        if move(directions[index]):
            break
        index = (index + 1) % 4
do_a_flip()
harvest()
}}
</spoiler>
<spoiler=montrer l'indice 3>
Au lieu de déplacer le drone dans des directions absolues comme l'est ou l'ouest, il peut être très utile de déplacer le drone dans des directions relatives comme "tourner à droite" ou "tourner à gauche". Pour ce faire, tu dois garder une trace de la direction dans laquelle le drone se déplace actuellement. Le drone ne tourne jamais réellement, mais tu peux toujours garder une rotation "virtuelle" dans le code.
L'astuce d'index suivante est utile pour cela :

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
directions = [North, East, South, West]
index = 0
move(directions[index])

#tourner à droite
index = (index + 1) % 4
move(directions[index])

#tourner à gauche
index = (index - 1) % 4
move(directions[index])
}}


`% 4` permet de tourner « en boucle » : `3 (West) + 1` redevient ainsi `0 (North)`, car `4 % 4 == 0` et `-1 % 4 == 3`.</spoiler>
<spoiler=montrer l'indice 4>
Si tu n'arrives pas à le résoudre, tu peux toujours te simplifier la vie et le faire de manière moins efficace. 
Résoudre un labyrinthe de `1`x`1` est trivial.</spoiler>

---

[Statistiques](docs/stats.md)      [Listes](docs/scripting/lists.md)      [Dictionnaires](docs/scripting/dicts.md)      [Tuples](docs/scripting/tuples.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [can_move()](functions/can_move)      [move()](functions/move)      [use_item()](functions/use_item)
