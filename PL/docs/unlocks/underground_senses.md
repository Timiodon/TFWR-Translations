[<- Górnictwo](docs/unlocks/mining.md)
---
# Podziemne zmysły
Dodajmy kilka czujników, aby dron potrafił poruszać się pod ziemią.

## Pozycja Z
Możesz teraz użyć `get_pos_z()`, aby odczytać wysokość drona (zaczyna od 0 i przyjmuje ujemne wartości, gdy dron schodzi niżej).

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 10},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "exclude_unlocks": ["watering", "fertilizer"],
    "items": [],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#SETUP
move(North)
move(North)
move(East)
move(East)
#CODE
print(get_pos_z())
dig()
dig()
dig()
print(get_pos_z())
}}

## Rodzaj podłoża
`get_ground_type()` zwraca rodzaj podłoża pod dronem. Możesz przekazać tej funkcji kierunek — na przykład `get_ground_type(North)` — aby uzyskać rodzaj podłoża na sąsiednim polu.

W ten sposób możesz sprawdzić, czy blok pod dronem jest ziemią:

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "exclude_unlocks": ["watering", "fertilizer"],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#CODE
dig()
if get_ground_type() == Grounds.Dirt:
    do_a_flip()
}}

## Twardość i stabilność
`get_hardness()` zwraca twardość pola pod dronem. Możesz przekazać tej funkcji kierunek, na przykład `get_hardness(North)`. Im twardsze pole, tym dłużej trwa kopanie.

`get_stability()` zwraca stabilność pola pod dronem. Możesz przekazać tej funkcji kierunek, na przykład `get_stability(North)`. Stabilność równa 1 oznacza, że blok wytrzyma różnicę wysokości wynoszącą 1, zanim się zawali.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 10},
    "show_image": true,
    "image_size": {"x": 800, "y": 250},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "exclude_unlocks": ["watering", "fertilizer"],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 0
}
#SETUP
jump(Unlocks.Rice)
#CODE
print(get_hardness(), "|", get_stability())
while get_hardness() == 1:
    dig()

print(get_hardness(), "|", get_stability())
while get_hardness() == 2 and get_stability() == 3:
    dig()
}}

Pamiętaj, że gdy dron kopie w dół, cztery bezpośrednio sąsiadujące z nim bloki są usuwane niezależnie od ich stabilności, chyba że pełnią specjalną funkcję. Ta zasada nie usuwa na przykład gliny, żelaza ani kwarcu. Wciąż mogą się one jednak zawalić z powodu niewystarczającej stabilności bloków.
---

[Górnictwo](docs/unlocks/mining.md)      [Zmysły](docs/unlocks/senses.md)

[get_pos_z()](functions/get_pos_z)      [get_ground_type()](functions/get_ground_type)      [get_hardness()](functions/get_hardness)      [get_stability()](functions/get_stability)
