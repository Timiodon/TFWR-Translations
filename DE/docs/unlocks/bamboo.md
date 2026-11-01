[<- Reis](docs/unlocks/rice.md) <right>[Farbige Blöcke ->](docs/unlocks/debug_place.md)
<right>[Pyramiden ->](docs/unlocks/pyramid.md)
---
# Bambus
Bambus ist eine Pflanze, die nach oben wächst. Damit er weiterwächst, muss deine Drohne regelmäßig seine braunen Früchte pflücken. Das schaffen wir mit dem neu freigeschalteten Befehl `hover`.

Bambus muss auf gepflügtem Boden (`Grounds.Soil`) gepflanzt werden und kostet Reis.

Der folgende Code pflanzt Bambus und wartet, bis er bis zur ersten Frucht gewachsen ist.
{{codeexample
{
"camera_position": {"x": -1, "y": 0, "z": 10},
"show_image": true,
"image_size": {"x": 800, "y": 500},
"show_code": true,
"show_inventory": true,
"show_output": false,
"collapsing": true,
"autoplay": false,
"items": [{"item": "rice", "n": 100}],
"world_size": {"x": 4, "y": 4},
"execution_speed": 2,
"action_ticks": 200,
"operation_ticks": 200,
"seed": 1,
"exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
move(East) # wegfliegen, damit der Bambus wachsen kann
}}

## Früchte
Bambus wächst genau 1 Block pro Sekunde.

Bambus bildet alle paar Blöcke Früchte. Dann hört er auf zu wachsen, und du musst mit deiner Drohne hineinfliegen, um die Frucht zu zerstören. Bambus kann bis zu seiner dritten Frucht in die Höhe wachsen. Danach wächst er nicht mehr höher, auch wenn du sie pflückst.

Um Früchte zu pflücken, musst du zuerst mit `hover` auf die richtige Höhe schweben. Fliege dann mit `move` in die Frucht hinein, um sie zu pflücken, und mit `move` wieder weg, damit der Bambus weiterwachsen kann.

Mit `measure()` kannst du prüfen, auf welcher Höhe die nächste Bambusfrucht erscheint. `measure()` zählt ab `0`, daher bringt `hover(measure())` deine Drohne auf die Höhe der nächsten Frucht.

{{codeexample
{
"camera_position": {"x": -1, "y": 0, "z": 10},
"show_image": true,
"image_size": {"x": 800, "y": 500},
"show_code": true,
"show_inventory": true,
"show_output": false,
"collapsing": true,
"autoplay": false,
"items": [{"item": "rice", "n": 100}],
"world_size": {"x": 4, "y": 4},
"execution_speed": 2,
"action_ticks": 200,
"operation_ticks": 200,
"seed": 1,
"exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
hover(measure()) # so schweben, dass die Drohne neben der Frucht ist

move(East) # wegfliegen und auf das Wachstum warten
for i in range(3):
    do_a_flip()

move(West) # Frucht pflücken
move(East) # wieder wegfliegen
}}

## Schweben
Der Befehl `hover` nimmt ein Argument entgegen: die Schwebehöhe als Zahl von `0` bis `18`. Die Standardschwebehöhe der Drohne ist `1`. `hover` kann die Drohne nicht nach unten in feste Entitäten bewegen. Wenn sie sich bereits über Bambus befindet, kannst du sie mit `hover(0)` also nicht hineinfliegen lassen.

`hover` gibt `True` zurück, wenn die Drohne die angegebene Schwebehöhe erreicht hat, andernfalls `False`.

Zusätzlich gibt es den Befehl `get_hover`, der die aktuelle Schwebehöhe der Drohne zurückgibt.

Wenn du beim Schweben `dig`, `harvest` oder `plant` verwendest, kehrt die Drohne zu ihrer Standardschwebehöhe (`1`) zurück.

Außerdem wird `get_pos_z()` nicht vom Schweben beeinflusst. Es gibt immer die z-Position des Blocks unter der Drohne zurück.

## Bambus ernten
Du kannst zwar `harvest()` verwenden, empfohlen wird aber, mit der Drohne auf Schwebehöhe `0` (`hover(0)`) in den Bambus hineinzufliegen. So erntest du die gesamte Pflanze auf einmal.

Wenn du den Bambus ernten möchtest, ohne ihn zu zerstören, kannst du auf einer beliebigen Höhe mit `move` hineinfliegen, zum Beispiel mit `hover(3)`. Dadurch werden alle Bambusstücke ab dieser Höhe geerntet, während die Pflanze am Leben bleibt. Teilweise geernteter Bambus bildet seine Früchte erneut, die du dann wieder pflücken musst.

In beiden Fällen entspricht dein Ertrag dem Quadrat der Anzahl zerstörter Bambusstücke. Je höher der Bambus, desto größer also dein Ertrag.

---

[Statistiken](docs/stats.md)      [For-Schleife](docs/scripting/for.md)      [Variablen](docs/scripting/variables.md)      [If](docs/scripting/if.md)      [Funktionen](docs/scripting/functions.md)      [Reis](docs/unlocks/rice.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [measure()](functions/measure)
