[<- Madencilik](docs/unlocks/mining.md) <right>[Demir ->](docs/unlocks/iron.md)
<right>[Zıplama ->](docs/unlocks/jump.md)
---
# Kömür

Görünüşe göre yüzeyin hemen altındaki zemin, kömür yatakları bulmak için iyi bir yer.

Kömür, 1 blok kalınlığında yatay katmanlar halinde rastgele oluşur. Katmanların boyutu çiftlik boyutunla orantılı olarak büyür; daha çok kömür bulmak için çiftlik boyutunu büyütmek isteyebilirsin!

Aşağıdaki program, kömür bulmak için iyi bir başlangıç noktasıdır. Bir kömür katmanı bulana kadar aşağı doğru kazar, sonra daha fazla kömür bulma umuduyla katmanın doğusunu ve batısını kazar.

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
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 4,
    "digging_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 2
}
#SETUP
move(North)
move(East)
move(East)
#CODE
while get_ground_type() != Grounds.Coal:
    dig()
dig()
move(East)
dig()
move(West)
move(West)
dig()
}}

---

[İstatistikler](docs/stats.md)      [Madencilik](docs/unlocks/mining.md)      [Yeraltı Duyuları](docs/unlocks/underground_senses.md)

[move()](functions/move)      [get_ground_type()](functions/get_ground_type)      [dig()](functions/dig)
