# Import
Den gesamten Code in eine einzige Datei zu packen, wird schnell unüberschaubar.
`import`-Anweisungen ermöglichen es dir, Funktionen und globale Variablen aus einer anderen Datei zu importieren.

`import filename`

Dies ist die einfachste Form der Import-Anweisung. Sie gibt dir Zugriff auf alles, was in der Datei namens `filename` definiert ist. Jedes Fenster im Spiel ist eine Datei, und der Dateiname ist der Name, der oben im Fenster angezeigt wird.

Hier ist ein Beispiel mit zwei Dateien:
Datei namens helper:
`x = 0

def say_hello():
    print("hello from helper")`

Eine andere Datei:
`import helper
helper.say_hello()
helper.x += 1`

Hier führt `import helper` die Datei namens `helper` aus und gibt dir Zugriff auf alle ihre globalen Variablen.
Du kannst dann mit dem `.`-Operator auf Variablen und Funktionen innerhalb des importierten Moduls zugreifen.
In diesem Beispiel ruft `helper.say_hello()` die Funktion `say_hello()` in der helper-Datei auf, und die letzte Zeile erhöht die globale Variable x.

Du kannst die globalen Variablen aus dem importierten Modul auch mit der `from`-Syntax in den aktuellen Geltungsbereich verschieben, in dem die Import-Anweisung ausgeführt wird.

`from helper import *`
Importiert alle globalen Variablen von helper.

oder

`from helper import say_hello`
Importiert nur die angegebenen globalen Variablen von helper.

Dies importiert auch die helper-Datei, aber anstatt über eine Variable namens `helper` darauf zuzugreifen, entpackt es die globalen Variablen aus `helper` und weist sie direkt im lokalen Geltungsbereich zu.

`from helper import say_hello
say_hello()`

Diese Form des Imports wird normalerweise nicht empfohlen, da sie nicht gut funktioniert, wenn zwei Dateien sich gegenseitig importieren, und du versehentlich Variablen in der importierenden Datei aufgrund von Namenskollisionen überschreiben könntest.

# Wie es wirklich funktioniert

## TLDR
Imports können ziemlich unintuitiv sein, aber die meisten Probleme lassen sich vermeiden, indem man sich an die `import file`-Syntax anstelle von `from file import` hält und alles, was keine globale Definition ist, in
`if __name__ == "__main__":` einbettet.

## Import-Seiteneffekte
Wenn du eine Datei zum ersten Mal importierst, wird die gesamte Datei ausgeführt und du erhältst Zugriff auf alle Variablen, die während der Ausführung definiert wurden.
Wenn du dieselbe Datei erneut importierst, wird einfach das zwischengespeicherte Modul vom ersten Mal zurückgegeben.

Das bedeutet, dass Import-Anweisungen Seiteneffekte haben können. Wenn du eine Datei importierst, die `harvest()` aufruft, wird während des Imports tatsächlich geerntet. Aber wenn du sie erneut importierst, wird nicht noch einmal geerntet, weil die Datei nur einmal ausgeführt wird.

Es gibt eine Möglichkeit, solche Seiteneffekte zu vermeiden, indem man die `__name__`-Variable verwendet. Dies ist eine Variable, die automatisch auf `"__main__"` gesetzt wird, wenn eine Datei direkt ausgeführt wird, und auf den Namen der Datei, wenn eine Datei durch `import` ausgeführt wird.
Es gilt als gute Praxis, jeglichen Code, der beim Importieren der Datei nicht ausgeführt werden soll, in einen `if __name__ == "__main__":`-Block zu packen.

Eine übliche Dateistruktur in Python ist es, den Code, der beim Ausführen der Datei ausgeführt werden soll, in eine `main()`-Funktion zu packen. Auf diese Weise hast du eine klare Unterscheidung zwischen lokalen Variablen (innerhalb von `main()` definiert) und globalen Variablen, die importiert werden können (außerhalb von `main()` definiert).

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

Das wird problemlos funktionieren. Nehmen wir an, keine der beiden Dateien ist bereits geladen, und jemand anderes führt `import a` aus.

-`a` wird bis zur Zeile `import b` ausgeführt.
-`b` wird bis zur Zeile `import a` ausgeführt.
-Das Modul `a` existiert bereits, enthält aber `x` noch nicht, da es erst die Zeile `import b` erreicht hat.
-`b` speichert eine Referenz auf das halb geladene Modul `a` in einer Variable namens `a`.
-`b` führt die `def`-Anweisung aus und speichert die Funktion `f()`.
-`a` wird weiter ausgeführt und initialisiert `x`.

Wenn jemand `b.f()` aufruft, wird korrekterweise `0` ausgegeben, weil das Modul `a`, auf das `b` eine Referenz hat, nun vollständig geladen ist.

Betrachten wir nun denselben Code mit der `from`-Syntax.

Datei `a`:
`from b import *
x = 0`

Datei `b`:
`from a import *
def f():
    print(x)`

-`a` wird bis zur Zeile `from b import *` ausgeführt.
-`b` wird bis zur Zeile `from a import *` ausgeführt.
-Das Modul `a` existiert bereits, wurde aber noch nicht vollständig ausgeführt.
-`b` entpackt alles, was sich derzeit in `a` befindet, in seinen eigenen globalen Geltungsbereich. An diesem Punkt enthält `a` nichts, da es die Zeile `x = 0` noch nicht erreicht hat, also wird nichts importiert.
-`b` führt die `def`-Anweisung aus und speichert die Funktion `f()`.
-`a` wird weiter ausgeführt und initialisiert `x`.

Wenn jetzt jemand `b.f()` aufruft, erhält er einen Fehler, dass `x` im aktuellen Geltungsbereich nicht existiert. Das liegt daran, dass `b` diesmal keine Referenz auf das noch ladende `a` hat und Definitionen, die nach dem Import hinzugefügt wurden, nicht sieht.