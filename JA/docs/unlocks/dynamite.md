[<- キノコ](docs/unlocks/mushroom.md) <right>[爆発ドリル ->](docs/unlocks/explosive_drill.md)
---
# ダイナマイト
かつての採掘隊が残した画期的な爆薬です。残念ながら、ドリルはダイナマイトを爆発させるのに最適で、周囲のブロックをすべて吹き飛ばします。集めたダイナマイトは`use_item(Items.Dynamite)`で使用でき、ドローンの真下ですぐに爆発します。

ダイナマイトを安全に採掘するには、`Grounds.Dynamite`と`Grounds.Soot`の二重の地層を見つける必要があります。上のダイナマイトの地面は古くなっており、安全に掘れるブロックもあります。しかし、まだ爆発するダイナマイトも残っているため、掘ると爆発することもあります。

この例はダイナマイトと最初の掘削地点の周りを掘り、数字のあるすす層を露出させ、測定値を表示します：
{{codeexample 
{
    "camera_position": {"x": -3, "y": 0, "z": 15},
    "show_image": true,
    "image_size": {"x": 800, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 7, "y": 7},
    "execution_speed": 2,
    "digging_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 6,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz", "petrified_pumpkins"]
}
#SETUP
jump(Unlocks.Dynamite)
for _ in range(3):
    move(East)
    move(North)
#CODE
# ダイナマイト層を抜けてすすの層まで掘る
while get_ground_type() != Grounds.Soot:
    dig()

# ドローンを一周させる方向のリスト
circle_directions = [
    East, South, West, West, 
    North, North, East, East
]
for dir in circle_directions:
    move(dir)
    dig()
    print(measure()) # すすブロックの数字
}}

## ダイナマイトスイーパー
不発のブロックをすべて見つけて掘り、爆発するブロックだけを残せますか？ダイナマイトの地層が消えたとき、周囲が爆発するブロック、またはすすのブロックだけになった爆発するブロックからは、追加のダイナマイトが得られます。

幸い、下のすすのブロックが手掛かりになります。これらは、爆発するダイナマイトを含んだ隣接するダイナマイトの数を検知できます。どのブロックが爆発するかは教えてくれず、わかるのは合計数だけです。複数のすすのブロックの数値を組み合わせて、自分で突き止めましょう。

すすのブロックで`measure()`を呼ぶと、1つ上のダイナマイトの地層で、周囲8タイルにある爆発するダイナマイトの数が返ります。これは、`0`（1つもない）から`8`（隣接するタイルがすべて爆発する）までの値です。

ダイナマイトの地層で最初に掘るブロックは必ず不発です。掘ったダイナマイトのブロックからは少量のダイナマイトが得られます。不発のブロックをすべて掘り終えた場合も、誤って爆発するダイナマイトを掘った場合も、地層が壊れると、完全に露出した爆発するブロックの数の2乗に相当するダイナマイトも得られます。

## 地層の構造
ダイナマイトの地層が深いほど、爆発するダイナマイトの数が増え、見つける難易度も増えます。農場が大きいほど地雷の総数が増えるので、層を解いたときの最大収穫量も増えます。

ダイナマイトをアップグレードすると、ブロックを掘ったときや爆発するブロックを完全に露出させたときの収穫量が増えます。アップグレードで爆発のエネルギーも30%上がります。

## 成功と失敗の判定
爆発するダイナマイトを掘ると、2つの地層が爆発します。`Grounds.Dynamite`を掘った後に`get_ground_type()`を使うと、爆発したかどうかを確認できます。地面が`Grounds.Soot`でなければ、パズルは失敗です。一方、最後の不発のダイナマイトブロックを掘ると、すべてのダイナマイトブロックが消え、パズルで得られる最大の収穫量を獲得します。すすの地層は残りますが、`measure()`は`None`を返し、パズルを解くのに成功したことを示します。

`# ダイナマイトブロックを掘り、パズルの状態を確認する
def dig_dynamite():
    dig()
    if get_ground_type() != Grounds.Soot:
        # 爆発するダイナマイトを掘ったため、パズル失敗
        return False
    elif measure() == None:
        # 最後の不発のブロックを掘ったため、パズル成功
        return True
    else:
        # 測定で数値が得られたため、パズルは進行中
        return None
`

## 戦略
<spoiler=ヒント>
次のコードはダイナマイト層を掘り、測定値が`0`のすすブロックを探します。見つけるたびに、その周りのダイナマイトブロックをすべて掘ります：
{{codeexample 
{
    "camera_position": {"x": -5, "y": 0, "z": 15},
    "show_image": true,
    "image_size": {"x": 800, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 7, "y": 7},
    "execution_speed": 4,
    "digging_speed": 8,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 6,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz", "petrified_pumpkins"]
}
#SETUP
jump(Unlocks.Dynamite)
for _ in range(3):
    move(East)
    move(North)
#CODE
while get_ground_type() != Grounds.Soot:
    dig()

circle_directions = [
    East, South, West, West, North,
    North, East, East, South, West
]
# 最初に掘ったブロックの周りを回る
for dir in circle_directions:
    # すすの測定値が0なら、
    # 周囲のダイナマイトはすべて不発弾と分かる
    if get_ground_type() == Grounds.Soot and measure() == 0:
        # 周囲のブロックをもう一周する
        for dir2 in circle_directions:
            move(dir2)
            # 不発のダイナマイトを掘る
            while get_ground_type() != Grounds.Soot:
                dig()
    move(dir)
}}
</spoiler>

---

[統計](docs/stats.md)      [地下の感覚](docs/unlocks/underground_senses.md)      [辞書](docs/scripting/dicts.md)      [セット](docs/scripting/sets.md)

[move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)      [use_item()](functions/use_item)
