# Bäume
[Trees](objects/tree) sind eine bessere Möglichkeit, Holz zu bekommen als Büsche. Sie geben jeweils 5 Holz. Wie Büsche können sie auf Gras oder Erde gepflanzt werden.

Bäume mögen etwas Platz und wenn man sie direkt nebeneinander pflanzt, verlangsamt sich ihr Wachstum. Die Wachstumszeit verdoppelt sich für jeden Baum, der sich auf einem direkt nördlichen, östlichen, westlichen oder südlichen Feld befindet. Wenn du also auf jedem Feld einen Baum pflanzt, dauert es `2*2*2*2 = 16` mal länger, bis sie wachsen.

<spoiler=show> Der `%` Operator kann hier nützlich sein. Denk daran, dass der `%` Operator den Rest der Division zurückgibt. Gerade Zahlen, die durch `2` geteilt werden, haben einen Rest von `0` und ungerade Zahlen, die durch `2` geteilt werden, haben einen Rest von `1`.
Du kannst also überprüfen, ob eine Zahl gerade ist, so:

`def is_even(n):
	return n % 2 == 0`

Dies gibt `True` zurück, wenn n gerade ist, und `False`, wenn nicht.
</spoiler>