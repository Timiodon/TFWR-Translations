# Leaderboard
Wenn du es bis hierher geschafft hast, hast du viele Herausforderungen gemeistert. Aber hast du sie effizient gelöst? Du kannst mit anderen Spielern in verschiedenen Leaderboards um die effizientesten Anbaumethoden konkurrieren.

Du kannst einen Leaderboard-Lauf starten, indem du `leaderboard_run(leaderboard, filename, speedup)` aufrufst. Dies startet eine [Simulation](docs/unlocks/simulation.md), die `simulate()` ähnelt, wobei die Startbedingungen festgelegt sind. Jede Leaderboard-Kategorie hat unterschiedliche Start- und Erfolgskriterien.

Der Leaderboard-Lauf ist erfolgreich, wenn die Erfolgsbedingung `True` ist, wenn die Simulation endet. Die Simulation endet nicht automatisch, wenn das Ziel erreicht ist. Du musst sicherstellen, dass das Programm beendet wird. Wenn der Lauf erfolgreich ist, wird deine Zeit zum Leaderboard hinzugefügt.

Um Schwankungen zu verringern, müssen alle Läufe mindestens 2 Stunden dauern (du kannst sie beschleunigen, damit es nicht so lange dauert). Wenn ein Lauf vorher abgeschlossen wird, wird er wiederholt, bis eine Gesamtzeit von 2 Stunden erreicht ist. Der Durchschnitt aller Läufe wird dann als deine Punktzahl hochgeladen.

Hier ist eine Beispielkonfiguration, die dich ins Heu-Leaderboard bringt.
![](LeaderboardSetup400)

## Schnellster Reset
Der schnellste Reset ist die prestigeträchtigste Kategorie. Automatisiere das Spiel vollständig von einem einzigen Feld bis zum erneuten Freischalten der Leaderboards.

Du musst nicht alles freischalten, versuche nur `Unlocks.Leaderboard` so schnell wie möglich freizuschalten.

Denk daran, dass du `num_unlocked(unlock) > 0` verwenden kannst, um zu prüfen, ob etwas freigeschaltet ist, und du kannst `get_cost()` auf Freischaltungen verwenden, um zu sehen, was sie kosten, damit du die richtigen Sachen automatisch farmen kannst.

Funktionsaufruf:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Äquivalente Simulation:
`unlocks = {}
items = {}
globals = {}
#a negative seed value means a random seed
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Erfolgsbedingung:
`num_unlocked(Unlocks.Leaderboard) > 0`

## Labyrinth
Starte mit allem freigeschaltet und ernte so schnell wie möglich `300000` Gold. Dies ist genau die Menge an Gold, die du verdienen wirst, wenn du ein Labyrinth `300` Mal löst.

Funktionsaufruf:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Äquivalente Simulation:
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Erfolgsbedingung:
`num_items(Items.Gold) >= 300000`

## Dinosaurier
Starte mit allem freigeschaltet und sammle so schnell wie möglich `98010` Knochen. Dies ist genau die Anzahl von Knochen, die du erhälst, wenn du einen 10x10-Bereich mit dem Dinosaurierschwanz füllst.

Funktionsaufruf:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Äquivalente Simulation:
`unlocks = Unlocks
items = {Items.Pumpkin : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Erfolgsbedingung:
`num_items(Items.Bone) >= 98010`

## Weitere Ressourcen-Leaderboards
Jede Pflanze hat ihr eigenes Leaderboard, um diese Pflanze so schnell wie möglich zu züchten. Du startest mit allen Freischaltungen, den Ressourcen, die du benötigst, um die Pflanze zu wachsen, und viel Power. Das Ziel ist, `100000` von der Ressource zu farmen, die die Pflanze produziert.

Funktionsaufrufe:
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
`leaderboard_run(Leaderboards.Polyculture, filename, speedup)`

Erfolgsbedingung:
`num_items(resource) >= 100000`

`Leaderboards.Polyculture` erfordert das Farmen von `100000` aller drei Polykultur-Ressourcen.