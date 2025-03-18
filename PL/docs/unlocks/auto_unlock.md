# Automatyczne Odblokowywanie
Aby w pełni zautomatyzować grę, możesz użyć funkcji `unlock()`, aby automatycznie odblokować funkcje.
Na przykład, możesz użyć `unlock(Unlocks.Speed)` i `unlock(Unlocks.Expand)`, aby odblokować funkcje szybkości i rozbudowy.

Aby określić koszt odblokowania, po prostu użyj funkcji `get_cost()`, tak jak dla rośliny lub przedmiotu.
Przykład:
`get_cost(Unlocks.Loops)`
zwraca `{Items.Hay:5}`

Jeśli chcesz dowiedzieć się, ile masz konkretnych odblokowań, użyj funkcji `num_unlocked(unlock)`.

Na przykład `num_unlocked(Unlocks.Speed)` zwróci liczbę ulepszeń szybkości, które posiadasz.

`num_unlocked(Unlocks.Senses)` zwróci `1`, jeśli zdolności są odblokowane i `0`, jeśli nie są.

Możesz również użyć `num_unlocked()` na Przedmiotach, Encjach lub Terenach. To zwróci `1`, jeśli jest odblokowane, w przeciwnym razie `0`.

Uważaj, `num_unlocked(Unlocks.Carrots)` zwróci liczbę razy, gdy zostało odblokowane/ulepszone.
`num_unlocked(Items.Carrot)` zwróci tylko `0` lub `1`. (Tak samo w przypadku innych roślin)