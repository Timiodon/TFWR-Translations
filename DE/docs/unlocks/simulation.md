# Simulation

Simulationen ermöglichen es dir, Code schnell zu testen, ohne den Zustand der echten Farm zu verändern.
Der Startzustand der Simulation kann frei gewählt werden, und wenn die Simulation endet, ist die echte Farm wieder in genau dem Zustand, in dem sie vor dem Start der Simulation war.

Die `simulate()`-Funktion wird verwendet, um eine Simulation zu starten.

die Datei, in der die Ausführung beginnen soll
`filename = "f1"`

starte mit allem freigeschaltet und voll aufgerüstet
`sim_unlocks = Unlocks`

starte mit 10000 Karotten und 50 Heu
`sim_items = {Items.Carrot : 10000, Items.Hay : 50}`

starte mit einer globalen Variable "a" mit dem Wert 13
`sim_globals = {"a" : 13}`

verwende einen festen Random-Seed
`seed = 0`

beschleunige die Simulation um den Faktor 64
`speedup = 64`

führe die Simulation aus
`run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)`

Die `simulate()`-Funktion gibt die Zeit in Sekunden zurück, die für die Simulation der angegebenen Startdatei benötigt wurde.

### Dateiname
Das erste Argument der `simulate()`-Funktion ist der Dateiname. Dies ist der Name, der oben im Codefenster angezeigt wird. Die Simulation führt die angegebene Datei so aus, als ob du den Ausführen-Button darauf geklickt hättest.

### Start-Freischaltungen
Alle Programmier-Features wie Schleifen, if-Anweisungen, Listen, dicts, ... bleiben immer freigeschaltet.

Das zweite Argument ermöglicht es dir anzugeben, mit welchen Freischaltungen/Upgrades die Simulation zusätzlich zu den Programmier-Features starten soll. Dies sollte eine Sequenz von Freischaltungen sein. Die Simulation startet mit allen Freischaltungen in der Sequenz, die auf ihr maximales Level aufgerüstet sind.

Wenn du ein anderes Upgrade-Level als das maximale angeben möchtest, kannst du ein Dictionary übergeben, das die Freischaltungen auf Upgrade-Levels abbildet. In diesem Fall entsprechen negative Werte dem maximalen Freischaltungslevel.

### Start-Items
Das dritte Argument ermöglicht es dir, ein Dictionary zu übergeben, das Items auf Zahlen abbildet. Es gibt an, mit welchen Items die Simulation starten soll.

### Start-Globals
Da die Simulation eine völlig neue Programmausführung startet, kannst du nicht auf Variablen aus dem Programm zugreifen, das die Simulation startet.
Es ist jedoch möglich, Werte mit dem vierten Argument an die Simulation zu übergeben. Dies ist ein dict, das Variablennamen in Form von Strings auf Werte abbildet. Diese Variablen werden dann dem globalen Scope der Ausführung innerhalb der Simulation hinzugefügt.

Beachte, dass dies alle Werte kopiert. Wenn du sie also innerhalb der Simulation veränderst, hat das keine Auswirkungen auf die ursprünglichen Werte außerhalb der Simulation. Es ist nicht möglich, andere Werte als die Laufzeit aus der Simulation zurückzugeben.

### Random-Seed
Das fünfte Argument ermöglicht es dir, den in der Simulation verwendeten Random-Seed anzugeben. Dies muss eine positive ganze Zahl sein. Negative Werte führen dazu, dass ein zufälliger Seed verwendet wird.

Der Random-Seed beeinflusst alles, von Pflanzenwachstumszeiten über Labyrinth-Layouts bis hin zu Wasserabfallzeiten. Wenn du dieselbe Simulation mehrmals mit demselben Random-Seed und denselben Startbedingungen startest, sollte das Ergebnis immer dasselbe sein.

### Speedup
Das sechste Argument ist der anfängliche Speedup der Simulation. Damit kannst du Dinge schnell testen. Wenn das Spiel mit der eingestellten Geschwindigkeit nicht mithalten kann, wird es automatisch langsamer.

Der Speedup hat keinerlei Einfluss auf das Ergebnis der Simulation. Er dient nur dazu, die Wartezeit zu verkürzen.