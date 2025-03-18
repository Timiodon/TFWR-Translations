# Variablen
Variablen kann man sich als benannte Behälter vorstellen, die einen Wert speichern können.
Der `=` Operator wird verwendet, um eine Variable zu deklarieren und einen Wert in ihr zu speichern.

`variable_name = value`

Die linke Seite des Operators ist der Variablenname. Du kannst ihm jeden Namen geben, den du möchtest.
Die rechte Seite ist ein Ausdruck, dessen resultierender Wert in der Variable gespeichert wird.

Deklariere eine Variable mit dem Namen `a` und speichere den Wert `5` darin:
`a = 5`
Deklariere eine Variable mit dem Namen `b` und speichere den Rückgabewert von `can_harvest()` darin:
`b = can_harvest()`

Verwechsele den `=` Operator nicht mit dem `==` Operator.
Der `==` Operator prüft, ob zwei Werte gleich sind, und gibt `True` oder `False` zurück.
Der `=` Operator weist den Wert auf der rechten Seite dem Namen auf der linken Seite zu.

Nachdem einer Variablen ein Wert zugewiesen wurde, kannst du sie im Code verwenden, um den gespeicherten Wert abzurufen.

`a = 5
for i in range(a):
	do_a_flip()`

Die obige Schleife wird 5 Mal ausgeführt, weil `a` auf `5` gesetzt wurde.
Das `i` in der `for` Schleife ist ebenfalls eine Variable, die automatisch bei jedem Durchlauf der Schleife den aktuellen Wert der Sequenz zugewiesen bekommt. (Es muss nicht `i` genannt werden, du kannst ihr jeden gültigen Variablennamen geben.)

Variablen ermöglichen dir auch, dasselbe mit einer while-Schleife zu tun:

`a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1`

Dies macht dasselbe wie die for-Schleife oben. Wir müssen `i` nur manuell erhöhen.
Beachte, dass wir zur Erhöhung von `i` es auf seinen eigenen Wert plus `1` setzen. Den Wert einer Variable basierend auf ihrem vorherigen Wert zu ändern, ist sehr verbreitet. 
Es kann mit diesen Operatoren abgekürzt werden: `+=, -=, *=, /=, %=`

`i = i + 1` ist dasselbe wie `i += 1`
`a = a / 3` ist dasselbe wie `a /= 3`