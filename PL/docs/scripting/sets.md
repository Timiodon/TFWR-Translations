# Sety
Sety są jak [słowniki (dictionaries)](docs/scripting/dicts.md), ale bez wartości. To po prostu nieuporządkowany zbiór kluczy.

Tworzy się je jak słowniki, ale bez wartości.
`set = {North, East, West}`

Użyj `set()`, aby utworzyć pusty set. Zauważ, że `{}` tworzy pusty słownik (dictionary).

Użyj `set.add(elem)`, aby dodać nowy element do setu.

Użyj `set.remove(elem)`, aby usunąć element z setu.

Użyj `if elem in set:`, aby sprawdzić, czy set zawiera element.

Użyj `for elem in set:`, aby iterować po wszystkich elementach w secie.
Dla większych setów operator `in` działa znacznie szybciej niż na liście.

Podobnie jak słowniki, sety są nieuporządkowane, więc nie ma gwarancji co do kolejności, w jakiej elementy są iterowane.

Ponadto, elementy w setach są unikalne, więc dodanie elementu, który już znajduje się w secie, nie zmieni go.