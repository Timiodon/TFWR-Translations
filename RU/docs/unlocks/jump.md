[<- Уголь](docs/unlocks/coal.md)
---
# Прыжки

Твой дрон разблокировал команду `jump()`.

Эта команда позволяет выбрать определенную технологию и перенестись к ней. Это особенно удобно для отладки или возврата к недавно пропущенной рудной жиле. Чтобы использовать ее, нужно передать технологию в качестве аргумента, например `Unlocks.Iron`.

`jump()` работает только с технологиями, появляющимися под землей, например `jump(Unlocks.Rice)` или `jump(Unlocks.Iron)`.

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
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 3,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms"],
    "starting_chunk": 0
}
#CODE
dig()
dig()
dig()
jump(Unlocks.Iron)
do_a_flip()
}}

Прыжок не обязательно доставит тебя прямо к цели, так что, возможно, придется немного поискать. Но цель гарантированно будет поблизости.

За один запуск программы `jump()` можно использовать только один раз.

---

[jump()](functions/jump)
