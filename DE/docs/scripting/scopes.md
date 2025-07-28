# Namens-Scopes
Scopes bestimmen, auf welche Variablen von wo aus zugegriffen werden kann. Ein Scope ist im Grunde eine Zuordnung von Namen zu Werten.
Sie funktionieren im Grunde genauso wie in Python.

Es gibt einen globalen Scope, und jede Funktion hat einen lokalen Scope.
Wenn du eine Variable definierst, wird sie dem aktuellen Scope hinzugefügt.
Alles außerhalb einer Funktionsdefinition wird als Teil des globalen Scopes betrachtet.

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
Holt die in `f` gespeicherte Funktion aus dem globalen Scope und ruft sie auf.

`print(y)`
Diese print-Anweisung im globalen Scope wirft einen Error, da `y` nie im globalen Scope deklariert wurde, also können wir sie hier nicht lesen.
Sie existierte nur im lokalen Scope von `f`.

## Das global-Schlüsselwort
Standardmäßig binden alle Variablen in Funktionen an den lokalen Scope, auch wenn eine Variable mit demselben Namen im globalen Scope existiert.

`x = 0

def f():
    x = 1
f()
print(x)`

Dieser Code gibt `0` aus, weil das lokale `x` innerhalb von `f` nicht dieselbe Variable ist wie das globale `x`, daher bleibt das globale `x` unverändert. Das ist wichtig, denn sonst könnte ein Funktionsaufruf versehentlich eine globale Variable überschreiben, die zufällig denselben Namen wie eine lokale Variable dieser Funktion hat.

Wenn du in eine globale Variable schreiben möchtest, musst du dies explizit mit dem `global`-Schlüsselwort tun.

`x = 0

def f():
    global x
    x = 1
f()
print(x)`

In diesem Beispiel bindet `global x` `x` an die darüber definierte globale Variable `x`. Dies wird nun `1` ausgeben.
Beachte, dass das Ändern globaler Variablen normalerweise der erste Schritt zu Spaghetti-Code ist, bei dem jeder Teil des Programms jeden anderen Teil des Programms beeinflusst, also übertreibe es nicht.

## Schleifen und Verzweigungen
Schleifen und Verzweigungen erstellen keine eigenen Scopes, daher kann alles, was in ihnen deklariert wird, auch außerhalb verwendet werden.

`for i in range(3):
    pass
print(i)`

Dies wird `2` ausgeben, weil die letzte Iteration der `for`-Schleife `i` den Wert `2` zugewiesen hat.