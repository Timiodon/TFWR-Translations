[<- Уголь](docs/unlocks/coal.md) <right>[Кварц ->](docs/unlocks/quartz.md)
<right>[Поиск железа ->](docs/unlocks/prospecting.md)
<right>[Карта сокровищ ->](docs/unlocks/treasure_map.md)
---
# Железо

В каменном слое под глиной обнаружены железные жилы.

Поначалу железные жилы малы, и найти их будет непросто. Повышение уровня этой технологии увеличивает максимальный размер рудной жилы. Для более надежного поиска железа также пригодится технология разведки руды.

Железная жила всегда непрерывна и не переходит по диагонали. Найдя железо, поищи еще ниже или рядом, чтобы собрать всю жилу.

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
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 1,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz"]
}
#SETUP
jump(Unlocks.Iron)
#CODE
for i in range(4):
    dig()
do_a_flip()
}}

---

[Статистика](docs/stats.md)      [Добыча](docs/unlocks/mining.md)      [Поиск железа](docs/unlocks/prospecting.md)      [Подземные датчики](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)
