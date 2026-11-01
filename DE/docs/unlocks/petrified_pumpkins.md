[<- Reis](docs/unlocks/rice.md)
---
# Versteinerte Kürbisse
Anscheinend kann man unter der Erde Kürbisse finden. Sie sind hart und versteinert, aber für unsere Zwecke immer noch gut genug. Du kannst sie mit `dig()` abbauen, um Kürbisse zu erhalten.

So kannst du Kürbisse erhalten, ohne sie an der Oberfläche anzubauen. Wenn du lieber Landwirtschaft betreibst, kannst du versteinerte Kürbisse getrost ignorieren.

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

Versteinerte Kürbisse kommen unterirdisch in Blöcken der Größe 3x3x3 oder 5x5x5 vor. Es gibt keine zuverlässige Methode, sie zu finden, daher musst du darauf hoffen, dass deine Drohne beim Graben auf einen solchen Block stößt. Sie kommen jedoch in der harten Erde unterhalb der Stein- und Eisenschicht vor, ungefähr auf der Höhe, auf der auch Quarz zu finden ist (wenn du ihn freigeschaltet hast).

---

[Statistiken](docs/stats.md)      [Bergbau](docs/unlocks/mining.md)      [Unterirdische Sinne](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
