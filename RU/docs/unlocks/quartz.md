[<- Железо](docs/unlocks/iron.md) <right>[Грибы ->](docs/unlocks/mushroom.md)
---
# Кварц

Кварц образует игольчатые жилы у нижней границы каменного слоя и в твердой почве под ним. Жилы растут вертикальными столбами, поэтому найти их наугад довольно трудно.

К счастью, из железа можно соорудить подобие лозоходной рамки, упрощающей поиск кварцевых жил. Для этого служит команда `prospect_quartz()`.

`prospect_quartz()` работает не так, как `prospect_iron()`. Она не указывает направление к ближайшему месторождению кварцевой руды, а возвращает евклидово расстояние (расстояние в трех измерениях) до ближайшего месторождения кварца. Вызов `prospect_quartz()` расходует 1 единицу железа, поэтому команду лучше использовать экономно.

Если `prospect_quartz()` не находит кварц поблизости или для поиска не хватает железа, команда возвращает `None`.

Следующий фрагмент кода позволяет дрону раскопать почву и углубиться в каменный слой. Если повезет, рядом окажется кварцевая жила, и дрон выведет расстояние до нее.

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
    "items": [{"item": "hay", "n": 100}, {"item": "iron", "n": 100}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 8,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "dynamite"]
}

#CODE
move(East)
move(North)
while get_ground_type() != Grounds.Rock:
    dig()
for i in range(30):
    dig()
do_a_flip()
do_a_flip()
print(prospect_quartz())
}}

---

[Статистика](docs/stats.md)      [Добыча](docs/unlocks/mining.md)      [Подземные датчики](docs/unlocks/underground_senses.md)      [Переменные](docs/scripting/variables.md)      [Операторы](docs/scripting/operators.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)      [prospect_quartz()](functions/prospect_quartz)
