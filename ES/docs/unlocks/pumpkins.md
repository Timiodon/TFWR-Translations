[<- Árboles](docs/unlocks/trees.md) <right>[Policultivo ->](docs/unlocks/polyculture.md)
<right>[Cactus ->](docs/unlocks/cactus.md)
---
# Calabazas
Las [calabazas](objects/pumpkin) crecen como las zanahorias en suelo arado. Plantarlas cuesta zanahorias.

Cuando todas las calabazas en un cuadrado están completamente crecidas, crecerán juntas para formar una calabaza gigante. Desafortunadamente, las calabazas tienen un 20% de probabilidad de morir una vez que están completamente crecidas, por lo que necesitarás replantar las muertas si quieres que se fusionen. 

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

Cuando una calabaza muere, deja atrás una calabaza muerta que no soltará nada al ser cosechada. Plantar una nueva planta en su lugar elimina automáticamente la calabaza muerta, por lo que no es necesario cosecharla. `can_harvest()` siempre devuelve `False` en calabazas muertas.

El rendimiento de una calabaza gigante depende del tamaño de la calabaza.

Una calabaza de 1x1 rinde `1*1*1 = 1` calabazas.
Una calabaza de 2x2 rinde `2*2*2 = 8` calabazas en lugar de `4`.
Una calabaza de 3x3 rinde `3*3*3 = 27` calabazas en lugar de `9`.
Una calabaza de 4x4 rinde `4*4*4 = 64` calabazas en lugar de `16`.
Una calabaza de 5x5 rinde `5*5*5 = 125` calabazas en lugar de `25`.
Una calabaza de `n`x`n` produce `n*n*6` calabazas para `n >= 6`.

Conviene cultivar calabazas de al menos 6x6 para obtener el multiplicador completo.

Esto significa que incluso si plantas una calabaza en cada casilla de un cuadrado, una de las calabazas puede morir e impedir que crezca la mega calabaza.
---

[Estadísticas](docs/stats.md)      [Operadores](docs/scripting/operators.md)      [Variables](docs/scripting/variables.md)      [Sentidos](docs/unlocks/senses.md)

[harvest()](functions/harvest)      [can_harvest()](functions/can_harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)
