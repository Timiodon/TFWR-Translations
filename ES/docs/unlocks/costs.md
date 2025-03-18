# Costos
Cualquier costo puede representarse como un dictionary que asigna elementos a números.

La función `get_cost()` devuelve dicho dictionary. Devuelve el costo de una planta o un desbloqueo.

`get_cost(Entities.Pumpkin)`
devuelve `{Items.Carrot:1}`

Para desbloqueos, se puede pasar un segundo argumento opcional para el nivel de desbloqueo que deseas obtener el costo. Por default, es el nivel de desbloqueo actual.

`get_cost(Unlocks.Loops, 0)`
devuelve `{Items.Hay:5}`

Para desbloqueos que ya están en el nivel máximo, `get_cost()` devolverá `None`.

Se puede usar de esta manera:
`cost = get_cost(something)
for item in cost:
	amount_of_this_item_needed = cost[item]`