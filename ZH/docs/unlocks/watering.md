[<- 胡萝卜](docs/unlocks/carrots.md) <right>[肥料 ->](docs/unlocks/fertilizer.md)
<right>[向日葵 ->](docs/unlocks/sunflowers.md)
---
# 浇水
植物在浇水后生长得更快。地块的含水量在 `0` 到 `1` 之间。
调用 `get_water()` 函数会返回无人机当前下方地块的含水量。

植物的生长速度从含水量为 0 时的 1 倍速度线性增加到含水量为 1 时的 5 倍速度。

地块会随着时间的推移而变干：它每秒平均会失去当前含水量的 1%，但还存在一些随机变化。维持高含水量会比维持低含水量消耗更多的水。

你可以给植物浇水。你的物品栏中每 10 秒会自动加入一罐水。
升级 `Unlocks.Watering` 会让你每 10 秒获得的水量翻倍。

1 桶水的含水量为 `0.25` 。

在任何地块上调用 `use_item(Items.Water)` 都可以给地块浇水。

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

[肥料](docs/unlocks/fertilizer.md)

[use_item()](functions/use_item)      [get_water()](functions/get_water)
