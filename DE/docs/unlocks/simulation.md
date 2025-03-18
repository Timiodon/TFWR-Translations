# Simulation

Simulationen ermöglichen es dir, Code schnell zu testen, ohne den Zustand der echten Farm zu verändern.
Der Anfangszustand der Simulation kann frei gewählt werden, und wenn die Simulation endet, wird die echte Farm genau in dem Zustand sein, in dem sie sich vor dem Start der Simulation befand.

Die `simulate()` Funktion wird verwendet, um eine Simulation zu starten.

die Datei, in der die Ausführung beginnen soll
`filename = "f1"`

beginne mit allem freigeschaltet und komplett aufgerüstet
`sim_unlocks = Unlocks`

beginne mit 10000 Karotten und 50 Heu
`sim_items = {Items.Carrot : 10000, Items.Hay : 50}`

beginne mit einer globalen Variable "a" mit einem Wert von 13
`sim_globals = {"a" : 13}`

verwende einen festen Zufallswert (random seed)
`seed = 0`

beschleunige die Simulation um den Faktor 64
`speedup = 64`

führe die Simulation aus
`run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)`

Die `simulate()` Funktion gibt die Zeit zurück, in Sekunden, die benötigt wurde, um die angegebene Startdatei zu simulieren.

### Dateiname
Das erste Argument der simulate Funktion ist der Dateiname. Dies ist der Name, der oben im Code-Fenster angezeigt wird. Die Simulation wird die angegebene Datei ausführen, als hättest du den Ausführen-Button darauf geklickt.

### Startfreischaltungen
Alle Programmierfunktionen wie Schleifen, if-Abfragen, Listen, dicts,... bleiben immer freigeschaltet.

Das zweite Argument ermöglicht es dir, anzugeben, mit welchen Freischaltungen/Aufrüstungen die Simulation zusätzlich zu den Programmierfunktionen beginnen soll. Dies sollte eine Sequenz von Freischaltungen sein. Die Simulation startet mit allen Freischaltungen in der Sequenz, die auf ihr maximales Level aufgerüstet sind.

Wenn du ein anderes Aufrüstungslevel als das Maximum angeben möchtest, kannst du ein dictionary übergeben, das die Freischaltungen zu Freischaltungsleveln zuordnet. In diesem Fall entsprechen negative Werte dem maximalen Freischaltungslevel.

### Startgegenstände
Das dritte Argument ermöglicht es dir, ein dictionary zu übergeben, das Gegenstände auf Zahlen abbildet. Es spezifiziert die Gegenstände, mit denen die Simulation beginnen soll.

### Start-Globals
Da die Simulation eine völlig neue Programmausführung startet, kannst du nicht auf Variablen aus dem Programm zugreifen, das die Simulation startet.
Es ist jedoch möglich, der Simulation Werte über das vierte Argument zu übergeben. Dies ist ein dict, das Variablennamen in Form von Strings zu Werten abbildet. Diese Variablen werden dann dem globalen scope der Ausführung innerhalb der Simulation hinzugefügt.

Beachte, dass dies alle Werte kopiert, sodass deren Veränderung innerhalb der Simulation die ursprünglichen Werte außerhalb der Simulation nicht beeinflusst. Es ist nicht möglich, andere Werte als die Laufzeit aus der Simulation zurückzugeben.

### Zufallswert (random seed)
Das fünfte Argument ermöglicht es dir, den in der Simulation verwendeten Zufallswert zu spezifizieren. Dieser muss eine positive ganze Zahl sein. Negative Werte führen dazu, dass ein Zufallswert verwendet wird.

Der Zufallswert beeinflusst alles, von Pflanzenwachstum- und Labyrinthlayouts bis hin zu Verfallzeiten von Wasser. Wenn du dieselbe Simulation mit demselben Zufallswert und denselben Startbedingungen mehrmals startest, sollte das Ergebnis immer dasselbe sein.

### Beschleunigung
Das sechste Argument ist die Anfangsbeschleunigung der Simulation. Dies ermöglicht es dir, Dinge schnell zu testen. Wenn das Spiel nicht in der Lage ist, die eingestellte Geschwindigkeit einzuhalten, wird es automatisch langsamer.

Die Beschleunigung beeinflusst in keiner Weise das Ergebnis der Simulation. Sie dient nur dazu, die Wartezeit zu verkürzen.