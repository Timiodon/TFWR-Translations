[<- Alberi](docs/unlocks/trees.md) <right>[Policoltura ->](docs/unlocks/polyculture.md)
<right>[Cactus ->](docs/unlocks/cactus.md)
---
# Zucche
Le [zucche](objects/pumpkin) crescono come le carote sul terreno arato. Piantarle costa carote.

Quando tutte le zucche in un quadrato sono completamente cresciute, cresceranno insieme per formare una zucca gigante. Sfortunatamente, le zucche hanno una probabilità del 20% di morire una volta cresciute, quindi dovrai ripiantare quelle morte se vuoi che si uniscano. 

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

Quando una zucca muore, lascia dietro di sé una zucca morta che non darà nulla quando raccolta. Piantare una nuova pianta al suo posto rimuove automaticamente la zucca morta, quindi non è necessario raccoglierla. `can_harvest()` restituisce sempre `False` sulle zucche morte.

La resa di una zucca gigante dipende dalla sua dimensione.

Una zucca 1x1 produce `1*1*1 = 1` zucche.
Una zucca 2x2 produce `2*2*2 = 8` zucche invece di `4`.
Una zucca 3x3 produce `3*3*3 = 27` zucche invece di `9`.
Una zucca 4x4 produce `4*4*4 = 64` zucche invece di `16`.
Una zucca 5x5 produce `5*5*5 = 125` zucche invece di `25`.
Una zucca `n`x`n` produce `n*n*6` zucche per `n >= 6`.

Conviene coltivare zucche grandi almeno 6x6 per ottenere il moltiplicatore completo.

Ciò significa che anche se pianti una zucca su ogni casella di un quadrato, una delle zucche potrebbe morire e impedire alla mega zucca di crescere.

---

[Statistiche](docs/stats.md)      [Operatori](docs/scripting/operators.md)      [Variabili](docs/scripting/variables.md)      [Sensori](docs/unlocks/senses.md)

[harvest()](functions/harvest)      [can_harvest()](functions/can_harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)
