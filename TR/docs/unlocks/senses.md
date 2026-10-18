[<- Operatörler](docs/scripting/operators.md)
---
# Duyular
Dron artık görebiliyor! 

`get_pos_x()` ve `get_pos_y()` fonksiyonları dronun mevcut x ve y koordinatlarını döndürür. Başlangıç konumunda ikisinin değeri de `0` olur. `East` yönünde gidilen her karede x koordinatı `1` artar, `North` yönünde gidilen her karede de y koordinatı `1` artar.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 2},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(East)
#CODE
print("x =", get_pos_x(), "y =", get_pos_y())
if get_pos_x() == 1 and get_pos_y() == 0:
    do_a_flip()
}}

`num_items(item)` bir eşyadan elinde kaç tane olduğunu döndürür.
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 10}],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(num_items(Items.Hay))
}}

`get_entity_type()` ve `get_ground_type()` dronun altındaki varlığın ya da zeminin türünü döndürür.
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
plant(Entities.Bush)
#CODE
print(get_entity_type())
if get_entity_type() == Entities.Bush:
	do_a_flip()

print(get_ground_type())
if get_ground_type() != Grounds.Soil:
	do_a_flip()
}}

`None` anahtar kelimesinin de kilidi artık açıldı! `None`, hiçbir değer olmadığını belirten bir değerdir.
Örneğin `return` ifadesi olmayan bir fonksiyon aslında `None` döndürür.

Dronun altında hiçbir varlık yoksa `get_entity_type()` fonksiyonu `None` döndürür.


Belirli bir kilit açmadan kaç tane sahip olduğunu öğrenmek istersen `num_unlocked(unlock)` fonksiyonunu kullan.

Örneğin `num_unlocked(Unlocks.Speed)` sahip olduğun hız yükseltmelerinin sayısını döndürür.

`num_unlocked(Unlocks.Senses)` duyuların kilidi açıldıysa `1`, açılmadıysa `0` döndürür.

`num_unlocked()` fonksiyonunu eşyalar ya da varlıklar için de kullanabilirsin. Eşyanın ya da varlığın kilidi açıksa `1`, değilse `0` döndürür.

Dikkat: `num_unlocked(Unlocks.Carrots)` kilidin kaç kez açıldığını ya da yükseltildiğini döndürür.
`num_unlocked(Items.Carrot)` ise yalnızca `0` ya da `1` döndürür. Diğer bitkiler için de aynısı geçerlidir.

---

[If](docs/scripting/if.md)      [Operatörler](docs/scripting/operators.md)      [Değişkenler](docs/scripting/variables.md)      [Tuple'lar](docs/scripting/tuples.md)      [Dictionary'ler](docs/scripting/dicts.md)      [Yeraltı Duyuları](docs/unlocks/underground_senses.md)

[get_pos_x()](functions/get_pos_x)      [get_pos_y()](functions/get_pos_y)      [get_entity_type()](functions/get_entity_type)      [get_ground_type()](functions/get_ground_type)      [num_items()](functions/num_items)      [num_unlocked()](functions/num_unlocked)
