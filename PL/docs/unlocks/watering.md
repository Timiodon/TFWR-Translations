[<- Marchewki](docs/unlocks/carrots.md) <right>[Nawóz ->](docs/unlocks/fertilizer.md)
<right>[Słoneczniki ->](docs/unlocks/sunflowers.md)
---
# Podlewanie
Rośliny rosną szybciej, gdy są podlewane. Podłoże ma poziom wody od `0` do `1`.
Funkcja `get_water()` zwraca poziom wody podłoża pod dronem.

Prędkość wzrostu rośliny rośnie liniowo od 1x przy poziomie wody 0 do 5x przy poziomie 1.

Podłoże z czasem wysycha. Średnio traci 1% bieżącego poziomu wody na sekundę, z pewnymi losowymi odchyleniami. Utrzymywanie wysokiego poziomu wody zużywa jej znacznie więcej niż utrzymywanie niskiego.

Możesz używać wody na swoich roślinach. Jeden zbiornik wody jest automatycznie dodawany do twojego ekwipunku co 10 sekund.
Ulepszenie `Unlocks.Watering` podwoi ilość wody, którą otrzymujesz co 10 sekund.

Jeden zbiornik mieści `0.25` wody.

Wywołaj `use_item(Items.Water)` nad dowolnym podłożem, aby je podlać.
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

[Nawóz](docs/unlocks/fertilizer.md)

[use_item()](functions/use_item)      [get_water()](functions/get_water)
