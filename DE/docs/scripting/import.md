# Import
Deinen ganzen Code in eine einzige Datei zu packen, wird schnell unübersichtlich. 
`import`-Anweisungen ermöglichen es dir, Funktionen und globale Variablen aus einer anderen Datei zu importieren.
So funktioniert's in einem Screenshot:
![](ImportsInOnePicture400)

Hier führt `import module2` die Datei namens `module2` aus und gibt dir Zugriff auf all ihre globalen Variablen.
Du kannst dann mit dem `.`-Operator auf Variablen und Funktionen innerhalb des importierten Moduls zugreifen.
In diesem Beispiel ruft `module2.print_x()` also `print_x()` in `module2` auf.

### Weiterlesen nicht nötig

Du kannst auch die globalen Variablen aus dem importierten Modul mit der `from`-Syntax in den aktuellen Geltungsbereich verschieben, in dem die `import`-Anweisung ausgeführt wird.

`from module2 import print_x
print_x()`
Importiert nur die angegebenen globalen Variablen aus `module2`.

oder

`from module2 import *
print_x()`
Importiert alle globalen Variablen aus `module2`.

Dies importiert auch die `module2`-Datei, aber anstatt über eine Variable namens `module2` darauf zuzugreifen, entpackt es die globalen Variablen aus `module2` und weist sie direkt im lokalen Geltungsbereich zu.

Diese Form des Imports wird normalerweise nicht empfohlen, da sie nicht gut funktioniert, wenn sich zwei Dateien gegenseitig importieren, und du versehentlich Variablen in der importierenden Datei aufgrund von Namenskollisionen überschreiben könntest. Es ist sicherer, die `from`-Syntax zu vermeiden, wenn du nicht weißt, was du tust.

# Wie es wirklich funktioniert

## TLDR
Imports können ziemlich unintuitiv sein, aber die meisten Probleme lassen sich vermeiden, indem man sich an die `import file`-Syntax anstatt `from file import` hält und alles, was keine globale Definition ist, in
`if __name__ == "__main__":`
packt.

## Nebenwirkungen von Imports
Wenn du eine Datei zum ersten Mal importierst, wird die gesamte Datei ausgeführt und du erhältst Zugriff auf alle Variablen, die während der Ausführung definiert wurden.
Wenn du dieselbe Datei erneut importierst, wird sie einfach das zwischengespeicherte Modul vom ersten Mal zurückgeben.

Das bedeutet, dass `import`-Anweisungen Nebenwirkungen haben können. Wenn du eine Datei importierst, die `harvest()` aufruft, wird während des Imports tatsächlich geerntet. Aber wenn du sie erneut importierst, wird nicht erneut geerntet, weil die Datei nur einmal ausgeführt wird.

Es gibt eine Möglichkeit, solche Nebenwirkungen mit der `__name__`-Variable zu vermeiden. Dies ist eine Variable, die automatisch auf `"__main__"` gesetzt wird, wenn eine Datei direkt ausgeführt wird, und auf den Namen der Datei, wenn eine Datei über `import` ausgeführt wird.
Es gilt als gute Praxis, Code, der beim Importieren der Datei nicht ausgeführt werden soll, in einen `if __name__ == "__main__":`-Block zu packen.

Eine übliche Dateistruktur in Python ist es, den Code, der beim Ausführen der Datei ausgeführt werden soll, in eine `main()`-Funktion zu packen. Auf diese Weise hast du eine klare Unterscheidung zwischen lokalen Variablen (innerhalb von `main()` definiert) und globalen Variablen, die importiert werden können (außerhalb von `main()` definiert).

`a_global_variable = "global"

def main():
    a_local_variable = "local"
    # do things

if __name__ == "__main__":
    main()`

## Import-Zyklen
Was passiert, wenn Datei `a` die Datei `b` importiert und Datei `b` die Datei `a` importiert?

Datei `a`:
`import b
x = 0`

Datei `b`:
`import a
def f():
    print(a.x)`

Das wird gut funktionieren. Nehmen wir an, keine der beiden Dateien ist bereits geladen und jemand führt `import a` aus.

-`a` wird bis zur Zeile `import b` ausgeführt.
-`b` wird bis zur Zeile `import a` ausgeführt.
-Das Modul `a` existiert bereits, enthält aber `x` noch nicht, da es erst die Zeile `import b` erreicht hat.
-`b` speichert eine Referenz auf das halb geladene Modul `a` in einer Variable namens `a`.
-`b` führt die `def`-Anweisung aus und speichert die Funktion `f()`.
-`a` wird weiter ausgeführt und initialisiert `x`.

Wenn jemand `b.f()` aufruft, wird korrekterweise `0` ausgegeben, da das Modul `a`, auf das `b` eine Referenz hat, nun vollständig geladen ist.

Betrachten wir nun den gleichen Code mit der `from`-Syntax.

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
-`b` entpackt alles, was sich derzeit in `a` befindet, in seinen eigenen globalen Geltungsbereich. Zu diesem Zeitpunkt enthält `a` noch nichts, da es die Zeile `x = 0` noch nicht erreicht hat, also wird nichts importiert.
-`b` führt die `def`-Anweisung aus und speichert die Funktion `f()`.
-`a` wird weiter ausgeführt und initialisiert `x`.

Wenn jetzt jemand `b.f()` aufruft, erhält er einen Fehler, dass `x` im aktuellen Geltungsbereich nicht existiert. Das liegt daran, dass `b` dieses Mal keine Referenz auf das noch ladende `a` hat und Definitionen nicht sieht, die nach dem Import hinzugefügt wurden.