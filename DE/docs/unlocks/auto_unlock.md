# Automatische Freischaltungen
Um das Spiel vollständig zu automatisieren, kannst du die `unlock()`-Funktion verwenden, um Features automatisch freizuschalten.
Zum Beispiel kannst du `unlock(Unlocks.Speed)` und `unlock(Unlocks.Expand)` verwenden, um die Geschwindigkeits- und Erweiterungs-Features freizuschalten.

Um die Kosten einer Freischaltung zu ermitteln, verwende einfach die `get_cost()`-Funktion, wie du es für eine Pflanze oder ein Item tun würdest.
Beispiel:
`get_cost(Unlocks.Loops)`
gibt `{Items.Hay:5}` zurück
