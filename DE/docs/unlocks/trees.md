# Bäume
[Bäume](objects/tree) sind eine bessere Möglichkeit, Holz zu bekommen als Büsche. Sie geben jeweils 5 Holz. Wie Büsche können sie auf Gras oder Erde gepflanzt werden.

Bäume mögen etwas Platz und wenn man sie direkt nebeneinander pflanzt, verlangsamt sich ihr Wachstum. Die Wachstumszeit verdoppelt sich für jeden Baum, der sich auf einem Feld direkt nördlich, östlich, westlich oder südlich von ihm befindet. Wenn du also auf jedes Feld Bäume pflanzt, brauchen sie `2*2*2*2 = 16`-mal länger zum Wachsen.

<spoiler=anzeigen> Der `%`-Operator kann hier nützlich sein. Erinnere dich daran, dass der `%`-Operator den Rest der Division zurückgibt. Gerade Zahlen geteilt durch `2` haben einen Rest von `0` und ungerade Zahlen geteilt durch `2` haben einen Rest von `1`.
Du kannst also so überprüfen, ob eine Zahl gerade ist:

`def is_even(n):
	return n % 2 == 0`

Das gibt `True` zurück, wenn n gerade ist, und `False`, wenn nicht.
</spoiler>