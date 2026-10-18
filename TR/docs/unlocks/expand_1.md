[<- Hız Yükseltmesi](docs/unlocks/speed.md) <right>[Genişletme 2 ->](docs/unlocks/expand_2.md)
<right>[Madencilik ->](docs/unlocks/mining.md)
---
# Genişletme 1
Çiftliğin büyüdü! Dronu hareket ettiremezsen bu alanın pek bir faydası olmaz; bu yüzden dronu hareket ettiren yeni bir `move()` fonksiyonu var. `move()`, dronun hangi yöne gitmesini istediğini belirtmeni gerektirir. Bunun için dört yeni sabit var: `North, East, South, West`

Örneğin `move(North)`, dronu bir kare kuzeye götürür.

Çiftliğin kenarından dışarı çıkarsan, dron çiftliğin diğer tarafına geçer.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 3},
    "execution_speed": 2,
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
while True:
	move(North)
}}

---

[While Döngüsü](docs/scripting/while.md)      [Operatörler](docs/scripting/operators.md)      [Genişletme 2](docs/unlocks/expand_2.md)

[move()](functions/move)
