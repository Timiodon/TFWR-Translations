# Koszty
Każdy koszt może być reprezentowany jako słownik, który mapuje przedmioty na liczby.

Funkcja `get_cost()` zwraca taki słownik. Zwraca koszt rośliny lub odblokowania.

`get_cost(Entities.Pumpkin)`
zwraca `{Items.Carrot:1}`

Dla odblokowań, opcjonalny drugi argument może być przekazany dla poziomu odblokowania, dla którego chcesz uzyskać koszt. Domyślnie jest to bieżący poziom odblokowania.

`get_cost(Unlocks.Loops, 0)`
zwraca `{Items.Hay:5}`

Dla odblokowań, które są już na maksymalnym poziomie, `get_cost()` zwróci `None`.

Można go użyć w ten sposób:
`koszt = get_cost(coś)
for przedmiot in koszt:
	potrzebna_ilość_tego_przedmiotu = koszt[przedmiot]`
