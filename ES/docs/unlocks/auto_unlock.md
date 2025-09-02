# Autodesbloqueos
Para automatizar completamente el juego, puedes usar la función `unlock()` para desbloquear características automáticamente.
Por ejemplo, puedes usar `unlock(Unlocks.Speed)` y `unlock(Unlocks.Expand)` para desbloquear las características de velocidad y expansión.

Para determinar el coste de un desbloqueo, simplemente usa la función `get_cost()` como lo harías para una planta o un ítem.
Ejemplo:
`get_cost(Unlocks.Loops)`
devuelve `{Items.Hay:5}`