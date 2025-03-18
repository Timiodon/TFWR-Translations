# Koszty
Każdy koszt można przedstawić jako dictionary, który mapuje przedmioty do liczb.

Funkcja `get_cost()` zwraca taki dictionary. Zwraca koszt rośliny lub odblokowania.

`get_cost(Entities.Pumpkin)`
zwraca `{Items.Carrot:1}`

Dla odblokowań, można przekazać opcjonalny drugi argument dla poziomu odblokowania, dla którego chcesz uzyskać koszt. Domyślnie jest to obecny poziom odblokowania.

`get_cost(Unlocks.Loops, 0)`
zwraca `{Items.Hay:5}`

Dla odblokowań, które są już na maksymalnym poziomie, `get_cost()` zwróci `None`.

Można tego użyć w ten sposób:
`cost = get_cost(something)
for item in cost:
	amount_of_this_item_needed = cost[item]`