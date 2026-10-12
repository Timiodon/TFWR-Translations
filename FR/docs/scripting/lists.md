[<- Variables](docs/scripting/variables.md) <right>[Dictionnaires ->](docs/scripting/dicts.md)
---
# Listes
Les listes sont un moyen facile de stocker plusieurs valeurs dans une seule variable.
Tu peux créer de nouvelles listes comme ceci :

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
some_list = [2, True, Items.Hay]
print(some_list)
}}

La liste contient maintenant les valeurs `2`, `True` et `Items.Hay`.
Une liste peut aussi être vide :

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
empty_list = []
print(empty_list)
}}

Tu peux accéder à un élément d'une liste par son index. L'index est `0` pour le premier élément, `1` pour le deuxième, `2` pour le troisième...

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 1}, {"item": "wood", "n": 1}],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
till()
#CODE
entities = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(entities[1])
}}

Tu peux itérer sur une liste en utilisant une boucle `for`. L'exemple suivant additionne tous les éléments de la liste.

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
numbers = [4, 7, 2, 5]
sum = 0
for number in numbers:
	sum += number
print(sum)
}}

Les méthodes de liste suivantes te permettent d'ajouter et de supprimer des éléments :

`elements.append(elem)` ajoute un élément à la fin de la liste :

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
numbers = [2, 6, 12]
numbers.append(7)
print(numbers)
}}

`elements.remove(elem)` supprime la première occurrence d'un élément d'une liste :

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
numbers = [1, 2, 4, 2]
numbers.remove(2)
print(numbers)
}}

`elements.insert(index, elem)` insère un élément à l'index donné :

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
some_list = [Entities.Tree, Items.Hay]
some_list.insert(1, Items.Wood)
print(some_list)
}}

`elements.pop(index)` supprime l'élément à l'index spécifié.
Si aucun index n'est spécifié, le dernier élément est supprimé.

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
numbers = [3, 5, 8, 25]
numbers.pop()
print(numbers)
numbers.pop(1)
print(numbers)
}}

La fonction `len()` renvoie la longueur de la liste.
{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
numbers = [3, 5, 8, 25]
print(len(numbers))
}}

Les listes ont une sémantique de référence. Cela signifie qu'assigner une liste à une variable assigne le même objet liste à cette variable, plutôt que de faire une copie de la liste.
Si deux variables font référence à la même liste, les modifications apportées à la liste seront vues par les deux.

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
a = [1, 2]
b = a
b.pop()
print(a)
print(b)
}}

---

[Variables](docs/scripting/variables.md)      [Boucle for](docs/scripting/for.md)      [Tuples](docs/scripting/tuples.md)      [Dictionnaires](docs/scripting/dicts.md)      [Sets](docs/scripting/sets.md)

[len()](functions/len)
