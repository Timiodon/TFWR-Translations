# Automatikus feloldások
A játék teljes automatizálásához használhatod az `unlock()` függvényt funkciók automatikus feloldásához.
Például használhatod az `unlock(Unlocks.Speed)` és `unlock(Unlocks.Expand)`-et a sebesség és bővítés funkciók feloldásához.

A feloldás költségének meghatározásához egyszerűen használd a `get_cost()` függvényt, ahogy növény vagy item esetén tennéd.
Példa:
`get_cost(Unlocks.Loops)`
visszaadja `{Items.Hay:5}`