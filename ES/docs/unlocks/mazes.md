[<- Fertilizante](docs/unlocks/fertilizer.md) <right>[Megagranja ->](docs/unlocks/megafarm.md)
---
# Laberintos
`Items.Weird_Substance` produce un extraño efecto en los arbustos. Si el dron está sobre un arbusto y llamas a `use_item(Items.Weird_Substance, amount)`, el arbusto se convertirá en un laberinto de setos.
El tamaño del laberinto depende de la cantidad de `Items.Weird_Substance` utilizada (el segundo argumento de la llamada a `use_item()`).
Sin mejoras de laberinto, usar `n` `Items.Weird_Substance` creará un laberinto de `n`x`n`. Cada nivel de mejora duplica el tesoro, pero también duplica la cantidad de `Items.Weird_Substance` necesaria.
Así que para hacer un laberinto de campo completo:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": -1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
}}


Por alguna razón, el dron no puede volar sobre los setos, aunque no parezcan tan altos.

Hay un tesoro oculto en algún lugar del laberinto. Usa `harvest()` sobre el tesoro para recibir una cantidad de oro igual al área del laberinto. Por ejemplo, un laberinto de 5x5 producirá 25 de oro.

Si usas `harvest()` en cualquier otro lugar, el laberinto simplemente desaparecerá.

`get_entity_type()` es igual a `Entities.Treasure` si el dron está sobre el tesoro y `Entities.Hedge` en cualquier otro lugar del laberinto.

Los laberintos no contienen bucles a menos que los reutilices (consulta más abajo). Por tanto, el dron no puede volver a la misma posición sin desandar el camino.

Puedes comprobar si hay una pared intentando moverte a través de ella. 
`move()` devuelve `True` si tuvo éxito y `False` en caso contrario.

`can_move()` se puede usar para comprobar si hay una pared sin moverse.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(East)
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
#CODE
quick_print(
    can_move(North), 
    can_move(East), 
    can_move(South), 
    can_move(West)
)
if move(North) and get_entity_type() == Entities.Treasure:
    harvest()
}}

Si no tienes idea de cómo llegar al tesoro, echa un vistazo a la Pista 1. Te muestra cómo abordar un problema como este.

Usar `measure()` en cualquier lugar del laberinto devuelve la posición del tesoro.
`x, y = measure()`

Si quieres un reto adicional, puedes reutilizar el laberinto volviendo a usar sobre el tesoro la misma cantidad de `Items.Weird_Substance`.
Esto recogerá el tesoro y generará un nuevo tesoro en una posición aleatoria del laberinto.

Cada vez que se mueve el tesoro, se pueden eliminar algunas de las paredes del laberinto de forma aleatoria. Así que los laberintos reutilizados pueden contener bucles.

Ten en cuenta que los bucles en el laberinto lo hacen mucho más difícil porque significa que puedes llegar a la misma ubicación de nuevo sin retroceder.
Reutilizar un laberinto no te da más oro que simplemente cosechar y generar un nuevo laberinto.
Este es un desafío 100% extra que puedes omitir.
Solo vale la pena si la información extra y los atajos te ayudan a resolver el laberinto más rápido.

El tesoro se puede reubicar hasta 300 veces. Después, usar Sustancia Extraña sobre él ya no te dará oro ni moverá el tesoro.

<spoiler=mostrar pista 1>
Este es un enfoque general para resolver el problema:

Crea un laberinto e imagina que eres el dron.

Piensa en cómo intentarías encontrar el tesoro si estuvieras en el laberinto.

Escribe tu estrategia paso a paso para que otra persona pueda seguirla sin pensar.

Ahora intenta traducir tus pasos a código.
</spoiler>
<spoiler=mostrar pista 2>
Mientras no haya bucles, todas las paredes forman una gran pared conectada. Si apoyas la mano izquierda en la pared y la sigues, te llevará por todo el laberinto.
Este método requiere muy poco código y no necesitas recordar por dónde has pasado. Bastan unas 10 líneas de código.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": true,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": -1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
#CODE
directions = [North, East, South, West]
index = 0
while get_entity_type() != Entities.Treasure:
    index = (index - 1) % 4
    for _ in range(4):
        if move(directions[index]):
            break
        index = (index + 1) % 4
do_a_flip()
harvest()
}}
</spoiler>
<spoiler=mostrar pista 3>
En vez de mover el dron en direcciones absolutas como este u oeste, puede ser útil moverlo en direcciones relativas como «girar a la derecha» o «girar a la izquierda». Para ello, debes llevar la cuenta de la dirección en la que se está moviendo. El dron nunca gira realmente, pero puedes mantener una rotación «virtual» en el código.
El siguiente truco de índice es útil para esto:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
directions = [North, East, South, West]
index = 0
move(directions[index])

# girar a la derecha
index = (index + 1) % 4
move(directions[index])

# girar a la izquierda
index = (index - 1) % 4
move(directions[index])
}}


`% 4` se usa para permitir que la rotación «dé la vuelta al círculo», de modo que `3 (West) + 1` vuelva a ser `0 (North)`, porque `4 % 4 == 0` y `-1 % 4 == 3`.</spoiler>
<spoiler=mostrar pista 4>
Si no logras resolverlo, siempre puedes simplificar el problema usando un enfoque menos eficiente.
Resolver un laberinto de `1`x`1` es trivial.</spoiler>

---

[Estadísticas](docs/stats.md)      [Listas](docs/scripting/lists.md)      [Diccionarios](docs/scripting/dicts.md)      [Tuplas](docs/scripting/tuples.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [can_move()](functions/can_move)      [move()](functions/move)      [use_item()](functions/use_item)
