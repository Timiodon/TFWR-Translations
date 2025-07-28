# Leaderboard
Wenn du es so weit geschafft hast, hast du viele Herausforderungen gemeistert. Aber hast du sie auch effizient gelöst?
Du kannst dich mit anderen Spielern auf verschiedenen Leaderboards um die effizientesten Anbaumethoden messen.

Du kannst einen Leaderboard-Lauf starten, indem du `leaderboard_run(leaderboard, filename, speedup)` aufrufst.
Dies startet eine [Simulation](docs/unlocks/simulation.md), ähnlich wie `simulate()`, außer dass die Startbedingungen festgelegt sind. Jede Leaderboard-Kategorie hat unterschiedliche Start- und Erfolgsbedingungen.

Der Leaderboard-Lauf ist erfolgreich, wenn die Erfolgsbedingung am Ende der Simulation `True` ist. Die Simulation endet nicht automatisch, wenn das Ziel erreicht ist. Du musst sicherstellen, dass das Programm terminiert.
Wenn der Lauf erfolgreich ist, wird deine Zeit dem Leaderboard hinzugefügt.

Um die Varianz zu reduzieren, müssen alle Läufe mindestens 2 Stunden dauern (du kannst es beschleunigen, also wird es nicht so lange dauern). Wenn ein Lauf früher abgeschlossen wird, wird er wiederholt, bis eine Gesamtzeit von 2 Stunden erreicht ist. Der Durchschnitt aller Läufe wird dann als dein Score hochgeladen.

Hier ist ein Beispiel-Setup, das dich auf das Heu-Leaderboard bringt.
![](LeaderboardSetup400)

## Schnellster Reset
Der schnellste Reset ist die prestigeträchtigste Kategorie. Automatisiere das Spiel vollständig von einem einzigen Farmfeld bis zum erneuten Freischalten der Leaderboards.

Du musst nicht alles freischalten, versuche einfach, `Unlocks.Leaderboard` so schnell wie möglich freizuschalten.

Denk daran, dass du `num_unlocked(unlock) > 0` verwenden kannst, um zu prüfen, ob etwas freigeschaltet ist, und du kannst `get_cost()` auf Freischaltungen anwenden, um zu sehen, was sie kosten, damit du automatisch die richtigen Items farmen kannst.

Funktionsaufruf:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Äquivalente Simulation:
`unlocks = {}
items = {}
globals = {}
#ein negativer Seed-Wert bedeutet einen zufälligen Seed
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Erfolgsbedingung:
`num_unlocked(Unlocks.Leaderboard) > 0`

## Labyrinth
Beginne mit allem freigeschaltet und farme `300000` Gold so schnell du kannst. Das ist genau die Menge an Gold, die du verdienst, indem du ein Labyrinth `300` Mal löst.

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
Beginne mit allem freigeschaltet und farme `98010` Knochen so schnell du kannst. Das ist genau die Anzahl der Knochen, die du bekommst, wenn du eine 10x10 Fläche mit dem Dinosaurierschwanz füllst.

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

## Andere Ressourcen-Leaderboards
Jede Pflanze hat ihr eigenes Leaderboard für das schnellstmögliche Farmen dieser speziellen Pflanze. Du startest mit allen Freischaltungen, den Ressourcen, die du zum Anbau der Pflanze benötigst, und viel Energie. Das Ziel ist es, `100000` der von der Pflanze produzierten Ressource zu farmen.

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

`Leaderboards.Polyculture` erfordert das Farmen von `100000` aller drei Polyculture-Ressourcen.