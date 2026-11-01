[<- Bambus](docs/unlocks/bamboo.md)
---
# Pyramiden
Unter der Erde befinden sich nun uralte pyramidenförmige Bauwerke, aus denen du Energie gewinnen kannst, um deine Drohne zu beschleunigen!

Pyramiden bestehen aus Sandblöcken (`Grounds.Sand`). Unter der eigentlichen Pyramide liegt ein Fundament aus Kalkstein (`Grounds.Limestone`). Weil die Pyramiden alt und verwittert sind, findest du sie nur in teilweise zerstörtem Zustand. Das Fundament ist immer vollständig, im Sand befinden sich jedoch Lücken.

So sieht eine Pyramidenruine aus, wenn du sie freilegst:
{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 100}, {"item": "block", "n": 100}],
    "world_size": {"x": 6, "y": 6},
    "execution_speed": 32,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 7,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "dynamite", "quartz"]
}
#SETUP
jump(Unlocks.Pyramid)
move(North)
#CODE
# Nach unten graben, um ein Pyramidenfundament zu finden
while get_ground_type() != Grounds.Limestone:
    dig()

z = get_pos_z() # Die Tiefe des Fundaments merken

# Alles weggraben, was nicht zur Pyramide gehört
for i in range(6):
    for j in range(6):
        while (get_ground_type() != Grounds.Limestone
                and get_ground_type() != Grounds.Sand
                and get_pos_z() > z):
            dig()
        move(North)
    move(East)
}}

## Die Pyramide wiederherstellen
Wie du siehst, weist der Sand mehrere Lücken auf, die gefüllt werden müssen. Wenn du diese Löcher füllst und die Pyramide wiederherstellst, zerstört sie sich selbst und in der Mitte des Kalksteinfundaments erscheint eine große Sonnenblume. Ernte sie, um `Items.Power` zu erhalten. Je größer die von dir vervollständigte Pyramide war, desto mehr Energie erhältst du.

Du kannst eine Pyramide wiederherstellen, indem du mit dem Befehl `place(Grounds.Sand)` Blöcke platzierst. Sand ist ein besonderer Block, der sofort einstürzt, wenn er nicht richtig abgestützt wird. Wenn du einen Sandblock platzierst, muss er sich entweder direkt auf Kalkstein oder auf einem 3x3-Feld aus Sandblöcken befinden. Zur Veranschaulichung dient diese kleine, von Hand gebaute Pyramide. Wenn du selbst eine baust, erhältst du natürlich keine Energie:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 100}, {"item": "block", "n": 100}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 4,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz"]
}
#CODE
# Wir brauchen ein Kalksteinfundament, um Sand darauf zu platzieren
for i in range(3):
    for j in range(3):
        place(Grounds.Limestone)
        move(North)
    move(East)

# Eine 3x3-Sandschicht auf dem Kalkstein platzieren
for i in range(3):
    for j in range(3):
        place(Grounds.Sand)
        move(North)
    move(East)

# Eine weitere 3x3-Schicht versuchen
# Nur der mittlere Block wird gestützt und bleibt erhalten
for i in range(3):
    for j in range(3):
        place(Grounds.Sand)
        move(North)
    move(East)
}}

Eine korrekt wiederhergestellte Pyramide besteht aus einem quadratischen Kalksteinfundament mit ungerader Seitenlänge, zum Beispiel 5x5. Darauf folgt eine gleich große Schicht aus Sandblöcken (5x5), gefolgt von immer kleineren Schichten: 3x3 und schließlich 1x1.

Über der Pyramide befinden sich ausschließlich Erdblöcke. Diese Tatsache kannst du nutzen, um eine Pyramide effizient freizulegen.

## Energie
Solange du Energie hast, nutzt die Drohne sie, um doppelt so schnell zu arbeiten.
Sie verbraucht alle 30 Aktionen 1 Energie, beispielsweise bei Bewegungen, beim Ernten oder beim Pflanzen.
Auch die Ausführung anderer Codeanweisungen kann Energie verbrauchen, allerdings deutlich weniger als Drohnenaktionen.

Im Allgemeinen wird alles, was durch Geschwindigkeits-Upgrades beschleunigt wird, auch durch Energie beschleunigt.
Alles, was durch Energie beschleunigt wird, verbraucht auch Energie proportional zur Ausführungszeit, wobei Geschwindigkeits-Upgrades ignoriert werden.

Energie hat keinen Einfluss auf `dig()`.

---

[Statistiken](docs/stats.md)      [Unterirdische Sinne](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [use_item()](functions/use_item)      [place()](functions/place)
