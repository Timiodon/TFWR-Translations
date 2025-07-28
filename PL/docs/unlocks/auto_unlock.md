# Automatyczne odblokowywanie
Aby w pełni zautomatyzować grę, możesz użyć funkcji `unlock()`, aby automatycznie odblokowywać funkcje.
Na przykład, możesz użyć `unlock(Unlocks.Speed)` i `unlock(Unlocks.Expand)`, aby odblokować funkcje prędkości i rozszerzenia.

Aby określić koszt odblokowania, po prostu użyj funkcji `get_cost()` tak samo, jak dla rośliny lub przedmiotu.
Przykład:
`get_cost(Unlocks.Loops)`
zwraca `{Items.Hay:5}`

Jeśli chcesz dowiedzieć się, ile masz danego odblokowania, użyj funkcji `num_unlocked(unlock)`.

Na przykład, `num_unlocked(Unlocks.Speed)` zwróci liczbę posiadanych ulepszeń prędkości.

`num_unlocked(Unlocks.Senses)` zwróci `1`, jeśli zmysły są odblokowane, i `0`, jeśli nie są.

Możesz także użyć `num_unlocked()` na przedmiotach, entity lub podłożach. Zwróci to `1`, jeśli jest odblokowane, w przeciwnym razie `0`.

Uważaj, `num_unlocked(Unlocks.Carrots)` zwróci liczbę odblokowań/ulepszeń.
`num_unlocked(Items.Carrot)` zwróci tylko `0` lub `1`. (To samo dotyczy innych roślin)
