[<-铁矿](docs/unlocks/iron.md) <right>[蘑菇->](docs/unlocks/mushroom.md)
---
# 石英
沿着 `Grounds.Rock` 中的铁矿脉继续向下，在岩石层下部及其下方的硬 `Grounds.Dirt` 中可以找到石英（用[地下感官](docs/unlocks/underground_senses.md)解锁的 `get_hardness()` 检查硬度）。

下面的代码穿过泥土，挖入岩石层。随后边挖掘边持续勘探石英，直到距离小于 2。最后输出到达位置的勘探距离。
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
    "items": [{"item": "block", "n": 1}, {"item": "iron", "n": 100}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 8,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "dynamite"]
}
#SETUP
move(East)
move(North)
#CODE
# 挖到岩石层
while get_ground_type() != Grounds.Rock:
    dig()

# 继续挖掘，直到接近石英矿脉
while prospect_quartz() == None or prospect_quartz() >= 2:
    for i in range(10):
        dig()

# 输出最终到矿脉的距离
print(prospect_quartz())
}}

## 矿脉结构
石英矿脉呈针状。矿脉形成垂直的柱状结构，单凭碰运气很难挖掘到。

## 勘探石英
好在我们可以把铁矿加工成类似探矿杖的东西，更容易找到石英矿脉。对应的命令是 `prospect_quartz()`。

`prospect_quartz()` 的工作方式与 `prospect_iron()` 不同。它不像铁矿勘探那样返回前往最近铁矿石的方向，而是返回最近石英地块与无人机之间的精确三维距离（欧几里得距离）。

执行 `prospect_quartz()` 命令需消耗 1 份铁矿，最好省着用。

如果附近没有石英，或者铁矿不足以执行探查，`prospect_quartz()` 就会返回 `None`。

## 策略
<spoiler=显示提示>可以反复勘探并移动，观察距离如何变化。在平面上设法缩短距离，就能到达石英矿脉上方。可以采用类似二分查找的策略，减少 `prospect_quartz()` 的调用次数和铁矿消耗。

更复杂的策略可以用二维几何求两个或多个圆的交点。也可以挑战完整的三边定位，求三个球面的交点，确定矿脉的精确三维位置。

可以用幂运算计算平方根，例如 `16**0.5` 就是 16 的平方根。游戏没有内置三角函数或向量运算函数，需要自己实现。

还要注意，附近可能有多条矿脉，因此相邻位置的多次测量未必指向同一条矿脉。</spoiler>

---

[统计数据](docs/stats.md)      [采矿](docs/unlocks/mining.md)      [地下感官](docs/unlocks/underground_senses.md)      [变量](docs/scripting/variables.md)      [运算符](docs/scripting/operators.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)      [prospect_quartz()](functions/prospect_quartz)
