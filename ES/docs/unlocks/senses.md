# Sentidos
¡El dron puede ver ahora! 

Las funciones `get_pos_x()` y `get_pos_y()` devuelven la posición x e y actual del dron. En la posición inicial ambas son `0`. La posición x aumenta en `1` por cada casilla hacia el `East` y la posición y aumenta en `1` por cada casilla hacia el `North`.

`num_items(item)` devuelve cuántos de un ítem tienes.
Por ejemplo, `num_items(Items.Hay)` devuelve cuánto heno tienes.

`get_entity_type()` y `get_ground_type()` devuelven el tipo de entidad o terreno que hay debajo del dron.

Haz un giro si estás sobre un arbusto:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

¡La palabra clave `None` también está desbloqueada ahora! `None` es un valor que representa que no hay valor.
Por ejemplo, una función que no tiene una instrucción `return` en realidad devolverá `None`.

`get_entity_type()` devuelve `None` si no hay ninguna entidad debajo del dron.


Si quieres saber cuántos de un desbloqueo en particular tienes, usa la función `num_unlocked(unlock)`.

Por ejemplo, `num_unlocked(Unlocks.Speed)` devolverá el número de mejoras de velocidad que tienes.

`num_unlocked(Unlocks.Senses)` devolverá `1` si los sentidos están desbloqueados y `0` si no lo están.

También puedes usar `num_unlocked()` en Ítems, Entidades o Terrenos. Esto devolverá `1` si está desbloqueado, de lo contrario `0`.

Ten cuidado, `num_unlocked(Unlocks.Carrots)` devolverá el número de veces que se ha desbloqueado/mejorado.
`num_unlocked(Items.Carrot)` solo devolverá `0` o `1`. (Lo mismo para otras plantas)