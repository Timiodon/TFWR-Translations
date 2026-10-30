[<- Havuçlar](docs/unlocks/carrots.md) <right>[Gübre ->](docs/unlocks/fertilizer.md)
<right>[Ayçiçekleri ->](docs/unlocks/sunflowers.md)
---
# Sulama
Bitkiler sulandıklarında daha hızlı büyür. Zeminin `0` ile `1` arasında değişen bir su seviyesi vardır.
`get_water()` fonksiyonu, dronun altındaki zeminin su seviyesini döndürür.

Bir bitkinin büyüme hızı, su seviyesi 0 iken 1x hızdan su seviyesi 1 iken 5x hıza kadar doğrusal olarak artar.

Zemin zamanla kurur. Ortalama olarak her saniye mevcut suyunun %1'ini kaybeder, ancak bunda biraz rastgele değişkenlik vardır. Yüksek bir su seviyesini korumak, düşük bir su seviyesini korumaktan çok daha fazla su tüketir.

Bitkilerinde su kullanabilirsin. Envanterine her 10 saniyede bir otomatik olarak bir tank su eklenir.
`Unlocks.Watering` yükseltmesi, her 10 saniyede aldığın su miktarını iki katına çıkarır.

Bir tank `0.25` su alır.

Zemini sulamak için herhangi bir zeminin üzerindeyken `use_item(Items.Water)` çağır.
{{codeexample 
{
    "camera_position": {"x": -4, "y": 1, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "water", "n": 10}],
    "world_size": {"x": 9, "y": 1},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
for _ in range(9):
    till()
    move(East)
#CODE
for i in range(5):
    if i > 0:
        use_item(Items.Water, i)
    plant(Entities.Tree)
    print(get_water())
	move(East)
	move(East)
}}

---

[Gübre](docs/unlocks/fertilizer.md)

[use_item()](functions/use_item)      [get_water()](functions/get_water)
