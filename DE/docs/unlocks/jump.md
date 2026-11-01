[<- Kohle](docs/unlocks/coal.md)
---
# Springen
Deine Drohne hat den Befehl `jump()` freigeschaltet. Übergib dazu eine Freischaltung als Argument, beispielsweise `Unlocks.Iron`.

Mit diesem Befehl kannst du bestimmte im Boden verborgene Ressourcen anvisieren und sofort zu ihnen hinunterspringen. Das ist besonders zum Debuggen oder zum Überspringen bis zu einer kürzlich verpassten Erzader nützlich.

Nach dem Sprung sollte die Zielressource höchstens 3 Blöcke unter der obersten Blockoberfläche liegen. `jump()` kann pro Programmausführung nur einmal verwendet werden. Weitere Sprungversuche führen zu einem Fehler.

Das folgende Beispiel springt zu [Reis](docs/unlocks/rice.md) hinunter, findet die Tonschicht und pflanzt eine Reihe Reisterrassen:
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
    "items": [{"item": "hay", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms"],
    "starting_chunk": 0
}
#CODE
# In die Nähe von Reis springen
jump(Unlocks.Rice)

# Eine Reihe Reisterrassen pflanzen
for i in range(get_world_size()):
    # Der Sprung ist ungenau, also die letzten Blöcke weggraben
    while get_ground_type() != Grounds.Clay:
        dig()

    plant(Entities.Rice)

    move(East)
}}

## Unterstützte Freischaltungen
`jump()` funktioniert nur mit den folgenden Bergbau-Freischaltungen:
- Kohle
- Eisen
- Quarz
- Reis
- Versteinerte Kürbisse
- Spezialböden
- Pyramide
- Schatzkarte
- Pilze
- Dynamit

---

[jump()](functions/jump)
