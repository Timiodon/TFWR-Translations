[<- Eisen](docs/unlocks/iron.md) <right>[Pilze ->](docs/unlocks/mushroom.md)
---
# Quarz
Ausgehend von den Eisenadern in `Grounds.Rock` findest du Quarz im unteren Teil der Gesteinsschicht und in der harten `Grounds.Dirt` darunter (prüfe die Härte mit `get_hardness()` aus der Freischaltung [Unterirdische Sinne](docs/unlocks/underground_senses.md)).

Der folgende Code gräbt durch die Erde in die Gesteinsschicht. Dort sucht er beim Graben fortlaufend nach Quarz, bis die Entfernung kleiner als 2 ist. Zum Schluss gibt er die erreichte Entfernung zur Ader aus.
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
    "items": [{"item": "block", "n": 1}, {"item": "iron", "n": 100}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 8,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "dynamite"]
}
#SETUP
move(East)
move(North)
#CODE
# Bis zur Gesteinsschicht graben
while get_ground_type() != Grounds.Rock:
    dig()

# Weitergraben, bis eine Quarzader nahe ist
while prospect_quartz() == None or prospect_quartz() >= 2:
    for i in range(10):
        dig()

# Die endgültige Entfernung zur Ader ausgeben
print(prospect_quartz())
}}

## Aufbau der Adern
Quarz wächst in nadelförmigen Adern, die senkrechte Säulen bilden. Das macht es recht schwierig, sie durch bloßes Ausprobieren zu finden.

## Quarz suchen
Zum Glück können wir unser Eisen zu etwas verbiegen, das einer Wünschelrute ähnelt und mit dem wir diese Quarzadern leichter aufspüren können. Der entsprechende Befehl lautet `prospect_quartz()`.

`prospect_quartz()` funktioniert anders als `prospect_iron()`. Statt der Richtung, in die sich die Drohne zum nächsten Eisenerz bewegen müsste, gibt es die genaue 3D-Entfernung zwischen dem nächsten Quarzblock und der Drohne zurück (euklidische Entfernung).

Die Ausführung von `prospect_quartz()` kostet 1 Eisen, daher solltest du den Befehl sparsam einsetzen.

Wenn `prospect_quartz()` keinen Quarz in der Nähe findet oder du nicht genug Eisen für die Suche hast, gibt der Befehl `None` zurück.

## Strategie
<spoiler=Hinweis anzeigen>Du kannst wiederholt nach Erz suchen und dich bewegen, um zu sehen, wie sich die Entfernung ändert. Auf einer ebenen Fläche kannst du durch Minimieren der Entfernung über eine Quarzader gelangen. Mit einer Strategie ähnlich der binären Suche kannst du die Zahl der `prospect_quartz()`-Aufrufe und ihren Eisenverbrauch minimieren.

Fortgeschrittenere Strategien können mit 2D-Geometrie die Schnittpunkte von zwei oder mehr Kreisen bestimmen. Oder du wählst den anspruchsvollen Weg einer vollständigen Trilateration: Bestimme den Schnittpunkt dreier Kugeln, um die genaue 3D-Position der Ader zu finden.

Für eine Quadratwurzel kannst du den Potenzoperator verwenden. Die Quadratwurzel von 16 erhältst du zum Beispiel mit `16**0.5`. Es gibt keine eingebauten Mathematikfunktionen für Trigonometrie oder Vektoren. Diese musst du selbst implementieren.

Beachte außerdem, dass sich mehrere Adern in der Nähe befinden können. Mehrere benachbarte Messungen müssen daher nicht auf dieselbe Ader zeigen.</spoiler>

---

[Statistiken](docs/stats.md)      [Bergbau](docs/unlocks/mining.md)      [Unterirdische Sinne](docs/unlocks/underground_senses.md)      [Variablen](docs/scripting/variables.md)      [Operatoren](docs/scripting/operators.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)      [prospect_quartz()](functions/prospect_quartz)
