[<- Erweitern 1](docs/unlocks/expand_1.md) <right>[Unterirdische Sinne ->](docs/unlocks/underground_senses.md)
<right>[Reis ->](docs/unlocks/rice.md)
<right>[Kohle ->](docs/unlocks/coal.md)
---
# Bergbau

Deine Drohne hat Zugriff auf einen einfachen Bohrer erhalten, mit dem sie unterirdisch nach Schätzen suchen kann.

Mit dem Befehl `dig()` kannst du in den Block unter dir graben.

Sammeln wir zunächst ein paar Blöcke:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "special_soils"]
}
#SETUP
move(North)
move(East)
#CODE
dig()
do_a_flip()
dig()
do_a_flip()
dig()
do_a_flip()
clear()
}}

Wenn du zur Oberfläche zurückkehren möchtest, kannst du jederzeit `clear()` verwenden. Dadurch wird auch deine Farm wiederhergestellt.

Wenn du den Mauszeiger über einen Block bewegst, werden sein Name, seine Stabilität und seine Härte angezeigt.

# Bohrer

Je tiefer du gräbst, desto härter werden die Blöcke und desto länger dauert das Graben. Gut, dass wir unseren Bohrer verbessern können!

Mit `get_hardness()` kannst du die Härte des Blocks unter dir prüfen. Wenn du auf einen Bereich mit besonders harten Blöcken stößt, kann es sinnvoll sein, sie zu umgehen, um schneller voranzukommen:

`while True:
    if get_hardness() < 5:
        dig()
    else:
        move(East)`

Natürlich werden die Blöcke nach unten hin immer härter. Diese Strategie hilft also nur bis zu einem gewissen Punkt.

## Einstürze

Wenn du nach unten gräbst, stürzen umliegende Blöcke ein. Die vier Blöcke neben der Drohne werden immer zerstört. Anschließend breitet sich der Einsturz abhängig von der Stabilität des Bodens aus. Ein Block mit Stabilität 1, etwa Grasland, verträgt einen Höhenunterschied von 1. Hat das Grasland also einen senkrechten oder waagerechten Nachbarn, dessen z-Koordinate mindestens 2 Blöcke tiefer liegt, wird es zerstört.

Die Stabilität eines Blocks wird in seinem Tooltip angezeigt.

Wenn ein Block einstürzt, werden auch alle Blöcke darüber entfernt. Du erhältst nur für Blöcke Ressourcen, die die Drohne direkt ausgräbt. Alle bei einem Einsturz verlorenen Blöcke werden ohne Ertrag zerstört.

---

[Unterirdische Sinne](docs/unlocks/underground_senses.md)      [While-Schleife](docs/scripting/while.md)

[move()](functions/move)      [dig()](functions/dig)
