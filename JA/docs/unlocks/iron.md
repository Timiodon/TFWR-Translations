[<- 石炭](docs/unlocks/coal.md) <right>[石英 ->](docs/unlocks/quartz.md)
<right>[鉄の探査 ->](docs/unlocks/prospecting.md)
<right>[宝物の地図 ->](docs/unlocks/treasure_map.md)
---
# 鉄

粘土の下にある石の層で、鉄の鉱脈を発見しました。

鉄の鉱脈は初めは小さく、見つけるには運も必要です。このアンロックのレベルを上げると、鉱石の鉱脈の最大サイズが大きくなります。もっと確実に鉄を見つけたいなら、鉄の探査のアンロックも試してみましょう。

鉄の鉱脈は必ずつながっており、斜めに飛び飛びにはなりません。鉄を1つ見つけたら、その下や隣を探して、鉱脈全体を採掘しましょう。

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
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 1,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz"]
}
#SETUP
jump(Unlocks.Iron)
#CODE
for i in range(4):
    dig()
do_a_flip()
}}

---

[統計](docs/stats.md)      [採掘](docs/unlocks/mining.md)      [鉄の探査](docs/unlocks/prospecting.md)      [地下の感覚](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)
