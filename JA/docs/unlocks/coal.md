[<- 採掘](docs/unlocks/mining.md) <right>[鉄 ->](docs/unlocks/iron.md)
<right>[ジャンプ ->](docs/unlocks/jump.md)
---
# 石炭

地表のすぐ下の地面は、石炭の鉱床を見つけるのに適しているようです。

石炭は厚さ1ブロックの水平な層としてランダムに生成されます。層のサイズはプレイヤーのワールドサイズに比例して広がるので、石炭をもっと見つけたいならワールドを大きくしましょう！

次のプログラムは石炭探しの出発点にぴったりです。石炭の層を探して下に掘り、見つけたら東西にも掘ってさらに石炭を探します。

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
    "execution_speed": 4,
    "digging_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 2
}
#SETUP
move(North)
move(East)
move(East)
#CODE
while get_ground_type() != Grounds.Coal:
    dig()
dig()
move(East)
dig()
move(West)
move(West)
dig()
}}

---

[統計](docs/stats.md)      [採掘](docs/unlocks/mining.md)      [地下の感覚](docs/unlocks/underground_senses.md)

[move()](functions/move)      [get_ground_type()](functions/get_ground_type)      [dig()](functions/dig)
