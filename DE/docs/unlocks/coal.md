[<- Bergbau](docs/unlocks/mining.md) <right>[Eisen ->](docs/unlocks/iron.md)
<right>[Springen ->](docs/unlocks/jump.md)
---
# Kohle
Unterirdisch sind verschiedene Erze verborgen, die darauf warten, von dir gefunden und abgebaut zu werden. Wenn du durch die Oberfläche in `Grounds.Dirt` gräbst, ist das erste Erz, das du findest, Kohle.

Um Kohle abzubauen, musst du nichts Besonderes tun: Führe einfach `dig()` aus, während sich die Drohne direkt über einem `Grounds.Coal`-Block befindet. Mit `get_ground_type()` prüfst du den Boden unter der Drohne und mit `get_ground_type(direction)` die vier benachbarten Blöcke.

Das folgende Programm ist ein guter Ausgangspunkt für die Kohlesuche. Es gräbt nach unten und sucht nach einer Kohleschicht.
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
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 4,
    "digging_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 2,
    "exclude_unlocks": ["watering", "fertilizer"]
}
#SETUP
move(North)
move(East)
move(East)
#CODE
# Graben, bis ein Kohleblock erscheint
while get_ground_type() != Grounds.Coal:
    dig()

# Kohle abbauen
dig()
}}

## Hinweis zu Einstürzen
Beachte, dass du nur Kohle für direkt abgebaute Kohleblöcke erhältst, nicht für Blöcke, die um die Drohne herum einstürzen. Berücksichtige das bei deiner Abbaustrategie, damit du möglichst viele Kohleblöcke selbst abbaust und möglichst wenige durch Einstürze verlierst.

## Aufbau der Adern
Die Adern bilden waagerechte, einen Block dicke Schichten, auf die du beim Graben durch Erde zufällig stoßen musst. Die Kohleblöcke einer Schicht liegen meist direkt nebeneinander, manche sind aber nur diagonal verbunden.

Die Kohlevorkommen wachsen proportional zur Farmgröße. Erforsche also [Erweitern](unlocks/expand) weiter, um mehr Kohle abbauen zu können.

## Strategie
<spoiler=zeige Hinweis> 
Eine einfache Strategie, besonders auf kleinen Farmen, ist es, alle Blöcke auf der Höhe abzubauen, auf der du Kohle gefunden hast. Für mehr Effizienz kannst du mit `get_ground_type(direction)` verfolgen, wo du Kohle gesehen hast, und vermeiden, Zeit mit Bewegungen über Erde zu verlieren. Achte besonders auf diagonale Verbindungen, die dir entgehen, wenn du dich ausschließlich über Kohleblöcken bewegst.
</spoiler>

---

[Statistiken](docs/stats.md)      [Bergbau](docs/unlocks/mining.md)      [Unterirdische Sinne](docs/unlocks/underground_senses.md)

[move()](functions/move)      [get_ground_type()](functions/get_ground_type)      [dig()](functions/dig)
