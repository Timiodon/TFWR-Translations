[<- 胡蘿蔔](docs/unlocks/carrots.md) <right>[肥料 ->](docs/unlocks/fertilizer.md)
<right>[向日葵 ->](docs/unlocks/sunflowers.md)
---
# 澆水
植物在澆水後生長得更快。地塊的含水量在 `0` 到 `1` 之間。
呼叫 `get_water()` 函式會回傳無人機目前下方地塊的含水量。

植物的生長速度從含水量為 0 時的 1 倍速度線性增加到含水量為 1 時的 5 倍速度。

地塊會隨著時間的推移而變乾：它每秒平均會失去目前含水量的 1%，但還存在一些隨機變化。維持高含水量會比維持低含水量消耗更多的水。

你可以給植物澆水。你的物品欄中每 10 秒會自動加入一罐水。
升級 `Unlocks.Watering` 會讓你每 10 秒獲得的水量翻倍。

1 桶水的含水量為 `0.25` 。

在任何地塊上呼叫 `use_item(Items.Water)` 都可以給地塊澆水。

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
