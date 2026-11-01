[<- Bambú](docs/unlocks/bamboo.md)
---
# Pirámides

¡El subsuelo contiene ahora antiguas estructuras piramidales de las que puedes cosechar energía!

Las pirámides están hechas de bloques de arena (`Grounds.Sand`). Debajo de la propia pirámide hay una capa de piedra caliza (`Grounds.Limestone`) que sirve como cimiento. Como son antiguas y están erosionadas, solo las encontrarás parcialmente destruidas. La capa de cimientos siempre está presente, pero habrá agujeros en la arena. Este es el aspecto de una pirámide al desenterrarla:

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
    "items": [{"item": "hay", "n": 100}, {"item": "block", "n": 100}],
    "world_size": {"x": 6, "y": 6},
    "execution_speed": 32,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 7,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "dynamite", "quartz"]
}
#SETUP
jump(Unlocks.Pyramid)
move(North)
#CODE
while get_ground_type() != Grounds.Limestone:
    dig()
do_a_flip()
z = get_pos_z()
for i in range(6):
    for j in range(6):
        while (get_ground_type() != Grounds.Limestone
                and get_ground_type() != Grounds.Sand
                and get_pos_z() > z):
            dig()
        move(North)
    move(East)
}}

Los bloques que hay encima de la pirámide siempre son de tierra. Puedes aprovechar este dato si quieres desenterrar una pirámide de forma más eficiente que con el código anterior.

Como puedes ver, hay varios agujeros en la arena que tendrás que rellenar. Cuando rellenes estos agujeros y restaures la pirámide a su estado original, esta se destruirá y recibirás energía como recompensa.

Puedes restaurar una pirámide colocando bloques con el comando `place(Grounds.Sand)`. La arena es un bloque especial que se derrumba inmediatamente si no está bien apoyado. Cada bloque de arena que coloques debe estar directamente sobre piedra caliza o sobre una cuadrícula de 3x3 bloques de arena. Aquí tienes una pequeña pirámide construida a mano como ejemplo. Por supuesto, construirla tú mismo no te dará energía:

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
    "items": [{"item": "hay", "n": 100}, {"item": "block", "n": 100}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 4,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz"]
}
#CODE
for i in range(3):
    for j in range(3):
        place(Grounds.Limestone)
        move(North)
    move(East)

for i in range(3):
    for j in range(3):
        place(Grounds.Sand)
        move(North)
    move(East)

move(North)
move(East)
place(Grounds.Sand)
}}

Una pirámide restaurada correctamente consta de un cimiento cuadrado de piedra caliza cuyos lados tienen una longitud impar, por ejemplo, 5x5. Encima hay una capa de bloques de arena del mismo tamaño (5x5), seguida de capas cada vez más pequeñas: 3x3 y luego 1x1.

Cuando se completa una pirámide, esta se desmorona y aparece un gran girasol en el centro. Puedes cosecharlo para recibir energía. Cuanto mayor sea la pirámide que completes, más energía recibirás.

---

[Estadísticas](docs/stats.md)      [Sentidos subterráneos](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [use_item()](functions/use_item)      [place()](functions/place)
