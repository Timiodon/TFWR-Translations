[<- 鉄](docs/unlocks/iron.md) <right>[キノコ ->](docs/unlocks/mushroom.md)
---
# 石英
`Grounds.Rock`の鉄の鉱脈より先に進むと、岩の層の下部とその下の硬い`Grounds.Dirt`に石英があります（[地下の感覚](docs/unlocks/underground_senses.md)の`get_hardness()`で硬さを調べてください）。

次のコードは土を通り抜け、岩の層まで掘ります。そこで掘りながら石英を探査し続け、距離が2未満になるまで進みます。最後に、その地点での探査距離を表示します。
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
    "items": [{"item": "block", "n": 1}, {"item": "iron", "n": 100}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 8,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "dynamite"]
}
#SETUP
move(East)
move(North)
#CODE
# 岩の層まで掘る
while get_ground_type() != Grounds.Rock:
    dig()

# 石英の鉱脈が近づくまで掘る
while prospect_quartz() == None or prospect_quartz() >= 2:
    for i in range(10):
        dig()

# 鉱脈までの最終的な距離を表示する
print(prospect_quartz())
}}

## 鉱脈の構造
石英は針状の鉱脈として生成されます。鉱脈は垂直方向に柱状の形を作るため、当てずっぽうで探すのはかなり困難です。

## 石英の探査
幸い、鉄を加工して占い棒のようなものを作れば、石英の鉱脈をもっと簡単に探せます。そのコマンドが `prospect_quartz()`です。

`prospect_quartz()`は`prospect_iron()`とは異なります。最も近い鉄鉱石に向かう方向ではなく、最も近い石英ブロックとドローンの正確な3D距離（ユークリッド距離）を返します。

`prospect_quartz()`の実行には鉄を1個消費するので、コマンドの使いどころを選ぶとよいでしょう。

近くに石英が見つからない場合、または鉄が足りない場合、`prospect_quartz()`は`None`を返します。

## 戦略
<spoiler=ヒントを表示>探査と移動を繰り返し、距離の変化を調べられます。平らな面で距離を最小にするように移動すれば、石英の鉱脈の上に到達できます。二分探索に似た方法を使えば、`prospect_quartz()`の呼び出し回数と鉄の消費量を抑えられます。

より高度な方法では、2Dの幾何を使って複数の円の交点を求められます。難しい方法として、3つの球の交点を求める三辺測量で鉱脈の正確な3D座標を割り出すこともできます。

平方根にはべき乗演算子を使えます。たとえば16の平方根は`16**0.5`で求められます。三角関数やベクトル用の組み込み数学関数はないので、自分で実装する必要があります。

近くに複数の鉱脈があることもあるので、近接した場所で測定しても、同じ鉱脈を指しているとは限りません。</spoiler>

---

[統計](docs/stats.md)      [採掘](docs/unlocks/mining.md)      [地下の感覚](docs/unlocks/underground_senses.md)      [変数](docs/scripting/variables.md)      [演算子](docs/scripting/operators.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)      [prospect_quartz()](functions/prospect_quartz)
