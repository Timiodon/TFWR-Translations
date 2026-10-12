[<- Добыча](docs/unlocks/mining.md)
---
# Подземные датчики

Добавим несколько датчиков, чтобы дрон мог ориентироваться под землей.

Теперь с помощью `get_pos_z()` можно узнать высоту дрона: она начинается с 0 и становится отрицательной по мере спуска.

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
    "exclude_unlocks": ["watering", "fertilizer"],
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#CODE
move(North)
move(North)
move(East)
dig()
dig()
dig()
print(get_pos_z())
}}

`get_ground_type()` возвращает тип земли под дроном. Можно передать функции аргумент направления, например `get_ground_type(North)`, чтобы узнать тип земли в соседней клетке.

Вот как проверить, является ли блок под дроном почвой:

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
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#CODE
dig()
if get_ground_type() == Grounds.Dirt:
    do_a_flip()
}}


`get_hardness()` возвращает твердость клетки земли под дроном. Функции можно передать аргумент направления, например `get_hardness(North)`. Чем тверже клетка, тем дольше придется ее раскапывать.

`get_stability()` возвращает устойчивость клетки земли под дроном. Функции можно передать аргумент направления, например `get_stability(North)`. Устойчивость 1 означает, что блок выдержит перепад высоты в 1 блок, прежде чем обвалиться.

Учти: при бурении вниз четыре соседних с дроном блока удаляются независимо от их устойчивости, если у блока нет особой функции. Например, глина, железо и кварц по этому правилу не удаляются. Однако они все равно могут обвалиться из-за недостаточной устойчивости.
---

[Добыча](docs/unlocks/mining.md)      [Датчики](docs/unlocks/senses.md)

[get_pos_z()](functions/get_pos_z)      [get_ground_type()](functions/get_ground_type)      [get_hardness()](functions/get_hardness)      [get_stability()](functions/get_stability)
