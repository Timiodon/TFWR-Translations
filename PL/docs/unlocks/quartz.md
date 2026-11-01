[<- Żelazo](docs/unlocks/iron.md) <right>[Grzyby ->](docs/unlocks/mushroom.md)
---
# Kwarc
Za żyłami żelaza w `Grounds.Rock` znajdziesz kwarc u dołu warstwy skał oraz w twardej `Grounds.Dirt` pod nią (sprawdź twardość przez `get_hardness()` z [Podziemnych zmysłów](docs/unlocks/underground_senses.md)).

Poniższy kod przekopuje się przez ziemię do warstwy skał. Tam nieustannie szuka kwarcu podczas kopania, aż odległość spadnie poniżej 2. Na koniec wypisuje uzyskaną odległość.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "block", "n": 1}, {"item": "iron", "n": 100}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 8,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "dynamite"]
}
#SETUP
move(East)
move(North)
#CODE
# Kop do warstwy skał
while get_ground_type() != Grounds.Rock:
    dig()

# Kop dalej, aż żyła kwarcu będzie blisko
while prospect_quartz() == None or prospect_quartz() >= 2:
    for i in range(10):
        dig()

# Wypisz końcową odległość do żyły
print(prospect_quartz())
}}

## Budowa żył
Kwarc występuje w igłowatych żyłach tworzących pionowe kolumny, dlatego trudno znaleźć go metodą prób i błędów.

## Poszukiwanie kwarcu
Na szczęście możemy przerobić żelazo na coś w rodzaju różdżki radiestezyjnej, która ułatwia odnajdywanie żył kwarcu. Służy do tego polecenie `prospect_quartz()`.

`prospect_quartz()` działa inaczej niż `prospect_iron()`. Zamiast kierunku ruchu do najbliższej rudy żelaza zwraca dokładną odległość 3D między najbliższym blokiem kwarcu a dronem (odległość euklidesową).

Wykonanie `prospect_quartz()` kosztuje 1 żelazo, więc warto używać go oszczędnie.

Jeśli `prospect_quartz()` nie znajdzie kwarcu w pobliżu albo nie masz dość żelaza na poszukiwanie, zwróci `None`.

## Strategia
<spoiler=pokaż wskazówkę>Możesz wielokrotnie szukać rud i się poruszać, obserwując zmiany odległości. Na płaskiej powierzchni minimalizowanie odległości może doprowadzić cię nad żyłę kwarcu. Strategia podobna do wyszukiwania binarnego pozwala ograniczyć wywołania `prospect_quartz()` i zużycie żelaza.

Bardziej złożone strategie mogą wykorzystywać geometrię 2D do znalezienia przecięcia co najmniej dwóch okręgów. Możesz też wybrać trudniejszą drogę pełnej trilateracji: przeciąć trzy sfery i wyznaczyć dokładną pozycję 3D żyły.

Pierwiastek kwadratowy obliczysz operatorem potęgowania, na przykład `16**0.5` daje pierwiastek z 16. Nie ma wbudowanych funkcji do trygonometrii ani wektorów — musisz napisać je samodzielnie.

Pamiętaj, że w pobliżu może być kilka żył, więc pomiary w sąsiednich miejscach nie muszą wskazywać tej samej.</spoiler>

---

[Statystyki](docs/stats.md)      [Górnictwo](docs/unlocks/mining.md)      [Podziemne zmysły](docs/unlocks/underground_senses.md)      [Zmienne](docs/scripting/variables.md)      [Operatory](docs/scripting/operators.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)      [prospect_quartz()](functions/prospect_quartz)
