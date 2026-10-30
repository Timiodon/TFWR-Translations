[<- Arbres](docs/unlocks/trees.md) <right>[Polyculture ->](docs/unlocks/polyculture.md)
<right>[Cactus ->](docs/unlocks/cactus.md)
---
# Citrouilles
Les [citrouilles](objects/pumpkin) poussent comme des carottes sur un sol labouré. Les planter coûte des carottes.

Lorsque toutes les citrouilles d'un carré sont entièrement développées, elles fusionnent pour former une citrouille géante. Malheureusement, les citrouilles ont 20% de chance de mourir une fois qu'elles sont adultes, tu devras donc replanter celles qui sont mortes si tu veux qu'elles fusionnent.

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

Lorsqu'une citrouille meurt, elle laisse derrière elle une citrouille morte qui ne donnera rien lors de la récolte. Planter une nouvelle plante à sa place retire automatiquement la citrouille morte, il n'est donc pas nécessaire de la récolter. `can_harvest()` renvoie toujours `False` sur les citrouilles mortes.

Le rendement d'une citrouille géante dépend de la taille de la citrouille.

Une citrouille de 1x1 rapporte `1*1*1 = 1` citrouille.
Une citrouille de 2x2 rapporte `2*2*2 = 8` citrouilles au lieu de `4`.
Une citrouille de 3x3 rapporte `3*3*3 = 27` citrouilles au lieu de `9`.
Une citrouille de 4x4 rapporte `4*4*4 = 64` citrouilles au lieu de `16`.
Une citrouille de 5x5 rapporte `5*5*5 = 125` citrouilles au lieu de `25`.
Une citrouille de `n`x`n` rapporte `n*n*6` citrouilles pour `n >= 6`.

C'est une bonne idée d'obtenir des citrouilles d'au moins 6x6 pour obtenir le multiplicateur complet.

Cela signifie que même si tu plantes une citrouille sur chaque case d'un carré, l'une des citrouilles peut mourir et empêcher la méga citrouille de pousser.
---

[Statistiques](docs/stats.md)      [Opérateurs](docs/scripting/operators.md)      [Variables](docs/scripting/variables.md)      [Sens](docs/unlocks/senses.md)

[harvest()](functions/harvest)      [can_harvest()](functions/can_harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)
