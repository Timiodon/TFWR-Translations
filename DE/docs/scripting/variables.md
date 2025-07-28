# Variablen
Variablen kann man sich als benannte Behälter vorstellen, die einen Wert enthalten können.
Der `=`-Operator wird verwendet, um eine Variable zu deklarieren und einen Wert darin zu speichern.

`variablen_name = wert`

Die linke Seite des Operators ist der Variablenname. Du kannst ihm jeden beliebigen Namen geben.
Die rechte Seite ist ein Ausdruck, dessen resultierender Wert in der Variable gespeichert wird.

Deklariere eine Variable namens `a` und speichere den Wert `5` darin:
`a = 5`
Deklariere eine Variable namens `b` und speichere den Rückgabewert von `can_harvest()` darin:
`b = can_harvest()`

Verwechsle den `=`-Operator nicht mit dem `==`-Operator.
Der `==`-Operator prüft, ob zwei Werte gleich sind, und gibt `True` oder `False` zurück.
Der `=`-Operator weist dem Namen auf der linken Seite den Wert auf der rechten Seite zu.

Nachdem einer Variable ein Wert zugewiesen wurde, kannst du sie im Code verwenden, um den darin enthaltenen Wert abzurufen

`a = 5
for i in range(a):
	do_a_flip()`

Die obige Schleife wird 5 Mal ausgeführt, weil `a` auf `5` gesetzt ist.
Das `i` in der `for`-Schleife ist auch eine Variable, der bei jeder Iteration der Schleife automatisch der aktuelle Wert der Sequenz zugewiesen wird. (Sie muss nicht `i` heißen, du kannst ihr jeden gültigen Variablennamen geben.)

Variablen ermöglichen es dir auch, dasselbe mit einer while-Schleife zu tun:

`a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1`

Dies tut dasselbe wie die for-Schleife oben. Wir müssen i nur manuell erhöhen.
Beachte, dass wir, um i zu erhöhen, es auf seinen eigenen Wert plus `1` setzen. Den Wert einer Variable basierend auf ihrem vorherigen Wert zu ändern, ist sehr verbreitet.
Es kann mit diesen Operatoren abgekürzt werden: `+=, -=, *=, /=, %=`

`i = i + 1` ist dasselbe wie `i += 1`
`a = a / 3` ist dasselbe wie `a /= 3`
