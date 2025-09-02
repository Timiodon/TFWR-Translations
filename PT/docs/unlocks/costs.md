# Custos
Qualquer custo pode ser representado como um dicionário que mapeia itens para números.

A função `get_cost()` retorna tal dicionário. Ela retorna o custo de uma planta ou de um desbloqueio.

`get_cost(Entities.Pumpkin)`
retorna `{Items.Carrot:1}`

Para desbloqueios, um segundo argumento opcional pode ser passado para o nível de desbloqueio para o qual você deseja obter o custo. Por padrão, é o nível de desbloqueio atual.

`get_cost(Unlocks.Loops, 0)`
retorna `{Items.Hay:5}`

Para desbloqueios que já estão no nível máximo, `get_cost()` retornará `None`.

Pode ser usado assim:
`cost = get_cost(something)
for item in cost:
	amount_of_this_item_needed = cost[item]`
