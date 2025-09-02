# Costes
Cualquier coste puede representarse como un diccionario que asigna ítems a números.

La función `get_cost()` devuelve dicho diccionario. Devuelve el coste de una planta o un desbloqueo.

`get_cost(Entities.Pumpkin)`
devuelve `{Items.Carrot:1}`

Para los desbloqueos, se puede pasar un segundo argumento opcional para el nivel de desbloqueo del que quieres obtener el coste. Por defecto, es el nivel de desbloqueo actual.

`get_cost(Unlocks.Loops, 0)`
devuelve `{Items.Hay:5}`

Para los desbloqueos que ya están en el nivel máximo, `get_cost()` devolverá `None`.

Se puede usar así:
`cost = get_cost(algo)
for item in cost:
	cantidad_de_este_item_necesaria = cost[item]`