[<- 拡張 1](docs/unlocks/expand_1.md) <right>[地下の感覚 ->](docs/unlocks/underground_senses.md)
<right>[稲 ->](docs/unlocks/rice.md)
<right>[石炭 ->](docs/unlocks/coal.md)
---
# 採掘

ドローンが原始的なドリルを手に入れました。これで地下の宝物を探せます。

`dig()`コマンドを使うと、真下のブロックを掘れます。

まずはブロックをいくつか集めてみましょう：

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
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "special_soils"]
}
#SETUP
move(North)
move(East)
#CODE
dig()
do_a_flip()
dig()
do_a_flip()
dig()
do_a_flip()
clear()
}}

地表に戻りたいときは、いつでも`clear()`を使えます。これで農場も修復されます。

ブロックにカーソルを合わせると、名前、安定性、硬さが表示されます。

# ドリル

深く掘り進むにつれ、ブロックが硬くなり、掘るのに時間がかかるようになります。そんなときはドリルをアップグレードしましょう！

`get_hardness()`で真下のブロックの硬さを確認できます。特に硬いブロックにぶつかったら、賢く回り道をしたほうが速く進めるかもしれません：

`while True:
        if get_hardness() < 5:
                dig()
        else:
                move(East)`

もちろん、下に進むほどブロックは硬くなるので、便利であるこの方法にも限界があります。

## 落盤

下に掘ると、周囲のブロックが落盤します。ドローンの隣にある4つのブロックは必ず破壊されます。その先は地面の安定性に応じて落盤が広がります。草原など安定性が1のブロックは、高さの差が1までなら耐えられます。つまり、水平または垂直方向に隣接するブロックのz座標が2ブロック以上深ければ、その草原は破壊されます。

ブロックの安定性は、カーソルを合わせたときのツールチップにも表示されます。

ブロックが落盤すると、その上にあるブロックもすべて取り除かれます。資源が得られるのはドローンが直接掘ったブロックだけなので、落盤で失ったブロックからは資源を得られません。

---

[地下の感覚](docs/unlocks/underground_senses.md)      [whileループ](docs/scripting/while.md)

[move()](functions/move)      [dig()](functions/dig)
