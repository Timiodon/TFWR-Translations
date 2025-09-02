# Conjuntos
Conjuntos são como [dicionários](docs/scripting/dicts.md), mas sem valores. Eles são apenas um conjunto não ordenado de chaves. 

Eles são criados como dicionários, mas sem valores.
`set = {North, East, West}`

Use `set()` para criar um conjunto vazio. Note que `{}` cria um dicionário vazio.

Use `set.add(elem)` para adicionar um novo elemento ao conjunto.

Use `set.remove(elem)` para remover um elemento de um conjunto.

Use `if elem in set:` para verificar se o conjunto contém um elemento.

Use `for elem in set:` para iterar todos os elementos no conjunto.
Para conjuntos maiores, o operador `in` funciona muito mais rápido do que em uma lista.

Assim como os dicionários, os conjuntos não são ordenados, então не há garantias sobre a ordem em que os elementos são iterados.

Além disso, os elementos nos conjuntos são únicos, então adicionar um elemento que já está no conjunto não alterará o conjunto.