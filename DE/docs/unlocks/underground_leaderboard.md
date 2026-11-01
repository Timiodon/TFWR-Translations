# Unterirdische Bestenliste
Unter der Erde warten noch größere Herausforderungen. Bist du bereit, deine Bergbau- und Farmprogramme zu optimieren?
Mit dieser Freischaltung kannst du um die effizientesten Methoden in der Tiefe wetteifern.

Du kannst einen unterirdischen Bestenlisten-Lauf starten, indem du `leaderboard_run(leaderboard, filename, speedup)` aufrufst.
Dies startet eine [Simulation](docs/unlocks/simulation.md), ähnlich wie `simulate()`, außer dass die Startbedingungen festgelegt sind. Jede Bestenlisten-Kategorie hat unterschiedliche Start- und Erfolgsbedingungen.

Der Bestenlisten-Lauf ist erfolgreich, wenn die Erfolgsbedingung am Ende der Simulation `True` ist. 

Die Simulation wird NICHT automatisch enden, wenn das Ziel erreicht ist. Du musst sicherstellen, dass das Programm terminiert.
Wenn der Lauf erfolgreich ist, wird deine Zeit zur Bestenliste hinzugefügt.

Um Schwankungen zu verringern, müssen alle Durchläufe mindestens 2 Stunden simulierter Zeit umfassen. Du kannst die Simulation beschleunigen, sodass dies in Echtzeit nicht so lange dauert. Endet ein Durchlauf früher, wird er wiederholt, bis insgesamt 2 Stunden simulierte Zeit erreicht sind. Anschließend wird die durchschnittliche Zeit aller Durchläufe als dein Ergebnis hochgeladen.

Hier ist ein Beispiel-Setup, das dich auf die Bestenliste `Leaderboards.Rice_Single` bringt.

![|x400](UndergroundLeaderboardSetup)

## Schnellster unterirdischer Reset
Der unterirdische Reset ist die prestigeträchtigste Kategorie. In dieser Kategorie automatisierst du den Bergbau-Forschungsbaum vollständig, von einem einzelnen Farmfeld bis zum erneuten Freischalten von `Unlocks.Underground_Leaderboard`.

Du musst nicht alles freischalten, versuche einfach, `Unlocks.Underground_Leaderboard` so schnell wie möglich freizuschalten.

Denke daran, dass du `num_unlocked(unlock) > 0` verwenden kannst, um zu prüfen, ob etwas freigeschaltet ist, und `get_cost()` auf Freischaltungen anwenden kannst, um zu sehen, was sie kosten, damit du automatisch die richtigen Gegenstände farmen kannst.

`unlock()` berücksichtigt Abhängigkeiten im Forschungsbaum nicht. Du kannst beispielsweise `Unlocks.Fertilizer` vor `Unlocks.Water` freischalten.

Funktionsaufruf:
`leaderboard_run(Leaderboards.Fastest_Underground_Reset, filename, speedup)`

Äquivalente Simulation:
`unlocks = {}
items = {}
globals = {}
#ein negativer Seed-Wert bedeutet ein zufälliger Seed
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Erfolgsbedingung:
`num_unlocked(Unlocks.Underground_Leaderboard) > 0`

## Erze
Diese Bestenliste prüft deine Fähigkeiten beim Farmen von Erzen, besonders Quarz. Sie ändert die Bodengenerierung so, dass die Schichten zuerst Kohle, dann Eisen und schließlich Quarz bereitstellen.

Beginne mit allem freigeschaltet und farme `20000` Quarz so schnell du kannst.

Funktionsaufruf:
`leaderboard_run(Leaderboards.Ores, filename, speedup)`

Äquivalente Simulation:
`unlocks = Unlocks
items = {Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Erfolgsbedingung:
`num_items(Items.Quartz) >= 20000`

## Schatzkarte
Diese Bestenliste startet mit allen Freischaltungen und viel Energie. Sie ändert die Bodengenerierung so, dass besonders viele Schatzkarten vorkommen.

Sie findet auf einer 8x8-Welt mit einer einzelnen Drohne statt. Das Ziel ist es, so schnell wie möglich `115000` Gold zu farmen.

Funktionsaufruf:
`leaderboard_run(Leaderboards.Treasure_Map, filename, speedup)`

Äquivalente Simulation:
`unlocks = Unlocks
items = {Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Erfolgsbedingung:
`num_items(Items.Gold) >= 115000`

## Ressourcen-Bestenlisten
Bei diesen Bestenlisten geht es darum, bestimmte Ressourcen so schnell wie möglich zu farmen. Du startest mit allen Freischaltungen und viel Energie. Die einzige Ausnahme ist die Pyramiden-Bestenliste, bei der du durch das Wiederherstellen von Pyramiden selbst Energie erzeugen musst.

Das Ziel ist es, eine festgelegte Menge an Ressourcen zu farmen.

Wie immer musst du sicherstellen, dass dein Programm terminiert, wenn du das Ziel erreichst. Ein Lauf ist nicht beendet, bis das Programm endet, auch wenn das Ziel erreicht ist.

Diese Bestenlisten ändern die Bodengenerierung so, dass die gewünschte Ressource immer wieder vorkommt. Du musst also nicht `clear()` verwenden. Die Reis-Bestenliste besteht zum Beispiel ausschließlich aus Tonschichten.

### `Leaderboards.Rice`
`leaderboard_run(Leaderboards.Rice, filename, speedup)`
Erfolgsbedingung: `num_items(Items.Rice) >= 2000000`

### `Leaderboards.Bamboo`
Beachte, dass Graben in der Bambus-Bestenliste nicht erlaubt ist.

`leaderboard_run(Leaderboards.Bamboo, filename, speedup)`
Erfolgsbedingung: `num_items(Items.Bamboo) >= 500000000`

### `Leaderboards.Dynamite`
`leaderboard_run(Leaderboards.Dynamite, filename, speedup)`
Erfolgsbedingung: `num_items(Items.Dynamite) >= 10000000`

### `Leaderboards.Mushrooms`
`leaderboard_run(Leaderboards.Mushrooms, filename, speedup)`
Erfolgsbedingung: `num_items(Items.Mushroom) >= 240000`

### `Leaderboards.Pyramids`
`leaderboard_run(Leaderboards.Pyramids, filename, speedup)`
Erfolgsbedingung: `num_items(Items.Power) >= 150000`

## Unterirdische Einzel-Drohnen-Bestenlisten
Es gibt auch Bestenlisten für das Farmen mit einer einzelnen Drohne. Du bekommst nur eine Drohne und eine 8x8-Farm und musst eine bestimmte Menge an Ressourcen so schnell wie möglich farmen.

### `Leaderboards.Rice_Single`
`leaderboard_run(Leaderboards.Rice_Single, filename, speedup)`
Erfolgsbedingung: `num_items(Items.Rice) >= 100000`

### `Leaderboards.Ores_Single`
`leaderboard_run(Leaderboards.Ores_Single, filename, speedup)`
Erfolgsbedingung: `num_items(Items.Quartz) >= 4000`

### `Leaderboards.Bamboo_Single`
`leaderboard_run(Leaderboards.Bamboo_Single, filename, speedup)`
Erfolgsbedingung: `num_items(Items.Bamboo) >= 25000000`

### `Leaderboards.Dynamite_Single`
`leaderboard_run(Leaderboards.Dynamite_Single, filename, speedup)`
Erfolgsbedingung: `num_items(Items.Dynamite) >= 100000`

### `Leaderboards.Mushrooms_Single`
`leaderboard_run(Leaderboards.Mushrooms_Single, filename, speedup)`
Erfolgsbedingung: `num_items(Items.Mushroom) >= 30000`

### `Leaderboards.Pyramids_Single`
`leaderboard_run(Leaderboards.Pyramids_Single, filename, speedup)`
Erfolgsbedingung: `num_items(Items.Power) >= 30000`

