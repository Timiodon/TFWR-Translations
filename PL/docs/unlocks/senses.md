# Zmysły
Dron teraz widzi!

Funkcje `get_pos_x()` i `get_pos_y()` zwracają bieżącą pozycję x i y drona. Na pozycji startowej obie wynoszą `0`. Pozycja x rośnie o `1` co pole w kierunku `East`, a pozycja y rośnie o `1` co pole w kierunku `North`.

`num_items(item)` zwraca, ile masz danego przedmiotu.
Na przykład `num_items(Items.Hay)` zwraca, ile masz siana.

`get_entity_type()` i `get_ground_type()` zwracają typ entity lub podłoża, które znajduje się pod dronem.

Zrób fikołka, jeśli jesteś nad krzakiem:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

Słowo kluczowe `None` jest teraz również odblokowane! `None` to wartość, która reprezentuje brak wartości.
Na przykład, funkcja, która nie ma instrukcji `return`, faktycznie zwróci `None`.

`get_entity_type()` zwraca `None`, jeśli pod dronem nie ma żadnego entity.
