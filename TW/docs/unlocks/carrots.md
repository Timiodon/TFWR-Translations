[<- 種植](docs/unlocks/plant.md) <right>[澆水 ->](docs/unlocks/watering.md)
<right>[樹 ->](docs/unlocks/trees.md)
---
# 胡蘿蔔
呼叫 `plant(Entities.Carrot)` 函式可以種植胡蘿蔔。在種植胡蘿蔔之前你必須先耕地，只需呼叫 `till()` 函式即可耕地，將地塊變為 `Grounds.Soil` 。再次呼叫 `till()` 則會將地塊變回 `Grounds.Grassland`。


種植胡蘿蔔所需的耗材是乾草和木材。請注意：呼叫 `plant(Entities.Carrot)` 函式種植胡蘿蔔時，這些耗材（乾草和木材）會被消耗一定數量。

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 1}, {"item": "wood", "n": 1}],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
till()
plant(Entities.Carrot)
for _ in range(8):
    do_a_flip()
harvest()
till()
}}

你可以在所有植物的[專屬頁面](objects/carrot)上檢視所需的耗材數量。

---

[統計資料](docs/stats.md)      [種植](docs/unlocks/plant.md)      [澆水](docs/unlocks/watering.md)      [If 陳述式](docs/scripting/if.md)      [感官](docs/unlocks/senses.md)      [混合種植](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)
