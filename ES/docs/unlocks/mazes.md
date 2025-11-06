# Laberintos
`Items.Weird_Substance`, que se obtiene [fertilizando](docs/unlocks/fertilizer.md) plantas, tiene un efecto extraño en los arbustos. Si el dron está sobre un arbusto y llamas a `use_item(Items.Weird_Substance, amount)`, el arbusto se convertirá en un laberinto de setos.
El tamaño del laberinto depende de la cantidad de `Items.Weird_Substance` utilizada (el segundo argumento de la llamada a `use_item()`).
Sin mejoras de laberinto, usar `n` `Items.Weird_Substance` resultará en un laberinto de `n`x`n`. Cada nivel de mejora del laberinto duplica el tesoro, pero también duplica la cantidad de `Items.Weird_Substance` necesaria. 
Así que para hacer un laberinto de campo completo:

`plant(Entities.Bush)
substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)`


Por alguna razón, el dron no puede volar sobre los setos, aunque no parezcan tan altos.

Hay un tesoro escondido en algún lugar del seto. Usa `harvest()` en el tesoro para recibir oro igual al área del laberinto. (Por ejemplo, un laberinto de 5x5 producirá 25 de oro).

Si usas `harvest()` en cualquier otro lugar, el laberinto simplemente desaparecerá.

`get_entity_type()` es igual a `Entities.Treasure` si el dron está sobre el tesoro y `Entities.Hedge` en cualquier otro lugar del laberinto.

Los laberintos no contienen bucles a menos que reutilices el laberinto (ver más abajo cómo reutilizar un laberinto). Así que no hay forma de que el dron termine en la misma posición de nuevo sin retroceder.

Puedes comprobar si hay una pared intentando moverte a través de ella. 
`move()` devuelve `True` si tuvo éxito y `False` en caso contrario.

`can_move()` se puede usar para comprobar si hay una pared sin moverse.

Si no tienes idea de cómo llegar al tesoro, echa un vistazo a la Pista 1. Te muestra cómo abordar un problema como este.

Usar `measure()` en cualquier lugar del laberinto devuelve la posición del tesoro.
`x, y = measure()`

Para un desafío extra, también puedes reutilizar el laberinto usando la misma cantidad de `Items.Weird_Substance` en el tesoro de nuevo. 
Esto recogerá el tesoro y generará un nuevo tesoro en una posición aleatoria del laberinto.
Solo los laberintos de tamaño 8x8 o más grandes pueden ser reutilizados.

Cada vez que se mueve el tesoro, se pueden eliminar algunas de las paredes del laberinto de forma aleatoria. Así que los laberintos reutilizados pueden contener bucles.

Ten en cuenta que los bucles en el laberinto lo hacen mucho más difícil porque significa que puedes llegar a la misma ubicación de nuevo sin retroceder.
Reutilizar un laberinto no te da más oro que simplemente cosechar y generar un nuevo laberinto.
Este es un desafío 100% extra que puedes omitir.
Solo vale la pena si la información extra y los atajos te ayudan a resolver el laberinto más rápido.

El tesoro se puede reubicar hasta 300 veces. Después de eso, usar sustancia rara en el tesoro ya no aumentará el oro en él y ya no se moverá más.

<spoiler=show hint 1>Aquí tienes un enfoque general para resolver el problema:

Crea un laberinto e imagina que eres el dron.

Piensa en cómo intentarías encontrar el tesoro si estuvieras en el laberinto.

Escribe tu estrategia paso a paso para que otra persona pueda seguirla sin pensar.

Ahora intenta traducir tus pasos a código.
</spoiler>
<spoiler=show hint 2>Mientras no haya bucles: todas las paredes son en realidad una gran pared conectada. Si sigues la pared, te llevará por todo el laberinto.
Este enfoque requiere muy poco código y no necesitas llevar un registro de dónde has estado. Unas 10 líneas de código es todo lo que necesitas.</spoiler>
<spoiler=show hint 3>En lugar de mover el dron en direcciones absolutas como este u oeste, puede ser muy útil moverlo en direcciones relativas como "girar a la derecha" o "girar a la izquierda". Para hacer esto, necesitas llevar un registro de la dirección en la que se está moviendo el dron. El dron nunca rota realmente, pero aún puedes mantener una rotación "virtual" en el código.
El siguiente truco de índice es útil para esto:

`directions = [North, East, South, West]
index = 0`

Usa `% 4` para permitirle rotar "alrededor del círculo", de modo que después de `West` vuelva a `North`.
`# girar a la derecha
index = (index + 1) % 4`

`# girar a la izquierda
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=show hint 4>Si no puedes resolverlo, siempre puedes facilitarte la vida y hacerlo de manera menos eficiente. 
Resolver un laberinto de `1`x`1` es trivial.</spoiler>