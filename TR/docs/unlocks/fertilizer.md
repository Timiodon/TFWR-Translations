[<- Sulama](docs/unlocks/watering.md) <right>[Labirentler ->](docs/unlocks/mazes.md)
---
# Gübre
Bir noktadan sonra bitkilerin büyümesini beklemek artık yeterince verimli olmaz.
Suda olduğu gibi, her 10 saniyede bir otomatik olarak 1 gübre alırsın. Bu miktar her yükseltmeyle iki katına çıkar.

Gübre bitkilerin anında büyümesini sağlayabilir. `use_item(Items.Fertilizer)`, dronun altındaki bitkinin kalan büyüme süresini 2 saniye azaltır.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "fertilizer", "n": 10}],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Tree)
use_item(Items.Fertilizer)
use_item(Items.Fertilizer)
use_item(Items.Fertilizer)
harvest()
}}

Bunun bazı yan etkileri var.
Gübreyle büyütülen bitkiler enfekte olur.

Enfekte bir bitki hasat edildiğinde, verimin yarısı `Items.Weird_Substance` maddesine dönüşür.
Tuhaf madde de bitkiler üzerinde kullanılabilir; bitkinin ve ona komşu tüm bitkilerin enfekte durumunu tersine çevirir.

`use_item(Items.Weird_Substance)` fonksiyonunu enfekte bir bitki üzerinde çağırırsan onu iyileştirir; sağlıklı bir bitki üzerinde kullanırsan onu enfekte eder.

Sağlıklı komşuları olan enfekte bir bitki üzerinde kullanırsan, bitkiyi iyileştirir ama komşularını enfekte eder; tersi de geçerlidir.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
for _ in range(3):
    for _ in range(3):
        plant(Entities.Tree)
        move(East)
    move(North)

move(North)
move(East)

for _ in range(60):
    do_a_flip()
#CODE
for _ in range(6):
    use_item(Items.Weird_Substance)
    move(East)
}}

---

[İstatistikler](docs/stats.md)      [Sulama](docs/unlocks/watering.md)      [Labirentler](docs/unlocks/mazes.md)

[use_item()](functions/use_item)
