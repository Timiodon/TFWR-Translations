# Słowniki
Słowniki to struktura danych, która pozwala na mapowanie kluczy na wartości, podobnie jak prawdziwy słownik mapuje słowa na ich definicje, i można je bardzo szybko wyszukiwać.

Słownik można utworzyć w ten sposób:
`right_of = {North:East, East:South, South:West, West:North}`

Wyrażenie przed dwukropkiem to klucz, a wyrażenie po dwukropku to wartość, na którą mapuje klucz.
Powyższy słownik mapuje każdy kierunek na kierunek po jego prawej stronie.

Oto inny przykład, który mapuje pozycję drona na obiekt, nad którym się znajduje.
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

Dostęp do wartości mapowanej na klucz jest podobny do dostępu do elementu na liście:
`value = dict[key]`

Przykład:
`orientation = right_of[South]`
To ustawia `orientation` na `West`.

Możesz dodać nową parę klucz-wartość do słownika w ten sposób:
`dict[key] = value`

Przykład:
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
To aktualizuje obiekt przechowywany dla bieżącej pozycji.

Klucze są unikalne, więc dodanie klucza, który już istnieje w słowniku, nadpisze poprzednią wartość.

Użyj `dict.pop(key)`, aby usunąć parę klucz-wartość ze słownika `dict`.

`key in dict` zwraca `True`, jeśli `key` jest kluczem w słowniku `dict`, i `False` w przeciwnym razie.
Więc możesz użyć `if key in dict:`, aby sprawdzić, czy `dict` zawiera dany klucz.

Umieszczenie słownika w pętli for pozwala na iterację po wszystkich kluczach:
`for key in dict:
	value = dict[key]`

Nie ma gwarancji co do kolejności, w jakiej klucze są iterowane.

Zobacz również [Zbiory](docs/scripting/sets.md)