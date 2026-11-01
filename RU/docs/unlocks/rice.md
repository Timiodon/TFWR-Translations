[<- Добыча](docs/unlocks/mining.md) <right>[Бамбук ->](docs/unlocks/bamboo.md)
<right>[Окаменевшие тыквы ->](docs/unlocks/petrified_pumpkins.md)
<right>[Перлит и суглинок ->](docs/unlocks/special_soils.md)
---
# Рис
Под поверхностью и слоем `Grounds.Dirt` находится тонкий пласт `Grounds.Clay`. Оказывается, эта плодородная, пропитанная водой земля идеально подходит для посадки риса.

Следующий код может пригодиться, чтобы копать вниз, пока не найдется глина, а затем посадить рис:
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
    "exclude_unlocks": ["watering", "fertilizer"],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 8,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#SETUP
move(East)
#CODE
while get_ground_type() != Grounds.Clay:
    dig()
plant(Entities.Rice)
}}

Пока дрон над `Grounds.Clay`, можно сажать рис через `plant(Entities.Rice)`, проверять зрелость через `can_harvest()` и собирать через `harvest()`.

## Террасы
После посадки риса земля превращается в `Grounds.Rice_Terrace`, создавая идеальные условия для созревания. Когда рис созреет, земля высохнет и станет `Grounds.Dry_Rice_Terrace`, где больше нельзя сажать рис. К счастью, пласт толщиной в несколько блоков: убери блок командой `dig()` и посади рис на `Grounds.Clay` ниже. Когда пласт кончится, можно восстановить мир через `clear()` и докопаться до нового.

---

[Статистика](docs/stats.md)      [Добыча](docs/unlocks/mining.md)      [Подземные датчики](docs/unlocks/underground_senses.md)      [If](docs/scripting/if.md)      [Цикл For](docs/scripting/for.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
