# Sentidos
¡Ahora el dron puede ver!

Las funciones `get_pos_x()` y `get_pos_y()` devuelven la posición actual x e y del dron. En la posición inicial, ambas son `0`. La posición x aumenta en `1` por cada casilla hacia `East` y la posición y aumenta en `1` por cada casilla hacia `North`.

`num_items(item)` devuelve cuántos tienes de un objeto.
Por ejemplo `num_items(Items.Hay)` te dice cuánto heno tienes.

`get_entity_type()` y `get_ground_type()` devuelven el tipo de entidad o de suelo que está debajo del dron.

Haz un giro si estás sobre un arbusto:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

¡La palabra clave `None` también está desbloqueada ahora! `None` es un valor que representa que no hay valor.
Por ejemplo, una función que no tiene una instrucción `return` en realidad devolverá `None`.

`get_entity_type()` devuelve `None` si no hay ninguna entidad debajo del dron.