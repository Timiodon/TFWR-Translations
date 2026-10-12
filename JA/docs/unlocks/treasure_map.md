[<- 鉄](docs/unlocks/iron.md)
---
# 宝物の地図

伝説によれば、ずっと昔に死んだ忘れっぽい海賊か、それに似たような誰かが幻の宝物を隠したそうです。もし、彼らが宝物までの道を地図に書いて、その地図をなくしたとしたらどうなるでしょうか？溶岩の川に追い詰められて地図を落とし、玄武岩の層の下に保存されたのかもしれません。玄武岩を測定すれば何かわかるかもしれません。

<spoiler=もう少し教えてください>
`Grounds.Basalt`の層を探してください。玄武岩を測定し、何がわかるか見てみましょう。手掛かりをたどれば宝物の地図に行き着くかもしれません。地図を測定すれば宝物までの道がわかるはずですが、その指示を読み解けるでしょうか？
</spoiler>

<spoiler=ただ答えを教えてください>
では説明します。`Grounds.Basalt`の地層と、その真下の`Grounds.Treasure_Map`ブロックを見つけます。玄武岩に `measure()`を使うと、下にある地図ブロックの`(x, y)`座標がわかります。

地図ブロックで`measure()`を呼ぶと、宝物までの道が方角を表す文字列で返ります。N、E、S、Wはそれぞれ `North`、`East`、`South`、`West`、Dは「下へ」または「掘る」を意味します。これらの文字は `Grounds.Treasure_Path`ブロックでできた、宝物へ続く道を表しています。

```
path = measure()
for letter in path:
    do_something(letter)
```

宝物の地図ブロックを掘ったドローンは、宝物を探す必要があります。その間ドローンは、ずっと`Grounds.Treasure_Path`ブロックの上にいなければなりません。別の地面へ移動すると道が途切れ、宝物は失われます。

道の終点には`Grounds.Treasure_Goal`ブロックがあります。ドローンが道を外れていなければ、その上に`Entities.Underground_Treasure`が現れます。ドローンが宝箱を`harvest()`すると、ゴールドを回収できます。

得られるゴールドの量は、宝物の道の長さに比例します。宝物の地図のアンロックをアップグレードすると道が深くなり、拡張をアップグレードすると横方向に進める範囲が広がります。どちらもアップグレードすることで、道が長くなり見つかるゴールドの量が増えます。
</spoiler>

---

[統計](docs/stats.md)      [forループ](docs/scripting/for.md)      [タプル](docs/scripting/tuples.md)      [地下の感覚](docs/unlocks/underground_senses.md)

[harvest()](functions/harvest)      [move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)
