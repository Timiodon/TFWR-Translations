[<- Ryż](docs/unlocks/rice.md)
---
# Skamieniałe dynie

Najwyraźniej pod ziemią można znaleźć dynie. Stwardniały i skamieniały, ale nadal nadają się do naszych celów.

Skamieniałe dynie występują pod ziemią w skupiskach 3x3x3 lub 5x5x5. Nie ma niezawodnego sposobu na ich znalezienie, więc trzeba liczyć, że dron na nie trafi. Występują w twardej ziemi pod warstwą skał i żelaza, mniej więcej na wysokości kwarcu (jeśli jest odblokowany).

To alternatywny sposób na zdobywanie dyń bez uprawiania ich na powierzchni. Jeśli wolisz uprawę, możesz całkowicie zignorować skamieniałe dynie.

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

[Statystyki](docs/stats.md)      [Górnictwo](docs/unlocks/mining.md)      [Podziemne zmysły](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
