[<- Primer programa](docs/first_program.md) <right>[Mejora de velocidad ->](docs/unlocks/speed.md)
---
# Bucle While
Has desbloqueado el bucle `while` y los valores `True` y `False`. El bucle `while` sigue ejecutando el cuerpo del bucle mientras la condición sea `True`.

`while condition:
	#cuerpo del bucle`

No te preocupes por crear bucles infinitos. Los retrasos en la ejecución evitarán que el programa se congele.

## Para Principiantes
Quizás ya has intentado poner varias llamadas a `harvest()` seguidas:

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
harvest()
harvest()
harvest()
}}
Esto te permite cosechar varias veces en una sola ejecución del programa.
Sin embargo, estaría bien cosechar más de tres veces, y escribir el mismo código varias veces es una mala práctica.
La solución es un bucle.
Un bucle te permite ejecutar el mismo código varias veces.

El bucle `while` toma una condición, que es un valor lógico que solo puede estar en uno de dos estados: `True` o `False`. 
Tal valor se llama valor booleano.

El bucle luego ejecuta el código dentro del bucle hasta que la condición sea `False`.
El bucle `while` se ve así:

`while condition:
	#cuerpo del bucle
	#cuerpo del bucle
	#...`

Donde tienes que reemplazar "condition" por un valor booleano y `#cuerpo del bucle` por lo que quieras hacer en el bucle.

Hay dos valores booleanos constantes disponibles. Las constantes son valores que nunca cambian durante el programa.

Para crear un valor booleano constante, basta con escribir `True` o `False`.
Así que podrías escribir

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while False:
	do_a_flip()
}}
o

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	do_a_flip()
}}
El primero nunca hará una voltereta y el segundo las hará para siempre (un bucle infinito).

Normalmente, crear un bucle infinito es mala idea porque bloqueará el programa. Sin embargo, en este juego hay pausas entre las iteraciones, así que el dron seguirá haciendo volteretas hasta que lo detengas manualmente pulsando otra vez el botón Ejecutar.

Observa cómo la línea después de los dos puntos está indentada. La indentación como esta se usa para separar bloques de código.
Pulsa Tab para añadir sangría y Mayús + Tab (o Retroceso) para quitarla. Si hay varias líneas seleccionadas, Tab y Mayús + Tab se aplicarán a todas.

Nota: si juegas a través de Steam, al pulsar Mayús + Tab se abrirá la interfaz de Steam. Puedes reasignar el atajo para quitar sangría en las opciones del juego o el atajo de la interfaz en las opciones de Steam.

Aquí, `do_a_flip()` y `pet_the_piggy()` se llaman repetidamente porque están dentro del bloque `while` con sangría. Sin embargo, `harvest()` nunca se ejecuta porque está después de ese bloque.
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	do_a_flip()
	pet_the_piggy()
harvest()
}}

---

[Bucle for](docs/scripting/for.md)      [If](docs/scripting/if.md)      [Break](docs/scripting/break.md)      [Continue](docs/scripting/continue.md)      [Editor externo](docs/external_editor.md)
