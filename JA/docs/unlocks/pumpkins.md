[<- 木](docs/unlocks/trees.md) <right>[混作 ->](docs/unlocks/polyculture.md)
<right>[サボテン ->](docs/unlocks/cactus.md)
---
# カボチャ
[カボチャ](objects/pumpkin)はニンジンと同じように耕した土で育ちます。植えるにはニンジンが必要です。

正方形内のすべてのカボチャが完全に成長すると、それらは一緒に成長して巨大なカボチャになります。残念ながら、カボチャは完全に成長すると20%の確率で枯れてしまうため、合体させたい場合は枯れたものを植え直す必要があります。

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

カボチャが枯れると、収穫しても何もドロップしない枯れたカボチャが残ります。その場所に新しい植物を植えると、枯れたカボチャは自動的に取り除かれるため、収穫する必要はありません。`can_harvest()` は枯れたカボチャに対して常に `False` を返します。

巨大なカボチャの収穫量は、カボチャのサイズによって異なります。

1x1のカボチャは `1*1*1 = 1` 個のカボチャを収穫します。
2x2のカボチャは `4` 個ではなく `2*2*2 = 8` 個のカボチャを収穫します。
3x3のカボチャは `9` 個ではなく `3*3*3 = 27` 個のカボチャを収穫します。
4x4のカボチャは `16` 個ではなく `4*4*4 = 64` 個のカボチャを収穫します。
5x5のカボチャは `25` 個ではなく `5*5*5 = 125` 個のカボチャを収穫します。
`n`x`n`のカボチャは `n >= 6` の場合、`n*n*6` 個のカボチャを収穫します。

完全な倍率を得るには、少なくとも6x6サイズのカボチャを手に入れるのが良いでしょう。

これは、正方形のすべてのタイルにカボチャを植えても、カボチャの1つが枯れてメガカボチャの成長を妨げる可能性があることを意味します。

---

[統計](docs/stats.md)      [演算子](docs/scripting/operators.md)      [変数](docs/scripting/variables.md)      [感覚](docs/unlocks/senses.md)

[harvest()](functions/harvest)      [can_harvest()](functions/can_harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)
