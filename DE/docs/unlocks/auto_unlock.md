# Automatische Freischaltungen
Um das Spiel vollständig zu automatisieren, kannst du die `unlock()`-Funktion verwenden, um Features automatisch freizuschalten.
Zum Beispiel kannst du `unlock(Unlocks.Speed)` und `unlock(Unlocks.Expand)` verwenden, um die Geschwindigkeits- und Erweiterungs-Features freizuschalten.

Um die Kosten einer Freischaltung zu bestimmen, benutze einfach die `get_cost()`-Funktion, so wie du es bei einer Pflanze oder einem Item tun würdest.
Beispiel:
`get_cost(Unlocks.Loops)`
gibt `{Items.Hay:5}` zurück