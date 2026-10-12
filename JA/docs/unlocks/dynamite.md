[<- キノコ](docs/unlocks/mushroom.md)
---
# ダイナマイト

かつての採掘隊が残した画期的な爆薬です。幸いなことに（あるいは不幸なことに）、あなたのドリルはダイナマイトを爆発させるのにぴったりで、周囲のブロックを吹き飛ばすことができます。

ダイナマイトを安全に採掘するには、`Grounds.Dynamite`と`Grounds.Soot`の二重の地層を見つける必要があります。上のダイナマイトの地面は古くなっており、安全に掘れるブロックもあります。しかし、まだ爆発するダイナマイトも残っているため、掘ると爆発することもあります。

{{codeexample 
{
    "camera_position": {"x": -3, "y": -3, "z": 12},
    "show_image": true,
    "image_size": {"x": 900, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "hay", "n": 100}],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 8,
    "digging_speed": 8,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 4,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz", "petrified_pumpkins"]
}
#SETUP
jump(Unlocks.Dynamite)
#CODE
while get_ground_type() != Grounds.Soot:
    dig()
dig()
dig()
}}

不発のブロックをすべて見つけて掘り、爆発するブロックだけを残せますか？ダイナマイトの地層が消えたとき、周囲が爆発するブロック、またはすすのブロックだけになった爆発するブロックからは、追加のダイナマイトが得られます。

幸い、下のすすのブロックが手掛かりになります。これらは、爆発するダイナマイトを含んだ隣接するダイナマイトの数を検知できます。どのブロックが爆発するかは教えてくれず、わかるのは合計数だけです。複数のすすのブロックの数値を組み合わせて、自分で突き止めましょう。

すすのブロックで`measure()`を呼ぶと、1つ上のダイナマイトの地層で、周囲8タイルにある爆発するダイナマイトの数が返ります。これは、`0`（1つもない）から`8`（隣接するタイルがすべて爆発する）までの値です。

ダイナマイトの地層で最初に掘るブロックは必ず不発です。掘ったダイナマイトのブロックからは少量のダイナマイトが得られます。不発のブロックをすべて掘り終えた場合も、誤って爆発するダイナマイトを掘った場合も、地層が壊れると、完全に露出した爆発するブロックの数の2乗に相当するダイナマイトも得られます。

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

ダイナマイトの地層が深いほど、爆発するダイナマイトの数が増え、見つける難易度も増えます。

集めたダイナマイトは`use_item(Items.Dynamite)`で使用でき、ドローンの真下ですぐに爆発します。

ダイナマイトをアップグレードすると、ブロックを掘ったときや爆発するブロックを完全に露出させたときの収穫量が増えます。アップグレードで爆発のエネルギーも30%上がります。

---

[統計](docs/stats.md)      [地下の感覚](docs/unlocks/underground_senses.md)      [辞書](docs/scripting/dicts.md)      [セット](docs/scripting/sets.md)

[move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)      [use_item()](functions/use_item)
