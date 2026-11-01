[<- 採掘](docs/unlocks/mining.md) <right>[鉄 ->](docs/unlocks/iron.md)
<right>[ジャンプ ->](docs/unlocks/jump.md)
---
# 石炭
地下にはさまざまな鉱石が隠され、見つけて掘り出されるのを待っています。地表を通り抜けて`Grounds.Dirt`を掘ると、最初に見つかる鉱石は石炭です。

石炭の採掘に特別な操作は必要ありません。ドローンが`Grounds.Coal`ブロックの真上にいるときに`dig()`を実行するだけです。`get_ground_type()`でドローンの下を、`get_ground_type(direction)`で隣接する4ブロックを調べられます。

次のプログラムは石炭探しの出発点にぴったりです。石炭の層を探して下に掘り進めます。
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
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 4,
    "digging_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 2,
    "exclude_unlocks": ["watering", "fertilizer"]
}
#SETUP
move(North)
move(East)
move(East)
#CODE
# 石炭が現れるまで掘る
while get_ground_type() != Grounds.Coal:
    dig()

# 石炭を掘る
dig()
}}

## 崩落について
石炭が手に入るのは直接掘った石炭ブロックだけで、ドローンの周りで崩れたブロックからは得られません。崩落で失う石炭を減らし、直接掘る石炭を増やせるよう、採掘方法を工夫しましょう。

## 鉱脈の構造
鉱脈は厚さ1ブロックの水平な層を作り、土を掘る途中で偶然見つける必要があります。層の石炭ブロックは主に直接隣り合っていますが、斜めにしかつながっていないものもあります。

石炭の鉱床は農場の大きさに比例して広がるので、[拡張](unlocks/expand)をさらにアンロックすれば、より多くの石炭を掘れます。

## 戦略
<spoiler=ヒントを表示> 
特に小さな農場では、石炭を見つけた深さのブロックをすべて掘るのが簡単な方法です。効率を上げるには、`get_ground_type(direction)`で石炭を見つけた場所を記録し、土の上を移動する時間を減らせます。石炭の上だけを移動すると見逃す、斜めのつながりにも注意してください。
</spoiler>

---

[統計](docs/stats.md)      [採掘](docs/unlocks/mining.md)      [地下の感覚](docs/unlocks/underground_senses.md)

[move()](functions/move)      [get_ground_type()](functions/get_ground_type)      [dig()](functions/dig)
