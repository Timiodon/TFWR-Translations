# 1.0 ist endlich da!
Nach über dreieinhalb Jahren stetiger Entwicklung, mehr als 20 Updates und eurem großartigen Feedback ist der Early Access nun endlich zu Ende.

## Was ist neu in 1.0?
- Mehrere Drohnen, um deine Farmarbeit zu maximieren
- Ein überarbeiteter Forschungsbaum mit exponentiellerem Fortschritt
- 60 Achievements, um deine Fähigkeiten zu testen
- Das Freischalten bestimmter Achievements gibt deiner Drohne besondere Hüte
- Eine komplette Sound-Überarbeitung
- Ein neuer Musiktitel
- Quality-of-Life-Verbesserungen und diverse Fixes
- Breaking Changes: Upgrades werden teilweise zurückgesetzt. Das Wiederverwenden von Labyrinthen funktioniert etwas anders.

Vielen Dank an euch alle für die Unterstützung von The Farmer Was Replaced vom Early Access bis zur Vollversion.
Ich kann es kaum erwarten zu sehen, wie ihr die mehreren Drohnen auf kreative und clevere Weise einsetzt!
-Timon

Schaut auch gerne auf unserem Discord vorbei:
[Discord](https://discord.com/invite/kj33cJkeJn)

## Vollständige Patch Notes
Breaking Changes:
-Aufgrund der Überarbeitung des Forschungsbaums sind die Upgrade-Stufen alter Spielstände nicht mehr gültig. Das Spiel wird alle Upgrades auf ein vernünftiges Niveau zurücksetzen, wenn du einen alten Spielstand öffnest.
-Wenn du Labyrinthe wiederverwendest, musst du jetzt zuerst den Schatz neu positionieren und dann die Position messen, anstatt zuerst zu messen und dann neu zu positionieren.

Gameplay:
-Tooltips mit hilfreichen Informationen hinzugefügt, wenn du mit der Maus über Felder auf der Farm fährst.
-Die Verwendung von `measure()` an beliebiger Stelle im Labyrinth gibt jetzt immer die Position des aktuellen Schatzes zurück. Du musst den Schatz nicht mehr gezielt messen.
-Es gibt jetzt eine `can_move()`-Funktion für das Labyrinth.
-Kürbisse skalieren jetzt bis zu 6x6 statt 5x5.
-Das Austrocknungsverhalten des Bodens hat sich leicht geändert. Anstatt alle 0,8 bis 1,2 Sekunden um 1% auszutrocknen, hat jedes Bodenfeld jetzt eine 10%ige Chance, alle 0,1 Sekunden auszutrocknen.
-Die Wachstumszeit von Kakteen beträgt jetzt immer genau 1 Sekunde.
-Kürbisse hinterlassen jetzt einen toten Kürbis, um anzuzeigen, dass sie gestorben sind.
-`pet_the_piggy()` hinzugefügt.
-`num_unlocked()` wird jetzt bereits mit Senses freigeschaltet.

Audio:
-Der Ton wurde komplett überarbeitet.
-Es gibt jetzt Musik, wenn du das Spiel startest!

Grafik:
-Die Grafik des Forschungsbaums wurde komplett überarbeitet.
-Das Inventar-Panel oben links auf dem Bildschirm hat jetzt einen schönen visuellen Effekt beim Aufsammeln von Items.
-Kakteen sind jetzt braun, wenn sie nicht richtig sortiert sind, um es sichtbarer zu machen.
-Pflanzen sind jetzt sofort nach dem Pflanzen sichtbar, auch wenn sie noch nicht gewachsen sind.

Code-Editor:
-Doppelklick auf Bezeichner mit Unterstrichen wählt jetzt den gesamten Bezeichner aus.
-Wenn die Option "Tabs zu Leerzeichen" ausgeschaltet ist, werden Einrückungs-Leerzeichen jetzt in Tabs umgewandelt.
-Das Zoomen ist jetzt viel flüssiger.
-Der Code-Vervollständiger berücksichtigt jetzt Importe korrekt und kann Vorschläge aus anderen Dateien machen.
-Unterschiedliche Cursor für das Bearbeiten von Text und das Ändern der Fenstergröße hinzugefügt.
-Debugger-Schritte basieren jetzt auf der Codezeile anstatt auf Simulations-Ticks.

Sonstiges:
-Du kannst jetzt Vergleichsoperatoren wie in Python verketten.
-`get_cost(Entities.Hedge)` und `get_cost(Entities.Treasure)` geben jetzt die Kosten eines 1x1 Labyrinths zurück.
-Eine Einstellung für die Auflösung hinzugefügt.
-Eine Einstellung hinzugefügt, um die blinkenden Hervorhebungen während der Code-Ausführung auszuschalten.
-Die Code-Ausführung wurde weiter optimiert, sodass das Spiel flüssiger läuft, während Code ausgeführt wird.
-Eine "HUD umschalten"-Tastenbelegung hinzugefügt.

Fehlerbehebungen:
-Einige der häufigsten Fälle behoben, in denen Code-Hervorhebungen durch andere Fenster sichtbar waren.
-Problem behoben, bei dem Aktionen wie das Pflügen das Austrocknen von Wasser beeinflussten.
-Probleme mit Tastenbelegungen auf Nicht-US-Tastaturen behoben.
-Problem behoben, bei dem sich das Sparschwein manchmal sehr weit von der Farm entfernte.
-Problem behoben, dass Dünger ausgewachsene Pflanzen nicht infizierte.
-Problem behoben, dass `set_world_size(get_world_size())` die Drohnenposition zurücksetzte.
-Problem bei einer Interaktion zwischen Simulation und Dinosaurier behoben, das zum Zurücklassen vieler Äpfel führte.
-Problem behoben, dass sich Fehlermeldungen nach dem Minimieren und Öffnen des Menüs verschoben.
-Problem behoben, dass Fehlermeldungen während des Tippens erschienen.

Breaking Changes aus älteren Patches, die du vielleicht verpasst hast:
-Funktionen, die in anderen Dateien (Fenstern im Spiel) definiert sind, werden nicht mehr implizit importiert. Du musst jetzt explizite Import-Anweisungen wie in Python freischalten und verwenden (Siehe die Import-Freischaltung).
-`Items.Bones` wurde in `Items.Bone` umbenannt, damit alle Items im Singular stehen.
-`Entities.Carrots` wurde in `Entities.Carrot` umbenannt, damit alle Entities im Singular stehen.
-`Grounds.Turf` wurde in `Grounds.Grassland` umbenannt, um es verständlicher zu machen.
-`Items.Water_Tank` wurde in `Items.Water` umbenannt, da die Funktion zum Nachfüllen des Tanks entfernt wurde.
-`Unlocks.Benchmark` wurde durch `Unlocks.Timing` ersetzt.
-`get_op_count()` wurde in `get_tick_count()` umbenannt.
-`set_farm_size()` wurde in `set_world_size()` umbenannt, um mit `get_world_size()` konsistent zu sein.
-`get_companion()` gibt jetzt ein Tupel der Form (entity, (x, y)) anstelle einer Liste zurück.
-`trade()` wurde aus dem Spiel entfernt.