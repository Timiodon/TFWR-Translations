# Árboles
[Trees](objects/tree) son una mejor manera de conseguir madera que los arbustos. Dan 5 maderas cada uno. Al igual que los arbustos, se pueden plantar en césped o tierra.

A los árboles les gusta tener algo de espacio y plantarlos justo al lado uno del otro ralentizará su crecimiento. El tiempo de crecimiento se duplica por cada árbol que esté en una casilla directamente al norte, este, oeste o sur de él. Así que si plantas árboles en cada casilla, tardarán `2*2*2*2 = 16` veces más en crecer.

<spoiler=show> El operador `%` puede ser útil aquí. Recuerda que el operador `%` devuelve el resto de la división. Los números pares divididos por `2` tienen un resto de `0` y los números impares divididos por `2` tienen un resto de `1`.
Así que puedes verificar si un número es par de esta manera:

`def is_even(n):
	return n % 2 == 0`

Esto devuelve `True` si n es par y `False` si no lo es.
</spoiler>