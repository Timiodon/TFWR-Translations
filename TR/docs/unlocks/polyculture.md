[<- Balkabakları](docs/unlocks/pumpkins.md)
---
# Karışık Ekim
Bazı bitkilerin birlikte ekildiklerinde daha fazla ürün verdiğini belki fark etmişsindir.
Çim, çalılar, ağaçlar ve havuçlar doğru yoldaş bitkiye sahip olduklarında daha fazla ürün verir. Yoldaş tercihi her bitkide farklıdır ve önceden tahmin edilemez. Neyse ki dronun altındaki bitkinin yoldaş tercihi `get_companion()` ile ölçülebilir. Bu fonksiyon bir tuple döndürür: ilk eleman bitkinin yoldaş olarak istediği bitki türü, ikinci eleman ise yoldaşını istediği konumdur. Verim bonusunu almak için yoldaşın tamamen büyümüş olması gerekmez.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Bush)
plant_type, (x, y) = get_companion()
print(plant_type, (x, y))
move(East)
move(South)
plant(plant_type)
move(West)
move(North)
do_a_flip()
harvest()
}}

Bir bitkinin yoldaş tercihi `Entities.Grass`, `Entities.Bush`, `Entities.Tree` ya da `Entities.Carrot` olabilir. Her bitki bunu rastgele seçer, ama her zaman kendisinden farklı bir bitki türü seçer. Konum da bitkiye en fazla 3 hamle uzaklıktaki herhangi bir konum olabilir; yalnızca bitkinin kendi konumu olamaz.

Dronun altında yoldaş tercihi olan bir bitki yoksa `get_companion()` fonksiyonu `None` döndürür.

Karışık ekimin kilidi ilk kez açılmadan önce verim çarpanı `5` değerindedir. Her yükselttiğinde iki katına çıkar.

---

[İstatistikler](docs/stats.md)      [Tuple'lar](docs/scripting/tuples.md)      [Dictionary'ler](docs/scripting/dicts.md)      [Duyular](docs/unlocks/senses.md)      [Ekim](docs/unlocks/plant.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [get_companion()](functions/get_companion)
