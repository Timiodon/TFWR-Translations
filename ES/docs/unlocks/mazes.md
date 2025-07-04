# Laberintos
`Items.Weird_Substance`, que se obtiene al [fertilizar](docs/unlocks/fertilizer.md) plantas, tiene un efecto extraño en los arbustos. Si el dron está sobre un arbusto y llamas a `use_item(Items.Weird_Substance, amount)`, el arbusto se transformará en un laberinto de setos.  
El tamaño del laberinto depende de la cantidad de `Items.Weird_Substance` usada (el segundo argumento de la llamada a `use_item()`).  
Sin mejoras de laberinto, usar `n` `Items.Weird_Substance` resultará en un laberinto de `n`x`n`. Cada nivel de mejora del laberinto duplica el tesoro, pero también duplica la cantidad de `Items.Weird_Substance` necesaria.  
Así que para hacer un laberinto de campo completo:

`plant(Entities.Bush)
n_substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, n_substance)`

Por alguna razón, el dron no puede volar sobre los setos, aunque no parecen tan altos.

Hay un tesoro escondido en algún lugar del seto. Usa `harvest()` en el tesoro para recibir oro igual al área del laberinto. (Por ejemplo, un laberinto de 5x5 dará 25 de oro.)

Si usas `harvest()` en cualquier otro lugar, el laberinto simplemente desaparecerá.

`get_entity_type()` es igual a `Entities.Treasure` si el dron está sobre el tesoro y `Entities.Hedge` en cualquier otro lugar del laberinto.

Los laberintos no contienen ningún bucle a menos que reutilices el laberinto (mira abajo cómo reutilizar un laberinto). Así que no hay manera de que el dron termine en la misma posición de nuevo sin retroceder.

Puedes verificar si hay una pared intentando moverte a través de ella.  
`move()` devuelve `True` si tuvo éxito y `False` de lo contrario.

Si no tienes idea de cómo llegar al tesoro, échale un vistazo a la Pista 1. Te muestra cómo abordar un problema como este.

Para un desafío extra, también puedes reutilizar el laberinto usando la misma cantidad de `Items.Weird_Substance` en el tesoro nuevamente.  
Esto aumentará la cantidad de oro en el tesoro por un laberinto completo y lo moverá a una posición aleatoria en el laberinto.

Usar `measure()` en un tesoro devuelve la posición a la que se moverá, como una tupla.  
`next_x, next_y = measure()`

Cada vez que el tesoro se mueve, una pared aleatoria puede ser eliminada del laberinto. Así que los laberintos reutilizados pueden contener bucles.

Ten en cuenta que los bucles en el laberinto lo hacen mucho más difícil porque significa que puedes llegar al mismo lugar de nuevo sin retroceder.  
Reutilizar un laberinto no te da más oro que simplemente cosechar y generar un nuevo laberinto.  
Este es 100% un desafío extra que puedes simplemente omitir.  
Solo vale la pena si la información extra y los atajos te ayudan a resolver el laberinto más rápido.

El mismo laberinto puede resolverse un máximo de 300 veces. Esto corresponde a 299 reubicaciones. Después de eso, usar sustancias extrañas en el tesoro ya no aumentará el oro en él y `measure()` devolverá `None`.

<spoiler=mostrar pista 1>Aquí hay un enfoque general para resolver el problema:

Crea un laberinto e imagina que eres el dron.

Piensa en cómo intentarías encontrar el tesoro si estuvieras en el laberinto.

Escribe tu estrategia paso a paso para que alguien más pueda seguirla sin pensar.

Ahora intenta traducir tus pasos a código.
</spoiler>
<spoiler=mostrar pista 2>Mientras no haya bucles: Todas las paredes son realmente una sola pared grande conectada. Si sigues la pared, te llevará por todo el laberinto.  
Este enfoque requiere muy poco código y no necesitas llevar un seguimiento de dónde ya has estado. Alrededor de 10 líneas de código son todo lo que necesitas.</spoiler>
<spoiler=mostrar pista 3>En lugar de mover el dron en direcciones absolutas como este u oeste, puede ser muy útil mover el dron en direcciones relativas como "gira a la derecha" o "gira a la izquierda". Para hacer esto, necesitas llevar un seguimiento de hacia dónde se está moviendo actualmente el dron. El dron nunca rota realmente, pero aún puedes mantener una rotación "virtual" en el código.  
El siguiente truco de índice es útil para esto:

`directions = [North, East, South, West]
index = 0`

Usa `% 4` para permitir que rote "alrededor del círculo", de modo que después de `West` vuelva a `North`.  
`# gira a la derecha
index = (index + 1) % 4`

`# gira a la izquierda
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=mostrar pista 4>Si no puedes resolverlo, siempre puedes hacer tu vida más fácil y hacerlo de manera menos eficiente.  
Resolver un laberinto de `1`x`1` es trivial.</spoiler>