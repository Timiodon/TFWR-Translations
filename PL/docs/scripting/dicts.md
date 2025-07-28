# Słowniki (Dictionaries)
Słowniki to struktura danych, która pozwala mapować klucze na wartości w taki sam sposób, w jaki prawdziwy słownik mapuje słowa na ich definicje, i można je bardzo szybko wyszukiwać.

Słownik można utworzyć w ten sposób:
`right_of = {North:East, East:South, South:West, West:North}`

Wyrażenie przed dwukropkiem to klucz, a wyrażenie po dwukropku to wartość, do której mapuje klucz.
Powyższy słownik mapuje każdy kierunek na kierunek po jego prawej stronie.

Oto kolejny, który mapuje pozycję drona na entity, nad którym się znajduje.
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

Dostęp do wartości przypisanej do klucza jest podobny do dostępu do elementu na liście:
`value = dict[key]`

Przykład:
`orientation = right_of[South]`
To ustawia `orientation` na `West`.

Możesz dodać nową parę klucz-wartość do słownika w ten sposób:
`dict[key] = value`

Przykład:
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
To aktualizuje entity przechowywane dla bieżącej pozycji.

Klucze są unikalne, więc dodanie klucza, który już istnieje w słowniku, nadpisze poprzednią wartość.

Użyj `dict.pop(key)`, aby usunąć parę klucz-wartość z `dict`.

`key in dict` daje w wyniku `True`, jeśli `key` jest kluczem w `dict`, a `False` w przeciwnym razie.
Możesz więc użyć `if key in dict:`, aby sprawdzić, czy `dict` zawiera dany klucz.

Umieszczenie słownika w pętli for pozwala na iterację przez wszystkie klucze:
`for key in dict:
	value = dict[key]`

Nie ma gwarancji co do kolejności, w jakiej klucze są iterowane.

Zobacz także [Sety (Sets)](docs/scripting/sets.md)