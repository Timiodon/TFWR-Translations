[<- 鉄](docs/unlocks/iron.md)
---
# 宝物の地図
伝説によれば、ずっと昔に死んだ忘れっぽい海賊か、それに似たような誰かが幻の宝物を隠したそうです。もし、彼らが宝物までの道を地図に書いて、その地図をなくしたとしたらどうなるでしょうか？溶岩の川に追い詰められて地図を落とし、玄武岩の層の下に保存されたのかもしれません。

玄武岩のブロックを測定すると、何かが分かるかもしれません！

<spoiler=もう少し教えてください>
`Grounds.Basalt`の層を探してください。玄武岩を測定し、何がわかるか見てみましょう。手掛かりをたどれば宝物の地図に行き着くかもしれません。地図を測定すれば宝物までの道がわかるはずですが、その指示を読み解けるでしょうか？
</spoiler>

<spoiler=ただ答えを教えてください>
では説明します。`Grounds.Basalt`の地層と、その真下の`Grounds.Treasure_Map`ブロックを見つけます。玄武岩に `measure()`を使うと、下にある地図ブロックの`(x, y)`座標がわかります。

地図ブロックで`measure()`を呼ぶと、宝物までの道が方角を表す文字列で返ります。N、E、S、Wはそれぞれ `North`、`East`、`South`、`West`、Dは「下へ」または「掘る」を意味します。これらの文字は `Grounds.Treasure_Path`ブロックでできた、宝物へ続く道を表しています。

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 3,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}

#SETUP
jump(Unlocks.Treasure_Map)
#CODE
# 玄武岩の層を探す
while get_ground_type() != Grounds.Basalt:
    dig()

# 玄武岩の測定で地図の座標が分かる
map_pos = measure()

while get_pos_x() < map_pos[0]:
    move(East)
while get_pos_y() < map_pos[1]:
    move(North)

while get_ground_type() != Grounds.Treasure_Map:
    dig()

# 地図を見つけたら測定して道を調べる
do_a_flip()
instructions = measure()
print("指示： ", instructions)

# 地図を掘って宝探しを始める
dig()
}}

文字列に`for`ループを使い、1文字ずつ処理できます：
{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 6},
    "show_image": false,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 3,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}
#SETUP
jump(Unlocks.Treasure_Map)
while get_ground_type() != Grounds.Basalt:
    dig()

map_pos = measure()

while get_pos_x() < map_pos[0]:
    move(East)
while get_pos_y() < map_pos[1]:
    move(North)

while get_ground_type() != Grounds.Treasure_Map:
    dig()
#CODE
# 地図の指示は1つの文字列で返される
instructions = measure()
# for-inで文字列を1文字ずつ処理する
for letter in instructions:
    print(letter)
}}

ドローンは、ずっと`Grounds.Treasure_Path`ブロックの上にいなければなりません。別の地面へ移動すると道が途切れ、宝物は失われます。

## ゴール
道の終点には`Grounds.Treasure_Goal`ブロックがあります。ドローンが道を外れていなければ、その上に`Entities.Underground_Treasure`が現れます。ドローンが宝箱を`harvest()`すると、ゴールドを回収できます。

## 報酬
得られるゴールドの量は、宝物の道の長さに比例します。宝物の地図のアンロックをアップグレードすると道が深くなり、拡張をアップグレードすると横方向に進める範囲が広がります。どちらもアップグレードすることで、道が長くなり見つかるゴールドの量が増えます。

## 複数のドローン
宝物の地図ブロックを掘ったドローンは、道のブロックから離れずに宝物を探す必要があります。
</spoiler>

---

[統計](docs/stats.md)      [forループ](docs/scripting/for.md)      [タプル](docs/scripting/tuples.md)      [地下の感覚](docs/unlocks/underground_senses.md)

[harvest()](functions/harvest)      [move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)
