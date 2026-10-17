[<- Reis](docs/unlocks/rice.md)
---
# Versteinerte Kürbisse

Anscheinend kann man unter der Erde Kürbisse finden. Sie sind hart und versteinert, aber für unsere Zwecke immer noch gut genug.

Versteinerte Kürbisse kommen unterirdisch in Blöcken der Größe 3x3x3 oder 5x5x5 vor. Es gibt keine zuverlässige Methode, sie zu finden, daher musst du darauf hoffen, dass deine Drohne beim Graben auf einen solchen Block stößt. Sie kommen jedoch in der harten Erde unterhalb der Stein- und Eisenschicht vor, ungefähr auf der Höhe, auf der auch Quarz zu finden ist (wenn du ihn freigeschaltet hast).

So kannst du Kürbisse erhalten, ohne sie an der Oberfläche anzubauen. Wenn du lieber Landwirtschaft betreibst, kannst du versteinerte Kürbisse getrost ignorieren.

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
    "items": [{"item": "hay", "n": 100}],
    "exclude_unlocks": ["mushrooms", "watering", "fertilizer", "pyramid", "dynamite"],
    "world_size": {"x": 6, "y": 6},
    "execution_speed": 8,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
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
        while get_pos_z() > z:
            dig()
        move(North)
    move(East)
}}

---

[Statistiken](docs/stats.md)      [Bergbau](docs/unlocks/mining.md)      [Unterirdische Sinne](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
