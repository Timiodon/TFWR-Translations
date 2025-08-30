# Sentidos
¡El dron ahora puede ver! 

Las funciones `get_pos_x()` y `get_pos_y()` devuelven la posición x e y actual del dron. En la posición inicial, ambas son `0`. La posición x aumenta en `1` por cada casilla hacia el `East` y la posición y aumenta en `1` por cada casilla hacia el `North`.

`num_items(item)` devuelve cuántos items de un tipo tienes.
Por ejemplo, `num_items(Items.Hay)` devuelve cuánto heno tienes.

`get_entity_type()` y `get_ground_type()` devuelven el tipo de entity o suelo que hay debajo del dron.

Haz una voltereta si estás sobre un arbusto:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

¡La palabra clave `None` también está desbloqueada ahora! `None` es un valor que representa que no hay valor.
Por ejemplo, una función que no tiene una sentencia `return` en realidad devolverá `None`.

`get_entity_type()` devuelve `None` si no hay ninguna entity debajo del dron.


Si quieres saber cuántos desbloqueos de un tipo particular tienes, usa la función `num_unlocked(unlock)`.

Por ejemplo, `num_unlocked(Unlocks.Speed)` devolverá el número de mejoras de velocidad que tienes.

`num_unlocked(Unlocks.Senses)` devolverá `1` si los sentidos están desbloqueados y `0` si no lo están.

También puedes usar `num_unlocked()` en Items, Entities o Grounds. Esto devolverá `1` si está desbloqueado, y `0` si no.

Ten cuidado, `num_unlocked(Unlocks.Carrots)` devolverá el número de veces que fue desbloqueado/mejorado.
`num_unlocked(Items.Carrot)` solo devolverá `0` o `1`. (Lo mismo para otras plantas)