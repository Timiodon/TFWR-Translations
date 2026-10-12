[<- 採掘](docs/unlocks/mining.md) <right>[竹 ->](docs/unlocks/bamboo.md)
<right>[石化したカボチャ ->](docs/unlocks/petrified_pumpkins.md)
<right>[パーライトと壌土 ->](docs/unlocks/special_soils.md)
---
# 稲

地表の下に薄い粘土の層があることに気づいたことでしょう。この肥沃な地面は、稲の苗を植えるのにぴったりです。

稲は植えた場所の粘土を乾燥させるため、各粘土ブロックは1回しか使えません。幸い、粘土の層は数ブロックの厚みがあります。もちろん、`clear()`でワールドを元に戻せば、粘土の層も復活します。

粘土が見つかるまで下へ掘るには、次のコードが役立つでしょう。

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
    "exclude_unlocks": ["watering", "fertilizer"],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 8,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#SETUP
move(East)
#CODE
while get_ground_type() != Grounds.Clay:
    dig()
plant(Entities.Rice)
move(North)
do_a_flip()
}}

---

[統計](docs/stats.md)      [採掘](docs/unlocks/mining.md)      [地下の感覚](docs/unlocks/underground_senses.md)      [If文](docs/scripting/if.md)      [forループ](docs/scripting/for.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
