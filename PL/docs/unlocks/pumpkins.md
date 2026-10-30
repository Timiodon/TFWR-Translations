[<- Drzewa](docs/unlocks/trees.md) <right>[Uprawa współrzędna ->](docs/unlocks/polyculture.md)
<right>[Kaktus ->](docs/unlocks/cactus.md)
---
# Dynie
[Dynie](objects/pumpkin) rosną jak marchewki na zaoranej glebie. Sadzenie ich kosztuje marchewki.

Gdy wszystkie dynie na kwadracie są w pełni wyrośnięte, zrosną się, tworząc gigantyczną dynię. Niestety, dynie mają 20% szansy na obumarcie, gdy są w pełni wyrośnięte, więc będziesz musiał ponownie zasadzić martwe, jeśli chcesz, aby się połączyły. 

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "carrot", "n": 11}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 5,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 3,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
for i in range(get_world_size()):
	for j in range(get_world_size()):
		till()
		plant(Entities.Pumpkin)
		move(North)
	move(East)
do_a_flip()
do_a_flip()
move(North)
move(North)
plant(Entities.Pumpkin)
do_a_flip()
plant(Entities.Pumpkin)
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
harvest()
}}

Gdy dynia obumrze, pozostawia po sobie martwą dynię, która nic nie da po zebraniu. Posadzenie nowej rośliny na jej miejscu automatycznie usuwa martwą dynię, więc nie trzeba jej zbierać. `can_harvest()` zawsze zwraca `False` na martwych dyniach.

Plon gigantycznej dyni zależy od jej rozmiaru.

Dynia 1x1 daje `1*1*1 = 1` dynię.
Dynia 2x2 daje `2*2*2 = 8` dyń zamiast `4`.
Dynia 3x3 daje `3*3*3 = 27` dyń zamiast `9`.
Dynia 4x4 daje `4*4*4 = 64` dynie zamiast `16`.
Dynia 5x5 daje `5*5*5 = 125` dyń zamiast `25`.
Dynia `n`x`n` daje `n*n*6` dyń dla `n >= 6`.

Dobrym pomysłem jest wyhodowanie dyni o rozmiarze co najmniej 6x6, aby uzyskać pełny mnożnik.

Oznacza to, że nawet jeśli posadzisz dynię na każdym polu w kwadracie, jedna z dyń może obumrzeć i uniemożliwić wzrost mega dyni.
---

[Statystyki](docs/stats.md)      [Operatory](docs/scripting/operators.md)      [Zmienne](docs/scripting/variables.md)      [Zmysły](docs/unlocks/senses.md)

[harvest()](functions/harvest)      [can_harvest()](functions/can_harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)
