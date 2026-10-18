[<- Havuçlar](docs/unlocks/carrots.md) <right>[Balkabakları ->](docs/unlocks/pumpkins.md)
---
# Ağaçlar
[Ağaçlar](objects/tree), odun elde etmek için çalılardan daha iyi bir yoldur. Her biri 5 odun verir. Çalılar gibi çimin ya da toprağın üzerine ekilebilirler.

Ağaçlar biraz alan sever; onları birbirinin hemen yanına ekmek büyümelerini yavaşlatır. Bir ağacın hemen kuzeyindeki, doğusundaki, batısındaki ya da güneyindeki karede bulunan her ağaç için büyüme süresi iki katına çıkar. Yani her kareye ağaç ekersen, büyümeleri `2*2*2*2 = 16` kat daha uzun sürer.
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
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 10,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
for i in range(get_world_size()):
	for j in range(get_world_size()):
		plant(Entities.Tree)
		move(North)
	move(East)
}}

<spoiler=show> 
Burada `%` operatörü işine yarayabilir. `%` operatörü bölme işleminden kalanı döndürür. Çift sayılar `2`'ye bölündüğünde kalan `0`, tek sayılar `2`'ye bölündüğünde kalan `1` olur.
Yani bir sayının çift olup olmadığını şöyle kontrol edebilirsin:

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": false,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def is_even(n):
	return n % 2 == 0

print("is_even(0): ", is_even(0))
print("is_even(1): ", is_even(1))
print("is_even(2): ", is_even(2))
print("is_even(5): ", is_even(5))
print("is_even(-1): ", is_even(-1))
print("is_even(x): ", is_even(get_pos_x()))
}}
</spoiler>

---

[İstatistikler](docs/stats.md)      [Operatörler](docs/scripting/operators.md)      [If](docs/scripting/if.md)      [For Döngüsü](docs/scripting/for.md)      [Karışık Ekim](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)
