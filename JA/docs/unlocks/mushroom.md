[<- 石英](docs/unlocks/quartz.md) <right>[ダイナマイト ->](docs/unlocks/dynamite.md)
---
# キノコ

地下にはさまざまな種類のキノコが群生しています。掘り進めながら`Grounds.Mushroom`の地層を探しましょう。その地面で`measure()`を使うと、`0`から始まる番号でキノコの種類を調べられます。

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
    "items": [{"item": "hay", "n": 100}, {"item": "iron", "n": 100}],
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
while get_ground_type() != Grounds.Mushroom:
    dig()
do_a_flip()
print(measure())
}}

同じ種類のキノコは一緒にいたいようですが、互いの上に生えるのは少し恥ずかしいようです。同じ種類のキノコのブロックを別のブロックの上に押し重ねると、両方が消えて、報酬としてキノコを得られます。

`can_push(direction)`で、ドローンの下のブロックを指定した方向に押せるか、障害物がないかを調べられます。`push(direction)`はブロックを押し、成功したかどうかを返します。

ブロックは上方向には押せません。別のブロックが邪魔をしている場合も押せません。空中に押し出されたブロックは落下し、下にある次のブロックの上に着地します。

`place(Grounds.Dirt)`を呼ぶと、ドローンの下にブロックを配置できることも覚えておきましょう。これは穴を埋めて、その上でブロックを押したいときに役立ちます。

---

[統計](docs/stats.md)      [地下の感覚](docs/unlocks/underground_senses.md)      [辞書](docs/scripting/dicts.md)

[move()](functions/move)      [measure()](functions/measure)      [can_push()](functions/can_push)      [push()](functions/push)      [place()](functions/place)      [get_ground_type()](functions/get_ground_type)
