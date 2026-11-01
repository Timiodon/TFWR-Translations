[<-采矿](docs/unlocks/mining.md) <right>[竹子->](docs/unlocks/bamboo.md)
<right>[石化南瓜->](docs/unlocks/petrified_pumpkins.md)
<right>[珍珠岩与壤土->](docs/unlocks/special_soils.md)
---
# 水稻
地表和 `Grounds.Dirt` 层下方有一层薄薄的 `Grounds.Clay`。这种肥沃且浸满水的地块非常适合种植水稻幼苗。

下面的代码可以帮助你向下挖掘，直到找到黏土并种下水稻：
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

只要无人机位于 `Grounds.Clay` 上方，就能用 `plant(Entities.Rice)` 种下水稻，再用 `can_harvest()` 检查是否成熟，最后用 `harvest()` 收获。

## 梯田
种下水稻后，地面会变成 `Grounds.Rice_Terrace`，为水稻成熟提供理想环境。水稻完全成熟后，地面会干燥并变成 `Grounds.Dry_Rice_Terrace`，无法再次种植水稻。幸好薄层有几格厚，因此可以用 `dig()` 挖掉地块，在下方的 `Grounds.Clay` 上再种水稻。如果整层都用完了，随时可以用 `clear()` 重置世界，再挖到新的黏土层。

---

[统计数据](docs/stats.md)      [采矿](docs/unlocks/mining.md)      [地下感官](docs/unlocks/underground_senses.md)      [If 语句](docs/scripting/if.md)      [For 循环](docs/scripting/for.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
