# Sentidos
¡El dron ahora puede ver!

Las funciones `get_pos_x()` y `get_pos_y()` devuelven la posición x e y actual del dron. En la posición inicial, ambas son `0`. La posición x aumenta en `1` por cada casilla hacia el `East` y la posición y aumenta en `1` por cada casilla hacia el `North`.

`num_items(item)` devuelve cuántos de un item tienes.
Por ejemplo, `num_items(Items.Hay)` devuelve cuánto heno tienes.

`get_entity_type()` y `get_ground_type()` devuelven el tipo de entity o suelo que está debajo del dron.

Haz una voltereta si estás sobre un arbusto:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

¡La palabra clave `None` también está desbloqueada ahora! `None` es un valor que representa que no hay valor.
Por ejemplo, una función que no tiene una sentencia `return` en realidad devolverá `None`.

`get_entity_type()` devuelve `None` si no hay ninguna entity debajo del dron.
