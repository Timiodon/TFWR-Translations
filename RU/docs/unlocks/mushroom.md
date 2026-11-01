[<- Кварц](docs/unlocks/quartz.md) <right>[Динамит ->](docs/unlocks/dynamite.md)
---
# Грибы
Под землей растут колонии разных видов грибов. Во время раскопок поищи слой `Grounds.Mushroom`. Затем вызови `measure()` на земле, чтобы узнать номер типа гриба от `0` до `5`.

Следующий код находит грибы и выводит их тип:
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
    "items": [],
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
# Обработай ряд грибов
for i in range(get_world_size()):
    # Докопайся до верхнего грибного блока
    while get_ground_type() != Grounds.Mushroom:
        dig()

    # Выведи номер типа гриба
    print(measure())

    move(East)
}}

## Сбор грибов
Грибы одного типа селятся рядом, но стесняются расти друг на друге. Толкни грибной блок под дроном командой `push(direction)`.

Поставь два грибных блока одного типа друг на друга, и они автоматически соберутся в грибы.

Код ниже освобождает место и толкает гриб, пока тот не совпадет с грибом внизу:
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
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 6,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 3,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron", "special_soils"]
}
#SETUP
jump(Unlocks.Mushrooms)
#CODE
while get_ground_type() != Grounds.Mushroom:
    dig()

depth = get_pos_z()
for i in range(2):
    # Освободи место для толчка гриба на восток
    move(East)
    while get_pos_z() > depth - 1:
        dig()
    # Вернись, толкни и следуй за блоком
    move(West)
    push(East) # Толкни гриб!
    move(East)
}}

# Перемещение блоков
С помощью `can_push(direction)` можно проверить, удастся ли толкнуть блок под дроном и не мешает ли что-нибудь в заданном направлении.

`push(direction)` толкает блок и сообщает, удалось ли это сделать.

Двигать можно только грибные блоки. Блоки нельзя толкать вверх, а другой блок на пути помешает толчку. Вытолкнутые с опоры блоки падают на ближайший блок под ними.

# Стратегия
<spoiler=подсказка>
Не забывай, что команда `place(Grounds.Dirt)` устанавливает блоки под дроном. Так можно заполнить ямы, чтобы проталкивать над ними блоки.
</spoiler>

---

[Статистика](docs/stats.md)      [Подземные датчики](docs/unlocks/underground_senses.md)      [Словари](docs/scripting/dicts.md)

[move()](functions/move)      [measure()](functions/measure)      [can_push()](functions/can_push)      [push()](functions/push)      [place()](functions/place)      [get_ground_type()](functions/get_ground_type)
