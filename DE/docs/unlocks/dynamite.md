[<- Pilze](docs/unlocks/mushroom.md) <right>[Sprengbohrer ->](docs/unlocks/explosive_drill.md)
---
# Dynamit
Der revolutionäre Sprengstoff, zurückgelassen von früheren Bergbauexpeditionen. Leider eignet sich dein Bohrer hervorragend dazu, Dynamit zur Explosion zu bringen und alle Blöcke um dich herum wegzusprengen. Gesammeltes Dynamit kann mit `use_item(Items.Dynamite)` verwendet werden und explodiert direkt unter der Drohne.

Um Dynamit sicher abzubauen, musst du die Doppelschicht aus `Grounds.Dynamite` und `Grounds.Soot` finden. Der Dynamitboden darüber ist etwas in die Jahre gekommen, weshalb sich einige seiner Blöcke gefahrlos aufgraben lassen. Ein Teil des Dynamits ist jedoch noch aktiv und explodiert beim Graben.

Dieses Beispiel gräbt in das Dynamit und um die erste Grabstelle herum, legt die Rußschicht mit ihren Zahlen frei und gibt den Messwert aus:
{{codeexample 
{
    "camera_position": {"x": -3, "y": 0, "z": 15},
    "show_image": true,
    "image_size": {"x": 800, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 7, "y": 7},
    "execution_speed": 2,
    "digging_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 6,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz", "petrified_pumpkins"]
}
#SETUP
jump(Unlocks.Dynamite)
for _ in range(3):
    move(East)
    move(North)
#CODE
# Durch die Dynamitschicht zur darunterliegenden Rußschicht graben
while get_ground_type() != Grounds.Soot:
    dig()

# Richtungsliste, mit der die Drohne im Kreis fliegt
circle_directions = [
    East, South, West, West, 
    North, North, East, East
]
for dir in circle_directions:
    move(dir)
    dig()
    print(measure()) # Die Zahl auf dem Rußblock
}}

## Dynamit-Räumer
Kannst du alle Blindgänger finden und ausgraben, sodass nur noch aktive Blöcke übrig bleiben? Jeder aktive Block, der ausschließlich von anderen aktiven Blöcken oder Rußblöcken umgeben ist, bringt dir zusätzliches Dynamit ein, sobald die Dynamitschicht verschwindet.

Zum Glück helfen dir die Rußblöcke darunter: Sie können erkennen, wie viele benachbarte Dynamitblöcke aktives Dynamit enthalten. Sie verraten dir nicht, welche Blöcke aktiv sind, sondern nur deren Gesamtzahl. Du musst also die Messwerte mehrerer Rußblöcke kombinieren und die Lösung selbst ermitteln.

Wenn du `measure()` auf einem Rußblock aufrufst, erhältst du die Anzahl der Minen in den acht benachbarten Feldern der darüberliegenden Dynamitschicht. Der Wert kann zwischen `0` (keine aktive Mine) und `8` (jeder Nachbar enthält eine aktive Mine) liegen.

Der erste aufgebrochene Block der Dynamitschicht ist immer ein Blindgänger. Jeder abgebaute Dynamitblock liefert etwas Dynamit. Wird die Dynamitschicht zerstört – entweder weil du erfolgreich alle Blindgänger ausgegraben oder versehentlich aktives Dynamit getroffen hast –, erhältst du außerdem Dynamit in Höhe des Quadrats der vollständig freigelegten aktiven Blöcke.

## Aufbau der Schichten
Die Anzahl der aktiven Minen in der Dynamitschicht und damit die Schwierigkeit, sie zu finden, nimmt mit der Tiefe zu. Die Gesamtzahl der Minen steigt mit der Farmgröße und damit auch der maximal mögliche Ertrag beim Räumen einer Dynamitschicht.

Verbessere Dynamit, um den Ertrag beim Graben in Dynamitblöcke und beim vollständigen Freilegen aktiver Blöcke zu erhöhen. Die Verbesserung steigert außerdem die Energie von Dynamitexplosionen um 30 %.

## Erfolg und Fehlschlag erkennen
Wenn du in aktives Dynamit gräbst, explodieren beide Schichten. Du kannst dies überprüfen, indem du nach dem Graben in `Grounds.Dynamite` `get_ground_type()` verwendest. Wenn der Boden nicht `Grounds.Soot` ist, hast du das Rätsel nicht gelöst. Wird hingegen der letzte nicht aktive Dynamitblock ausgegraben, verschwinden alle Dynamitblöcke und du erhältst den maximalen Ertrag für das Rätsel. Die Rußschicht bleibt bestehen, aber `measure()` gibt `None` zurück, was anzeigt, dass das Rätsel erfolgreich gelöst wurde.

`# In einen Dynamitblock graben und den Zustand des Rätsels überprüfen
def dig_dynamite():
    dig()
    if get_ground_type() != Grounds.Soot:
        # In aktives Dynamit gegraben, Rätsel fehlgeschlagen
        return False
    elif measure() == None:
        # Letzten Blindgänger ausgegraben, Rätsel gelöst
        return True
    else:
        # Messung ergab eine Anzahl, Rätsel läuft noch
        return None
`

## Strategie
<spoiler=Hinweis>
Der folgende Code gräbt in die Dynamitschicht und sucht nach Rußblöcken mit dem Messwert `0`. Für jeden solchen Block baut er alle umliegenden Dynamitblöcke ab:
{{codeexample 
{
    "camera_position": {"x": -5, "y": 0, "z": 15},
    "show_image": true,
    "image_size": {"x": 800, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 7, "y": 7},
    "execution_speed": 4,
    "digging_speed": 8,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 6,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz", "petrified_pumpkins"]
}
#SETUP
jump(Unlocks.Dynamite)
for _ in range(3):
    move(East)
    move(North)
#CODE
while get_ground_type() != Grounds.Soot:
    dig()

circle_directions = [
    East, South, West, West, North,
    North, East, East, South, West
]
# Um den zuerst angegrabenen Block herumgehen
for dir in circle_directions:
    # Wenn der Ruß 0 misst,
    # wissen wir, dass alle umliegenden Dynamitblöcke Blindgänger sind
    if get_ground_type() == Grounds.Soot and measure() == 0:
        # Noch eine Runde durch die umliegenden Blöcke drehen
        for dir2 in circle_directions:
            move(dir2)
            # Dynamitblindgänger abbauen
            while get_ground_type() != Grounds.Soot:
                dig()
    move(dir)
}}
</spoiler>

---

[Statistiken](docs/stats.md)      [Unterirdische Sinne](docs/unlocks/underground_senses.md)      [Dictionaries](docs/scripting/dicts.md)      [Sets](docs/scripting/sets.md)

[move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)      [use_item()](functions/use_item)
