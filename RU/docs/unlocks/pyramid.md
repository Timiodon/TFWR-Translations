[<- Бамбук](docs/unlocks/bamboo.md)
---
# Пирамиды

Теперь под землей встречаются древние пирамиды, из которых можно получать энергию!

Пирамиды построены из блоков песка (`Grounds.Sand`). Под самой пирамидой находится фундаментный слой известняка (`Grounds.Limestone`). Из-за возраста и эрозии все пирамиды частично разрушены. Фундамент сохраняется всегда, но в песке будут пустоты. Вот как выглядит откопанная пирамида:

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
while get_ground_type() != Grounds.Limestone:
    dig()
do_a_flip()
z = get_pos_z()
for i in range(6):
    for j in range(6):
        while (get_ground_type() != Grounds.Limestone
                and get_ground_type() != Grounds.Sand
                and get_pos_z() > z):
            dig()
        move(North)
    move(East)
}}

Над пирамидой всегда находятся блоки почвы. Этот факт поможет тебе откапывать пирамиды эффективнее, чем с помощью приведенного выше кода.

Как видишь, в песке есть несколько пустот, которые нужно заполнить. Восстановленная пирамида разрушится, а ты получишь в награду энергию.

Чтобы восстановить пирамиду, устанавливай блоки командой `place(Grounds.Sand)`. Песок — особый блок: без правильной опоры он сразу обваливается. Блок песка нужно ставить либо прямо на известняк, либо на площадку из песка размером 3x3. Вот небольшая пирамида, построенная вручную для примера. Конечно, созданная тобой пирамида энергии не даст:

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
for i in range(3):
    for j in range(3):
        place(Grounds.Limestone)
        move(North)
    move(East)

for i in range(3):
    for j in range(3):
        place(Grounds.Sand)
        move(North)
    move(East)

move(North)
move(East)
place(Grounds.Sand)
}}

Правильно восстановленная пирамида состоит из квадратного известнякового фундамента с нечетной длиной стороны, например 5x5. Над ним расположен слой песка того же размера (5x5), затем все меньшие слои: 3x3 и 1x1.

Восстановленная пирамида рассыплется, а в центре появится большой подсолнух. Собери его, чтобы получить энергию. Чем больше восстановленная пирамида, тем больше энергии она даст.

---

[Статистика](docs/stats.md)      [Подземные датчики](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [use_item()](functions/use_item)      [place()](functions/place)
