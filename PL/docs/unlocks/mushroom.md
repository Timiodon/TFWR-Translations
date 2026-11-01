[<- Kwarc](docs/unlocks/quartz.md) <right>[Dynamit ->](docs/unlocks/dynamite.md)
---
# Grzyby
W podziemnych koloniach rośnie wiele rodzajów grzybów. Podczas kopania szukaj warstwy `Grounds.Mushroom`. Następnie możesz użyć `measure()` na podłożu, aby uzyskać rodzaj grzyba jako liczbę od `0` do `5`.

Poniższy kod znajduje grzyby i wypisuje ich typ:
{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 6,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}
#SETUP
jump(Unlocks.Mushrooms)
#CODE
# Przetwórz rząd grzybów
for i in range(get_world_size()):
    # Kop do górnego bloku grzybów
    while get_ground_type() != Grounds.Mushroom:
        dig()

    # Wypisz numer typu grzyba
    print(measure())

    move(East)
}}

## Zbieranie grzybów
Grzyby tego samego rodzaju lubią być razem, ale są zbyt nieśmiałe, by rosnąć jeden na drugim. Przesuń blok grzybów pod dronem przez `push(direction)`.

Ustaw dwa bloki grzybów tego samego typu jeden na drugim, a zostaną automatycznie zebrane.

Poniższy kod robi miejsce, a następnie przesuwa grzyba, aż trafi na taki sam typ poniżej:
{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 6,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 3,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron", "special_soils"]
}
#SETUP
jump(Unlocks.Mushrooms)
#CODE
while get_ground_type() != Grounds.Mushroom:
    dig()

depth = get_pos_z()
for i in range(2):
    # Zrób miejsce na pchnięcie grzyba na wschód
    move(East)
    while get_pos_z() > depth - 1:
        dig()
    # Wróć, popchnij i podążaj za przesuniętym blokiem
    move(West)
    push(East) # Popchnij grzyba!
    move(East)
}}

# Przesuwanie bloków
Za pomocą `can_push(direction)` możesz sprawdzić, czy blok pod dronem można popchnąć i czy coś nie blokuje go w danym kierunku.

`push(direction)` popycha blok i zwraca informację, czy operacja się powiodła.

Przesuwać można tylko bloki grzybów. Bloków nie można popychać w górę, a pchnięcie nie powiedzie się, jeśli na drodze znajduje się inny blok. Bloki wypchnięte w powietrze spadają i lądują na najbliższym bloku poniżej.

# Strategia
<spoiler=wskazówka>
Pamiętaj, że możesz wywołać `place(Grounds.Dirt)`, aby umieszczać bloki pod dronem. Przydaje się to do wypełniania dziur, tak aby można było przepychać nad nimi inne bloki.
</spoiler>

---

[Statystyki](docs/stats.md)      [Podziemne zmysły](docs/unlocks/underground_senses.md)      [Słowniki](docs/scripting/dicts.md)

[move()](functions/move)      [measure()](functions/measure)      [can_push()](functions/can_push)      [push()](functions/push)      [place()](functions/place)      [get_ground_type()](functions/get_ground_type)
