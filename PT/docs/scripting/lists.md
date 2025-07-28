# Listas
As listas são uma forma fácil de armazenar múltiplos valores numa única variável.
Podes criar novas listas assim:

`list = [2, True, Items.Hay]`

A lista agora contém os valores `2`, `True` e `Items.Hay`.
Uma lista também pode estar vazia:

`empty_list = []`

Podes aceder a um elemento de uma lista pelo seu índice. O índice é `0` para o primeiro elemento, `1` para o segundo, `2` para o terceiro...

planta cenouras
`list = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(list[1])`

Podes iterar sobre uma lista usando um loop for. O exemplo seguinte soma todos os elementos na lista.

`list = [4, 7, 2, 5]
sum = 0
for number in list:
	sum += number`
`sum` é agora `18`

Os seguintes métodos de lista permitem-te adicionar e remover elementos:

`list.append(elem)` adiciona um elemento ao fim da lista:

`list = [2, 6, 12]
list.append(7)`
`list` é agora `[2, 6, 12, 7]`

`list.remove(elem)` remove a primeira ocorrência de um elemento de uma lista:

`list = [1, 2, 4, 2]
list.remove(2)`
`list` é agora `[1, 4, 2]`

`list.insert(index, elem)` insere um elemento no índice dado:

`list = [Entities.Tree, Items.Hay]
list.insert(1, Items.Wood)`
`list` é agora `[Entities.Tree, Items.Wood, Items.Hay]`

`list.pop(index)` remove o elemento no índice especificado.
Se nenhum índice for especificado, o último item é removido.

`list = [3, 5, 8, 25]
list.pop()`
`list` é agora `[3, 5, 8]`
`list.pop(1)`
`list` é agora `[3, 8]`

A função `len()` retorna o comprimento da lista.
`list = [3, 2, 1]
x = len(list)`
`x` é agora `3`

As listas têm semântica de referência. Isto significa que atribuir uma lista a uma variável atribui o mesmo objeto de lista a essa variável, em vez de fazer uma cópia da lista.
Se duas variáveis referenciam a mesma lista, as alterações na lista serão vistas por ambas.

`a = [1,2]
b = a
b.pop()`
`a` e `b` são agora ambos `[1]`
