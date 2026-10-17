[<- Рис](docs/unlocks/rice.md)
---
# Окаменевшие тыквы

Оказывается, тыквы можно найти и под землей. Они затвердели и окаменели, но для наших целей все еще подходят.

Окаменевшие тыквы встречаются под землей кубами размером 3x3x3 или 5x5x5. Надежного способа найти их нет — остается полагаться на удачу. Они появляются в твердой почве под слоем камня и железа, примерно на той же глубине, что и кварц (если он разблокирован).

Это еще один способ получать тыквы без выращивания на поверхности. Если ты предпочитаешь выращивать их, можешь вообще не заниматься окаменевшими тыквами.

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

[Статистика](docs/stats.md)      [Добыча](docs/unlocks/mining.md)      [Подземные датчики](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
