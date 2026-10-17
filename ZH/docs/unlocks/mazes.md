[<- 肥料](docs/unlocks/fertilizer.md) <right>[巨型农场 ->](docs/unlocks/megafarm.md)
---
# 迷宫
`Items.Weird_Substance` 对灌木有奇怪的效果。如果在无人机位于灌木上方时调用 `use_item(Items.Weird_Substance, amount)`，灌木将长成一个树篱迷宫。
迷宫的大小取决于使用的 `Items.Weird_Substance` 的数量（`use_item()` 调用的第二个参数）。
未升级迷宫时，使用 `n` 份 `Items.Weird_Substance` 将生成一个 `n`x`n` 的迷宫。每次迷宫升级都会使宝藏中的金币数量翻倍，但所需的 `Items.Weird_Substance` 数量也会随之翻倍。
所以若要生成一个全场迷宫：

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": -1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
}}


出于某种原因，无人机无法飞过树篱，尽管树篱看起来并没有那么高。

树篱中隐藏着一份宝藏。对宝藏使用 `harvest()` 可以获得等于迷宫面积的金币。（例如，一个 5x5 的迷宫将产出 25 份金币。）

如果在其他任何地方使用 `harvest()`，迷宫将直接消失。

如果无人机在宝藏上方，则 `get_entity_type()` 等于 `Entities.Treasure`，在迷宫的其他地方则等于 `Entities.Hedge`。

除非重复使用迷宫（关于如何重复使用迷宫，请见下文），否则迷宫不包含任何循环。因此，无人机不可能在不回头的情况下再次到达相同的位置。

你可以通过尝试穿过墙壁来检查是否有墙。
`move()` 如果成功则返回 `True`，否则返回 `False`。

`can_move()` 可以用来在不移动的情况下检查是否有墙。

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(East)
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
#CODE
quick_print(
    can_move(North), 
    can_move(East), 
    can_move(South), 
    can_move(West)
)
if move(North) and get_entity_type() == Entities.Treasure:
    harvest()
}}

如果不知道如何到达宝藏所在处，请看提示 1，其中说明了如何处理这样的问题。

在迷宫中的任何地方使用 `measure()` 都会返回宝藏的位置。
`x, y = measure()`

为了增加挑战，你也可以通过在宝藏上再次使用相同数量的 `Items.Weird_Substance` 来重复使用迷宫。
这将收集宝藏，并在迷宫中的一个随机位置生成一个新的宝藏。

每次宝藏被移动时，迷宫中的一些墙壁可能会被随机移除。所以重复使用的迷宫可能包含循环。

请注意，迷宫中的循环会显著提升难度，因为循环意味着你可以在不回头的情况下再次到达相同的位置。
重复使用迷宫得到的金币也并不会比直接收获并生成一个新迷宫更多。
这百分百是一个可以直接跳过的额外挑战。
只有当额外的信息和捷径能帮助你更快地破解迷宫时，才值得重复使用迷宫。

宝藏最多可以被重新定位 300 次。之后，在宝藏上使用奇异物质将不再获得金币，也不会再移动宝藏。

<spoiler=显示提示 1>以下是解决这个问题的一种通用方法：

创建一个迷宫，并想象你是无人机。

思考一下如果你在迷宫中会如何尝试找到宝藏。

一步步写下你的策略，清晰到可以让其他人不加思考地照办。

现在尝试将你的步骤翻译成代码。
</spoiler>
<spoiler=显示提示 2>只要没有循环，那么所有的墙壁实际上只是一长串的相连墙壁。如果沿着墙走，就会走遍整个迷宫。
这种方法需要编写的代码很少，而且不必记录已经去过的地方。大约 10 行代码就足够了。
{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": true,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": -1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
#CODE
directions = [North, East, South, West]
index = 0
while get_entity_type() != Entities.Treasure:
    index = (index - 1) % 4
    for _ in range(4):
        if move(directions[index]):
            break
        index = (index + 1) % 4
do_a_flip()
harvest()
}}
</spoiler>
<spoiler=显示提示 3>与其让无人机朝东西南北这样的绝对方向移动，朝相对方向（如“右转”或“左转”）移动可能更加实用。为此，你需要记录无人机当前移动的方向。无人机实际上从不旋转，但你仍然可以在代码中保持“虚拟”的旋转。
下面的索引技巧对此很有帮助：

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
directions = [North, East, South, West]
index = 0
move(directions[index])

#右转
index = (index + 1) % 4
move(directions[index])

#左转
index = (index - 1) % 4
move(directions[index])
}}

使用 `% 4` 可让方向在一个循环中轮转。例如，`3 (West) + 1` 又回到了 `0 (North)`，因为 `4 % 4 == 0`，而且 `-1 % 4 == 3`。</spoiler>
<spoiler=显示提示 4>如果无法破解也不必为难自己，你始终可以选择效率更低的方式。
破解一个 `1`x`1` 的迷宫总归是小菜一碟。</spoiler>

---

[统计数据](docs/stats.md)      [列表](docs/scripting/lists.md)      [字典](docs/scripting/dicts.md)      [元组](docs/scripting/tuples.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [can_move()](functions/can_move)      [move()](functions/move)      [use_item()](functions/use_item)
