# Dictionaries
Los dictionaries son una estructura de datos que te permite mapear claves a valores de la misma manera que un diccionario real mapea palabras a sus definiciones y puedes buscarlas muy rápidamente.

Un dictionary se puede crear así:
`right_of = {North:East, East:South, South:West, West:North}`

La expresión antes de los dos puntos es la clave y la expresión después de los dos puntos es el valor al que se mapea la clave.
El dictionary anterior mapea cada dirección a la dirección a su derecha.

Aquí hay otro que mapea la posición del dron a la entity sobre la que se encuentra.
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

Acceder al valor mapeado a una clave es similar a acceder a un elemento en una lista:
`value = dict[key]`

Ejemplo:
`orientation = right_of[South]`
Esto establece `orientation` en `West`.

Puedes agregar un nuevo par clave-valor a un dictionary así:
`dict[key] = value`

Ejemplo:
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
Esto actualiza la entity almacenada para la posición actual.

Las claves son únicas, por lo que agregar una clave que ya existe en el dictionary sobrescribirá el valor anterior.

Usa `dict.pop(key)` para eliminar un par clave-valor de `dict`.

`key in dict` evalúa a `True` si `key` es una clave en el `dict` y `False` en caso contrario.
Así que puedes usar `if key in dict:` para verificar si `dict` contiene la clave.

Poner un dictionary en un bucle for te permite iterar a través de todas las claves:
`for key in dict:
	value = dict[key]`

No hay garantías sobre el orden en que se iteran las claves.

Ver también [Sets](docs/scripting/sets.md)