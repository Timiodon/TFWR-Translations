[<- Árvores](docs/unlocks/trees.md) <right>[Policultura ->](docs/unlocks/polyculture.md)

<right>[Cacto ->](docs/unlocks/cactus.md)

---

# Abóboras

[Abóboras](objects/pumpkin) crescem como cenouras em solo arado. Plantá-las custa cenouras.

Quando todas as abóboras em um quadrado estão totalmente crescidas, elas se juntam para formar uma abóbora gigante. Infelizmente, as abóboras têm 20% de chance de morrer quando estão totalmente crescidas, então você precisará replantar as mortas se quiser que elas se fundam. 

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

Quando uma abóbora morre, ela deixa para trás uma abóbora morta que não renderá nada quando colhida. Plantar uma nova planta em seu lugar remove automaticamente a abóbora morta, então não há necessidade de colhê-la. `can_harvest()` sempre retorna `False` em abóboras mortas.

O rendimento de uma abóbora gigante depende do tamanho da abóbora.

Uma abóbora 1x1 rende `1*1*1 = 1` abóbora.
Uma abóbora 2x2 rende `2*2*2 = 8` abóboras em vez de `4`.
Uma abóbora 3x3 rende `3*3*3 = 27` abóboras em vez de `9`.
Uma abóbora 4x4 rende `4*4*4 = 64` abóboras em vez de `16`.
Uma abóbora 5x5 rende `5*5*5 = 125` abóboras em vez de `25`.
Uma abóbora de `n`x`n` rende `n*n*6` abóboras para `n >= 6`.

É uma boa ideia cultivar abóboras de pelo menos 6x6 para obter o multiplicador completo.

Isso significa que, mesmo que você plante uma abóbora em cada casa de um quadrado, uma das abóboras pode morrer e impedir que a mega abóbora cresça.

---

[Estatísticas](docs/stats.md)      [Operadores](docs/scripting/operators.md)      [Variáveis](docs/scripting/variables.md)      [Sentidos](docs/unlocks/senses.md)

[harvest()](functions/harvest)      [can_harvest()](functions/can_harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)
