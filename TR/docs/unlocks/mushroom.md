[<- Kuvars](docs/unlocks/quartz.md) <right>[Dinamit ->](docs/unlocks/dynamite.md)
---
# Mantar

Pek çok mantar türü yeraltında koloniler halinde yetişir. Kazarken bir `Grounds.Mushroom` katmanı ara. Ardından mantarın türünü `0` ile başlayan bir sayı olarak öğrenmek için zemini `measure()` ile ölçebilirsin.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 100}, {"item": "iron", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 6,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}

#SETUP
jump(Unlocks.Mushrooms)
#CODE
while get_ground_type() != Grounds.Mushroom:
    dig()
do_a_flip()
print(measure())
}}

Aynı türden mantarlar bir arada olmayı sever, ama üst üste büyümeye çekinecek kadar da utangaçtırlar. Bir mantar bloğunu aynı türden başka bir mantar bloğunun üstüne ittiğinde ikisi de kaybolur ve ödül olarak mantar kazanırsın.

Dronun altındaki bloğun itilip itilemeyeceğini ve verilen yönde önünü kapatan bir şey olup olmadığını kontrol etmek için `can_push(direction)` kullanabilirsin. `push(direction)` bloğu iter ve itmenin başarılı olup olmadığını döndürür.

Bloklar yukarı doğru itilemez; yolda başka bir blok varsa itme başarısız olur. Boşluğa itilen bloklar düşer ve altlarındaki ilk bloğun üstüne konar.

Dronun altına blok yerleştirmek için `place(Grounds.Dirt)` çağırabileceğini unutma. Bu, blokları üzerinden itebilmek için çukurları doldururken işine yarayabilir.

---

[İstatistikler](docs/stats.md)      [Yeraltı Duyuları](docs/unlocks/underground_senses.md)      [Dictionary'ler](docs/scripting/dicts.md)

[move()](functions/move)      [measure()](functions/measure)      [can_push()](functions/can_push)      [push()](functions/push)      [place()](functions/place)      [get_ground_type()](functions/get_ground_type)
