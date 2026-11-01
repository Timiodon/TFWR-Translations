[<- 石英](docs/unlocks/quartz.md) <right>[ダイナマイト ->](docs/unlocks/dynamite.md)
---
# キノコ
地下にはさまざまな種類のキノコが群生しています。掘り進めながら`Grounds.Mushroom`の地層を探しましょう。その地面で`measure()`を使うと、`0`から`5`までの番号でキノコの種類を調べられます。

次のコードはキノコを探して種類を表示します：
{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 6,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}
#SETUP
jump(Unlocks.Mushrooms)
#CODE
# キノコを一列処理する
for i in range(get_world_size()):
    # いちばん上のキノコまで掘る
    while get_ground_type() != Grounds.Mushroom:
        dig()

    # キノコの種類の番号を表示する
    print(measure())

    move(East)
}}

## キノコの集め方
同じ種類のキノコは一緒にいたいようですが、互いの上に生えるのは少し恥ずかしいようです。`push(direction)`でドローンの下のキノコブロックを押してください。

同じ種類のキノコブロックを2つ重ねると、自動的に収穫されてキノコが手に入ります。

次のコードは場所を空けてから、下のキノコと同じ種類になるまでキノコを押します：
{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 6,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 3,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron", "special_soils"]
}
#SETUP
jump(Unlocks.Mushrooms)
#CODE
while get_ground_type() != Grounds.Mushroom:
    dig()

depth = get_pos_z()
for i in range(2):
    # キノコを東に押せるように場所を空ける
    move(East)
    while get_pos_z() > depth - 1:
        dig()
    # 戻って押し、押したブロックを追う
    move(West)
    push(East) # キノコを押す！
    move(East)
}}

# ブロックを押す
`can_push(direction)`で、ドローンの下のブロックを指定した方向に押せるか、障害物がないかを調べられます。

`push(direction)`はブロックを押し、成功したかどうかを返します。

押せるのはキノコのブロックだけです。ブロックは上方向には押せません。別のブロックが邪魔をしている場合も押せません。空中に押し出されたブロックは落下し、下にある次のブロックの上に着地します。

# 戦略
<spoiler=ヒント>
`place(Grounds.Dirt)`を呼ぶと、ドローンの下にブロックを配置できることも覚えておきましょう。これは穴を埋めて、その上でブロックを押したいときに役立ちます。
</spoiler>

---

[統計](docs/stats.md)      [地下の感覚](docs/unlocks/underground_senses.md)      [辞書](docs/scripting/dicts.md)

[move()](functions/move)      [measure()](functions/measure)      [can_push()](functions/can_push)      [push()](functions/push)      [place()](functions/place)      [get_ground_type()](functions/get_ground_type)
