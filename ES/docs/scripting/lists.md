# Listas
Las listas son una forma fácil de almacenar múltiples valores en una sola variable.
Puedes crear nuevas listas así:

`list = [2, True, Items.Hay]`

La lista ahora contiene los valores `2`, `True` y `Items.Hay`.
Una lista también puede estar vacía:

`empty_list = []`

Puedes acceder a un elemento de una lista por su índice. El índice es `0` para el primer elemento, `1` para el segundo elemento, `2` para el tercero...

plantas zanahorias
`list = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(list[1])`

Puedes iterar sobre una lista usando un bucle for. El siguiente ejemplo suma todos los elementos en la lista.

`list = [4, 7, 2, 5]
sum = 0
for number in list:
	sum += number`
`sum` es ahora `18`

Los siguientes métodos de lista te permiten añadir y eliminar elementos:

`list.append(elem)` añade un elemento al final de la lista:

`list = [2, 6, 12]
list.append(7)`
`list` es ahora `[2, 6, 12, 7]`

`list.remove(elem)` elimina la primera ocurrencia de un elemento de una lista:

`list = [1, 2, 4, 2]
list.remove(2)`
`list` es ahora `[1, 4, 2]`

`list.insert(index, elem)` inserta un elemento en el índice dado:

`list = [Entities.Tree, Items.Hay]
list.insert(1, Items.Wood)`
`list` es ahora `[Entities.Tree, Items.Wood, Items.Hay]`

`list.pop(index)` elimina el elemento en el índice especificado.
Si no se especifica un índice, se elimina el último elemento.

`list = [3, 5, 8, 25]
list.pop()`
`list` es ahora `[3, 5, 8]`
`list.pop(1)`
`list` es ahora `[3, 8]`

La función `len()` devuelve la longitud de la lista.
`list = [3, 2, 1]
x = len(list)`
`x` es ahora `3`

Las listas tienen semánticas de referencia. Esto significa que asignar una lista a una variable asigna el mismo objeto de lista a esa variable, en lugar de hacer una copia de la lista.
Si dos variables hacen referencia a la misma lista, los cambios en la lista serán visibles para ambas.

`a = [1,2]
b = a
b.pop()`
`a` y `b` son ahora ambas `[1]`