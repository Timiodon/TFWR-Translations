[<- Ekim](docs/unlocks/plant.md) <right>[Sulama ->](docs/unlocks/watering.md)
<right>[Ağaçlar ->](docs/unlocks/trees.md)
---
# Havuçlar
`plant(Entities.Carrot)` ile havuç ekebilmek için önce toprağı sürmen gerekir. Bu, zemini `Grounds.Soil` olarak değiştirir. Toprağı sürmek için `till()` çağırman yeterli. `till()` fonksiyonunu tekrar çağırırsan zemin yeniden `Grounds.Grassland` olur.

Havuç ekmek odun ve samana mal olur. Bu eşyalar `plant(Entities.Carrot)` çağrıldığında otomatik olarak düşülür.
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

Her bitkinin maliyetini [kendi sayfasında](objects/carrot) görebilirsin.

---

[İstatistikler](docs/stats.md)      [Ekim](docs/unlocks/plant.md)      [Sulama](docs/unlocks/watering.md)      [If](docs/scripting/if.md)      [Duyular](docs/unlocks/senses.md)      [Karışık Ekim](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)
