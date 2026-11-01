[<- 稲](docs/unlocks/rice.md) <right>[カラフルなブロック ->](docs/unlocks/debug_place.md)
<right>[ピラミッド ->](docs/unlocks/pyramid.md)
---
# 竹
竹は上に向かって伸びる植物です。成長を続けるには、ドローンで茶色の実を定期的に取り除く必要があります。新しくアンロックされた`hover`コマンドを使えば実現できます。

竹は耕した土（`Grounds.Soil`）に植える必要があり、植えるには稲を消費します。

次のコードは竹を植え、最初の実がなる高さまで育つのを待ちます。
{{codeexample
{
"camera_position": {"x": -1, "y": 0, "z": 10},
"show_image": true,
"image_size": {"x": 800, "y": 500},
"show_code": true,
"show_inventory": true,
"show_output": false,
"collapsing": true,
"autoplay": false,
"items": [{"item": "rice", "n": 100}],
"world_size": {"x": 4, "y": 4},
"execution_speed": 2,
"action_ticks": 200,
"operation_ticks": 200,
"seed": 1,
"exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
move(East) # 竹が成長できるように離れる
}}

## 実
竹は1秒ごとにちょうど1ブロック成長します。

竹には数ブロックおきに実がなります。実がなると成長が止まるので、ドローンを飛び込ませて実を破壊する必要があります。

実を取り除くには、まず`hover`で正しい高さに移動します。次に`move`で実に飛び込んで取り除き、もう一度`move`で離れて竹が成長できるようにします。

竹に`measure()`を使うと、次の実がなる高さを調べられます。`measure()`は`0`から数えるので、`hover(measure())`で実の高さまで移動できます。

{{codeexample
{
"camera_position": {"x": -1, "y": 0, "z": 10},
"show_image": true,
"image_size": {"x": 800, "y": 500},
"show_code": true,
"show_inventory": true,
"show_output": false,
"collapsing": true,
"autoplay": false,
"items": [{"item": "rice", "n": 100}],
"world_size": {"x": 4, "y": 4},
"execution_speed": 2,
"action_ticks": 200,
"operation_ticks": 200,
"seed": 1,
"exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
hover(measure()) # 実の隣の高さに移動する

move(East) # 離れて成長を待つ
for i in range(3):
    do_a_flip()

move(West) # 実を取り除く
move(East) # もう一度離れる
}}

## ホバリング
`hover`コマンドには、飛行高度を表す`0`から`18`までの数値を1つ渡します。ドローンの既定の飛行高度は`1`です。`hover`では固体のエンティティの中に降下できません。そのため、すでに竹の上にいるドローンを`hover(0)`で竹に入れることはできません。

`hover`は指定した高度まで移動できた場合に`True`、そうでなければ`False`を返します。

また、`get_hover`コマンドはドローンの現在の飛行高度を返します。

ホバリング中に`dig`、`harvest`、`plant`を使うと、飛行高度は既定値の`1`に戻ります。

なお、`get_pos_z()`は飛行高度の影響を受けません。常にドローンの下にあるブロックのz座標を返します。

## 竹の収穫
`harvest()`も使えますが、竹を収穫するおすすめの方法は、飛行高度を`0`にして（`hover(0)`）竹に飛び込むことです。これで植物全体を一度に収穫できます。

竹を枯らさずに収穫したい場合は、たとえば`hover(3)`のように好きな高さで`move`して竹に入れます。その高さから上の節がすべて収穫されますが、竹は生き続けます。このように一部を収穫した竹には再び実がなるので、また実を取り除く必要があります。

どちらの場合も、収穫量は破壊した竹の節の数の2乗になります。竹が高いほど収穫量も増えます。

---

[統計](docs/stats.md)      [forループ](docs/scripting/for.md)      [変数](docs/scripting/variables.md)      [If文](docs/scripting/if.md)      [関数](docs/scripting/functions.md)      [稲](docs/unlocks/rice.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [measure()](functions/measure)
