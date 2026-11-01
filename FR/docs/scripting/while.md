[<- Premier programme](docs/first_program.md) <right>[Amélioration de Vitesse ->](docs/unlocks/speed.md)
---
# Boucle While
Tu as débloqué la boucle `while` et les valeurs `True` et `False`. La boucle `while` continue d'exécuter le corps de la boucle tant que la condition est `True`.

`while condition:
	#corps de la boucle`

Ne t'inquiète pas de créer des boucles infinies. Le drone peut rester bloqué, mais le jeu entier ne se figera pas : il suffit d’arrêter le programme et de réessayer.

## Pour les Débutants
Peut-être as-tu déjà essayé de mettre plusieurs appels `harvest()` à la suite :

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
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
harvest()
harvest()
harvest()
}}
Cela te permet de récolter plusieurs fois en une seule exécution du programme.
Mais ce serait bien de récolter plus de trois fois, et répéter le même code rend vite le programme brouillon.
La solution est une boucle.
Une boucle te permet d'exécuter le même code plusieurs fois.

La boucle while prend une condition, qui est une valeur logique qui ne peut être que dans l'un des deux états : `True` ou `False`.
Une telle valeur est appelée une valeur booléenne.

La boucle exécute ensuite le code à l'intérieur de la boucle jusqu'à ce que la condition soit `False`.
La boucle while ressemble à ceci :

`while condition:
	#corps de la boucle
	#corps de la boucle
	#...`
	
Où tu dois remplacer "condition" par une valeur booléenne et `#corps de la boucle` par ce que tu veux faire dans la boucle.

Il y a deux valeurs booléennes constantes disponibles. Les constantes sont des valeurs qui ne changent jamais pendant le programme.

Pour créer une valeur booléenne constante, écris simplement `True` ou `False`.
Donc tu pourrais soit écrire

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
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while False:
	do_a_flip()
}}
ou

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
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	do_a_flip()
}}
Le premier ne fera jamais de looping et le second en fera pour toujours (une boucle infinie).

Normalement, créer une boucle infinie est une mauvaise idée car cela figera le programme, mais dans ce jeu, il y a des délais entre chaque itération de la boucle, donc cela fera que le drone continuera à faire des loopings jusqu'à ce que tu l'arrêtes manuellement en appuyant à nouveau sur le bouton d'exécution.

Remarque comment la ligne après les deux-points est indentée. Une indentation comme celle-ci est utilisée pour séparer les blocs de code.
Appuie simplement sur Tab pour ajouter une indentation et sur Maj + Tab (ou Retour arrière) pour la supprimer.

Remarque : si tu joues via Steam, appuyer sur Maj + Tab ouvre plutôt l’interface Steam. Tu peux réassigner le raccourci de désindentation dans les options du jeu, ou le raccourci de l’interface dans les options de l’interface Steam.

Ici, `do_a_flip()` et `pet_the_piggy()` sont appelées en boucle parce qu’elles se trouvent dans le bloc `while` indenté. En revanche, `harvest()` ne s’exécute jamais puisqu’elle se trouve après ce bloc.
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
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	do_a_flip()
	pet_the_piggy()
harvest()
}}

---

[Boucle for](docs/scripting/for.md)      [If](docs/scripting/if.md)      [Break](docs/scripting/break.md)      [Continue](docs/scripting/continue.md)      [Éditeur externe](docs/external_editor.md)
