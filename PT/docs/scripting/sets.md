# Sets
Sets são como [dictionaries](docs/scripting/dicts.md), mas sem valores. Eles são apenas um conjunto desordenado de chaves.

Eles são criados como dictionaries, mas sem valores. 
`set = {North, East, West}`

Use `set()` para criar um set vazio. Note que `{}` cria um dictionary vazio.

Use `set.add(elem)` para adicionar um novo elemento ao set.

Use `set.remove(elem)` para remover um elemento de um set.

Use `if elem in set:` para verificar se o set contém um elemento.

Use `for elem in set:` para iterar por todos os elementos no set. Para sets maiores, o operador `in` funciona muito mais rápido do que em uma lista.

Assim como dictionaries, sets são desordenados, então não há garantias sobre a ordem em que os elementos são iterados.

Além disso, os elementos nos sets são únicos, então adicionar um elemento que já está no set não mudará o set.