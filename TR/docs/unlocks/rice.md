[<- Madencilik](docs/unlocks/mining.md) <right>[Bambu ->](docs/unlocks/bamboo.md)
<right>[Taşlaşmış Balkabakları ->](docs/unlocks/petrified_pumpkins.md)
<right>[Perlit ve Tınlı Toprak ->](docs/unlocks/special_soils.md)
---
# Pirinç

Yüzeyin altında ince bir kil tabakası olduğunu fark ettin. Anlaşılan bu verimli zemin, pirinç fidesi ekmek için biçilmiş kaftan.

Pirinç, ekildiği kili kurutur. Her kil bloğunu yalnızca bir kez kullanabilirsin. Neyse ki tabaka birkaç blok kalınlığında. Ve tabii ki kil tabakasını geri getirmek için dünyayı her zaman `clear()` ile sıfırlayabilirsin.

Kil bulana kadar aşağı kazmak için aşağıdaki kodu faydalı bulabilirsin.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "exclude_unlocks": ["watering", "fertilizer"],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 8,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#SETUP
move(East)
#CODE
while get_ground_type() != Grounds.Clay:
    dig()
plant(Entities.Rice)
move(North)
do_a_flip()
}}

---

[İstatistikler](docs/stats.md)      [Madencilik](docs/unlocks/mining.md)      [Yeraltı Duyuları](docs/unlocks/underground_senses.md)      [If](docs/scripting/if.md)      [For Döngüsü](docs/scripting/for.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
