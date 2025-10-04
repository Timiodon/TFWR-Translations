# Bestenliste
Wenn du es bis hierher geschafft hast, hast du viele Herausforderungen gemeistert. Aber hast du sie auch effizient gelöst? 
Du kannst mit anderen Spielern auf verschiedenen Bestenlisten um die effizientesten Farmmethoden wetteifern.

Du kannst einen Bestenlisten-Lauf starten, indem du `leaderboard_run(leaderboard, filename, speedup)` aufrufst.
Dies startet eine [Simulation](docs/unlocks/simulation.md), ähnlich wie `simulate()`, außer dass die Startbedingungen festgelegt sind. Jede Bestenlisten-Kategorie hat unterschiedliche Start- und Erfolgsbedingungen.

Der Bestenlisten-Lauf ist erfolgreich, wenn die Erfolgsbedingung am Ende der Simulation `True` ist. 

Die Simulation wird NICHT automatisch enden, wenn das Ziel erreicht ist. Du musst sicherstellen, dass das Programm terminiert.
Wenn der Lauf erfolgreich ist, wird deine Zeit zur Bestenliste hinzugefügt.

Um die Varianz zu reduzieren, müssen alle Läufe mindestens 2 Stunden dauern (Du kannst es beschleunigen, also wird es nicht so lange dauern). Wenn ein Lauf früher abgeschlossen wird, wird er wiederholt, bis eine Gesamtzeit von 2 Stunden erreicht ist. Der Durchschnitt aller Läufe wird dann als dein Ergebnis hochgeladen.

Hier ist ein Beispiel-Setup, das dich auf die Heu-Bestenliste bringt.
![](LeaderboardSetup400)

## Schnellster Reset
Der schnellste Reset ist die prestigeträchtigste Kategorie. Automatisiere das Spiel vollständig von einem einzelnen Farmfeld bis zum erneuten Freischalten der Bestenlisten.

Du musst nicht alles freischalten, versuche einfach, `Unlocks.Leaderboard` so schnell wie möglich freizuschalten.

Denke daran, dass du `num_unlocked(unlock) > 0` verwenden kannst, um zu prüfen, ob etwas freigeschaltet ist, und `get_cost()` auf Freischaltungen anwenden kannst, um zu sehen, was sie kosten, damit du automatisch die richtigen Gegenstände farmen kannst.

Funktionsaufruf:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Äquivalente Simulation:
`unlocks = {}
items = {}
globals = {}
#ein negativer Seed-Wert bedeutet ein zufälliger Seed
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Erfolgsbedingung:
`num_unlocked(Unlocks.Leaderboard) > 0`

## Labyrinth
Beginne mit allem freigeschaltet und farme `9863168` Gold so schnell du kannst. Das ist genau die Menge an Gold, die du verdienst, wenn du ein 32x32 Labyrinth `300` Mal löst.

Funktionsaufruf:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Äquivalente Simulation:
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Erfolgsbedingung:
`num_items(Items.Gold) >= 9863168`

## Dinosaurier
Beginne mit allem freigeschaltet und farme `33488928` Knochen so schnell du kannst. Das ist genau die Anzahl der Knochen, die du bekommst, wenn du eine 32x32 Fläche mit dem Dinosaurierschwanz füllst.

Funktionsaufruf:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Äquivalente Simulation:
`unlocks = Unlocks
items = {Items.Cactus : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Erfolgsbedingung:
`num_items(Items.Bone) >= 33488928`

## Andere Ressourcen-Bestenlisten
Jede Pflanze hat ihre eigene Bestenliste, um diese bestimmte Pflanze so schnell wie möglich zu farmen. Du startest mit allen Freischaltungen, den Ressourcen, die du zum Anbau der Pflanze benötigst, und viel Energie. Das Ziel ist es, eine festgelegte Menge der von der Pflanze produzierten Ressource zu farmen.

Wie immer musst du sicherstellen, dass dein Programm terminiert, wenn du das Ziel erreichst. Ein Lauf ist nicht beendet, bis das Programm endet, auch wenn das Ziel erreicht ist.

### `Leaderboards.Cactus`
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
Erfolgsbedingung: `num_items(Items.Cactus) >= 33554432`

### `Leaderboards.Sunflowers`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
Erfolgsbedingung: `num_items(Items.Sunflower) >= 100000`

### `Leaderboards.Pumpkins`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
Erfolgsbedingung: `num_items(Items.Pumpkin) >= 200000000`

### `Leaderboards.Wood`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
Erfolgsbedingung: `num_items(Items.Wood) >= 10000000000`

### `Leaderboards.Carrots`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
Erfolgsbedingung: `num_items(Items.Carrot) >= 2000000000`

### `Leaderboards.Hay`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
Erfolgsbedingung: `num_items(Items.Hay) >= 2000000000`

## Einzel-Drohnen-Bestenlisten
Es gibt auch Bestenlisten für das Farmen mit einer einzelnen Drohne. Du bekommst nur eine Drohne und eine 8x8-Farm und musst eine bestimmte Menge an Ressourcen so schnell wie möglich farmen.

### `Leaderboards.Maze_Single`
`leaderboard_run(Leaderboards.Maze_Single, filename, speedup)`
Erfolgsbedingung: `num_items(Items.Gold) >= 616448`

### `Leaderboards.Cactus_Single`
`leaderboard_run(Leaderboards.Cactus_Single, filename, speedup)`
Erfolgsbedingung: `num_items(Items.Cactus) >= 131072`

### `Leaderboards.Sunflowers_Single`
`leaderboard_run(Leaderboards.Sunflowers_Single, filename, speedup)`
Erfolgsbedingung: `num_items(Items.Sunflower) >= 10000`

### `Leaderboards.Pumpkins_Single`
`leaderboard_run(Leaderboards.Pumpkins_Single, filename, speedup)`
Erfolgsbedingung: `num_items(Items.Pumpkin) >= 10000000`

### `Leaderboards.Wood_Single`
`leaderboard_run(Leaderboards.Wood_Single, filename, speedup)`
Erfolgsbedingung: `num_items(Items.Wood) >= 500000000`

### `Leaderboards.Carrots_Single`
`leaderboard_run(Leaderboards.Carrots_Single, filename, speedup)`
Erfolgsbedingung: `num_items(Items.Carrot) >= 100000000`

### `Leaderboards.Hay_Single`
`leaderboard_run(Leaderboards.Hay_Single, filename, speedup)`
Erfolgsbedingung: `num_items(Items.Hay) >= 100000000`