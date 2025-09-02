# Conjuntos
Los conjuntos son como los [diccionarios](docs/scripting/dicts.md), pero sin valores. Son solo un conjunto desordenado de claves. 

Se crean como los diccionarios, pero sin valores.
`set = {North, East, West}`

Usa `set()` para crear un conjunto vacío. Ten en cuenta que `{}` crea un diccionario vacío.

Usa `set.add(elem)` para añadir un nuevo elemento al conjunto.

Usa `set.remove(elem)` para eliminar un elemento de un conjunto.

Usa `if elem in set:` para comprobar si el conjunto contiene un elemento.

Usa `for elem in set:` para iterar sobre todos los elementos del conjunto.
Para conjuntos más grandes, el operador `in` funciona mucho más rápido que en una lista.

Al igual que los diccionarios, los conjuntos son desordenados, por lo que no hay garantías sobre el orden en que se iteran los elementos.

Además, los elementos en los conjuntos son únicos, por lo que añadir un elemento que ya está en el conjunto no cambiará el conjunto.