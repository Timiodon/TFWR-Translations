# Import
Deinen ganzen Code in eine einzige Datei zu packen, wird schnell unübersichtlich.
`import`-Anweisungen erlauben es dir, Funktionen und globale Variablen aus einer anderen Datei zu importieren.

`import dateiname`

Dies ist die einfachste Form einer Import-Anweisung. Sie gibt dir Zugriff auf alles, was in der Datei namens `dateiname` definiert ist. Jedes Fenster im Spiel ist eine Datei, und der Dateiname ist der Name, der oben im Fenster angezeigt wird.

Hier ist ein Beispiel mit zwei Dateien:
Datei namens `helper`:
`x = 0

def say_hello():
    print("hallo von helper")`

Eine andere Datei:
`import helper
helper.say_hello()
helper.x += 1`

Hier führt `import helper` die Datei namens `helper` aus und gibt dir Zugriff auf alle ihre Globals.
Du kannst dann mit dem `.`-Operator auf Variablen und Funktionen innerhalb des importierten Moduls zugreifen.
In diesem Beispiel ruft `helper.say_hello()` `say_hello()` innerhalb von `helper` auf und die letzte Zeile erhöht die globale Variable `x`.

Du kannst auch die Globals aus dem importierten Modul in den aktuellen Scope verschieben, in dem die Import-Anweisung ausgeführt wird, indem du die `from`-Syntax verwendest.

`from helper import *`
Importiert alle Globals von `helper`.

oder

`from helper import say_hello`
Importiert nur die angegebenen Globals von `helper`.

Dies importiert auch die `helper`-Datei, aber anstatt über eine Variable namens `helper` darauf zuzugreifen, entpackt es Globals aus `helper` und weist sie direkt im lokalen Scope zu.

`from helper import say_hello
say_hello()`

Diese Form des Imports wird normalerweise nicht empfohlen, weil sie nicht gut funktioniert, wenn sich zwei Dateien gegenseitig importieren, und du versehentlich Variablen in der importierenden Datei aufgrund von Namenskollisionen überschreiben könntest.

# Wie es wirklich funktioniert

## TLDR
Imports können ziemlich unintuitiv sein, aber die meisten Probleme können vermieden werden, indem man bei der `import datei`-Syntax anstelle von `from datei import` bleibt und alles, was keine globale Definition ist, in
`if __name__ == "__main__":`
einschließt.

## Import-Nebeneffekte
Wenn du eine Datei zum ersten Mal importierst, wird die gesamte Datei ausgeführt und du erhältst Zugriff auf alle Variablen, die während der Ausführung definiert wurden.
Wenn du dieselbe Datei erneut importierst, wird nur das zwischengespeicherte Modul vom ersten Mal zurückgegeben.

Das bedeutet, dass Import-Anweisungen Nebeneffekte haben können. Wenn du eine Datei importierst, die `harvest()` aufruft, wird sie während des Imports tatsächlich ernten. Aber wenn du sie erneut importierst, wird sie nicht erneut ernten, weil die Datei nur einmal ausgeführt wird.

Es gibt eine Möglichkeit, solche Nebeneffekte mit der `__name__`-Variable zu vermeiden. Dies ist eine Variable, die automatisch auf `"__main__"` gesetzt wird, wenn eine Datei direkt ausgeführt wird, und auf den Namen der Datei, wenn eine Datei über `import` ausgeführt wird.
Es gilt als gute Praxis, jeden Code, der nicht beim Importieren der Datei ausgeführt werden soll, in einen `if __name__ == "__main__":`-Block zu packen.

Eine übliche Dateistruktur in Python ist es, den Code, der ausgeführt werden soll, wenn die Datei gestartet wird, in eine `main()`-Funktion zu packen. Auf diese Weise hast du eine klare Unterscheidung zwischen lokalen Variablen (innerhalb von `main()` definiert) und globalen Variablen, die importiert werden können (außerhalb von `main()` definiert).

`a_global_variable = "global"

def main():
    a_local_variable = "local"
    # do things

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

Das wird gut funktionieren. Nehmen wir an, keine der beiden Dateien ist bereits geladen, und jemand anderes führt `import a` aus.

-`a` läuft bis zur Zeile `import b`.
-`b` läuft bis zur Zeile `import a`.
-Das Modul `a` existiert bereits, enthält aber `x` nicht, weil es nur die Zeile `import b` erreicht hat.
-`b` speichert eine Referenz auf das halb geladene Modul `a` in einer Variable namens `a`.
-`b` führt die `def`-Anweisung aus und speichert die Funktion `f()`.
-`a` läuft weiter und initialisiert `x`.

Wenn jemand `b.f()` aufruft, wird es korrekt `0` ausgeben, weil das Modul `a`, auf das `b` eine Referenz hat, jetzt vollständig geladen ist.

Betrachten wir nun denselben Code mit der `from`-Syntax.

Datei `a`:
`from b import *
x = 0`

Datei `b`:
`from a import *
def f():
    print(x)`

-`a` läuft bis zur Zeile `from b import *`.
-`b` läuft bis zur Zeile `from a import *`.
-Das Modul `a` existiert bereits, wurde aber noch nicht vollständig ausgeführt.
-`b` entpackt alles, was sich gerade in `a` befindet, in seinen eigenen globalen Scope. Zu diesem Zeitpunkt enthält `a` nichts, da es die Zeile `x = 0` noch nicht erreicht hat, also wird nichts importiert.
-`b` führt die `def`-Anweisung aus und speichert die Funktion `f()`.
-`a` läuft weiter und initialisiert `x`.

Wenn jemand jetzt `b.f()` aufruft, erhält er einen Error, dass `x` im aktuellen Scope nicht existiert. Das liegt daran, dass `b` diesmal keine Referenz auf das noch ladende `a` hat und keine Definitionen sieht, die nach dem Import hinzugefügt wurden.