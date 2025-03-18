# Dictionaries
Dictionaries to struktura danych, która pozwala na mapowanie kluczy do wartości w ten sam sposób, w jaki prawdziwy słownik mapuje słowa do ich definicji i można je bardzo szybko wyszukiwać.

Dictionary można stworzyć w ten sposób:
`rotation = {North:East, East:South, South:West, West:North}`

Wyrażenie przed dwukropkiem to klucz, a wyrażenie po dwukropku to wartość, do której klucz jest mapowany. Powyższy dictionary mapuje każdy kierunek na kierunek po jego prawej stronie.

Oto inny przykład, który mapuje pozycję drona na entity, nad którym się znajduje.
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

Dostęp do wartości mapowanej do klucza jest podobny do dostępu do elementu na liście:
`value = dict[key]`

Przykład:
`orientation = rotation[South]`
To ustawia `orientation` na `West`.

Możesz dodać nową parę klucz-wartość do dictionary w ten sposób:
`dict[key] = value`

Przykład:
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
To aktualizuje entity przechowywane dla bieżącej pozycji.

Klucze są unikalne, więc dodanie klucza, który już istnieje w dictionary, nadpisze poprzednią wartość.

Użyj `dict.pop(key)`, aby usunąć parę klucz-wartość z `dict`.

`key in dict` zwraca `True`, jeśli `key` jest kluczem w `dict`, i `False` w przeciwnym wypadku. Możesz więc użyć `if key in dict:`, aby sprawdzić, czy `dict` zawiera dany klucz.

Umieszczenie dictionary w pętli for pozwala na iterację wszystkich kluczy:
`for key in dict:
	value = dict[key]`

Nie ma gwarancji co do kolejności, w jakiej klucze są iterowane.

Zobacz także [Sets](docs/scripting/sets.md)