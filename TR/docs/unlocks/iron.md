[<- Kömür](docs/unlocks/coal.md) <right>[Kuvars ->](docs/unlocks/quartz.md)
<right>[Demir Arama ->](docs/unlocks/prospecting.md)
<right>[Hazine Haritası ->](docs/unlocks/treasure_map.md)
---
# Demir

Kilin altındaki taş katmanında demir damarları keşfettin.

Demir damarları başta küçüktür ve onları bulmak için biraz şansa ihtiyacın olacak. Bu kilit açmanın seviyesini yükselttikçe bir cevher damarının ulaşabileceği en büyük boyut da artar. Demiri daha güvenilir bir şekilde bulmak için cevher arama kilit açmasına da göz atmak isteyebilirsin.

Bir demir damarı her zaman kesintisizdir, çapraz atlamalar içermez. Bir parça demir bulursan, damarın tamamını topladığından emin olmak için altında ya da yanında başka demir var mı diye bak.

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
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 1,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz"]
}
#SETUP
jump(Unlocks.Iron)
#CODE
for i in range(4):
    dig()
do_a_flip()
}}

---

[İstatistikler](docs/stats.md)      [Madencilik](docs/unlocks/mining.md)      [Demir Arama](docs/unlocks/prospecting.md)      [Yeraltı Duyuları](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)
