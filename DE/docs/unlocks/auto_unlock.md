# Automatische Freischaltungen
Um das Spiel vollständig zu automatisieren, kannst du die `unlock()`-Funktion verwenden, um Features automatisch freizuschalten.
Zum Beispiel kannst du `unlock(Unlocks.Speed)` und `unlock(Unlocks.Expand)` verwenden, um die Geschwindigkeits- und Erweiterungs-Features freizuschalten.

Um die Kosten einer Freischaltung zu ermitteln, benutze einfach die `get_cost()`-Funktion, wie du es für eine Pflanze oder ein Item tun würdest.
Beispiel:
`get_cost(Unlocks.Loops)`
gibt `{Items.Hay:5}` zurück

Wenn du herausfinden möchtest, wie viele einer bestimmten Freischaltung du hast, benutze die `num_unlocked(unlock)`-Funktion.

Zum Beispiel wird `num_unlocked(Unlocks.Speed)` die Anzahl der Geschwindigkeits-Upgrades zurückgeben, die du hast.

`num_unlocked(Unlocks.Senses)` wird `1` zurückgeben, wenn Sinne freigeschaltet sind, und `0`, wenn nicht.

Du kannst `num_unlocked()` auch auf Items, Entities oder Grounds anwenden. Dies gibt `1` zurück, wenn es freigeschaltet ist, ansonsten `0`.

Sei vorsichtig, `num_unlocked(Unlocks.Carrots)` gibt die Anzahl der Freischaltungen/Upgrades zurück.
`num_unlocked(Items.Carrot)` wird nur `0` oder `1` zurückgeben. (Dasselbe gilt für andere Pflanzen)
