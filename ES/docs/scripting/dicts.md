# Diccionarios
Los diccionarios son una estructura de datos que te permite mapear claves a valores de la misma manera que un diccionario real mapea palabras a sus definiciones, y puedes buscarlos muy rápidamente.

Un diccionario puede ser creado así:
`rotation = {North:East, East:South, South:West, West:North}`

La expresión antes del dos puntos es la clave y la expresión después del dos puntos es el valor al cual la clave se asigna.
El diccionario anterior asigna cada dirección a la dirección a su derecha.

Aquí hay otro que asigna la posición del dron a la entidad sobre la que está.
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

Acceder al valor asignado a una clave es similar a acceder a un elemento en una lista:
`value = dict[key]`

Ejemplo:
`orientation = rotation[South]`
Esto establece `orientation` a `West`.

Puedes agregar un nuevo par clave-valor a un diccionario así:
`dict[key] = value`

Ejemplo:
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
Esto actualiza la entidad almacenada para la posición actual.

Las claves son únicas, por lo que agregar una clave que ya existe en el diccionario sobrescribirá el valor anterior.

Usa `dict.pop(key)` para remover un par clave-valor de `dict`.

`key in dict` evalúa a `True` si `key` es una clave en el `dict` y `False` de lo contrario.
Así que puedes usar `if key in dict:` para verificar si `dict` contiene la clave.

Poner un diccionario en un bucle for te permite iterar a través de todas las claves:
`for key in dict:
	value = dict[key]`

No hay garantías sobre el orden en el que se iteran las claves.

Ver también [Sets](docs/scripting/sets.md)