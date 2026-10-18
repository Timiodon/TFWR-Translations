[<- While Döngüsü](docs/scripting/while.md) <right>[Genişletme 1 ->](docs/unlocks/expand_1.md)
<right>[Ekim ->](docs/unlocks/plant.md)
---
# Hız Yükseltmesi
Yürütme hızı iki katına çıktı. Sorun şu ki dron artık çimin büyüyebileceğinden daha hızlı hasat ediyor ve sonuçta hiç ürün alınamıyor. Bununla başa çıkmak için [if](docs/scripting/if.md) dallarının ve [can_harvest()](functions/can_harvest) fonksiyonunun kilidi artık açıldı.

## Hasattan Önce Kontrol Etmek
Bir `if` ifadesi, verilen koşul `True` ise kod bloğunu bir kez çalıştırır.

Yeni `can_harvest()` fonksiyonu işe yarar bir koşul sağlar. `can_harvest()`, dronun altındaki bitki hasat edilebiliyorsa `True`, edilemiyorsa `False` döndürür.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
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
do_a_flip()
#CODE
if can_harvest():
	do_a_flip()
}}

Böyle bir dönüş değerini şöyle düşünebilirsin: `if` değerlendirilirken `can_harvest()` fonksiyon çağrısı ifadesinin yerini döndürülen `True` değeri alır.

Yukarıdaki kod çalıştığında neler olur:
- `if` ifadesi çalışır.
- `can_harvest()` çağrılır.
- Çim tamamen büyümüş olduğu için `can_harvest()`, `True` döndürür.
- İfade artık `if True:` olur.
- Değer `True` olduğu için dal çalıştırılır.

Çim tamamen büyümemiş olsaydı dron takla atmazdı.

Artık dronun erken hasat yapmasını önlemek için `if` kullanabiliriz.

---

[If](docs/scripting/if.md)      [While Döngüsü](docs/scripting/while.md)

[harvest()](functions/harvest)      [can_harvest()](functions/can_harvest)
