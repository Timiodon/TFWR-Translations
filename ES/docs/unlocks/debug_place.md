[<- Bambú](docs/unlocks/bamboo.md)
---
# Bloques de colores
Como quizá ya sepas, puedes usar `place()` para hacer que tu dron coloque un bloque. Este desbloqueo añade tres bloques de colores que se distinguen visualmente de su entorno: `Grounds.Block_Red`, `Grounds.Block_Green` y `Grounds.Block_Blue`.

Los bloques de colores sirven para marcar cosas o crear dibujos bonitos.

Para colocar los nuevos bloques:
{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 10},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "block", "n": 100}],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 5,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"],
    "starting_chunk": 2
}
#SETUP
move(East)
move(North)
#CODE
place(Grounds.Block_Green)
move(East)

place(Grounds.Block_Blue)
move(East)

place(Grounds.Block_Green)
move(North)

place(Grounds.Block_Blue)
move(North)

place(Grounds.Block_Green)
move(West)

place(Grounds.Block_Blue)
move(West)

place(Grounds.Block_Green)
move(South)

place(Grounds.Block_Blue)
move(East)

place(Grounds.Block_Red)
place(Grounds.Block_Red)

do_a_flip()
}}

---

[Depuración](docs/scripting/debug.md)      [Depuración 2](docs/unlocks/debug2.md)      [Bambú](docs/unlocks/bamboo.md)

[place()](functions/place)
