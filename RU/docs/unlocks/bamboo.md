[<- Рис](docs/unlocks/rice.md) <right>[Цветные блоки ->](docs/unlocks/debug_place.md)
<right>[Пирамиды ->](docs/unlocks/pyramid.md)
---
# Бамбук
Бамбук растет вверх. Дрону нужно регулярно срывать его коричневые плоды, чтобы рост продолжался. Для этого подойдет недавно открытая команда `hover`.

Бамбук нужно сажать во вспаханную почву (`Grounds.Soil`), посадка стоит рис.

Следующий код сажает бамбук и ждет, пока он вырастет до первого плода.
{{codeexample
{
"camera_position": {"x": -1, "y": 0, "z": 10},
"show_image": true,
"image_size": {"x": 800, "y": 500},
"show_code": true,
"show_inventory": true,
"show_output": false,
"collapsing": true,
"autoplay": false,
"items": [{"item": "rice", "n": 100}],
"world_size": {"x": 4, "y": 4},
"execution_speed": 2,
"action_ticks": 200,
"operation_ticks": 200,
"seed": 1,
"exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
move(East) # отлети, чтобы бамбук мог расти
}}

## Плоды
Бамбук растет со скоростью ровно 1 блок в секунду.

Бамбук дает плоды через каждые несколько блоков. При этом он перестает расти, и нужно влететь в него дроном, чтобы уничтожить плод.

Чтобы сорвать плод, сначала займи нужную высоту командой `hover`. Затем влети в плод командой `move`, чтобы сорвать его, и снова используй `move`, чтобы отлететь и дать бамбуку расти дальше.

Командой `measure()` можно узнать, на какой высоте появится следующий плод бамбука. `measure()` считает с `0`, поэтому `hover(measure())` приведет дрона на высоту плода.

{{codeexample
{
"camera_position": {"x": -1, "y": 0, "z": 10},
"show_image": true,
"image_size": {"x": 800, "y": 500},
"show_code": true,
"show_inventory": true,
"show_output": false,
"collapsing": true,
"autoplay": false,
"items": [{"item": "rice", "n": 100}],
"world_size": {"x": 4, "y": 4},
"execution_speed": 2,
"action_ticks": 200,
"operation_ticks": 200,
"seed": 1,
"exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
hover(measure()) # поднимись на высоту рядом с плодом

move(East) # отлети и дождись роста
for i in range(3):
    do_a_flip()

move(West) # сорви плод
move(East) # снова отлети
}}

## Зависание
Команда `hover` принимает один аргумент — высоту зависания, число от `0` до `18`. Стандартная высота зависания дрона — `1`. `hover` не позволяет опускаться внутрь твердых сущностей. Если дрон уже над бамбуком, команда `hover(0)` не переместит его внутрь.

`hover` возвращает `True`, если дрон достиг указанной высоты, иначе `False`.

Также есть команда `get_hover`, возвращающая текущую высоту зависания дрона.

При использовании `dig`, `harvest` или `plant` во время зависания дрон возвращается на стандартную высоту (`1`).

Наконец, высота зависания не влияет на `get_pos_z()`. Эта функция всегда возвращает координату z блока под дроном.

## Сбор бамбука
Можно использовать `harvest()`, но рекомендуемый способ сбора бамбука — влететь в него дроном на высоте `0` (`hover(0)`). Так все растение собирается за один раз.

Чтобы собрать бамбук, не уничтожая его, можно влететь в него командой `move` на любой высоте, например после `hover(3)`. Все части начиная с этой высоты будут собраны, но бамбук останется жив. После такого частичного сбора бамбук снова отрастит плоды, которые придется сорвать еще раз.

В обоих случаях урожай равен квадрату числа уничтоженных частей бамбука, так что чем выше растение, тем больше урожай.

---

[Статистика](docs/stats.md)      [Цикл For](docs/scripting/for.md)      [Переменные](docs/scripting/variables.md)      [If](docs/scripting/if.md)      [Функции](docs/scripting/functions.md)      [Рис](docs/unlocks/rice.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [measure()](functions/measure)
