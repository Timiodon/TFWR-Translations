[<- Первая программа](docs/first_program.md) <right>[Повышение скорости ->](docs/unlocks/speed.md)
---
# Цикл `while`
Разблокирован цикл `while` и значения `True` и `False`. Цикл `while` выполняет тело цикла без остановки, пока условие равно `True`.

`while condition:
	#тело цикла`

Не бойся создать бесконечные циклы. Дрон может застрять, но вся игра не зависнет: просто останови программу и попробуй снова.

## Для начинающих
Возможно, тебе уже довелось добавить несколько вызовов `harvest()` подряд:

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
harvest()
harvest()
harvest()
}}
Это позволяет собрать урожай несколько раз за один запуск программы.
Однако было бы неплохо собирать урожай более трех раз, а если писать многократно один и тот же код, программа быстро превращается в кашу.
Решением станет цикл. 
Цикл позволяет выполнять один и тот же код многократно.

Цикл `while` принимает условие, которое является логическим значением и может находиться в одном из двух состояний: `True` или `False`.
Такое значение называется логическим, или булевым.

Затем цикл выполняет код внутри него до тех пор, пока условие не станет `False`.
Цикл `while` выглядит так:

`while condition:
	#тело цикла
	#тело цикла
	#...`

Здесь `condition` нужно заменить на логическое значение, а `#тело цикла` на то, что должно происходить в цикле.

Доступны два постоянных логических значения. Константы — это значения, которые не меняются во время выполнения программы.

Чтобы создать постоянное логическое значение, просто напиши `True` или `False`.
Поэтому можно написать

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while False:
	do_a_flip()
}}
либо

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	do_a_flip()
}}
В первом случае дрон никогда не делает сальто, во втором — будет делать его вечно (бесконечный цикл).

Обычно создавать бесконечные циклы не рекомендуется, потому что они приводят к зависанию программы. Однако в игре между каждой итерацией цикла есть задержки, поэтому дрон будет продолжать делать сальто, пока ты не остановишь его вручную, снова нажав кнопку выполнения.

Обрати внимание, что строка после двоеточия имеет отступ. Такие отступы используются для разделения блоков кода.
Нажми Tab, чтобы добавить отступ, или Shift + Tab (либо Backspace), чтобы его убрать. Если выделено несколько строк, Tab и Shift + Tab применятся ко всем сразу.

Примечание: если ты играешь через Steam, сочетание Shift + Tab вместо этого откроет оверлей Steam. Сочетание для удаления отступа можно переназначить в настройках игры, а сочетание для оверлея — в настройках оверлея Steam.

Здесь `do_a_flip()` и `pet_the_piggy()` вызываются снова и снова, потому что находятся внутри блока `while` с отступом. А `harvest()` не запускается никогда, поскольку расположен после этого блока.
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	do_a_flip()
	pet_the_piggy()
harvest()
}}

---

[Цикл for](docs/scripting/for.md)      [If](docs/scripting/if.md)      [Break](docs/scripting/break.md)      [Continue](docs/scripting/continue.md)      [Внешний редактор](docs/external_editor.md)
