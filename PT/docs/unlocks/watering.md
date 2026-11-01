[<- Cenouras](docs/unlocks/carrots.md) <right>[Fertilizante ->](docs/unlocks/fertilizer.md)

<right>[Girassóis ->](docs/unlocks/sunflowers.md)

---

# Irrigação

As plantas crescem mais rápido quando são regadas. O solo tem um nível de água que varia de `0` a `1`.
A função `get_water()` retorna o nível de água do solo sob o drone.

A velocidade de crescimento de uma planta aumenta linearmente de 1x no nível de água 0 até 5x no nível de água 1.

O solo seca com o tempo. Em média, perde 1% da água atual por segundo, com alguma variação aleatória. Manter um nível alto consome muito mais água do que manter um nível baixo.

Você pode usar água em suas plantas. Um tanque de água é adicionado automaticamente ao seu inventário a cada 10 segundos.
Melhorar `Unlocks.Watering` dobrará a quantidade de água que você recebe a cada 10 segundos.

Um tanque comporta `0.25` de água.

Chame `use_item(Items.Water)` sobre qualquer solo para regar o solo.

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
