[<- 南瓜](docs/unlocks/pumpkins.md)
---
# 混合種植
你可能已經注意到，有時植物種在一起時的產量會更高。
草、灌木、樹和胡蘿蔔在有合適的「伴生植物」時產量更高。每個植物的伴生偏好都不同，這是隨機的，無法預測。還好，無人機下方地塊上的植物的伴生屬性可以透過呼叫 `get_companion()` 函式來取得。結果會回傳一個元組，其中第一個元素是植物想要的伴生植物類型，第二個元素則是它想要伴生植物種下的位置（座標）。伴生植物無需完全成熟，就能提供產量加成。

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
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Bush)
plant_type, (x, y) = get_companion()
print(plant_type, (x, y))
move(East)
move(South)
plant(plant_type)
move(West)
move(North)
do_a_flip()
harvest()
}}

具有伴生屬性的植物種類只有 `Entities.Grass`、`Entities.Bush`、`Entities.Tree` 和 `Entities.Carrot` 這四種。每個植物都會隨機選擇與自身種類不同的植物作為伴生物件；伴生物件的位置可以在距植物三步以內的任何地塊，但不會是植物自身的位置。

如果無人機下方沒有具有伴生偏好的植物，呼叫 `get_companion()` 函式將回傳 `None`。

首次解鎖混合種植之前，產量乘數為 `5`。此後每次升級都會翻倍。

---

[統計資料](docs/stats.md)      [元組](docs/scripting/tuples.md)      [字典](docs/scripting/dicts.md)      [感官](docs/unlocks/senses.md)      [種植](docs/unlocks/plant.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [get_companion()](functions/get_companion)
