[<-煤炭](docs/unlocks/coal.md) <right>[石英->](docs/unlocks/quartz.md)
<right>[铁矿探查->](docs/unlocks/prospecting.md)
<right>[藏宝图->](docs/unlocks/treasure_map.md)
---
# 铁矿
在 `Grounds.Dirt` 中找到煤炭后，继续向下穿过 `Grounds.Clay` 层，进入 `Grounds.Rock` 就能找到铁矿。

与煤矿脉不同，铁矿脉也会沿竖直方向延伸。矿脉内的铁矿地块始终直接相邻，绝不会只有对角连接。

铁矿脉的矿头很小，要找到还需要一点运气。继续升级铁矿可以增加矿脉的最大规模，让你更容易偶然遇到。想稳定找到铁矿，应该解锁[铁矿探查](docs/unlocks/prospecting.md)。

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
# 挖到出现铁矿地块
while get_ground_type() != Grounds.Iron:
    dig()

# 开采铁矿
dig()
}}

---

[统计数据](docs/stats.md)      [采矿](docs/unlocks/mining.md)      [铁矿探查](docs/unlocks/prospecting.md)      [地下感官](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)
