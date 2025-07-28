# Sets
Os sets são como [dictionaries](docs/scripting/dicts.md), mas sem valores. São apenas um conjunto não ordenado de chaves.

São criados como os dictionaries, mas sem valores.
`set = {North, East, West}`

Usa `set()` para criar um set vazio. Nota que `{}` cria um dictionary vazio.

Usa `set.add(elem)` para adicionar um novo elemento ao set.

Usa `set.remove(elem)` para remover um elemento de um set.

Usa `if elem in set:` para verificar se o set contém um elemento.

Usa `for elem in set:` para iterar todos os elementos no set.
Para sets maiores, o operador `in` tem um desempenho muito mais rápido do que teria numa lista.

Tal como os dictionaries, os sets não são ordenados, por isso não há garantias sobre a ordem em que os elementos são iterados.

Além disso, os elementos nos sets são únicos, por isso adicionar um elemento que já está no set não alterará o set.