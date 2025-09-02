# Diccionarios
Los diccionarios son una estructura de datos que te permite mapear claves a valores de la misma manera que un diccionario real mapea palabras a sus definiciones y puedes buscarlas muy rápidamente.

Un diccionario se puede crear así:
`right_of = {North:East, East:South, South:West, West:North}`

La expresión antes de los dos puntos es la clave y la expresión después de los dos puntos es el valor al que se mapea la clave.
El diccionario anterior mapea cada dirección a la dirección a su derecha.

Aquí hay otro que mapea la posición del dron a la entidad sobre la que se encuentra.
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

Acceder al valor mapeado a una clave es similar a acceder a un elemento en una lista:
`value = dict[key]`

Ejemplo:
`orientation = right_of[South]`
Esto establece `orientation` en `West`.

Puedes añadir un nuevo par clave-valor a un diccionario así:
`dict[key] = value`

Ejemplo:
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
Esto actualiza la entidad almacenada para la posición actual.

Las claves son únicas, por lo que añadir una clave que ya existe en el diccionario sobrescribirá el valor anterior.

Usa `dict.pop(key)` para eliminar un par clave-valor de `dict`.

`key in dict` evalúa a `True` si `key` es una clave en el `dict` y `False` en caso contrario.
Así que puedes usar `if key in dict:` para comprobar si `dict` contiene la clave.

Poner un diccionario en un bucle for te permite iterar a través de todas las claves:
`for key in dict:
	value = dict[key]`

No hay garantías sobre el orden en que se iteran las claves.

Ver también [Conjuntos](docs/scripting/sets.md)