[<- Деревья](docs/unlocks/trees.md) <right>[Поликультура ->](docs/unlocks/polyculture.md)
<right>[Кактус ->](docs/unlocks/cactus.md)
---
# Тыквы
[Тыквы](objects/pumpkin), как и морковь, растут на вспаханных грядках. Чтобы их посадить, нужна морковь.

Когда все тыквы в квадрате полностью созревают, то срастаются, образуя огромную тыкву. К сожалению, тыквы с шансом в 20% могут погибнуть, как только созреют. Чтобы тыквы срослись, вместо погибших придется посадить новые.

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

Когда тыква умирает, она оставляет после себя погибшую тыкву, которая ничего не дает при сборе урожая. Она автоматически убирается, если ты сажаешь на ее месте новое растение, так что собирать ее не нужно. `can_harvest()` всегда возвращает `False` для погибших тыкв.

Урожай огромной тыквы зависит от ее размера.

Тыква размером 1х1 производит `1*1*1 = 1` тыкву.
Тыква размером 2х2 производит `2*2*2 = 8` тыкв вместо `4`.
Тыква размером 3х3 производит `3*3*3 = 27` тыкв вместо `9`.
Тыква размером 4х4 производит `4*4*4 = 64` тыквы вместо `16`.
Тыква размером 5х5 производит `5*5*5 = 125` тыкв вместо `25`.
Тыква размером `n`х`n` производит `n*n*6` тыкв для `n >= 6`.

Имеет смысл собирать тыквы размером не менее 6х6, чтобы получить максимальный множитель.

Даже если посадить тыкву на каждой клетке квадрата, одна из них может погибнуть и помешать росту мегатыквы.

---

[Статистика](docs/stats.md)      [Операторы](docs/scripting/operators.md)      [Переменные](docs/scripting/variables.md)      [Датчики](docs/unlocks/senses.md)

[harvest()](functions/harvest)      [can_harvest()](functions/can_harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)
