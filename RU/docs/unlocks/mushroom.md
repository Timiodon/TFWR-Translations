[<- Кварц](docs/unlocks/quartz.md) <right>[Динамит ->](docs/unlocks/dynamite.md)
---
# Грибы

Под землей растут колонии разных видов грибов. Во время раскопок поищи слой `Grounds.Mushroom`. Затем вызови `measure()` на земле, чтобы узнать номер типа гриба, начиная с `0`.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 100}, {"item": "iron", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 6,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}

#SETUP
jump(Unlocks.Mushrooms)
#CODE
while get_ground_type() != Grounds.Mushroom:
    dig()
do_a_flip()
print(measure())
}}

Грибы одного типа селятся рядом, но стесняются расти друг на друге. Столкни грибной блок на другой того же типа: оба исчезнут, и в награду ты получишь грибы.

С помощью `can_push(direction)` можно проверить, удастся ли толкнуть блок под дроном и не мешает ли что-нибудь в заданном направлении. `push(direction)` толкает блок и сообщает, удалось ли это сделать.

Блоки нельзя толкать вверх, а другой блок на пути помешает толчку. Вытолкнутые с опоры блоки падают на ближайший блок под ними.

Не забывай, что команда `place(Grounds.Dirt)` устанавливает блоки под дроном. Так можно заполнить ямы, чтобы проталкивать над ними блоки.

---

[Статистика](docs/stats.md)      [Подземные датчики](docs/unlocks/underground_senses.md)      [Словари](docs/scripting/dicts.md)

[move()](functions/move)      [measure()](functions/measure)      [can_push()](functions/can_push)      [push()](functions/push)      [place()](functions/place)      [get_ground_type()](functions/get_ground_type)
