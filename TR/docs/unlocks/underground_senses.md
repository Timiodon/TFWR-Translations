[<- Madencilik](docs/unlocks/mining.md)
---
# Yeraltı Duyuları

Dronunun yeraltında yolunu bulabilmesi için birkaç sensör ekleyelim.

Artık dronun yüksekliğini öğrenmek için `get_pos_z()` kullanabilirsin (yükseklik 0'dan başlar ve dron aşağı indikçe negatif olur).

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "exclude_unlocks": ["watering", "fertilizer"],
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#CODE
move(North)
move(North)
move(East)
dig()
dig()
dig()
print(get_pos_z())
}}

`get_ground_type()` dronun altındaki zeminin türünü döndürür. Komşu bir karenin zemin türünü öğrenmek için ona bir yön argümanı verebilirsin; örneğin `get_ground_type(North)`.

Dronun altındaki bloğun toprak olup olmadığını şöyle kontrol edebilirsin:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#CODE
dig()
if get_ground_type() == Grounds.Dirt:
    do_a_flip()
}}


`get_hardness()` dronun altındaki zemin karesinin sertliğini döndürür. Ona bir yön argümanı da verebilirsin, örneğin `get_hardness(North)`. Bir karenin sertliği ne kadar yüksekse kazılması o kadar uzun sürer.

`get_stability()` dronun altındaki zemin karesinin sağlamlığını döndürür. Ona bir yön argümanı da verebilirsin, örneğin `get_stability(North)`. Sağlamlığın 1 olması, bloğun göçmeden önce 1 birimlik yükseklik farkına dayanabileceği anlamına gelir.

Dron aşağı doğru kazarken, özel bir işlevi olmadığı sürece hemen yanındaki dört blok sağlamlıklarından bağımsız olarak kaldırılır. Örneğin kil, demir ve kuvars bu kural nedeniyle kaldırılmaz. Ancak yeterli sağlamlıkları yoksa bunlar da göçebilir.
---

[Madencilik](docs/unlocks/mining.md)      [Duyular](docs/unlocks/senses.md)

[get_pos_z()](functions/get_pos_z)      [get_ground_type()](functions/get_ground_type)      [get_hardness()](functions/get_hardness)      [get_stability()](functions/get_stability)
