[<- 採掘](docs/unlocks/mining.md)
---
# 地下の感覚

地下でも道を見つけられるよう、ドローンにセンサーをいくつか追加しましょう。

`get_pos_z()`を使ってドローンの高さを取得しましょう。高さは0から始まり、下に進むほど負の値になります。

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
    "exclude_unlocks": ["watering", "fertilizer"],
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#CODE
move(North)
move(North)
move(East)
dig()
dig()
dig()
print(get_pos_z())
}}

`get_ground_type()`はドローンの下にある地面の種類を返します。たとえば`get_ground_type(North)`のように方角を引数に渡すと、隣接タイルの地面の種類を取得できます。

ドローンの下のブロックが土かどうかを確認するには、次のようにします：

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
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#CODE
dig()
if get_ground_type() == Grounds.Dirt:
    do_a_flip()
}}


`get_hardness()`はドローンの下の地面のタイルの硬さを返します。`get_hardness(North)`のように方角を引数に渡すこともできます。タイルが硬いほど、掘るのに時間がかかります。

`get_stability()`はドローンの下の地面のタイルの安定性を返します。`get_stability(North)`のように方角を引数に渡すこともできます。安定性が1なら、ブロックが落盤するまでに高さの差1に耐えられます。

ドローンが下に掘るとき、すぐ隣の4つのブロックは、特殊な機能がない限り安定性に関係なく取り除かれます。たとえば粘土、鉄、石英はこの規則では取り除かれません。ただし、安定性が足りなければ落盤する可能性はあります。
---

[採掘](docs/unlocks/mining.md)      [感覚](docs/unlocks/senses.md)

[get_pos_z()](functions/get_pos_z)      [get_ground_type()](functions/get_ground_type)      [get_hardness()](functions/get_hardness)      [get_stability()](functions/get_stability)
