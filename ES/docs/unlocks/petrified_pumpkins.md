[<- Arroz](docs/unlocks/rice.md)
---
# Calabazas petrificadas
Al parecer, puedes encontrar calabazas bajo tierra. Se han endurecido y petrificado, pero aún sirven para lo que necesitamos. Puedes usar `dig()` para obtener calabazas.

Esto ofrece otra forma de obtener calabazas sin cultivarlas en la superficie. Si prefieres cultivarlas, puedes ignorar por completo las calabazas petrificadas.

{{codeexample 
{
    "camera_position": {"x": -2, "y": 1, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [],
    "exclude_unlocks": ["mushrooms", "watering", "fertilizer", "pyramid", "dynamite", "quartz"],
    "world_size": {"x": 6, "y": 6},
    "execution_speed": 8,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 3
}
#SETUP
jump(Unlocks.Petrified_Pumpkins)
move(East)
move(North)
move(North)
move(North)
#CODE
while get_ground_type() != Grounds.Petrified_Pumpkin:
    dig()
z = get_pos_z()
for i in range(get_world_size()):
    for j in range(get_world_size()):
        while get_pos_z() > z - 2 and get_ground_type() != Grounds.Petrified_Pumpkin:
            dig()
        move(North)
    move(East)
for _ in range(3):
    dig()
    move(East)
    dig()
    move(South)
    dig()
    move(West)
    dig()
    move(West)
    dig()
    move(North)
    dig()
    move(North)
    dig()
    move(East)
    dig()
    move(East)
    dig()
    move(South)
    move(West)
}}

Las calabazas petrificadas aparecen bajo tierra en bloques de 3x3x3 o 5x5x5. No hay una forma infalible de encontrarlas, así que tendrás que confiar en que tu dron se tope con una al excavar. Aparecen en la tierra dura que hay debajo de la capa de roca y hierro, más o menos a la misma altura que el cuarzo (si lo has desbloqueado).

---

[Estadísticas](docs/stats.md)      [Minería](docs/unlocks/mining.md)      [Sentidos subterráneos](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
