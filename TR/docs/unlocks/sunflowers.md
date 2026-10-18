[<- Sulama](docs/unlocks/watering.md)
---
# Ayçiçekleri
[Ayçiçekleri](objects/sunflower) güneşin gücünü toplar. Bu gücü hasat edebilirsin.

Ayçiçeği ekmek, havuç ya da balkabağı ekmekle tamamen aynı şekilde çalışır.

Büyümüş bir ayçiçeğini hasat etmek güç verir.
Çiftlikte en az 10 ayçiçeği varsa ve en çok taç yaprağına sahip olanlardan birini hasat edersen `8` kat daha fazla güç elde edersin!
Daha çok taç yaprağı olan başka bir ayçiçeği varken bir ayçiçeğini hasat edersen, hasat ettiğin bir sonraki ayçiçeği de yalnızca normal miktarda güç verir (8 katlık bonus olmaz).

`measure()` dronun altındaki ayçiçeğinin taç yaprağı sayısını döndürür.
Ayçiçeklerinin en az `7`, en fazla `15` taç yaprağı olur.
Ayçiçekleri tam olarak büyümeden önce de ölçülebilir ve 10 ayçiçeği sınırına dahil edilir.

Birden fazla ayçiçeğinin taç yaprağı sayısı aynı olabilir, yani en çok taç yaprağına sahip birden fazla ayçiçeği de olabilir. Bu durumda hangisini hasat ettiğin fark etmez.

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "inventory_scale": 5,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "carrot", "n": 10}],
    "world_size": {"x": 5, "y": 2},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 4,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(North)
for _ in range(5):
    till()
    plant(Entities.Sunflower)
    move(East)
move(North)
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
#CODE
for _ in range(5):
    till()
    plant(Entities.Sunflower)
    print(measure())
    move(East)
for _ in range(5):
    while not can_harvest():
        pass
    harvest()
    move(East)
}}

Gücün olduğu sürece dron bu gücü iki kat hızlı çalışmak için kullanır.
Hareket, hasat ya da ekim gibi her 30 eylemde 1 güç tüketir.
Diğer kod ifadelerini çalıştırmak da güç harcayabilir, ama dron eylemlerine göre çok daha az.

Genel olarak, hız yükseltmeleriyle hızlanan her şey güçle de hızlanır.
Güçle hızlanan her şey, hız yükseltmeleri hesaba katılmadan, çalışması için gereken süreyle orantılı olarak güç harcar.

---

[İstatistikler](docs/stats.md)      [Listeler](docs/scripting/lists.md)      [Dictionary'ler](docs/scripting/dicts.md)      [Değişkenler](docs/scripting/variables.md)      [For Döngüsü](docs/scripting/for.md)      [If](docs/scripting/if.md)      [Operatörler](docs/scripting/operators.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [measure()](functions/measure)
