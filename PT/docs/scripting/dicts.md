# Dictionaries
Os Dictionaries são uma estrutura de dados que te permite mapear chaves para valores da mesma forma que um dicionário real mapeia palavras para as suas definições, e podes consultá-los muito rapidamente.

Um dictionary pode ser criado assim:
`right_of = {North:East, East:South, South:West, West:North}`

A expressão antes dos dois pontos é a chave e a expressão depois dos dois pontos é o valor ao qual a chave mapeia.
O dictionary acima mapeia cada direção para a direção à sua direita.

Aqui está outro que mapeia a posição do drone para a entity sobre a qual ele está.
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

Aceder ao valor mapeado a uma chave é semelhante a aceder a um elemento numa lista:
`value = dict[key]`

Exemplo:
`orientation = right_of[South]`
Isto define `orientation` como `West`.

Podes adicionar um novo par chave-valor a um dictionary assim:
`dict[key] = value`

Exemplo:
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
Isto atualiza a entity armazenada para a posição atual.

As chaves são únicas, por isso adicionar uma chave que já existe no dictionary irá substituir o valor anterior.

Usa `dict.pop(key)` para remover um par chave-valor de `dict`.

`key in dict` avalia para `True` se `key` for uma chave em `dict` e `False` caso contrário.
Assim, podes usar `if key in dict:` para verificar se `dict` contém a chave.

Colocar um dictionary num loop for permite-te iterar por todas as chaves:
`for key in dict:
	value = dict[key]`

Não há garantias sobre a ordem em que as chaves são iteradas.

Vê também [Sets](docs/scripting/sets.md)