[<- ニンジン](docs/unlocks/carrots.md) <right>[肥料 ->](docs/unlocks/fertilizer.md)
<right>[ヒマワリ ->](docs/unlocks/sunflowers.md)
---
# 水やり
植物は水をやると成長が早くなります。地面には `0` から `1` までの水位があります。
`get_water()` 関数は、ドローンの下にある地面の水位を返します。

植物の成長速度は、水位0の1倍速から水位1の5倍速まで直線的に変化します。

地面は時間とともに乾きます：平均して、毎秒現在の水分の1%を失いますが、これにはランダムなばらつきがあります。高い水位を維持することは、低い水位を維持するよりもはるかに多くの水を消費します。

植物に水を使うことができます。10秒ごとに水タンクが1つ、自動的にインベントリに追加されます。
`Unlocks.Watering` をアップグレードすると、10秒ごとに手に入る水の量が倍になります。

タンク1つには `0.25` の水が入ります。

地面の上で `use_item(Items.Water)` を呼び出すと、地面に水をやることができます。
{{codeexample 
{
    "camera_position": {"x": -4, "y": 1, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "water", "n": 10}],
    "world_size": {"x": 9, "y": 1},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
for _ in range(9):
    till()
    move(East)
#CODE
for i in range(5):
    if i > 0:
        use_item(Items.Water, i)
    plant(Entities.Tree)
    print(get_water())
    move(East)
    move(East)
}}

---

[肥料](docs/unlocks/fertilizer.md)

[use_item()](functions/use_item)      [get_water()](functions/get_water)