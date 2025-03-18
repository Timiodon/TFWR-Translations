# Sets
Sets są jak [dictionaries](docs/scripting/dicts.md), ale bez wartości. To po prostu nieuporządkowany zbiór kluczy.

Tworzy się je tak jak dictionaries, ale bez wartości.
`set = {North, East, West}`

Użyj `set()`, aby stworzyć pusty set. Pamiętaj, że `{}` tworzy pusty dictionary.

Użyj `set.add(elem)`, aby dodać nowy element do seta.

Użyj `set.remove(elem)`, aby usunąć element z seta.

Użyj `if elem in set:`, aby sprawdzić, czy set zawiera dany element.

Użyj `for elem in set:`, aby przeiterować wszystkie elementy w secie. 
Dla większych setów operator `in` działa znacznie szybciej niż w przypadku list.

Podobnie jak dictionaries, sets są nieuporządkowane, więc nie ma gwarancji co do kolejności, w jakiej elementy będą iterowane.

Dodatkowo, elementy w setach są unikalne, więc dodanie elementu, który już jest w secie, nie zmieni seta.