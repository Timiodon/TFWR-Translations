# Koszty
Każdy koszt można przedstawić jako słownik, który mapuje przedmioty na liczby.

Funkcja `get_cost()` zwraca taki słownik. Zwraca koszt rośliny lub odblokowania.

`get_cost(Entities.Pumpkin)`
zwraca `{Items.Carrot:1}`

W przypadku odblokowań, można przekazać opcjonalny drugi argument dla poziomu odblokowania, dla którego chcesz uzyskać koszt. Domyślnie jest to bieżący poziom odblokowania.

`get_cost(Unlocks.Loops, 0)`
zwraca `{Items.Hay:5}`

Dla odblokowań, które są już na maksymalnym poziomie, `get_cost()` zwróci `None`.

Można go używać w ten sposób:
`cost = get_cost(coś)
for item in cost:
	potrzebna_ilość_tego_przedmiotu = cost[item]`