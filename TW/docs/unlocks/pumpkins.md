[<- 樹](docs/unlocks/trees.md) <right>[混合種植 ->](docs/unlocks/polyculture.md)
<right>[仙人掌 ->](docs/unlocks/cactus.md)
---
# 南瓜
[南瓜](objects/pumpkin)像胡蘿蔔一樣生長在耕過的土地上。種植南瓜需要消耗胡蘿蔔。

當方形區域內所有的南瓜都完全成熟時，它們會長到一起，合併成 1 個巨型南瓜。不幸的是，南瓜在完全成熟後，有 20% 的機率枯死，南瓜會變為枯萎南瓜，枯萎南瓜不會參與合併行為，並且會阻止合併行為，所以如果想讓周圍的南瓜合併，需要重新種植新的南瓜，代替枯萎南瓜。

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

南瓜在枯萎時會留下枯萎南瓜，收穫時不會掉落任何東西。在枯萎南瓜的位置上種植新植物會自動將枯萎南瓜移除，所以不必收穫枯萎南瓜。請注意： `can_harvest()` 在枯萎南瓜上始終回傳 `False`。

巨型南瓜的產量取決於南瓜的大小。

1 個 1 * 1 的南瓜會產出 `1*1*1 = 1` 個南瓜。
1 個 2 * 2 的南瓜會產出 `2*2*2 = 8` 個南瓜，而不是 `4` 個。
1 個 3 * 3 的南瓜會產出 `3*3*3 = 27` 個南瓜，而不是 `9` 個。
1 個 4 * 4 的南瓜會產出 `4*4*4 = 64` 個南瓜，而不是 `16` 個。
1 個 5 * 5 的南瓜會產出 `5*5*5 = 125` 個南瓜，而不是 `25` 個。
1 個 `n` * `n` 的南瓜在 `n >= 6` 時會產出 `n*n*6` 個南瓜。

建議至少種成 6×6，才能獲得完整的產量倍率。

如果你在方形區域的每個地塊上都種上南瓜，只要其中有一個南瓜變為枯萎南瓜就會阻止巨型南瓜的合併。

---

[統計資料](docs/stats.md)      [運算子](docs/scripting/operators.md)      [變數](docs/scripting/variables.md)      [感官](docs/unlocks/senses.md)

[harvest()](functions/harvest)      [can_harvest()](functions/can_harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)
