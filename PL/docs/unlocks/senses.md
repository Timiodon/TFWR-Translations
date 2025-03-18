# Zmysły
Dron potrafi teraz widzieć!

Funkcje `get_pos_x()` i `get_pos_y()` zwracają aktualną pozycję x i y drona. Na początku obie mają wartość `0`. Pozycja x zwiększa się o `1` na każdej pozycji w stronę `East`, a pozycja y zwiększa się o `1` na każdej pozycji w stronę `North`.

`num_items(item)` zwraca ilość posiadanych przedmiotów.
Na przykład, `num_items(Items.Hay)` zwraca ile masz siana.

`get_entity_type()` i `get_ground_type()` zwracają typ entity lub ziemi, która znajduje się pod dronem.

Zrób flip, jeśli jesteś nad krzakiem:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

Słowo kluczowe `None` również jest teraz dostępne! `None` to wartość, która reprezentuje brak wartości.
Na przykład, funkcja, która nie ma instrukcji `return`, faktycznie zwróci `None`.

`get_entity_type()` zwraca `None`, jeśli pod dronem nie ma żadnej entity.