# Laberintos
`Items.Weird_Substance`, que se obtiene al [fertilizar](docs/unlocks/fertilizer.md) plantas, tiene un efecto extraño en los arbustos. Si el dron está sobre un arbusto y llamas a `use_item(Items.Weird_Substance, amount)`, el arbusto se transformará en un laberinto de setos.  
El tamaño del laberinto depende de la cantidad de `Items.Weird_Substance` usada (el segundo argumento de la llamada a `use_item()`).  
Sin mejoras de laberinto, usar `n` `Items.Weird_Substance` resultará en un laberinto de `n`x`n`. Por cada nivel de mejora del laberinto, necesitas usar un `n` `Items.Weird_Substance` extra para obtener el mismo efecto.  
Así que para hacer un laberinto en un campo completo:

`plant(Entities.Bush)
n_substance = get_world_size() * num_unlocked(Unlocks.Mazes)
use_item(Items.Weird_Substance, n_substance)`

Por alguna razón, el dron no puede volar sobre los setos, aunque no parecen tan altos.

Hay un tesoro escondido en algún lugar del seto. Usa `harvest()` en el tesoro para recibir oro igual al área del laberinto. (Por ejemplo, un laberinto de 5x5 dará 25 de oro.)

Si usas `harvest()` en cualquier otro lugar, el laberinto simplemente desaparecerá.

`get_entity_type()` es igual a `Entities.Treasure` si el dron está sobre el tesoro y `Entities.Hedge` en cualquier otro lugar del laberinto.

Los laberintos no contienen bucles a menos que reutilices el laberinto (ver abajo cómo reutilizar un laberinto). Así que no hay forma de que el dron termine en la misma posición nuevamente sin retroceder.

Puedes comprobar si hay una pared intentando moverte a través de ella.  
`move()` devuelve `True` si tuvo éxito y `False` en caso contrario.

Si no tienes idea de cómo llegar al tesoro, echa un vistazo a la Pista 1. Te muestra cómo abordar un problema como este.

Para un reto adicional, también puedes reutilizar el laberinto usando la misma cantidad de `Items.Weird_Substance` en el tesoro nuevamente.  
Esto aumentará la cantidad de oro en el tesoro por un laberinto completo y lo moverá a una posición aleatoria en el laberinto.

Usar `measure()` en un tesoro devuelve la posición a la que se moverá, como una tupla.  
`next_x, next_y = measure()`

Cada vez que el tesoro se mueve, una pared aleatoria puede ser eliminada del laberinto. Así que los laberintos reutilizados pueden contener bucles.

Ten en cuenta que los bucles en el laberinto lo hacen mucho más difícil porque significa que puedes llegar a la misma ubicación nuevamente sin retroceder.  
Reutilizar un laberinto no te da más oro que solo cosechar y generar un nuevo laberinto.  
Esto es un 100% un reto adicional que puedes simplemente omitir.  
Solo vale la pena si la información adicional y los atajos te ayudan a resolver el laberinto más rápido.

El mismo laberinto puede resolverse un máximo de 300 veces. Esto corresponde a 299 reubicaciones. Después de eso, usar sustancia extraña en el tesoro no aumentará el oro en él y `measure()` devolverá `None`.

<spoiler=ver pista 1>Aquí tienes un enfoque general para resolver el problema:

Crea un laberinto e imagina que eres el dron.

Piensa cómo intentarías encontrar el tesoro si estuvieras en el laberinto.

Escribe tu estrategia paso a paso para que alguien más pueda seguirla sin pensar.

Ahora intenta traducir tus pasos en código.
</spoiler>
<spoiler=ver pista 2>Mientras no haya bucles: Todas las paredes son solo una gran pared conectada. Si sigues la pared, te guiará a través de todo el laberinto.  
Este enfoque requiere muy poco código y no necesitas llevar un control de dónde has estado antes. Alrededor de 10 líneas de código es todo lo que necesitas.</spoiler>
<spoiler=ver pista 3>En lugar de mover el dron en direcciones absolutas como este o oeste, puede ser muy útil mover el dron en direcciones relativas como "girar a la derecha" o "girar a la izquierda". Para hacer esto, necesitas llevar un control de hacia dónde se está moviendo el dron actualmente. El dron nunca rota realmente, pero aún puedes mantener una rotación "virtual" en el código.  
El siguiente truco de índice es útil para esto:

`directions = [North, East, South, West]
index = 0`

Usa `% 4` para permitir que gire "alrededor del círculo", de modo que después de `West` vuelva a `North`.  
`# girar a la derecha
index = (index + 1) % 4`

`# girar a la izquierda
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=ver pista 4>Si no puedes resolverlo, siempre puedes hacer la vida más fácil y hacerlo de manera menos eficiente.  
Resolver un laberinto de `1`x`1` es trivial.</spoiler>