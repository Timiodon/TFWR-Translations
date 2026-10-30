[<- Pirinç](docs/unlocks/rice.md) <right>[Renkli Bloklar ->](docs/unlocks/debug_place.md)
<right>[Piramitler ->](docs/unlocks/pyramid.md)
---
# Bambu

Bambu, 6 blok yüksekliğe kadar uzayabilen bir bitkidir. Üzerinde bir dron varken büyümez, bu yüzden `plant(Entities.Bamboo)` kullandıktan sonra dronu `move` ile başka bir yere götürmeyi unutma. Bambu ekmek pirinç gerektirir.

Bambu, rastgele belirlenen bir yüksekliğe ulaştığında çiçek açar. Hangi yükseklikte çiçek açacağını öğrenmek için `measure()` kullan. `measure()` saymaya 0'dan başlar; yani bambu ikinci blokta çiçek açacaksa `measure()` 1 döndürür:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 1000, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "rice", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
print(measure())
move(East)
}}

Bambudan en yüksek verimi, dronun tam çiçeğin üzerindeyken `harvest()` yaptığında alırsın. Bu konumdan uzaklaşılan her blok için verim sekize bölünür.
Örneğin çiçeği 3 yüksekliğindeyse ama sen onu bunun iki blok üstünden hasat edersen, verim 64'e bölünür.

Daha yüksekteki çiçekleri hasat etmek için, dron istediğin yüksekliğe geldiğinde bambunun içine doğru uç. Yeni açılan `place()` komutu bu konuda işine yarar.

Yukarı tırmanmak için `place(Grounds.Dirt)` ile bambunun yanına blokları üst üste diz. Ardından `move()` ile bambunun içine yandan uç. `harvest()` çağırdığında dronun tam çiçeğin üzerinde olmalı.

`place(Grounds.Dirt)` sana 1 bloğa mal olur! `Grounds.Rock` gibi başka zeminler de yerleştirebilirsin, ama `Grounds.Clay` gibi özel blokları yerleştiremezsin.

Bambu saniyede tam olarak 1 blok uzar.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 1000, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "block", "n": 100}, {"item": "rice", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
print(measure())
move(East)
place(Grounds.Dirt)
do_a_flip() # wait a bit
do_a_flip()
move(West)
harvest()
}}

---

[İstatistikler](docs/stats.md)      [For Döngüsü](docs/scripting/for.md)      [Değişkenler](docs/scripting/variables.md)      [If](docs/scripting/if.md)      [Fonksiyonlar](docs/scripting/functions.md)      [Pirinç](docs/unlocks/rice.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [place()](functions/place)      [measure()](functions/measure)
