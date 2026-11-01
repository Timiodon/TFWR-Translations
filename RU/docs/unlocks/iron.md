[<- Уголь](docs/unlocks/coal.md) <right>[Кварц ->](docs/unlocks/quartz.md)
<right>[Поиск железа ->](docs/unlocks/prospecting.md)
<right>[Карта сокровищ ->](docs/unlocks/treasure_map.md)
---
# Железо
Найдя уголь в `Grounds.Dirt`, копай глубже через пласт `Grounds.Clay` до `Grounds.Rock`, чтобы найти железо.

В отличие от угольных, железные жилы идут и по вертикали. Все железные блоки жилы всегда соприкасаются напрямую, а не только по диагонали.

Поначалу железные жилы малы, и найти их будет непросто. Дальнейшие улучшения железа увеличивают максимальный размер жил и облегчают случайный поиск. Для надежного поиска открой [разведку руды](docs/unlocks/prospecting.md).

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
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 1,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 50,
    "seed": 5,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "quartz"]
}
#SETUP
#CODE
# Копай до появления железного блока
while get_ground_type() != Grounds.Iron:
    dig()

# Добудь железо
dig()
}}

---

[Статистика](docs/stats.md)      [Добыча](docs/unlocks/mining.md)      [Поиск железа](docs/unlocks/prospecting.md)      [Подземные датчики](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)
