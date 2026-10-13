[<- 澆水](docs/unlocks/watering.md)
---
# 向日葵
[向日葵](objects/sunflower)會收集太陽的能量，而你可以收穫那種能量。

種植向日葵的方式與種植胡蘿蔔或南瓜完全相同，只不過收穫的不再是某種果實，而是能量。

收穫一株成熟的向日葵會產出能量。
如果農場上至少有 10 株向日葵，並且你收穫了花瓣數量最多的那一株，就能獲得 `8` 倍的能量！
如果你收穫一株向日葵時，農場上還有另一株花瓣更多的向日葵，那麼你接下來收穫的向日葵也只能獲得普通數量的能量（沒有 8 倍加成）。

`measure()` 回傳無人機下方那株向日葵的花瓣數量。
向日葵最少有 `7` 片花瓣，最多有 `15` 片。
向日葵在完全成熟前就能測量花瓣數量，也會計入至少 10 株向日葵的要求。

幾株向日葵可能擁有相同數量的花瓣，因此也可能不止一株向日葵的花瓣數量是最多的。在這種情況下，無論收穫哪一株都一樣。

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "inventory_scale": 5,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "carrot", "n": 10}],
    "world_size": {"x": 5, "y": 2},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 4,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(North)
for _ in range(5):
    till()
    plant(Entities.Sunflower)
    move(East)
move(North)
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
#CODE
for _ in range(5):
    till()
    plant(Entities.Sunflower)
    print(measure())
    move(East)
for _ in range(5):
    while not can_harvest():
        pass
    harvest()
    move(East)
}}

只要有能量，無人機就會以兩倍的速度執行。
無人機每 30 次行動（如移動、收穫、種植……）消耗 1 點能量。
執行其他程式碼陳述式也會消耗能量，但比無人機行動少得多。

總的來說，所有可以透過提升速度來加速的東西都可以使用能量進行加速。
在不考慮速度倍率的情況下，任何使用能量加速的東西消耗的能量都與執行時間成正比。

---

[統計資料](docs/stats.md)      [串列](docs/scripting/lists.md)      [字典](docs/scripting/dicts.md)      [變數](docs/scripting/variables.md)      [For 迴圈](docs/scripting/for.md)      [If 陳述式](docs/scripting/if.md)      [運算子](docs/scripting/operators.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [measure()](functions/measure)
