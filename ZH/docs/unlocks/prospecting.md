[<-铁矿](docs/unlocks/iron.md)
---
# 铁矿探查
你可能已经发现，铁矿脉有时很难找。你可以四处挖掘碰碰运气，但还有更好的办法：铁矿有磁性，因此可以从远处探测到它。

`prospect_iron()` 命令正是为此而设。`prospect_iron()` 会返回一个方向（`North`、`East`、`South` 或 `West`），指示无人机该往哪边走一步才能接近最近的铁矿石。

每次执行此命令需消耗 1 份煤炭。

如果无人机已在最近的铁矿石正上方、煤炭不足以执行命令，或者探测范围内没有铁矿，`prospect_iron()` 就会返回 `None`。

你可以用下面的代码向下一块铁矿石靠近一步：

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
    "items": [{"item": "coal", "n": 100}],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 1,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 50,
    "seed": 8,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "quartz"]
}
#SETUP
jump(Unlocks.Iron)
#CODE
# 确保勘探返回了方向
if prospect_iron() != None:
    move(prospect_iron()) # 靠近铁矿脉
}}

这段代码当前会调用两次 `prospect_iron()`，消耗 2 份煤炭。你可以考虑用变量来优化它。

## 距离计算
最近的铁矿石按无人机必须行走的步数判断。如果铁矿石位于无人机以东 2 格、以北 3 格处，距离就算作 5，因为无人机需要走五步才能到达。

挖掘也算一步。因此，如果这块铁矿埋在地下 7 个地块深处，距离就是 12：无人机需要先走五步到铁矿上方，再向下挖七次。

---

[铁矿](docs/unlocks/iron.md)      [地下感官](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [prospect_iron()](functions/prospect_iron)
