[<- Riz](docs/unlocks/rice.md) <right>[Blocs colorés ->](docs/unlocks/debug_place.md)
<right>[Pyramides ->](docs/unlocks/pyramid.md)
---
# Bambou
Le bambou est une plante qui pousse vers le haut. Ton drone devra cueillir régulièrement ses fruits bruns pour qu’il continue à pousser. La commande `hover` que tu viens de débloquer permet de le faire.

Le bambou se plante sur un sol labouré (`Grounds.Soil`) et coûte du riz.

Le code suivant plante du bambou et attend qu’il pousse jusqu’à son premier fruit.
{{codeexample
{
"camera_position": {"x": -1, "y": 0, "z": 10},
"show_image": true,
"image_size": {"x": 800, "y": 500},
"show_code": true,
"show_inventory": true,
"show_output": false,
"collapsing": true,
"autoplay": false,
"items": [{"item": "rice", "n": 100}],
"world_size": {"x": 4, "y": 4},
"execution_speed": 2,
"action_ticks": 200,
"operation_ticks": 200,
"seed": 1,
"exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
move(East) # s’éloigner pour laisser pousser le bambou
}}

## Fruits
Le bambou pousse d’exactement 1 bloc par seconde.

Le bambou produit des fruits tous les quelques blocs. Il cesse alors de pousser, et tu dois y faire entrer ton drone pour détruire le fruit. Le bambou peut pousser jusqu’à son troisième fruit. Ensuite, il ne grandira plus, même si tu cueilles ce fruit.

Pour cueillir des fruits, utilise d’abord `hover` pour atteindre la bonne hauteur. Entre ensuite dans le fruit avec `move` pour le cueillir, puis éloigne-toi avec `move` pour laisser le bambou continuer à pousser.

Tu peux utiliser `measure()` sur le bambou pour savoir à quelle hauteur apparaîtra le prochain fruit. `measure()` compte à partir de `0`, donc `hover(measure())` place le drone à la hauteur du fruit.

{{codeexample
{
"camera_position": {"x": -1, "y": 0, "z": 10},
"show_image": true,
"image_size": {"x": 800, "y": 500},
"show_code": true,
"show_inventory": true,
"show_output": false,
"collapsing": true,
"autoplay": false,
"items": [{"item": "rice", "n": 100}],
"world_size": {"x": 4, "y": 4},
"execution_speed": 2,
"action_ticks": 200,
"operation_ticks": 200,
"seed": 1,
"exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
hover(measure()) # se placer à la hauteur du fruit

move(East) # s’éloigner et attendre la croissance
for i in range(3):
    do_a_flip()

move(West) # cueillir le fruit
move(East) # s’éloigner à nouveau
}}

## Vol stationnaire
La commande `hover` prend un argument : la hauteur de vol, un nombre de `0` à `18`. La hauteur de vol par défaut du drone est `1`. `hover` ne peut pas faire descendre le drone dans une entité solide : s’il est déjà au-dessus du bambou, tu ne peux pas l’y faire entrer avec `hover(0)`.

`hover` renvoie `True` si le drone a atteint la hauteur indiquée, sinon `False`.

La commande `get_hover` renvoie quant à elle la hauteur de vol actuelle du drone.

Si tu utilises `dig`, `harvest` ou `plant` en vol stationnaire, le drone revient à sa hauteur de vol par défaut (`1`).

Enfin, la hauteur de vol n’affecte pas `get_pos_z()`. Cette commande renvoie toujours la position z du bloc sous le drone.

## Récolter le bambou
Tu peux utiliser `harvest()`, mais la méthode recommandée consiste à entrer dans le bambou avec ton drone à la hauteur de vol `0` (`hover(0)`). Cela récolte toute la plante en une fois.

Pour récolter le bambou sans le détruire, tu peux y entrer avec `move` à n’importe quelle hauteur, par exemple avec `hover(3)`. Tous les morceaux à partir de cette hauteur seront récoltés, mais le bambou restera vivant. Un bambou partiellement récolté produit de nouveau des fruits, que tu devras donc cueillir à nouveau.

Dans les deux cas, ton rendement est égal au carré du nombre de morceaux de bambou détruits : plus le bambou est haut, meilleur est le rendement.

---

[Statistiques](docs/stats.md)      [Boucle for](docs/scripting/for.md)      [Variables](docs/scripting/variables.md)      [If](docs/scripting/if.md)      [Fonctions](docs/scripting/functions.md)      [Riz](docs/unlocks/rice.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [measure()](functions/measure)
