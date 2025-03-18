# Desbloqueos Automáticos
Para automatizar completamente el juego, puedes usar la función `unlock()` para desbloquear características automáticamente.
Por ejemplo, puedes usar `unlock(Unlocks.Speed)` y `unlock(Unlocks.Expand)` para desbloquear las características de velocidad y expansión.

Para determinar el costo de un desbloqueo, simplemente usa la función `get_cost()` como lo harías para una planta o un objeto.
Ejemplo:
`get_cost(Unlocks.Loops)`
devuelve `{Items.Hay:5}`

Si quieres averiguar cuántos desbloqueos específicos tienes, utiliza la función `num_unlocked(unlock)`.

Por ejemplo, `num_unlocked(Unlocks.Speed)` te devolverá el número de mejoras de velocidad que tienes.

`num_unlocked(Unlocks.Senses)` devolverá `1` si los sentidos están desbloqueados y `0` si no lo están.

También puedes usar `num_unlocked()` en Items, Entities o Grounds. Esto devolverá `1` si está desbloqueado, de lo contrario `0`.

Ten cuidado, `num_unlocked(Unlocks.Carrots)` devolverá el número de veces que se desbloqueó/mejoró.
`num_unlocked(Items.Carrot)` solo devolverá `0` o `1`. (Lo mismo para otras plantas)