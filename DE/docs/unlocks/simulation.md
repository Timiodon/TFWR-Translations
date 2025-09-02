# Simulation

Simulationen ermöglichen es dir, Code schnell zu testen, ohne den Zustand der echten Farm zu verändern.
Der Startzustand der Simulation kann frei gewählt werden, und wenn die Simulation endet, ist die echte Farm wieder in genau dem Zustand, in dem sie vor dem Start der Simulation war.

Die `simulate()`-Funktion wird verwendet, um eine Simulation zu starten.

Die Datei, in der die Ausführung starten soll
`filename = "f1"`

Starte mit allem freigeschaltet und voll aufgerüstet
`sim_unlocks = Unlocks`

Starte mit 10000 Karotten und 50 Heu
`sim_items = {Items.Carrot : 10000, Items.Hay : 50}`

Starte mit einer globalen Variable "a" mit dem Wert 13
`sim_globals = {"a" : 13}`

Verwende einen festen Zufalls-Seed
`seed = 0`

Beschleunige die Simulation um den Faktor 64
`speedup = 64`

Führe die Simulation aus
`run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)`

Die `simulate()`-Funktion gibt die Zeit in Sekunden zurück, die benötigt wurde, um die angegebene Startdatei zu simulieren.

### Dateiname
Das erste Argument der `simulate`-Funktion ist der Dateiname. Dies ist der Name, der oben im Codefenster angezeigt wird. Die Simulation führt die angegebene Datei so aus, als ob du den Ausführen-Button darauf geklickt hättest.

### Start-Freischaltungen
Alle Programmier-Features wie Schleifen, if-Anweisungen, Listen, Dicts,... bleiben immer freigeschaltet. 

Das zweite Argument ermöglicht es dir, anzugeben, mit welchen Freischaltungen/Upgrades die Simulation zusätzlich zu den Programmier-Features starten soll. Dies sollte eine Sequenz von Freischaltungen sein. Die Simulation startet mit allen Freischaltungen in der Sequenz, die auf ihre maximale Stufe aufgerüstet sind.

Wenn du eine andere Upgrade-Stufe als die maximale angeben möchtest, kannst du ein Dictionary übergeben, das die Freischaltungen auf Freischalt-Stufen abbildet. In diesem Fall entsprechen negative Werte der maximalen Freischalt-Stufe.

### Start-Items
Das dritte Argument ermöglicht es dir, ein Dictionary zu übergeben, das Items auf Zahlen abbildet. Es gibt die Items an, mit denen die Simulation gestartet werden soll.

### Start-Globals
Da die Simulation eine komplett neue Programmausführung startet, kannst du nicht auf Variablen aus dem Programm zugreifen, das die Simulation startet.
Es ist jedoch möglich, Werte mit dem vierten Argument an die Simulation zu übergeben. Dies ist ein Dict, das Variablennamen in Form von Strings auf Werte abbildet. Diese Variablen werden dann zum globalen Geltungsbereich der Ausführung innerhalb der Simulation hinzugefügt.

Beachte, dass dies alle Werte kopiert, daher beeinflusst eine Änderung innerhalb der Simulation nicht die ursprünglichen Werte außerhalb der Simulation. Es ist nicht möglich, andere Werte als die Laufzeit aus der Simulation zurückzugeben.

### Zufalls-Seed
Das fünfte Argument ermöglicht es dir, den in der Simulation verwendeten Zufalls-Seed anzugeben. Dies muss eine positive ganze Zahl sein. Negative Werte führen dazu, dass ein zufälliger Seed verwendet wird.

Der Zufalls-Seed beeinflusst alles, von den Wachstumszeiten der Pflanzen über Labyrinth-Layouts bis hin zu den Wasserzerfallszeiten. Wenn du dieselbe Simulation mehrmals mit demselben Zufalls-Seed und denselben Startbedingungen startest, sollte das Ergebnis immer dasselbe sein.

### Speedup
Das sechste Argument ist der anfängliche Speedup der Simulation. Dies ermöglicht es dir, Dinge schnell zu testen. Wenn das Spiel mit der eingestellten Geschwindigkeit nicht mithalten kann, wird es automatisch langsamer.

Der Speedup beeinflusst das Ergebnis der Simulation in keiner Weise. Er dient nur dazu, die Wartezeit zu verkürzen.