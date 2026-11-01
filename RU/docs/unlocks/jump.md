[<- Уголь](docs/unlocks/coal.md)
---
# Прыжки
Твой дрон разблокировал команду `jump()`. Чтобы использовать ее, нужно передать технологию в качестве аргумента, например `Unlocks.Iron`.

Эта команда позволяет нацелиться на определенные подземные ресурсы и мгновенно прыгнуть к ним вниз. Она особенно полезна для отладки или перемещения к недавно пропущенной жиле.

После прыжка нужный ресурс должен оказаться не глубже 3 блоков от верхней поверхности. `jump()` можно использовать только раз за выполнение программы; повторные попытки вызовут ошибку.

Следующий пример прыгает к [рису](docs/unlocks/rice.md), находит пласт глины и сажает ряд рисовых террас:
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
    "items": [{"item": "hay", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms"],
    "starting_chunk": 0
}
#CODE
# Прыгни поближе к рису
jump(Unlocks.Rice)

# Посади ряд рисовых террас
for i in range(get_world_size()):
    # Прыжок неточен: выкопай оставшиеся блоки
    while get_ground_type() != Grounds.Clay:
        dig()

    plant(Entities.Rice)

    move(East)
}}

## Поддерживаемые технологии
`jump()` работает только со следующими технологиями добычи:
- Уголь
- Железо
- Кварц
- Рис
- Окаменевшие тыквы
- Особые почвы
- Пирамида
- Карта сокровищ
- Грибы
- Динамит

---

[jump()](functions/jump)
