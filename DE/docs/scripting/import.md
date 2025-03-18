# Importieren
Wenn du deinen gesamten Code in eine einzige Datei packst, wird es schnell unübersichtlich. 
`import`-Anweisungen ermöglichen es dir, Funktionen und globale Variablen aus einer anderen Datei zu importieren.

`import dateiname`

Dies ist die einfachste Form einer Import-Anweisung. Sie gibt dir Zugriff auf alles, was in der Datei mit dem Namen `dateiname` definiert ist. Jedes Fenster im Spiel ist eine Datei, und der Dateiname ist der Name, der oben im Fenster angezeigt wird.

Hier ist ein Beispiel mit zwei Dateien:
Datei mit dem Namen helper:
`x = 0

def say_hello():
    print("hello from helper")`

Eine andere Datei:
`import helper
helper.say_hello()
helper.x += 1`

Hier führt `import helper` die Datei mit dem Namen `helper` aus und gibt dir Zugriff auf alle ihre globalen Variablen.
Du kannst dann auf Variablen und Funktionen innerhalb des importierten Moduls mit dem `.`-Operator zugreifen.
In diesem Beispiel ruft `helper.say_hello()` die Funktion `say_hello()` innerhalb von helper auf, und die letzte Zeile erhöht die globale Variable x.

Du kannst auch die globalen Variablen aus dem importierten Modul in den aktuellen Gültigkeitsbereich verschieben, in dem die Import-Anweisung ausgeführt wird, indem du die `from`-Syntax verwendest.

`from helper import *`
Importiert alle globalen Variablen aus helper.

oder

`from helper import say_hello`
Importiert nur die angegebenen globalen Variablen aus helper.

Dies importiert auch die helper-Datei, aber anstatt sie über eine Variable namens `helper` zu erreichen, werden globale Variablen aus `helper` entpackt und direkt im lokalen Gültigkeitsbereich zugewiesen.

`from helper import say_hello
say_hello()`

Diese Form des Imports wird normalerweise nicht empfohlen, da sie nicht gut funktioniert, wenn zwei Dateien sich gegenseitig importieren, und du möglicherweise versehentlich Variablen in der importierenden Datei überschreibst, aufgrund von Namenskollisionen.

# Wie es wirklich funktioniert

## Kurzfassung
Importe können ziemlich unintuitiv sein, aber die meisten Probleme können vermieden werden, indem du bei der `import datei`-Syntax bleibst, anstatt `from datei import`, und alles, was keine globale Definition ist, in
`if __name__ == "__main__":` einpackst.

## Import-Nebenwirkungen
Beim ersten Import einer Datei wird die gesamte Datei ausgeführt und gibt dir dann Zugriff auf alle Variablen, die während der Ausführung definiert wurden.
Wenn du dieselbe Datei noch einmal importierst, wird einfach das im Cache gespeicherte Modul vom ersten Mal zurückgegeben.

Das bedeutet, dass Import-Anweisungen Nebenwirkungen haben können. Wenn du eine Datei importierst, die `harvest()` aufruft, wird tatsächlich während des Imports geerntet. Aber wenn du sie erneut importierst, wird nicht erneut geerntet, weil die Datei nur einmal ausgeführt wird.

Es gibt eine Möglichkeit, solche Nebenwirkungen mit der `__name__`-Variable zu vermeiden. Diese Variable wird automatisch auf `"__main__"` gesetzt, wenn eine Datei direkt ausgeführt wird, und auf den Namen der Datei, wenn eine Datei über `import` ausgeführt wird.
Es gilt als gute Praxis, jeden Code, den du nicht ausführen möchtest, wenn die Datei importiert wird, in einen `if __name__ == "__main__":`-Block zu setzen.

Eine gängige Dateistruktur in Python ist, den Code, der ausgeführt werden soll, wenn die Datei ausgeführt wird, in eine `main()`-Funktion zu packen. So hast du eine klare Unterscheidung zwischen lokalen Variablen (innerhalb von `main()` definiert) und globalen Variablen, die importiert werden können (außerhalb von `main()` definiert).

`a_global_variable = "global"

def main():
    a_local_variable = "local"
    # Aktionen ausführen

if __name__ == "__main__":
    main()`

## Import-Zyklen
Was passiert, wenn Datei `a` Datei `b` importiert und Datei `b` Datei `a` importiert?

Datei `a`:
`import b
x = 0`

Datei `b`:
`import a
def f():
    print(a.x)`

Das wird problemlos funktionieren. Angenommen, keine der beiden Dateien sind bereits geladen, und jemand anderes führt `import a` aus.

-`a` läuft bis zur `import b`-Zeile.
-`b` läuft bis zur `import a`-Zeile.
-Das Modul `a` existiert bereits, enthält aber noch nicht `x`, da es nur die `import b`-Zeile erreicht hat.
-`b` speichert eine Referenz auf das halbgeladene Modul `a` in einer Variable namens `a`.
-`b` führt die `def`-Anweisung aus und speichert die Funktion `f()`.
-`a` läuft weiter und initialisiert `x`.

Wenn jemand `b.f()` aufruft, wird korrekt `0` ausgegeben, weil das Modul `a`, auf das `b` verweist, jetzt vollständig geladen ist.

Betrachten wir nun dasselbe Codebeispiel mit der `from`-Syntax.

Datei `a`:
`from b import *
x = 0`

Datei `b`:
`from a import *
def f():
    print(x)`

-`a` läuft bis zur `from b import *`-Zeile.
-`b` läuft bis zur `from a import *`-Zeile.
-Das Modul `a` existiert bereits, wurde aber noch nicht vollständig ausgeführt.
-`b` entpackt alles, was derzeit in `a` ist, in seinen eigenen globalen Gültigkeitsbereich. Zu diesem Zeitpunkt enthält `a` nichts, da es noch nicht zur `x = 0`-Zeile gelangt ist, daher wird nichts importiert.
-`b` führt die `def`-Anweisung aus und speichert die Funktion `f()`.
-`a` läuft weiter und initialisiert `x`.

Wenn jetzt jemand `b.f()` aufruft, wird es einen Fehler geben, dass `x` im aktuellen Gültigkeitsbereich nicht existiert. Das liegt daran, dass `b` diesmal keine Referenz auf das noch ladende `a` hat und keine Definitionen sieht, die nach dem Import hinzugefügt wurden.