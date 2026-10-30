[<- 树](docs/unlocks/trees.md) <right>[混合种植 ->](docs/unlocks/polyculture.md)
<right>[仙人掌 ->](docs/unlocks/cactus.md)
---
# 南瓜
[南瓜](objects/pumpkin)像胡萝卜一样生长在耕过的土地上。种植南瓜需要消耗胡萝卜。

当方形区域内所有的南瓜都完全成熟时，它们会长到一起，合并成 1 个巨型南瓜。不幸的是，南瓜在完全成熟后，有 20% 的几率枯死，南瓜会变为枯萎南瓜，枯萎南瓜不会参与合并行为，并且会阻止合并行为，所以如果想让周围的南瓜合并，需要重新种植新的南瓜，代替枯萎南瓜。

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "carrot", "n": 11}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 5,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 3,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
for i in range(get_world_size()):
	for j in range(get_world_size()):
		till()
		plant(Entities.Pumpkin)
		move(North)
	move(East)
do_a_flip()
do_a_flip()
move(North)
move(North)
plant(Entities.Pumpkin)
do_a_flip()
plant(Entities.Pumpkin)
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
harvest()
}}

南瓜在枯萎时会留下枯萎南瓜，收获时不会掉落任何东西。在枯萎南瓜的位置上种植新植物会自动将枯萎南瓜移除，所以不必收获枯萎南瓜。请注意： `can_harvest()` 在枯萎南瓜上始终返回 `False`。

巨型南瓜的产量取决于南瓜的大小。

1 个 1 * 1 的南瓜会产出 `1*1*1 = 1` 个南瓜。
1 个 2 * 2 的南瓜会产出 `2*2*2 = 8` 个南瓜，而不是 `4` 个。
1 个 3 * 3 的南瓜会产出 `3*3*3 = 27` 个南瓜，而不是 `9` 个。
1 个 4 * 4 的南瓜会产出 `4*4*4 = 64` 个南瓜，而不是 `16` 个。
1 个 5 * 5 的南瓜会产出 `5*5*5 = 125` 个南瓜，而不是 `25` 个。
1 个 `n` * `n` 的南瓜在 `n >= 6` 时会产出 `n*n*6` 个南瓜。

所以，最佳的南瓜种植大小是 6 * 6 这样获得的南瓜产量是最大的。

如果你在方形区域的每个地块上都种上南瓜，只要其中有一个南瓜变为枯萎南瓜就会阻止巨型南瓜的合并。

---

[统计数据](docs/stats.md)      [运算符](docs/scripting/operators.md)      [变量](docs/scripting/variables.md)      [感官](docs/unlocks/senses.md)

[harvest()](functions/harvest)      [can_harvest()](functions/can_harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)
