[<-水稻](docs/unlocks/rice.md) <right>[彩色地块->](docs/unlocks/debug_place.md)
<right>[金字塔->](docs/unlocks/pyramid.md)
---
# 竹子

竹子是一种最高可长到 6 个地块的植物。如果上方有无人机，它就不会生长。因此，使用 `plant(Entities.Bamboo)` 后，记得用 `move` 移开无人机。种植竹子需要消耗水稻。

竹子长到随机高度时会开花。使用 `measure()` 查看开花高度。`measure()` 从 0 开始计数，因此竹子在第二个地块开花时，`measure()` 会返回 1：

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 1000, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "rice", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
print(measure())
move(East)
}}

当无人机正好位于竹花上方时调用 `harvest()`，竹子的产量最高。每偏离一个地块，产量就会变成原来的八分之一。
例如，如果开花高度为 3，而你在其上方两个地块的位置收获，产量就会变成原来的六十四分之一。

要收获更高处的竹花，先让无人机升到所需高度，再从侧面飞入竹子。新解锁的 `place()` 命令能帮上忙。

用 `place(Grounds.Dirt)` 在竹子旁边堆叠地块，爬到高处。然后用 `move()` 从侧面飞入竹子。调用 `harvest()` 时，无人机应正好位于竹花上方。

`place(Grounds.Dirt)` 会消耗 1 个地块！你也可以放置 `Grounds.Rock` 等其他地块，但不能放置 `Grounds.Clay` 这样的特殊地块。

竹子每秒长高 1 个地块。

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 1000, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "block", "n": 100}, {"item": "rice", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
print(measure())
move(East)
place(Grounds.Dirt)
do_a_flip() # 稍等片刻
do_a_flip()
move(West)
harvest()
}}

---

[统计数据](docs/stats.md)      [For 循环](docs/scripting/for.md)      [变量](docs/scripting/variables.md)      [If 语句](docs/scripting/if.md)      [函数](docs/scripting/functions.md)      [水稻](docs/unlocks/rice.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [place()](functions/place)      [measure()](functions/measure)
