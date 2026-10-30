[<- Ağaçlar](docs/unlocks/trees.md) <right>[Karışık Ekim ->](docs/unlocks/polyculture.md)
<right>[Kaktüs ->](docs/unlocks/cactus.md)
---
# Balkabakları
[Balkabakları](objects/pumpkin), havuçlar gibi sürülmüş toprakta büyür. Onları ekmek havuca mal olur.

Bir kare alandaki tüm balkabakları tamamen büyüdüğünde, birleşerek dev bir balkabağı oluştururlar. Ne yazık ki balkabaklarının tamamen büyüdükten sonra çürüme ihtimali %20'dir, bu yüzden birleşmelerini istiyorsan çürüyenleri yeniden ekmen gerekir. 

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

Bir balkabağı çürüdüğünde, geride hasat edildiğinde hiçbir şey vermeyen çürük bir balkabağı bırakır. Yerine yeni bir bitki ekmek çürük balkabağını otomatik olarak kaldırır, bu yüzden onu hasat etmene gerek yoktur. `can_harvest()`, çürük balkabakları için her zaman `False` döndürür.

Dev bir balkabağının verimi, balkabağının boyutuna bağlıdır.

1x1 bir balkabağı `1*1*1 = 1` balkabağı verir.
2x2 bir balkabağı `4` yerine `2*2*2 = 8` balkabağı verir.
3x3 bir balkabağı `9` yerine `3*3*3 = 27` balkabağı verir.
4x4 bir balkabağı `16` yerine `4*4*4 = 64` balkabağı verir.
5x5 bir balkabağı `25` yerine `5*5*5 = 125` balkabağı verir.
`n >= 6` için `n`x`n` bir balkabağı `n*n*6` balkabağı verir.

Tam çarpanı elde etmek için en az 6x6 boyutunda balkabakları yetiştirmek iyi bir fikirdir.

Bu, bir kare alandaki her kareye balkabağı eksen bile balkabaklarından birinin çürüyüp dev balkabağının oluşmasını engelleyebileceği anlamına gelir.

---

[İstatistikler](docs/stats.md)      [Operatörler](docs/scripting/operators.md)      [Değişkenler](docs/scripting/variables.md)      [Duyular](docs/unlocks/senses.md)

[harvest()](functions/harvest)      [can_harvest()](functions/can_harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)
