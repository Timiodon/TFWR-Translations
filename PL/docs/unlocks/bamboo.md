[<- Ryż](docs/unlocks/rice.md) <right>[Kolorowe bloki ->](docs/unlocks/debug_place.md)
<right>[Piramidy ->](docs/unlocks/pyramid.md)
---
# Bambus
Bambus to roślina rosnąca w górę. Dron musi regularnie zrywać jego brązowe owoce, aby mógł dalej rosnąć. Umożliwia to nowo odblokowane polecenie `hover`.

Bambus trzeba sadzić na zaoranej glebie (`Grounds.Soil`), a posadzenie kosztuje ryż.

Poniższy kod sadzi bambus i czeka, aż urośnie do pierwszego owocu.
{{codeexample
{
"camera_position": {"x": -1, "y": 0, "z": 10},
"show_image": true,
"image_size": {"x": 800, "y": 500},
"show_code": true,
"show_inventory": true,
"show_output": false,
"collapsing": true,
"autoplay": false,
"items": [{"item": "rice", "n": 100}],
"world_size": {"x": 4, "y": 4},
"execution_speed": 2,
"action_ticks": 200,
"operation_ticks": 200,
"seed": 1,
"exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
move(East) # odleć, aby bambus mógł rosnąć
}}

## Owoce
Bambus rośnie dokładnie o 1 blok na sekundę.

Bambus wydaje owoce co kilka bloków. Wtedy przestaje rosnąć i trzeba wlecieć w niego dronem, aby zniszczyć owoc. Bambus może rosnąć w górę do trzeciego owocu. Potem nie urośnie już wyżej, nawet jeśli zerwiesz ten owoc.

Aby zerwać owoc, najpierw użyj `hover`, by osiągnąć odpowiednią wysokość. Następnie wleć w owoc przez `move`, aby go zerwać, i ponownie użyj `move`, aby odlecieć i umożliwić dalszy wzrost.

Użyj `measure()` na bambusie, aby sprawdzić wysokość następnego owocu. `measure()` liczy od `0`, więc `hover(measure())` ustawi drona na wysokości owocu.

{{codeexample
{
"camera_position": {"x": -1, "y": 0, "z": 10},
"show_image": true,
"image_size": {"x": 800, "y": 500},
"show_code": true,
"show_inventory": true,
"show_output": false,
"collapsing": true,
"autoplay": false,
"items": [{"item": "rice", "n": 100}],
"world_size": {"x": 4, "y": 4},
"execution_speed": 2,
"action_ticks": 200,
"operation_ticks": 200,
"seed": 1,
"exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
hover(measure()) # ustaw wysokość obok owocu

move(East) # odleć i poczekaj na wzrost
for i in range(3):
    do_a_flip()

move(West) # zerwij owoc
move(East) # ponownie odleć
}}

## Zawis
Polecenie `hover` przyjmuje jeden argument: wysokość zawisu, czyli liczbę od `0` do `18`. Domyślna wysokość zawisu drona to `1`. `hover` nie może obniżyć drona do wnętrza stałego obiektu. Jeśli dron jest już nad bambusem, nie wlecisz w niego przez `hover(0)`.

`hover` zwraca `True`, jeśli dron osiągnął wskazaną wysokość, w przeciwnym razie `False`.

Jest też polecenie `get_hover`, które zwraca aktualną wysokość zawisu drona.

Użycie `dig`, `harvest` lub `plant` podczas zawisu przywróci dronowi domyślną wysokość (`1`).

Wysokość zawisu nie wpływa natomiast na `get_pos_z()`. Ta funkcja zawsze zwraca pozycję z bloku pod dronem.

## Zbieranie bambusa
Możesz użyć `harvest()`, ale zalecanym sposobem zbioru bambusa jest wlecenie w niego dronem na wysokości `0` (`hover(0)`). Zbiera to całą roślinę naraz.

Aby zebrać bambus bez niszczenia rośliny, wleć w niego poleceniem `move` na dowolnej wysokości, na przykład po `hover(3)`. Zbierzesz wszystkie części od tej wysokości w górę, ale roślina pozostanie żywa. Tak częściowo zebrany bambus ponownie wyda owoce, które trzeba będzie znów zerwać.

W obu przypadkach plon jest równy kwadratowi liczby zniszczonych części bambusa, więc im wyższa roślina, tym lepszy plon.

---

[Statystyki](docs/stats.md)      [Pętla For](docs/scripting/for.md)      [Zmienne](docs/scripting/variables.md)      [If](docs/scripting/if.md)      [Funkcje](docs/scripting/functions.md)      [Ryż](docs/unlocks/rice.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [measure()](functions/measure)
