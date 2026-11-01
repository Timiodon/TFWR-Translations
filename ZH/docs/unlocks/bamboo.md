[<-水稻](docs/unlocks/rice.md) <right>[彩色地块->](docs/unlocks/debug_place.md)
<right>[金字塔->](docs/unlocks/pyramid.md)
---
# 竹子
竹子是一种向上生长的植物。无人机需要定期摘除它的棕色果实，才能让它继续生长。新解锁的 `hover` 命令可以帮我们实现这一点。

竹子必须种在耕过的土壤（`Grounds.Soil`）上，种植需要消耗水稻。

下面的代码种下竹子，并等待它长到第一个果实出现。
{{codeexample
{
"camera_position": {"x": -1, "y": 0, "z": 10},
"show_image": true,
"image_size": {"x": 800, "y": 500},
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
move(East) # 移开，让竹子继续生长
}}

## 果实
竹子每秒长高 1 个地块。

竹子每长几格就会结出果实。此时竹子会停止生长，需要让无人机飞入竹子破坏果实。

要摘除果实，先用 `hover` 到达正确高度。然后用 `move` 飞入果实将其摘除，再用 `move` 移开，让竹子继续生长。

使用 `measure()` 测量竹子，可以查看下一个果实会出现的高度。`measure()` 从 `0` 开始计数，因此 `hover(measure())` 会将无人机带到果实所在的高度。

{{codeexample
{
"camera_position": {"x": -1, "y": 0, "z": 10},
"show_image": true,
"image_size": {"x": 800, "y": 500},
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
hover(measure()) # 悬停到果实旁边的高度

move(East) # 移开并等待竹子生长
for i in range(3):
    do_a_flip()

move(West) # 摘除果实
move(East) # 再次移开
}}

## 悬停
`hover` 命令接受一个参数：悬停高度，取值为 `0` 到 `18`。无人机的默认悬停高度为 `1`。`hover` 不能向下降入实体内部。因此，如果无人机已经位于竹子上方，就不能通过 `hover(0)` 进入竹子。

无人机成功到达指定高度时，`hover` 返回 `True`，否则返回 `False`。

此外，`get_hover` 命令可以返回无人机当前的悬停高度。

悬停时使用 `dig`、`harvest` 或 `plant`，无人机会恢复默认悬停高度（`1`）。

最后，悬停高度不会影响 `get_pos_z()`。它始终返回无人机下方地块的 z 坐标。

## 收获竹子
虽然可以使用 `harvest()`，但更推荐将悬停高度设为 `0`（`hover(0)`），再让无人机飞入竹子。这样能一次收获整株竹子。

若想保留竹子，可以在任意高度用 `move` 飞入竹子，例如先调用 `hover(3)`。这样会收获该高度及以上的所有竹节，但竹子仍然存活。以这种方式部分收获的竹子会重新长出果实，因此你还需要再次摘除。

无论采用哪种方式，产量都等于被破坏竹节数量的平方，因此竹子越高，产量越好。

---

[统计数据](docs/stats.md)      [For 循环](docs/scripting/for.md)      [变量](docs/scripting/variables.md)      [If 语句](docs/scripting/if.md)      [函数](docs/scripting/functions.md)      [水稻](docs/unlocks/rice.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [measure()](functions/measure)
