[<- Bambou](docs/unlocks/bamboo.md)
---
# Pyramides
Le sous-sol contient désormais d’anciennes structures pyramidales dont tu peux récolter la puissance pour accélérer ton drone !

Les pyramides sont constituées de blocs de sable (`Grounds.Sand`). Sous la pyramide elle-même se trouve une couche de fondation en calcaire (`Grounds.Limestone`). Comme elles sont anciennes et érodées, tu ne les trouveras que partiellement détruites. La couche de fondation est toujours présente, mais le sable comporte des trous.

Voici à quoi ressemble une pyramide en ruines une fois dégagée :
{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 100}, {"item": "block", "n": 100}],
    "world_size": {"x": 6, "y": 6},
    "execution_speed": 32,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 7,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "dynamite", "quartz"]
}
#SETUP
jump(Unlocks.Pyramid)
move(North)
#CODE
# Creuser pour trouver la fondation d’une pyramide
while get_ground_type() != Grounds.Limestone:
    dig()

z = get_pos_z() # Mémoriser la profondeur de la fondation

# Creuser tout ce qui ne fait pas partie de la pyramide
for i in range(6):
    for j in range(6):
        while (get_ground_type() != Grounds.Limestone
                and get_ground_type() != Grounds.Sand
                and get_pos_z() > z):
            dig()
        move(North)
    move(East)
}}

## Restaurer la pyramide
Comme tu peux le voir, le sable présente plusieurs trous qu’il faudra combler. Lorsque tu combles les trous et restaures la pyramide, elle se détruit et un grand tournesol apparaît au centre de la base en calcaire. Récolte-le pour recevoir `Items.Power`. Plus la pyramide achevée est grande, plus tu reçois de puissance.

Tu peux restaurer une pyramide en plaçant des blocs avec la commande `place(Grounds.Sand)`. Le sable est un bloc spécial qui s’effondre immédiatement s’il n’est pas correctement soutenu. Chaque bloc de sable doit être placé soit directement sur du calcaire, soit sur une surface de sable de 3x3. Voici une petite pyramide construite à la main pour illustrer le principe. Bien sûr, la construire toi-même ne te rapportera aucune puissance :

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 100}, {"item": "block", "n": 100}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 4,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz"]
}
#CODE
# Il faut une fondation en calcaire pour poser du sable
for i in range(3):
    for j in range(3):
        place(Grounds.Limestone)
        move(North)
    move(East)

# Poser une couche de sable de 3x3 sur le calcaire
for i in range(3):
    for j in range(3):
        place(Grounds.Sand)
        move(North)
    move(East)

# Essayer de poser une autre couche de 3x3
# Seul le bloc central est soutenu et reste en place
for i in range(3):
    for j in range(3):
        place(Grounds.Sand)
        move(North)
    move(East)
}}

Une pyramide correctement restaurée possède une fondation carrée en calcaire dont les côtés ont une longueur impaire, par exemple 5x5. Elle est surmontée d’une couche de blocs de sable de même taille (5x5), puis de couches de plus en plus petites : 3x3, puis 1x1.

Les blocs situés au-dessus de la pyramide sont toujours en terre. Tu peux exploiter cette information pour dégager une pyramide efficacement.

## Puissance
Tant que tu as de la puissance, le drone l'utilisera pour fonctionner deux fois plus vite.
Il consomme 1 de puissance toutes les 30 actions (comme les déplacements, les récoltes, les plantations...)
Exécuter d'autres instructions de code peut aussi utiliser de la puissance, mais beaucoup moins que les actions du drone.

En général, tout ce qui est accéléré par les améliorations de vitesse est aussi accéléré par la puissance.
Tout ce qui est accéléré par la puissance utilise aussi de la puissance proportionnellement au temps que cela prend pour s'exécuter, sans tenir compte des améliorations de vitesse.

La puissance n’affecte pas `dig()`.

---

[Statistiques](docs/stats.md)      [Sens souterrains](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [use_item()](functions/use_item)      [place()](functions/place)
