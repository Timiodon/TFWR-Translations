[<- Морковь](docs/unlocks/carrots.md) <right>[Удобрение ->](docs/unlocks/fertilizer.md)
<right>[Подсолнухи ->](docs/unlocks/sunflowers.md)
---
# Полив
Растения растут быстрее, если их поливать. У земли есть уровень воды в диапазоне от `0` до `1`.
Функция `get_water()` возвращает уровень воды в земле под дроном.

Скорость роста линейно масштабируется от х1 при уровне воды 0 до х5 при уровне воды 1.

Земля со временем высыхает: в среднем она теряет 1% от текущего уровня воды в секунду, но значение случайным образом варьируется. На поддержание высокого уровня уходит гораздо больше воды, чем на поддержание низкого уровня.

Водой можно поливать растения. Один бак воды автоматически добавляется в инвентарь каждые 10 секунд.
Улучшение `Unlocks.Watering` удвоит количество воды, которое ты получаешь каждые 10 секунд.

Бак вмещает `0.25` воды.

Вызови `use_item(Items.Water)` над любым участком земли, чтобы его полить.
{{codeexample 
{
    "camera_position": {"x": -4, "y": 1, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "water", "n": 10}],
    "world_size": {"x": 9, "y": 1},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
for _ in range(9):
    till()
    move(East)
#CODE
for i in range(5):
    if i > 0:
        use_item(Items.Water, i)
    plant(Entities.Tree)
    print(get_water())
    move(East)
    move(East)
}}

---

[Удобрение](docs/unlocks/fertilizer.md)

[use_item()](functions/use_item)      [get_water()](functions/get_water)
