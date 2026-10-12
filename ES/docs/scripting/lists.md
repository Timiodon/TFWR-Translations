[<- Variables](docs/scripting/variables.md) <right>[Diccionarios ->](docs/scripting/dicts.md)
---
# Listas
Las listas son una forma fácil de almacenar múltiples valores en una sola variable.
Puedes crear nuevas listas así:

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
some_list = [2, True, Items.Hay]
print(some_list)
}}

La lista ahora contiene los valores `2`, `True` y `Items.Hay`.
Una lista también puede estar vacía:

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
empty_list = []
print(empty_list)
}}

Puedes acceder a un elemento de una lista mediante su índice. El índice es `0` para el primer elemento, `1` para el segundo, `2` para el tercero, y así sucesivamente.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 1}, {"item": "wood", "n": 1}],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
till()
#CODE
entities = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(entities[1])
}}

Puedes iterar por una lista usando un bucle `for`. El siguiente ejemplo suma todos los elementos de la lista.

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
numbers = [4, 7, 2, 5]
sum = 0
for number in numbers:
	sum += number
print(sum)
}}

Los siguientes métodos de lista te permiten añadir y eliminar elementos:

`elements.append(elem)` añade un elemento al final de la lista:

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
numbers = [2, 6, 12]
numbers.append(7)
print(numbers)
}}

`elements.remove(elem)` elimina la primera aparición de un elemento de una lista:

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
numbers = [1, 2, 4, 2]
numbers.remove(2)
print(numbers)
}}

`elements.insert(index, elem)` inserta un elemento en el índice dado:

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
some_list = [Entities.Tree, Items.Hay]
some_list.insert(1, Items.Wood)
print(some_list)
}}

`elements.pop(index)` elimina el elemento en el índice especificado.
Si no se especifica ningún índice, se elimina el último ítem.

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
numbers = [3, 5, 8, 25]
numbers.pop()
print(numbers)
numbers.pop(1)
print(numbers)
}}

La función `len()` devuelve la longitud de la lista.
{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
numbers = [3, 5, 8, 25]
print(len(numbers))
}}

Las listas tienen semántica de referencia. Esto significa que asignar una lista a una variable le asigna el mismo objeto de lista, en lugar de hacer una copia de la lista.
Si dos variables hacen referencia a la misma lista, los cambios en la lista serán visibles para ambas.

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
a = [1, 2]
b = a
b.pop()
print(a)
print(b)
}}

---

[Variables](docs/scripting/variables.md)      [Bucle for](docs/scripting/for.md)      [Tuplas](docs/scripting/tuples.md)      [Diccionarios](docs/scripting/dicts.md)      [Conjuntos](docs/scripting/sets.md)

[len()](functions/len)
