[<-竹子](docs/unlocks/bamboo.md)
---
# 金字塔
现在地下会出现古代金字塔，你可以从中收获能量来加速无人机！

金字塔由沙地块（`Grounds.Sand`）构成，下方是一层石灰岩（`Grounds.Limestone`）地基。由于年代久远、遭受侵蚀，找到时总有一部分损坏。石灰岩地基始终完整，但沙层会出现坑洞。

挖出的金字塔遗迹是这样的：
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
    "items": [{"item": "hay", "n": 100}, {"item": "block", "n": 100}],
    "world_size": {"x": 6, "y": 6},
    "execution_speed": 32,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 7,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "dynamite", "quartz"]
}
#SETUP
jump(Unlocks.Pyramid)
move(North)
#CODE
# 向下挖掘，寻找金字塔地基
while get_ground_type() != Grounds.Limestone:
    dig()

z = get_pos_z() # 记住地基的深度

# 挖掉不属于金字塔的部分
for i in range(6):
    for j in range(6):
        while (get_ground_type() != Grounds.Limestone
                and get_ground_type() != Grounds.Sand
                and get_pos_z() > z):
            dig()
        move(North)
    move(East)
}}

## 修复金字塔
如你所见，沙层里有几个坑洞需要填补。填满这些坑洞、将金字塔修复还原后，金字塔会自行崩塌，石灰岩底座中央会出现一株巨大的向日葵。收获它即可获得 `Items.Power`。修复的金字塔越大，获得的能量越多。

使用 `place(Grounds.Sand)` 命令放置地块，就能修复金字塔。沙是特殊地块，缺乏适当支撑时会立即塌方。每次放置沙地块时，必须将其直接放在石灰岩上，或放在 3x3 的沙地块上。下面是一座用于演示的手工建造小金字塔。当然，自己建造的金字塔不会提供能量：

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
    "items": [{"item": "hay", "n": 100}, {"item": "block", "n": 100}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 4,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz"]
}
#CODE
# 放置沙子需要石灰岩地基
for i in range(3):
    for j in range(3):
        place(Grounds.Limestone)
        move(North)
    move(East)

# 在石灰岩上铺一层 3x3 的沙子
for i in range(3):
    for j in range(3):
        place(Grounds.Sand)
        move(North)
    move(East)

# 尝试再铺一层 3x3 的沙子
# 只有中间地块有支撑并保留下来
for i in range(3):
    for j in range(3):
        place(Grounds.Sand)
        move(North)
    move(East)
}}

正确修复的金字塔，底部是一块边长为奇数（如 5x5）的正方形石灰岩地基。其上是一层同样规模的沙地块（5x5），再向上逐层缩小：3x3，最后是 1x1。

金字塔上方的地块总是泥土。你可以利用这一点，更加有效地挖掘金字塔。

## 能量
只要有能量，无人机就会以两倍的速度运行。
无人机每 30 次行动（如移动、收获、种植……）消耗 1 点能量。
执行其他代码语句也会消耗能量，但比无人机行动少得多。

总的来说，所有可以通过提升速度来加速的东西都可以使用能量进行加速。
在不考虑速度倍率的情况下，任何使用能量加速的东西消耗的能量都与执行时间成正比。

能量不会影响 `dig()`。

---

[统计数据](docs/stats.md)      [地下感官](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [use_item()](functions/use_item)      [place()](functions/place)
