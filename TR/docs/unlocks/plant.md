[<- Hız Yükseltmesi](docs/unlocks/speed.md) <right>[Havuçlar ->](docs/unlocks/carrots.md)
<right>[Hata Ayıklama ->](docs/scripting/debug.md)
<right>[Operatörler ->](docs/scripting/operators.md)
---
# Ekim
Çimin güzel yanı kendiliğinden büyümesidir. Diğer tüm bitkilerin `plant()` fonksiyonuyla ekilmesi gerekir. Şu anda ekebileceğin tek bitki çalı.
Ekmek istediğin bitkinin türünü fonksiyona şöyle verebilirsin:

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
#CODE
plant(Entities.Bush)
}}

Bu, dronun altına bir çalı eker.

Çiftliği tamamen çime döndürmek ve dronun konumunu sıfırlamak için `clear()` çağır.

Görünüşe göre çiftlikte aynı anda birden fazla bitki türü yetiştirirsen bazen daha yüksek verim alabiliyorsun. Daha fazlasını öğrenmek için karışık ekimi araştırman gerekecek.

---

[İstatistikler](docs/stats.md)      [If](docs/scripting/if.md)      [Duyular](docs/unlocks/senses.md)      [Karışık Ekim](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)
