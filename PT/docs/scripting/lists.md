# Listas
Listas são uma maneira fácil de armazenar múltiplos valores em uma única variável.
Você pode criar novas listas assim:

`list = [2, True, Items.Hay]`

A lista agora contém os valores `2`, `True` e `Items.Hay`.
Uma lista também pode estar vazia:

`empty_list = []`

Você pode acessar um elemento de uma lista pelo seu índice. O índice é `0` para o primeiro elemento, `1` para o segundo, `2` para o terceiro...

planta cenouras
`list = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(list[1])`

Você pode iterar sobre uma lista usando um loop for. O exemplo a seguir soma todos os elementos da lista.

`list = [4, 7, 2, 5]
sum = 0
for number in list:
	sum += number`
`sum` agora é `18`

Os seguintes métodos de lista permitem que você adicione e remova elementos:

`list.append(elem)` adiciona um elemento ao final da lista:

`list = [2, 6, 12]
list.append(7)`
`list` agora é `[2, 6, 12, 7]`

`list.remove(elem)` remove a primeira ocorrência de um elemento de uma lista:

`list = [1, 2, 4, 2]
list.remove(2)`
`list` agora é `[1, 4, 2]`

`list.insert(index, elem)` insere um elemento no índice fornecido:

`list = [Entities.Tree, Items.Hay]
list.insert(1, Items.Wood)`
`list` agora é `[Entities.Tree, Items.Wood, Items.Hay]`

`list.pop(index)` remove o elemento no índice especificado.
Se nenhum índice for especificado, o último item é removido.

`list = [3, 5, 8, 25]
list.pop()`
`list` agora é `[3, 5, 8]`
`list.pop(1)`
`list` agora é `[3, 8]`

A função `len()` retorna o comprimento da lista.
`list = [3, 2, 1]
x = len(list)`
`x` agora é `3`

Listas têm semântica de referência. Isso significa que atribuir uma lista a uma variável atribui o mesmo objeto de lista a essa variável, em vez de fazer uma cópia da lista.
Se duas variáveis fazem referência à mesma lista, as alterações na lista serão vistas por ambas.

`a = [1,2]
b = a
b.pop()`
`a` e `b` são agora ambos `[1]`
