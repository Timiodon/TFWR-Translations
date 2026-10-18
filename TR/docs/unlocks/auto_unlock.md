[<- Maliyetler](docs/unlocks/costs.md)
---
# Otomatik Kilit Açma
Oyunu tamamen otomatikleştirmek için `unlock()` fonksiyonunu kullanarak özelliklerin kilidini otomatik olarak açabilirsin.
Örneğin, hız ve genişletme özelliklerinin kilidini açmak için `unlock(Unlocks.Speed)` ve `unlock(Unlocks.Expand)` kullanabilirsin.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 300}, {"item": "wood", "n": 100000}],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
for _ in range(6):
    harvest()
    unlock(Unlocks.Grass)
}}

Bir kilit açmanın maliyetini öğrenmek için, bir bitki ya da eşya için yaptığın gibi `get_cost()` fonksiyonunu kullanman yeterli.
{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "loops"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(get_cost(Unlocks.Loops))
}}

---

[Maliyetler](docs/unlocks/costs.md)      [Dictionary'ler](docs/scripting/dicts.md)      [If](docs/scripting/if.md)      [Sıralama Tablosu](docs/unlocks/leaderboard.md)

[get_cost()](functions/get_cost)      [unlock()](functions/unlock)
