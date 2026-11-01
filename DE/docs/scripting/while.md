[<- Erstes Programm](docs/first_program.md) <right>[Geschwindigkeits-Upgrade ->](docs/unlocks/speed.md)
---
# While-Schleife
Du hast die `while`-Schleife und die Werte `True` und `False` freigeschaltet. Die `while`-Schleife führt den Schleifenkörper so lange aus, wie die Bedingung `True` ist.

`while condition:
	#Schleifenkörper`

Mach dir keine Sorgen über Endlosschleifen. Die Drohne kann zwar stecken bleiben, aber nicht das ganze Spiel zum Stillstand bringen. Du kannst das laufende Programm einfach stoppen und es erneut versuchen.

## Für Anfänger
Vielleicht hast du schon versucht, mehrere `harvest()`-Aufrufe hintereinander zu setzen:

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
harvest()
harvest()
harvest()
}}
Dies ermöglicht es dir, mehrmals in einem Programmlauf zu ernten.
Allerdings wäre es schön, mehr als dreimal zu ernten, und derselbe Code wird bei mehrfachem Wiederholen schnell unübersichtlich.
Die Lösung ist eine Schleife.
Eine Schleife ermöglicht es dir, denselben Code mehrmals auszuführen.

Die while-Schleife benötigt eine Bedingung, die ein logischer Wert ist, der nur einen von zwei Zuständen haben kann: `True` oder `False`.
Ein solcher Wert wird als boolescher Wert bezeichnet.

Die Schleife führt dann den Code innerhalb der Schleife aus, bis die Bedingung `False` ist.
Die while-Schleife sieht so aus:

`while condition:
	#Schleifenkörper
	#Schleifenkörper
	#...`
	
Wobei du "condition" durch einen booleschen Wert und `#loop body` durch das ersetzen musst, was du in der Schleife tun möchtest.

Es gibt zwei konstante boolesche Werte. Konstanten sind Werte, die sich während des Programms nie ändern.

Um einen konstanten booleschen Wert zu erstellen, schreibst du einfach `True` oder `False`.
Du könntest also entweder schreiben

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while False:
	do_a_flip()
}}
oder

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	do_a_flip()
}}
Die erste Schleife führt nie einen Salto aus, während die zweite endlos Saltos ausführt (eine Endlosschleife).

Normalerweise ist eine Endlosschleife keine gute Idee, da sie das Programm zum Stillstand bringt. In diesem Spiel gibt es jedoch Verzögerungen zwischen den Schleifendurchläufen. Die Drohne macht daher so lange Saltos, bis du sie manuell stoppst, indem du erneut auf den Ausführen-Button drückst.

Beachte, wie die Zeile nach dem Doppelpunkt eingerückt ist. Solche Einrückungen werden verwendet, um Codeblöcke zu trennen.
Drücke einfach die Tab-Taste, um eine Einrückung hinzuzufügen, und Umschalt + Tab (oder Rücktaste), um sie zu entfernen. Wenn mehrere Zeilen ausgewählt sind, werden Tab und Umschalt + Tab auf alle angewendet.

Hinweis: Wenn du das Spiel über Steam spielst, öffnet Umschalt + Tab stattdessen das Steam-Overlay. Du kannst die Tastenkombination zum Entfernen der Einrückung in den Spieloptionen oder die Tastenkombination für das Steam-Overlay in dessen Optionen ändern.

Hier werden `do_a_flip()` und `pet_the_piggy()` wiederholt aufgerufen, weil sie sich im eingerückten `while`-Block befinden. `harvest()` wird jedoch nie ausgeführt, da es nach diesem Block steht.
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	do_a_flip()
	pet_the_piggy()
harvest()
}}

---

[For-Schleife](docs/scripting/for.md)      [If](docs/scripting/if.md)      [Break](docs/scripting/break.md)      [Continue](docs/scripting/continue.md)      [Externer Editor](docs/external_editor.md)
