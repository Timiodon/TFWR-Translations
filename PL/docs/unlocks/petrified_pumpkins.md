[<- Ryż](docs/unlocks/rice.md)
---
# Skamieniałe dynie
Najwyraźniej pod ziemią można znaleźć dynie. Stwardniały i skamieniały, ale nadal nadają się do naszych celów. Możesz je wykopać przez `dig()`, aby otrzymać dynie.

To alternatywny sposób na zdobywanie dyń bez uprawiania ich na powierzchni. Jeśli wolisz uprawę, możesz całkowicie zignorować skamieniałe dynie.

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

Skamieniałe dynie występują pod ziemią w skupiskach 3x3x3 lub 5x5x5. Nie ma niezawodnego sposobu na ich znalezienie, więc trzeba liczyć, że dron na nie trafi. Występują w twardej ziemi pod warstwą skał i żelaza, mniej więcej na wysokości kwarcu (jeśli jest odblokowany).

---

[Statystyki](docs/stats.md)      [Górnictwo](docs/unlocks/mining.md)      [Podziemne zmysły](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
