# Zbiory
Zbiory są jak [słowniki](docs/scripting/dicts.md), ale bez wartości. To po prostu nieuporządkowany zbiór kluczy. 

Tworzy się je jak słowniki, ale bez wartości.
`zbiór = {North, East, West}`

Użyj `set()`, aby utworzyć pusty zbiór. Zauważ, że `{}` tworzy pusty słownik.

Użyj `set.add(elem)`, aby dodać nowy element do zbioru.

Użyj `set.remove(elem)`, aby usunąć element ze zbioru.

Użyj `if elem in set:`, aby sprawdzić, czy zbiór zawiera dany element.

Użyj `for elem in set:`, aby iterować po wszystkich elementach w zbiorze.
Dla większych zbiorów operator `in` działa znacznie szybciej niż w przypadku listy.

Podobnie jak słowniki, zbiory są nieuporządkowane, więc nie ma gwarancji co do kolejności, w jakiej elementy są iterowane.

Ponadto elementy w zbiorach są unikalne, więc dodanie elementu, który już znajduje się w zbiorze, nie zmieni zbioru.