# Dicionários
Dicionários são uma estrutura de dados que te permite mapear chaves para valores da mesma forma que um dicionário real mapeia palavras para suas definições e você pode consultá-las muito rapidamente.

Um dicionário pode ser criado assim:
`rotation = {North:East, East:South, South:West, West:North}`

A expressão antes dos dois pontos é a chave e a expressão depois dos dois pontos é o valor para o qual a chave é mapeada. O dicionário acima mapeia cada direção para a direção à sua direita.

Aqui está outro que mapeia a posição do drone para a entidade sobre a qual ele está.
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

Acessar o valor mapeado para uma chave é semelhante a acessar um elemento em uma lista:
`value = dict[key]`

Exemplo:
`orientation = rotation[South]`
Isto define `orientation` para `West`.

Você pode adicionar um novo par chave-valor a um dicionário assim:
`dict[key] = value`

Exemplo:
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
Isto atualiza a entidade armazenada para a posição atual.

As chaves são únicas, então adicionar uma chave que já existe no dicionário substituirá o valor anterior.

Use `dict.pop(key)` para remover um par chave-valor do `dict`.

`key in dict` avalia para `True` se `key` for uma chave no `dict` e `False` caso contrário. Assim, você pode usar `if key in dict:` para verificar se o `dict` contém a chave.

Colocar um dicionário em um loop for te permite iterar por todas as chaves:
`for key in dict:
	value = dict[key]`

Não há garantias sobre a ordem em que as chaves são iteradas.

Veja também [Sets](docs/scripting/sets.md)