[<-採礦](docs/unlocks/mining.md) <right>[竹子->](docs/unlocks/bamboo.md)
<right>[石化南瓜->](docs/unlocks/petrified_pumpkins.md)
<right>[珍珠岩與壤土->](docs/unlocks/special_soils.md)
---
# 水稻

你注意到地表下方有一層薄薄的黏土。這種肥沃的地塊非常適合種植水稻幼苗。

種植水稻後，黏土會變乾。每塊黏土只能使用一次。好在這層黏土有好幾個地塊厚。當然，你也隨時可以使用 `clear()` 重設世界，讓黏土層重新出現。

下面的程式碼可以幫助你向下挖掘，直到找到黏土。

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

[統計資料](docs/stats.md)      [採礦](docs/unlocks/mining.md)      [地下感官](docs/unlocks/underground_senses.md)      [If 陳述式](docs/scripting/if.md)      [For 迴圈](docs/scripting/for.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
