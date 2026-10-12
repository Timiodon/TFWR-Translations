[<- 稲](docs/unlocks/rice.md) <right>[カラフルなブロック ->](docs/unlocks/debug_place.md)
<right>[ピラミッド ->](docs/unlocks/pyramid.md)
---
# 竹

竹は高さ6ブロックまで育つ植物です。上にドローンがいる間は成長しないので、`plant(Entities.Bamboo)`を使ったらドローンを`move`で移動させてください。竹を植えるには稲がコストとして消費されます。

竹はランダムに決まる高さに達すると花を咲かせます。`measure()`で開花する高さを調べられます。`measure()`は0から数えるので、2番目のブロックで竹が開花する場合`measure()`は1を返します：

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 1000, "y": 500},
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
print(measure())
move(East)
}}

花の真上にドローンがいるときに`harvest()`で、竹の収穫量が最大になります。花から1ブロック離れるごとに、収穫量は8分の1になります。
たとえば、花の高さが3で、その2ブロック上から収穫すると、収穫量は64分の1になります。

高い位置の花を収穫するには、ドローンを目的の高さにしてから竹の中へ飛び込みます。新しくアンロックされた`place()`コマンドが役立ちます。

`place(Grounds.Dirt)`を使って竹の隣にブロックを重ねて、上に登ります。次に`move()`で横から竹の中へ飛び込みます。`harvest()`を呼ぶときは、ドローンが花の真上にいる必要があります。

`place(Grounds.Dirt)`はブロックを1個消費します！`Grounds.Rock`など別の地面も配置できますが、`Grounds.Clay`のような特殊なブロックは配置できません。

竹は1秒ごとにちょうど1ブロック成長します。

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 1000, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "block", "n": 100}, {"item": "rice", "n": 100}],
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
print(measure())
move(East)
place(Grounds.Dirt)
do_a_flip() # 少し待つ
do_a_flip()
move(West)
harvest()
}}

---

[統計](docs/stats.md)      [forループ](docs/scripting/for.md)      [変数](docs/scripting/variables.md)      [If文](docs/scripting/if.md)      [関数](docs/scripting/functions.md)      [稲](docs/unlocks/rice.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [place()](functions/place)      [measure()](functions/measure)
