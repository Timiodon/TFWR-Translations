[<-煤炭](docs/unlocks/coal.md) <right>[石英->](docs/unlocks/quartz.md)
<right>[铁矿探查->](docs/unlocks/prospecting.md)
<right>[藏宝图->](docs/unlocks/treasure_map.md)
---
# 铁矿

你在黏土下方的岩石层中发现了铁矿脉。

铁矿脉的矿头很小，要找到还需要一点运气。随着此解锁项等级提高，矿脉的最大规模也会增大。想更稳定地找到铁矿，还可以看看矿石探查解锁项。

铁矿脉始终连成一片，不会斜着跨越地块。如果找到一块铁矿，就检查它的下方及相邻地块，确保采完整条矿脉。

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

[统计数据](docs/stats.md)      [采矿](docs/unlocks/mining.md)      [铁矿探查](docs/unlocks/prospecting.md)      [地下感官](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)
