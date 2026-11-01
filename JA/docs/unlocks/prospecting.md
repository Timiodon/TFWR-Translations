[<- 鉄](docs/unlocks/iron.md)
---
# 鉄の探査
すでに気づかれたかもしれませんが、鉄の鉱脈はなかなか見つからないことがあります。手当たり次第に掘って偶然見つけることもできますが、もっとよい方法があります。鉄は磁性を持つので、離れた場所から探せるのです。

`prospect_iron()`コマンドがその役割を果たします。`prospect_iron()`は、最も近い鉄鉱石に1ステップ近づくためにドローンが進むべき方角（`North`、`East`、`South`、`West`）を返します。

実行には石炭を1個消費します。

ドローンがすでに最も近い鉄鉱石の真上にいる場合、コマンドを実行するための石炭が足りない場合、または範囲内に鉄がない場合、`prospect_iron()`は`None`を返します。

次のコードで、次の鉄鉱石に1ステップ近づけます：

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
    "items": [{"item": "coal", "n": 100}],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 1,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 50,
    "seed": 8,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "quartz"]
}
#SETUP
jump(Unlocks.Iron)
#CODE
# 探査結果が方向であることを確認する
if prospect_iron() != None:
    move(prospect_iron()) # 鉄の鉱脈に近づく
}}

このコードでは`prospect_iron()`を2回呼ぶため、石炭を2個消費しているので、変数を使って最適化したほうがよいかもしれません。

## 距離の計算
最も近い鉄鉱石は、ドローンが移動するのに必要なステップ数で判定されます。ドローンから東に2ブロック、北に3ブロックの位置に鉄があるなら、到達するには5ステップ必要なので、距離は5と数えます。

掘ることも1ステップとして数えます。その鉄がさらに地下7ブロックの深さに埋まっているなら、真上までの移動に5ステップ、到達するまでに7回掘るので、距離は12になります。

---

[鉄](docs/unlocks/iron.md)      [地下の感覚](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [prospect_iron()](functions/prospect_iron)
