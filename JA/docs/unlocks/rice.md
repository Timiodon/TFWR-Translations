[<- 採掘](docs/unlocks/mining.md) <right>[竹 ->](docs/unlocks/bamboo.md)
<right>[石化したカボチャ ->](docs/unlocks/petrified_pumpkins.md)
<right>[パーライトと壌土 ->](docs/unlocks/special_soils.md)
---
# 稲
地表と`Grounds.Dirt`の層の下には、薄い`Grounds.Clay`の層があります。この肥沃で水をたっぷり含む地面は、稲を植えるのに最適です。

粘土まで掘って稲を植えるには、次のコードが役立ちます：
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
}}

ドローンが`Grounds.Clay`の上にいれば、`plant(Entities.Rice)`で稲を植え、`can_harvest()`で成長を確認し、最後に`harvest()`で収穫できます。

## 段々畑
稲を植えると、地面が`Grounds.Rice_Terrace`に変わり、稲の成長に最適な環境になります。稲が育ちきると地面が乾いて`Grounds.Dry_Rice_Terrace`になり、もう稲を植えられません。幸い、層は数ブロックの厚さがあるので、`dig()`でブロックを取り除き、下の`Grounds.Clay`に新しい稲を植えられます。層を使い切ったら、いつでも`clear()`で世界を復元し、新しい層まで掘れます。

---

[統計](docs/stats.md)      [採掘](docs/unlocks/mining.md)      [地下の感覚](docs/unlocks/underground_senses.md)      [If文](docs/scripting/if.md)      [forループ](docs/scripting/for.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
