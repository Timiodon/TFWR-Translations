[<- Riz](docs/unlocks/rice.md)
---
# Citrouilles pétrifiées
Apparemment, on peut trouver des citrouilles sous terre. Elles se sont solidifiées et pétrifiées, mais elles conviennent encore parfaitement à nos besoins. Creuse-les avec `dig()` pour obtenir des citrouilles.

Cela offre un autre moyen d’obtenir des citrouilles sans les cultiver en surface. Si tu préfères les cultiver, tu peux tout simplement ignorer les citrouilles pétrifiées.

{{codeexample 
{
    "camera_position": {"x": -2, "y": 1, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [],
    "exclude_unlocks": ["mushrooms", "watering", "fertilizer", "pyramid", "dynamite", "quartz"],
    "world_size": {"x": 6, "y": 6},
    "execution_speed": 8,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 3
}
#SETUP
jump(Unlocks.Petrified_Pumpkins)
move(East)
move(North)
move(North)
move(North)
#CODE
while get_ground_type() != Grounds.Petrified_Pumpkin:
    dig()
z = get_pos_z()
for i in range(get_world_size()):
    for j in range(get_world_size()):
        while get_pos_z() > z - 2 and get_ground_type() != Grounds.Petrified_Pumpkin:
            dig()
        move(North)
    move(East)
for _ in range(3):
    dig()
    move(East)
    dig()
    move(South)
    dig()
    move(West)
    dig()
    move(West)
    dig()
    move(North)
    dig()
    move(North)
    dig()
    move(East)
    dig()
    move(East)
    dig()
    move(South)
    move(West)
}}

Les citrouilles pétrifiées apparaissent sous terre dans des blocs de 3x3x3 ou de 5x5x5. Il n’existe aucun moyen infaillible de les trouver : il faut simplement espérer que ton drone tombe dessus en creusant. Elles se trouvent cependant dans la terre dure sous la couche de pierre et de fer, à peu près à la même profondeur que le quartz (si tu l’as débloqué).

---

[Statistiques](docs/stats.md)      [Exploitation minière](docs/unlocks/mining.md)      [Sens souterrains](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
