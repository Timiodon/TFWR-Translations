[<- Cuarzo](docs/unlocks/quartz.md) <right>[Dinamita ->](docs/unlocks/dynamite.md)
---
# Hongo
Muchos tipos de hongos crecen en colonias bajo tierra. Busca un estrato de `Grounds.Mushroom` mientras excavas. Después puedes usar `measure()` sobre el terreno para obtener el tipo de hongo como un número entre `0` y `5`.

El siguiente código encuentra hongos e imprime su tipo:
{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 6,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}
#SETUP
jump(Unlocks.Mushrooms)
#CODE
# Procesa una fila de hongos
for i in range(get_world_size()):
    # Excava hasta el bloque de hongos superior
    while get_ground_type() != Grounds.Mushroom:
        dig()

    # Imprime el número del tipo de hongo
    print(measure())

    move(East)
}}

## Cómo recoger hongos
A los hongos del mismo tipo les gusta estar juntos, pero les da demasiada vergüenza crecer unos encima de otros. Empuja el bloque de hongo debajo del dron con `push(direction)`.

Apila dos bloques de hongos del mismo tipo y se cosecharán automáticamente para obtener sus hongos.

El código siguiente hace espacio y empuja un hongo hasta que coincida con el que tiene debajo:
{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 6,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 3,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron", "special_soils"]
}
#SETUP
jump(Unlocks.Mushrooms)
#CODE
while get_ground_type() != Grounds.Mushroom:
    dig()

depth = get_pos_z()
for i in range(2):
    # Haz espacio para empujar el hongo hacia el este
    move(East)
    while get_pos_z() > depth - 1:
        dig()
    # Vuelve, empuja y sigue el bloque empujado
    move(West)
    push(East) # ¡Empuja el hongo!
    move(East)
}}

# Empujar bloques
Puedes usar `can_push(direction)` para comprobar si se puede empujar el bloque que hay debajo del dron y si hay algo que lo bloquee en la dirección indicada.

`push(direction)` empuja el bloque y devuelve si el empujón tuvo éxito.

Solo se pueden empujar bloques de hongos. Los bloques no se pueden empujar hacia arriba, y el empujón fallará si hay otro bloque en medio. Al empujarlos al aire, los bloques caen y aterrizan sobre el siguiente bloque que haya debajo.

# Estrategia
<spoiler=pista>
Recuerda que puedes llamar a `place(Grounds.Dirt)` para colocar bloques debajo del dron. Esto puede resultar útil para rellenar agujeros y poder empujar bloques por encima de ellos.
</spoiler>

---

[Estadísticas](docs/stats.md)      [Sentidos subterráneos](docs/unlocks/underground_senses.md)      [Diccionarios](docs/scripting/dicts.md)

[move()](functions/move)      [measure()](functions/measure)      [can_push()](functions/can_push)      [push()](functions/push)      [place()](functions/place)      [get_ground_type()](functions/get_ground_type)
