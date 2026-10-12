[<- Добыча](docs/unlocks/mining.md) <right>[Железо ->](docs/unlocks/iron.md)
<right>[Прыжки ->](docs/unlocks/jump.md)
---
# Уголь

Оказывается, прямо под поверхностью земли можно найти залежи угля.

Уголь случайным образом появляется в горизонтальных пластах толщиной в 1 блок. Размер пласта растет пропорционально размеру мира, поэтому, чтобы найти больше угля, увеличь мир!

Следующая программа — хорошая отправная точка для поиска угля. Она бурит вниз в поисках угольного пласта, а затем — к востоку и западу от него в надежде найти еще уголь.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 4,
    "digging_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 2
}
#SETUP
move(North)
move(East)
move(East)
#CODE
while get_ground_type() != Grounds.Coal:
    dig()
dig()
move(East)
dig()
move(West)
move(West)
dig()
}}

---

[Статистика](docs/stats.md)      [Добыча](docs/unlocks/mining.md)      [Подземные датчики](docs/unlocks/underground_senses.md)

[move()](functions/move)      [get_ground_type()](functions/get_ground_type)      [dig()](functions/dig)
