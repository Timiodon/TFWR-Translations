[<- 肥料](docs/unlocks/fertilizer.md) <right>[メガファーム ->](docs/unlocks/megafarm.md)
---
# 迷路
`Items.Weird_Substance` は茂みに奇妙な効果をもたらします。ドローンが茂みの上にいるときに `use_item(Items.Weird_Substance, amount)` を呼び出すと、茂みは生垣の迷路に成長します。
迷路のサイズは、使用される`Items.Weird_Substance`の量（`use_item()`呼び出しの2番目の引数）によって異なります。
迷路のアップグレードがない場合、`n`個の`Items.Weird_Substance`を使用すると、`n`x`n`の迷路ができます。各迷路アップグレードレベルは宝物を2倍にしますが、必要な`Items.Weird_Substance`の量も2倍になります。
したがって、フィールドいっぱいの迷路を作るには:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": -1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
}}


どういうわけか、ドローンはそれほど高くないように見える生垣の上を飛ぶことができません。

迷路のどこかに宝物が隠されています。宝物に対して `harvest()` を使用すると、迷路の面積に等しいゴールドを受け取ります。（例えば、5x5の迷路は25ゴールドをもたらします。）

他の場所で `harvest()` を使用すると、迷路は単に消えてしまいます。

ドローンが宝物の上にある場合、`get_entity_type()` は `Entities.Treasure` と等しく、迷路の他の場所では `Entities.Hedge` と等しくなります。

迷路には、再利用しない限りループはありません（迷路の再利用については下記を参照）。そのため、ドローンが後戻りせずに同じ場所に戻ることはありません。

壁があるかどうかは、それを通り抜けようとすることで確認できます。
`move()` は成功した場合は `True` を、それ以外の場合は `False` を返します。

`can_move()` を使用すると、移動せずに壁があるかどうかを確認できます。

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(East)
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
#CODE
quick_print(
    can_move(North), 
    can_move(East), 
    can_move(South), 
    can_move(West)
)
if move(North) and get_entity_type() == Entities.Treasure:
    harvest()
}}

宝物への行き方がわからない場合は、ヒント1を見てください。このような問題へのアプローチ方法が示されています。

迷路のどこかで `measure()` を使用すると、宝物の位置が返されます。
`x, y = measure()`

さらなる挑戦として、同じ量の`Items.Weird_Substance`を再び宝物に使用することで、迷路を再利用することもできます。
これにより、宝物が回収され、迷路内のランダムな位置に新しい宝物がスポーンします。

宝物が移動するたびに、迷路の壁の一部がランダムに削除されることがあります。そのため、再利用された迷路にはループが含まれることがあります。

迷路にループがあると、戻ることなく同じ場所に再び到達できるため、はるかに難しくなることに注意してください。
迷路を再利用しても、新しい迷路を収穫してスポーンするよりも多くのゴールドが得られるわけではありません。
これは100％追加の挑戦であり、スキップしても構いません。
追加情報とショートカットが迷路をより速く解くのに役立つ場合にのみ価値があります。

宝物は最大300回まで再配置できます。その後、宝物に奇妙な物質を使用しても、ゴールドは得られなくなり、宝物も移動しなくなります。

<spoiler=ヒント1を表示>
問題解決への一般的なアプローチは次のとおりです:

迷路を作成し、自分がドローンであると想像してください。

もし自分が迷路にいたら、どのようにして宝物を見つけようとするか考えてみてください。

あなたの戦略を、他の誰かが考えずに従えるように、ステップバイステップで書き留めてください。

次に、あなたのステップをコードに翻訳してみてください。
</spoiler>
<spoiler=ヒント2を表示>
ループがない限り、すべての壁は1つの大きなつながった壁です。左手を壁に当ててたどれば、迷路全体を通り抜けられます。
このアプローチは非常に少ないコードで済み、すでにどこにいたかを追跡する必要はありません。約10行のコードで十分です。
{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": true,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": -1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
#CODE
directions = [North, East, South, West]
index = 0
while get_entity_type() != Entities.Treasure:
    index = (index - 1) % 4
    for _ in range(4):
        if move(directions[index]):
            break
        index = (index + 1) % 4
do_a_flip()
harvest()
}}
</spoiler>
<spoiler=ヒント3を表示>
ドローンを東や西のような絶対的な方向に動かす代わりに、「右に曲がる」や「左に曲がる」のような相対的な方向に動かすと非常に便利です。これを行うには、ドローンが現在どちらの方向に動いているかを追跡する必要があります。ドローンは実際には回転しませんが、コード内で「仮想的」な回転を維持することができます。
次のインデックストリックが役立ちます:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
directions = [North, East, South, West]
index = 0
move(directions[index])

#右に曲がる
index = (index + 1) % 4
move(directions[index])

#左に曲がる
index = (index - 1) % 4
move(directions[index])
}}


`% 4` を使うと方角を一周させられます。`4 % 4 == 0` かつ `-1 % 4 == 3` なので、`3 (West) + 1` は再び `0 (North)` になります。</spoiler>
<spoiler=ヒント4を表示>
解けない場合は、効率の低い方法を使って問題を単純にすることもできます。
`1`x`1`の迷路を解くのは簡単です。</spoiler>

---

[統計](docs/stats.md)      [リスト](docs/scripting/lists.md)      [辞書](docs/scripting/dicts.md)      [タプル](docs/scripting/tuples.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [can_move()](functions/can_move)      [move()](functions/move)      [use_item()](functions/use_item)