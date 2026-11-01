[<- Eisen](docs/unlocks/iron.md)
---
# Eisensuche
Vielleicht ist dir schon aufgefallen, dass Eisenerzadern manchmal schwer zu finden sind. Du könntest einfach auf gut Glück herumgraben, aber es gibt eine bessere Methode: Da Eisen magnetisch ist, können wir es aus einiger Entfernung aufspüren.

Der Befehl `prospect_iron()` tut genau das. `prospect_iron()` gibt die Richtung (`North`, `East`, `South` oder `West`) zurück, in die sich die Drohne bewegen müsste, um dem nächstgelegenen Eisenerz einen Schritt näher zu kommen.

Die Ausführung des Befehls kostet 1 Kohle.

`prospect_iron()` gibt `None` zurück, wenn sich die Drohne bereits direkt über dem nächstgelegenen Eisenerz befindet, wenn du nicht genügend Kohle für den Befehl hast oder wenn sich kein Eisen in Reichweite befindet.

Mit dem folgenden Code kannst du dich dem nächsten Eisenerz um einen Schritt nähern:

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
    "items": [{"item": "coal", "n": 100}],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 1,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 50,
    "seed": 8,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "quartz"]
}
#SETUP
jump(Unlocks.Iron)
#CODE
# Sicherstellen, dass die Erzsuche eine Richtung zurückgibt
if prospect_iron() != None:
    move(prospect_iron()) # Der Eisenader nähern
}}

Du solltest diesen Code vielleicht mithilfe einer Variable optimieren, denn momentan ruft er `prospect_iron()` zweimal auf und kostet daher 2 Kohle.

## Entfernungsberechnung
Die Entfernung zum nächstgelegenen Eisenerz wird anhand der Anzahl der Schritte berechnet, welche die Drohne zurücklegen muss. Befindet sich ein Eisenerz 2 Blöcke östlich und 3 Blöcke nördlich der Drohne, entspricht das einer Entfernung von 5, da die Drohne fünf Schritte bräuchte, um dorthin zu gelangen.

Auch Graben zählt als Schritt. Liegt das Eisen zusätzlich 7 Blöcke tief unter der Erde, entspricht das einer Entfernung von 12: Die Drohne braucht fünf Schritte, um sich über dem Eisen zu positionieren, und muss dann siebenmal graben, um es zu erreichen.

---

[Eisen](docs/unlocks/iron.md)      [Unterirdische Sinne](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [prospect_iron()](functions/prospect_iron)
