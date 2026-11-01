[<-采矿](docs/unlocks/mining.md) <right>[铁矿->](docs/unlocks/iron.md)
<right>[跳转->](docs/unlocks/jump.md)
---
# 煤炭
地下隐藏着各种矿石，等着你去发现和开采。穿过地表挖入 `Grounds.Dirt` 后，最先找到的矿石是煤炭。

开采煤炭不需要特殊操作，只要无人机位于 `Grounds.Coal` 地块正上方时执行 `dig()` 即可。用 `get_ground_type()` 检查无人机下方，用 `get_ground_type(direction)` 检查四个相邻地块。

下面的程序很适合用来寻找煤炭。它会向下挖掘寻找煤炭层。
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
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 4,
    "digging_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 2,
    "exclude_unlocks": ["watering", "fertilizer"]
}
#SETUP
move(North)
move(East)
move(East)
#CODE
# 挖到出现煤炭地块
while get_ground_type() != Grounds.Coal:
    dig()

# 开采煤炭
dig()
}}

## 关于塌方
只有直接挖掘的煤炭地块才会提供煤炭，无人机周围塌方的地块不会。规划采煤方式时请记住这一点，尽量多挖出煤炭，减少塌方损失。

## 矿脉结构
煤炭矿脉形成厚度为 1 格的水平薄层，需要在挖掘泥土时偶然发现。薄层内的煤炭大多直接相邻，但也有只通过对角相连的地块。

煤矿规模随农场大小成比例增加，因此可以继续升级[扩张](unlocks/expand)，增加可开采的煤炭。

## 策略
<spoiler=显示提示>
一种简单的策略，尤其适合小农场，是挖掉发现煤炭时所在深度的所有地块。要提高效率，可以用 `get_ground_type(direction)` 记录看见过煤炭的位置，避免在泥土地块上移动浪费时间。只在煤炭上移动会漏掉对角连接，务必留意。
</spoiler>

---

[统计数据](docs/stats.md)      [采矿](docs/unlocks/mining.md)      [地下感官](docs/unlocks/underground_senses.md)

[move()](functions/move)      [get_ground_type()](functions/get_ground_type)      [dig()](functions/dig)
