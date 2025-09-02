# Namensbereiche (Scopes)
Scopes (Geltungsbereiche) bestimmen, welche Variablen von wo aus zugegriffen werden können. Ein Scope ist im Grunde eine Zuordnung von Namen zu Werten.
Sie funktionieren im Grunde genauso wie in Python.

Es gibt einen globalen Geltungsbereich, und jede Funktion hat einen lokalen Geltungsbereich.
Wenn du eine Variable definierst, wird sie dem aktuellen Geltungsbereich hinzugefügt.
Alles außerhalb einer Funktionsdefinition wird als Teil des globalen Geltungsbereichs betrachtet.

`x = 1`
Weist dem Namen `x` im globalen Geltungsbereich den Wert `1` zu.

Diese `def`-Anweisung weist dem Namen `f` im globalen Geltungsbereich eine Funktion zu.
`def f():
    `Weist dem Namen `y` im lokalen Geltungsbereich von `f` den Wert `1` zu.`
    y = 1

    `Weist dem Namen `g` im lokalen Geltungsbereich von `f` eine Funktion zu.`
    def g():
        pass`

`f()`
Ruft die in `f` gespeicherte Funktion aus dem globalen Geltungsbereich ab und führt sie aus.

`print(y)`
Diese print-Anweisung im globalen Geltungsbereich löst einen Fehler aus, da `y` nie im globalen Geltungsbereich deklariert wurde und wir es hier nicht lesen können.
Es existierte nur im lokalen Geltungsbereich von `f`.

## Das global-Schlüsselwort
Standardmäßig binden alle Variablen in Funktionen an den lokalen Geltungsbereich, auch wenn eine Variable mit demselben Namen im globalen Geltungsbereich existiert.

`x = 0

def f():
    x = 1
f()
print(x)`

Dieser Code gibt `0` aus, weil das lokale `x` innerhalb von `f` nicht dieselbe Variable ist wie das globale `x`, sodass das globale `x` unverändert bleibt. Das ist wichtig, weil sonst ein Funktionsaufruf versehentlich eine globale Variable überschreiben könnte, die zufällig denselben Namen hat wie eine lokale Variable dieser Funktion.

Wenn du auf eine globale Variable schreiben möchtest, musst du dies explizit mit dem `global`-Schlüsselwort tun.

`x = 0

def f():
    global x
    x = 1
f()
print(x)`

In diesem Beispiel bindet `global x` die Variable `x` an die globale Variable `x`, die darüber definiert ist. Dies wird nun `1` ausgeben.
Beachte, dass das Ändern globaler Variablen normalerweise der erste Schritt in Richtung Spaghetticode ist, bei dem jeder Teil des Programms jeden anderen Teil des Programms beeinflusst, also verwende es nicht übermäßig.

## Schleifen und Verzweigungen
Schleifen und Verzweigungen erstellen keine eigenen Geltungsbereiche, daher kann alles, was in ihnen deklariert wird, auch außerhalb verwendet werden.

`for i in range(3):
    pass
print(i)`

Dies gibt `2` aus, weil die letzte Iteration der `for`-Schleife `i` den Wert `2` zugewiesen hat.