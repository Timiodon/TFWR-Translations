[<- Zanahorias](docs/unlocks/carrots.md) <right>[Fertilizante ->](docs/unlocks/fertilizer.md)
<right>[Girasoles ->](docs/unlocks/sunflowers.md)
---
# Riego
Las plantas crecen más rápido cuando se riegan. El suelo tiene un nivel de agua que va de `0` a `1`.
La función `get_water()` devuelve el nivel de agua del suelo sobre el que se encuentra.

La velocidad de crecimiento de una planta escala linealmente desde una velocidad de 1x con un nivel de agua de 0 hasta una velocidad de 5x con un nivel de agua de 1.

El suelo se seca con el tiempo: de media, pierde el 1% de su agua actual por segundo, pero hay cierta variación aleatoria en esto.
Mantener un nivel de agua alto consumirá mucha más agua que mantener un nivel de agua bajo.

Puedes usar agua en tus plantas. Se añade automáticamente un tanque de agua a tu inventario cada 10 segundos.
Mejorar `Unlocks.Watering` duplicará la cantidad de agua que obtienes cada 10 segundos.

Un tanque contiene `0.25` de agua.

Llama a `use_item(Items.Water)` sobre cualquier suelo para regar el terreno.
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

[Fertilizante](docs/unlocks/fertilizer.md)

[use_item()](functions/use_item)      [get_water()](functions/get_water)
