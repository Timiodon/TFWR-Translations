# Zmysły
Dron teraz widzi! 

Funkcje `get_pos_x()` i `get_pos_y()` zwracają aktualną pozycję x i y drona. Na pozycji startowej obie wynoszą `0`. Pozycja x rośnie o `1` co pole w kierunku `East`, a pozycja y rośnie o `1` co pole w kierunku `North`.

`num_items(item)` zwraca, ile sztuk danego przedmiotu posiadasz.
Na przykład `num_items(Items.Hay)` zwraca, ile masz siana.

`get_entity_type()` i `get_ground_type()` zwracają typ obiektu lub podłoża, które znajduje się pod dronem.

Wykonaj obrót, jeśli jesteś nad krzakiem:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

Słowo kluczowe `None` jest teraz również odblokowane! `None` to wartość, która reprezentuje brak wartości.
Na przykład, funkcja, która nie ma instrukcji `return`, w rzeczywistości zwróci `None`.

`get_entity_type()` zwraca `None`, jeśli pod dronem nie ma żadnego obiektu.


Jeśli chcesz dowiedzieć się, ile masz danego odblokowania, użyj funkcji `num_unlocked(unlock)`.

Na przykład, `num_unlocked(Unlocks.Speed)` zwróci liczbę posiadanych ulepszeń prędkości.

`num_unlocked(Unlocks.Senses)` zwróci `1`, jeśli zmysły są odblokowane, i `0`, jeśli nie są.

Możesz również użyć `num_unlocked()` na przedmiotach, obiektach lub podłożach. Zwróci to `1`, jeśli jest odblokowane, w przeciwnym razie `0`.

Uważaj, `num_unlocked(Unlocks.Carrots)` zwróci liczbę razy, kiedy zostało odblokowane/ulepszone.
`num_unlocked(Items.Carrot)` zwróci tylko `0` lub `1`. (To samo dotyczy innych roślin)