# Listas
Las listas son una forma fácil de almacenar múltiples valores en una sola variable.
Puedes crear nuevas listas así:

`some_list = [2, True, Items.Hay]`

La lista ahora contiene los valores `2`, `True` y `Items.Hay`.
Una lista también puede estar vacía:

`empty_list = []`

Puedes acceder a un elemento de una lista por su índice. El índice es `0` para el primer elemento, `1` para el segundo, `2` para el tercero...

planta zanahorias
`entities = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(entities[1])`

Puedes iterar sobre una lista usando un bucle `for`. El siguiente ejemplo suma todos los elementos de la lista.

`numbers = [4, 7, 2, 5]
sum = 0
for number in numbers:
	sum += number`
`sum` ahora es `18`

Los siguientes métodos de lista te permiten añadir y eliminar elementos:

`elements.append(elem)` añade un elemento al final de la lista:

`numbers = [2, 6, 12]
numbers.append(7)`
`numbers` ahora es `[2, 6, 12, 7]`

`elements.remove(elem)` elimina la primera aparición de un elemento de una lista:

`numbers = [1, 2, 4, 2]
numbers.remove(2)`
`numbers` ahora es `[1, 4, 2]`

`elements.insert(index, elem)` inserta un elemento en el índice dado:

`some_list = [Entities.Tree, Items.Hay]
some_list.insert(1, Items.Wood)`
`some_list` ahora es `[Entities.Tree, Items.Wood, Items.Hay]`

`elements.pop(index)` elimina el elemento en el índice especificado.
Si no se especifica ningún índice, se elimina el último ítem.

`numbers = [3, 5, 8, 25]
numbers.pop()`
`numbers` ahora es `[3, 5, 8]`
`numbers.pop(1)`
`numbers` ahora es `[3, 8]`

La función `len()` devuelve la longitud de la lista.
`numbers = [3, 2, 1]
x = len(numbers)`
`x` ahora es `3`

Las listas tienen semántica de referencia. Esto significa que asignar una lista a una variable le asigna el mismo objeto de lista, en lugar de hacer una copia de la lista.
Si dos variables hacen referencia a la misma lista, los cambios en la lista serán visibles para ambas.

`a = [1, 2]
b = a
b.pop()`
`a` y `b` ahora son ambos `[1]`
