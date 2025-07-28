# Custos
Qualquer custo pode ser representado como um dictionary que mapeia itens para números.

A função `get_cost()` retorna um tal dictionary. Retorna o custo de uma planta ou de um unlock.

`get_cost(Entities.Pumpkin)`
retorna `{Items.Carrot:1}`

Para unlocks, um segundo argumento opcional pode ser passado para o nível do unlock para o qual queres obter o custo. Por defeito, é o nível de unlock atual.

`get_cost(Unlocks.Loops, 0)`
retorna `{Items.Hay:5}`

Para unlocks que já estão no nível máximo, `get_cost()` retornará `None`.

Pode ser usado assim:
`cost = get_cost(alguma_coisa)
for item in cost:
	quantidade_deste_item_necessaria = cost[item]`
