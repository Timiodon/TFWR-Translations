[<- Повышение скорости](docs/unlocks/speed.md) <right>[Расширение 2 ->](docs/unlocks/expand_2.md)
<right>[Добыча ->](docs/unlocks/mining.md)
---
# Расширение 1
Твоя ферма выросла! От нового пространства мало пользы, если дрон не может перемещаться, поэтому появилась функция `move()`. Функция `move()` перемещает дрон в указанном направлении. Доступны четыре новые константы: `North, East, South, West`

Например, `move(North)` переместит дрона на одну клетку на север.

Если выйти за край фермы, дрон появится с противоположной стороны.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 3},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	move(North)
}}

---

[Цикл while](docs/scripting/while.md)      [Операторы](docs/scripting/operators.md)      [Расширение 2](docs/unlocks/expand_2.md)

[move()](functions/move)
