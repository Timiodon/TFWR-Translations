[<- Carbón](docs/unlocks/coal.md)
---
# Saltar
Tu dron ha desbloqueado el comando `jump()`. Para usarlo, debes pasarle un desbloqueo como argumento, por ejemplo, `Unlocks.Iron`.

Este comando permite apuntar a ciertos recursos ocultos en el terreno y saltar al instante hasta ellos. Es especialmente útil para depurar o para llegar a una veta que acabas de pasar por alto.

Después del salto, el recurso buscado debería estar a un máximo de 3 bloques de la superficie superior. `jump()` solo se puede usar una vez por ejecución del programa; los intentos posteriores producirán un error.

El ejemplo siguiente salta hasta el [arroz](docs/unlocks/rice.md), encuentra la capa de arcilla y planta una fila de terrazas de arroz:
{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms"],
    "starting_chunk": 0
}
#CODE
# Salta cerca del arroz
jump(Unlocks.Rice)

# Planta una fila de terrazas de arroz
for i in range(get_world_size()):
    # El salto no es exacto; excava los últimos bloques
    while get_ground_type() != Grounds.Clay:
        dig()

    plant(Entities.Rice)

    move(East)
}}

## Desbloqueos compatibles
`jump()` solo funciona con estos desbloqueos de minería:
- Carbón
- Hierro
- Cuarzo
- Arroz
- Calabazas petrificadas
- Suelos especiales
- Pirámide
- Mapa del tesoro
- Hongos
- Dinamita

---

[jump()](functions/jump)
