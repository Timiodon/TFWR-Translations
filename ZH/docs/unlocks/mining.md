[<-扩张 1](docs/unlocks/expand_1.md) <right>[地下感官->](docs/unlocks/underground_senses.md)
<right>[水稻->](docs/unlocks/rice.md)
<right>[煤炭->](docs/unlocks/coal.md)
---
# 采矿

无人机可以使用简陋钻头了，可以用它到地下寻找宝藏。

使用 `dig()` 命令挖掘下方的地块。

先来收集一些地块吧：

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
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "special_soils"]
}
#SETUP
move(North)
move(East)
#CODE
dig()
do_a_flip()
dig()
do_a_flip()
dig()
do_a_flip()
clear()
}}

如果想回到地表，随时可以使用 `clear()`。这也会修复你的农场。

将鼠标悬停在地块上，可以看到它的名称、稳定度和硬度。

# 钻头

越往下挖，地块越坚硬，挖掘所需的时间也越长。好在可以升级钻头来应对！

使用 `get_hardness()` 可以检查下方地块的硬度。如果遇到特别坚硬的一片地块，不妨绕过去，以便更快取得进展：

`while True:
    if get_hardness() < 5:
        dig()
    else:
        move(East)`

当然，越往下地块越坚硬，所以这个策略虽然有用，也无法让你一路畅通无阻。

## 塌方

向下挖掘会导致周围地块塌方。无人机四周的四个地块总会被摧毁。之后，塌方如何扩散取决于地块的稳定度。稳定度为 1 的地块（如草地）能承受 1 格的高度差。换句话说，如果草地在垂直或水平方向上的相邻地块的 z 坐标比它至少深 2 格，这块草地就会被摧毁。

地块的悬停提示框中会显示其稳定度。

地块塌方时，其上方的所有地块也会被移除。只有无人机直接挖掘的地块才会提供资源，因此塌方中损失的地块会被直接摧毁，不会产出资源。

---

[地下感官](docs/unlocks/underground_senses.md)      [While 循环](docs/scripting/while.md)

[move()](functions/move)      [dig()](functions/dig)
