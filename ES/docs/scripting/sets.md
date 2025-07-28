# Sets
Los sets son como los [dictionaries](docs/scripting/dicts.md), pero sin valores. Son solo un conjunto desordenado de claves.

Se crean como los dictionaries, pero sin valores.
`set = {North, East, West}`

Usa `set()` para crear un set vacío. Ten en cuenta que `{}` crea un dictionary vacío.

Usa `set.add(elem)` para añadir un nuevo elemento al set.

Usa `set.remove(elem)` para eliminar un elemento de un set.

Usa `if elem in set:` para comprobar si el set contiene un elemento.

Usa `for elem in set:` para iterar sobre todos los elementos del set.
Para sets más grandes, el operador `in` funciona mucho más rápido que en una lista.

Al igual que los dictionaries, los sets son desordenados, por lo que no hay garantías sobre el orden en que se iteran los elementos.

Además, los elementos en los sets son únicos, por lo que añadir un elemento que ya está en el set no cambiará el set.