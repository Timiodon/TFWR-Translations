# Automatyczne odblokowania
Aby w pełni zautomatyzować grę, możesz użyć funkcji `unlock()`, aby automatycznie odblokowywać funkcje.
Na przykład, możesz użyć `unlock(Unlocks.Speed)` i `unlock(Unlocks.Expand)`, aby odblokować ulepszenia prędkości i rozszerzenia.

Aby określić koszt odblokowania, po prostu użyj funkcji `get_cost()` tak samo, jak w przypadku rośliny lub przedmiotu.
Przykład:
`get_cost(Unlocks.Loops)`
zwraca `{Items.Hay:5}`
