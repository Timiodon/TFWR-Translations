[<- Hierro](docs/unlocks/iron.md)
---
# Mapa del tesoro
Las leyendas hablan de un escurridizo tesoro escondido por un pirata olvidadizo que murió hace mucho... o algo así. ¿Y si trazó en un mapa el camino hacia el tesoro y luego lo perdió? Quizá dejó caer el mapa al verse acorralado por un río de lava y este quedó conservado bajo una capa de basalto.

¡Medir los bloques de basalto podría revelar algo!

<spoiler=cuéntame más>
Deberías buscar una capa de `Grounds.Basalt`. Prueba a medir el basalto y comprueba qué te dice. Puede que la pista te lleve hasta el mapa del tesoro, y medir el mapa sin duda te dará el camino hacia el propio tesoro... pero ¿serás capaz de descifrar sus instrucciones?
</spoiler>

<spoiler=dime cómo hacerlo>
Muy bien, esto es lo que hay: encuentra el estrato de `Grounds.Basalt` y el bloque de `Grounds.Treasure_Map` situado justo debajo. Puedes usar `measure()` sobre el basalto para obtener la posición `(x, y)` del bloque del mapa inferior.

Llama a `measure()` sobre el bloque del mapa para obtener el camino del tesoro como una cadena de letras que representan direcciones. N, E, S y W corresponden a `North`, `East`, `South` y `West`, respectivamente, mientras que D significa «Down» o «Dig». Estas letras describen un camino formado por bloques de `Grounds.Treasure_Path` que conduce al tesoro.

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 3,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}

#SETUP
jump(Unlocks.Treasure_Map)
#CODE
# Encuentra la capa de basalto
while get_ground_type() != Grounds.Basalt:
    dig()

# Medir el basalto devuelve la posición del mapa
map_pos = measure()

while get_pos_x() < map_pos[0]:
    move(East)
while get_pos_y() < map_pos[1]:
    move(North)

while get_ground_type() != Grounds.Treasure_Map:
    dig()

# Mapa encontrado; mídelo para obtener el camino
do_a_flip()
instructions = measure()
print("instrucciones: ", instructions)

# Excava el mapa para iniciar la búsqueda del tesoro
dig()
}}

Puedes recorrer la cadena con un bucle `for` para procesarla letra por letra:
{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 6},
    "show_image": false,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 3,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}
#SETUP
jump(Unlocks.Treasure_Map)
while get_ground_type() != Grounds.Basalt:
    dig()

map_pos = measure()

while get_pos_x() < map_pos[0]:
    move(East)
while get_pos_y() < map_pos[1]:
    move(North)

while get_ground_type() != Grounds.Treasure_Map:
    dig()
#CODE
# Las instrucciones del mapa se devuelven en una sola cadena
instructions = measure()
# Usa for-in para separar la cadena en letras
for letter in instructions:
    print(letter)
}}

Debe permanecer sobre bloques de `Grounds.Treasure_Path` en todo momento. Si se desplaza a otro terreno, el camino se romperá y el tesoro se perderá.

## Objetivo
Al final del camino hay un bloque de `Grounds.Treasure_Goal`. Si el dron no se ha desviado del camino, aparecerá un `Entities.Underground_Treasure` encima. El dron puede usar `harvest()` sobre el cofre para recoger su oro.

## Recompensa
La cantidad de oro es proporcional a la longitud del camino del tesoro. Mejorar el desbloqueo Mapa del tesoro aumenta la profundidad del camino, mientras que mejorar Expandir le proporciona más espacio para moverse lateralmente. Ambas mejoras aumentan la longitud del camino del tesoro y la cantidad de oro que encontrarás.

## Varios drones
El dron que excave el bloque del mapa del tesoro es el que debe encontrar el tesoro sin abandonar los bloques del camino.
</spoiler>

---

[Estadísticas](docs/stats.md)      [Bucle for](docs/scripting/for.md)      [Tuplas](docs/scripting/tuples.md)      [Sentidos subterráneos](docs/unlocks/underground_senses.md)

[harvest()](functions/harvest)      [move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)
