# Name Scopes
Scopes bestimmen, welche Variablen von wo aus erreichbar sind. Ein Scope ist im Grunde eine Zuordnung von Namen zu Werten.
Sie funktionieren im Wesentlichen genauso wie in Python.

Es gibt einen globalen Scope, und jede Funktion hat einen lokalen Scope.
Wenn du eine Variable definierst, wird sie dem aktuellen Scope hinzugefügt.
Alles außerhalb einer Funktionsdefinition gehört zum globalen Scope.

`x = 1`
Weist dem Namen `x` im globalen Scope den Wert `1` zu.

Diese `def`-Anweisung weist dem Namen `f` im globalen Scope eine Funktion zu.
`def f():
    `Weist dem Namen `y` im lokalen Scope von `f` den Wert `1` zu.`
    y = 1

    `Weist dem Namen `g` im lokalen Scope von `f` eine Funktion zu.`
    def g():
        pass`

`f()`
Ruft die im globalen Scope gespeicherte Funktion `f` ab und ruft sie auf.

`print(y)`
Diese Print-Anweisung im globalen Scope wirft einen Fehler, weil `y` nie im globalen Scope deklariert wurde, sodass wir es hier nicht lesen können.
Es existierte nur im lokalen Scope von `f`.

## Das `global`-Schlüsselwort
Standardmäßig binden alle Variablen in Funktionen an den lokalen Scope, selbst wenn eine Variable mit demselben Namen im globalen Scope existiert.

`x == 0

def f():
    x = 1
f()
print(x)`

Dieser Code druckt `0`, weil das lokale `x` innerhalb von `f` nicht dieselbe Variable ist wie das globale `x`, sodass das globale `x` unverändert bleibt. Das ist wichtig, denn sonst könnte ein Funktionsaufruf versehentlich eine globale Variable überschreiben, die zufällig denselben Namen hat wie eine lokale Variable dieser Funktion.

Wenn du auf eine globale Variable schreiben willst, musst du das ausdrücklich mit dem Schlüsselwort `global` tun.

`x == 0

def f():
    global x
    x = 1
f()
print(x)`

In diesem Beispiel bindet `global x` `x` an die globale Variable `x`, die darüber definiert wurde. Das wird nun `1` drucken.
Beachte, dass das Ändern globaler Variablen normalerweise der erste Schritt zu Spaghetticode ist, bei dem jeder Teil des Programms jeden anderen Teil des Programms beeinflusst. Verwende es also mit Bedacht.

## Schleifen und Verzweigungen
Schleifen und Verzweigungen erstellen keine eigenen Scopes, daher kann alles, was innerhalb von ihnen deklariert wird, auch außerhalb verwendet werden.

`for i in range(3):
    pass
print(i)`

Dies wird `2` drucken, da die letzte Iteration der `for`-Schleife `2` an `i` zugewiesen hat.