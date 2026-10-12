[<- Zmienne](docs/scripting/variables.md) <right>[Słowniki ->](docs/scripting/dicts.md)
---
# Listy
Listy to łatwy sposób na przechowywanie wielu wartości w jednej zmiennej.
Możesz tworzyć nowe listy w ten sposób:

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
some_list = [2, True, Items.Hay]
print(some_list)
}}

Lista zawiera teraz wartości `2`, `True` i `Items.Hay`.
Lista może być również pusta:

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
empty_list = []
print(empty_list)
}}

Możesz uzyskać dostęp do elementu listy za pomocą jego indeksu. Indeks to `0` dla pierwszego elementu, `1` dla drugiego, `2` dla trzeciego i tak dalej.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 1}, {"item": "wood", "n": 1}],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
till()
#CODE
entities = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(entities[1])
}}

Możesz iterować po liście za pomocą pętli `for`. Poniższy przykład sumuje wszystkie elementy listy.

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
numbers = [4, 7, 2, 5]
sum = 0
for number in numbers:
	sum += number
print(sum)
}}

Poniższe metody list pozwalają na dodawanie i usuwanie elementów:

`elements.append(elem)` dodaje element na koniec listy:

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
numbers = [2, 6, 12]
numbers.append(7)
print(numbers)
}}

`elements.remove(elem)` usuwa pierwsze wystąpienie elementu z listy:

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
numbers = [1, 2, 4, 2]
numbers.remove(2)
print(numbers)
}}

`elements.insert(index, elem)` wstawia element na podanym indeksie:

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
some_list = [Entities.Tree, Items.Hay]
some_list.insert(1, Items.Wood)
print(some_list)
}}

`elements.pop(index)` usuwa element na określonym indeksie.
Jeśli nie podano indeksu, usuwany jest ostatni element.

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
numbers = [3, 5, 8, 25]
numbers.pop()
print(numbers)
numbers.pop(1)
print(numbers)
}}

Funkcja `len()` zwraca długość listy.
{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
numbers = [3, 5, 8, 25]
print(len(numbers))
}}

Listy mają semantykę referencji. Oznacza to, że przypisanie listy do zmiennej przypisuje ten sam obiekt listy do tej zmiennej, zamiast tworzyć kopię listy.
Jeśli dwie zmienne odnoszą się do tej samej listy, zmiany na liście będą widoczne dla obu.

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
a = [1, 2]
b = a
b.pop()
print(a)
print(b)
}}

---

[Zmienne](docs/scripting/variables.md)      [Pętla For](docs/scripting/for.md)      [Krotki](docs/scripting/tuples.md)      [Słowniki](docs/scripting/dicts.md)      [Zbiory](docs/scripting/sets.md)

[len()](functions/len)
