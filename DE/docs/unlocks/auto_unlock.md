# Automatische Freischaltungen
Um das Spiel vollständig zu automatisieren, kannst du die Funktion `unlock()` verwenden, um Features automatisch freizuschalten.
Zum Beispiel kannst du `unlock(Unlocks.Speed)` und `unlock(Unlocks.Expand)` nutzen, um die Geschwindigkeit und die Erweiterungs-Features freizuschalten.

Um die Kosten einer Freischaltung zu bestimmen, verwende einfach die Funktion `get_cost()`, wie du es für eine Pflanze oder ein Objekt tun würdest.
Beispiel:
`get_cost(Unlocks.Loops)`
gibt `{Items.Hay:5}` zurück

Wenn du herausfinden möchtest, wie viele von einem bestimmten Unlock du hast, verwende die Funktion `num_unlocked(unlock)`.

Zum Beispiel, `num_unlocked(Unlocks.Speed)` wird die Anzahl der Geschwindigkeitsupgrades zurückgeben, die du hast.

`num_unlocked(Unlocks.Senses)` wird `1` zurückgeben, wenn die Sinne freigeschaltet sind, und `0`, wenn nicht.

Du kannst `num_unlocked()` auch auf Items, Entities oder Grounds anwenden. Das wird `1` zurückgeben, wenn es freigeschaltet ist, andernfalls `0`.

Sei vorsichtig `num_unlocked(Unlocks.Carrots)` wird die Anzahl der Male zurückgeben, die es freigeschaltet/aufgerüstet wurde.
`num_unlocked(Items.Carrot)` wird nur `0` oder `1` zurückgeben. (Dasselbe gilt für andere Pflanzen)