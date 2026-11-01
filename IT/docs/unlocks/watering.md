[<- Carote](docs/unlocks/carrots.md) <right>[Fertilizzante ->](docs/unlocks/fertilizer.md)
<right>[Girasoli ->](docs/unlocks/sunflowers.md)
---
# Annaffiare
Le piante crescono più velocemente quando vengono annaffiate. Il terreno ha un livello d'acqua che va da `0` a `1`.
La funzione `get_water()` restituisce il livello d'acqua del terreno sotto il drone.

La velocità di crescita di una pianta aumenta linearmente da 1x con livello d'acqua 0 a 5x con livello d'acqua 1.

Il terreno si asciuga nel tempo. In media perde ogni secondo l'1% dell'acqua presente, con una certa variazione casuale. Mantenere un livello d'acqua alto consuma molta più acqua rispetto a mantenerne uno basso.

Puoi usare l'acqua sulle tue piante. Un serbatoio d'acqua viene aggiunto automaticamente al tuo inventario ogni 10 secondi.
Potenziare `Unlocks.Watering` ti darà un serbatoio d'acqua aggiuntivo ogni 10 secondi.

Un serbatoio contiene `0.25` di acqua.

Chiama `use_item(Items.Water)` su qualsiasi terreno per annaffiarlo.
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

[Fertilizzante](docs/unlocks/fertilizer.md)

[use_item()](functions/use_item)      [get_water()](functions/get_water)
