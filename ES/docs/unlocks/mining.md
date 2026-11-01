[<- Expansión 1](docs/unlocks/expand_1.md) <right>[Sentidos subterráneos ->](docs/unlocks/underground_senses.md)
<right>[Arroz ->](docs/unlocks/rice.md)
<right>[Carbón ->](docs/unlocks/coal.md)
---
# Minería

Tu dron ha conseguido un taladro primitivo que le permite buscar tesoros bajo tierra.

Puedes usar el comando `dig()` para excavar el bloque que tienes debajo.

Por ahora, vamos a recoger algunos bloques:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "special_soils"]
}
#SETUP
move(North)
move(East)
#CODE
dig()
do_a_flip()
dig()
do_a_flip()
dig()
do_a_flip()
clear()
}}

Si quieres volver a la superficie, puedes usar `clear()` en cualquier momento. Esto también restaura tu granja.

Al pasar el cursor sobre un bloque se mostrarán su nombre, estabilidad y dureza.

# Taladro

Al excavar a mayor profundidad, notarás que los bloques se vuelven más duros, por lo que tardas más en excavarlos. ¡Menos mal que podemos mejorar el taladro para ayudarnos!

Puedes usar `get_hardness()` para comprobar la dureza del bloque que tienes debajo. Si encuentras una zona de bloques especialmente duros, puede ser buena idea rodearlos para avanzar más deprisa:

`while True:
    if get_hardness() < 5:
        dig()
    else:
        move(East)`

Por supuesto, los bloques se vuelven cada vez más duros a medida que bajas, así que, aunque esta estrategia ayuda, solo te servirá hasta cierto punto.

## Derrumbes

Excavar hacia abajo hará que los bloques de alrededor se derrumben. Los cuatro bloques adyacentes al dron siempre se destruyen. Después, el derrumbe se propaga en función de la estabilidad del terreno. Un bloque con estabilidad 1, como la pradera, puede soportar una diferencia de altura de 1. En otras palabras, si la pradera tiene un vecino vertical u horizontal cuya coordenada z está 2 o más bloques por debajo, la pradera se destruirá.

La estabilidad de un bloque aparece en su descripción al pasar el cursor sobre él.

Cuando un bloque se derrumba, también elimina todos los bloques que tiene encima. Solo recibes recursos de los bloques que el dron excava directamente, así que los bloques perdidos en un derrumbe se destruyen sin producir recursos.

---

[Sentidos subterráneos](docs/unlocks/underground_senses.md)      [Bucle while](docs/scripting/while.md)

[move()](functions/move)      [dig()](functions/dig)
