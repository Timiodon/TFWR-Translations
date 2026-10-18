[<- Kaktüs](docs/unlocks/cactus.md)
---
# Dinozorlar
Dinozorlar, antik kemikleri için yetiştirilebilen kadim ve görkemli yaratıklardır.

Ne yazık ki dinozorların soyu uzun zaman önce tükendi, bu yüzden şu an yapabileceğimizin en iyisi dinozor kılığına girmek.
Bu iş için yeni dinozor şapkasını aldın.

Şapkayı şu şekilde takabilirsin:
`change_hat(Hats.Dinosaur_Hat)`

Ne yazık ki pek de reklamdaki gibi görünmüyor...

Dinozor şapkasını takarsan ve yeterince kaktüsün varsa, otomatik olarak bir [elma](objects/apple) satın alınır ve dronun altına yerleştirilir.
Dron bir elmanın üzerindeyken yeniden hareket ettiğinde elmayı yer ve kuyruğu bir parça uzar. Parası yetiyorsa yeni bir elma satın alınır ve rastgele bir konuma yerleştirilir.
Elmanın çıkmak istediği yerde başka bir şey ekiliyse elma ortaya çıkamaz.

Dinozorun kuyruğu dronun arkasından sürüklenir ve dronun daha önce üzerinden geçtiği kareleri doldurur. Dron kuyruğun üzerine gitmeye çalışırsa `move()` başarısız olur ve `False` döndürür.
Kuyruğun son parçası hareket sırasında yoldan çekilir, bu yüzden onun üzerine gidebilirsin. Ancak yılan tüm çiftliği doldurursa artık hareket edemezsin. Bu nedenle yılanın tamamen büyüyüp büyümediğini, hâlâ hareket edip edemediğine bakarak kontrol edebilirsin.
Dinozor şapkası takılıyken dron çiftliğin kenarından geçip öbür tarafa çıkamaz.

Bir elmanın üzerinde `measure()` kullanırsan bir sonraki elmanın konumunu tuple olarak döndürür.

`next_x, next_y = measure()`

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "cactus", "n": 10000}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 5,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
change_hat(Hats.Dinosaur_Hat)
while True:
    next_x, next_y = measure()
    while get_pos_x() != next_x:
        move(East)
    while get_pos_y() != next_y:
        move(North)
}}

Başka bir şapka takılarak dinozor şapkası çıkarıldığında kuyruk hasat edilir.
Kuyruk uzunluğunun karesi kadar kemik alırsın. `n` uzunluğundaki bir kuyruk için `n**2` `Items.Bone` alırsın.
Örneğin:
uzunluk 1 => 1 kemik
uzunluk 2 => 4 kemik
uzunluk 3 => 9 kemik
uzunluk 4 => 16 kemik
uzunluk 16 => 256 kemik
uzunluk 100 => 10000 kemik

Dinozor Şapkası çok ağırdır; onu takarsan `move()` 200 yerine 400 tik sürer. Ancak her elma topladığında `move()` fonksiyonunun harcadığı tik sayısı %3 azalır (aşağı yuvarlanır), çünkü daha uzun bir kuyruk hareket etmene yardımcı olabilir.

Aşağıdaki döngü, belirli sayıda elmadan sonra `move()` fonksiyonunun harcadığı tik sayısını yazdırır:

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
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
ticks = 400
for i in range(100):
    quick_print("ticks after ", i, " apples: ", ticks)
    ticks -= ticks * 0.03 // 1
}}

Yalnızca bir dinozor şapkan var, bu yüzden onu yalnızca bir dron takabilir.

<spoiler=1. ipucunu göster>
Tüm tarlayı kaplayan aynı yolda hareket etmeye devam edersen, her seferinde tüm tarlayı kaplayan bir yılanı kolayca elde edebilirsin. Çok verimli değil ama işe yarar.
Çok büyük bir çiftliği baştan sona dolaşmak uzun sürebilir ve aslında o kadar çok kemiğe ihtiyacın olmayabilir. Çiftliğin boyutunu daha kullanışlı bir değere değiştirmek için `set_world_size()` kullanmaktan çekinme.</spoiler>

---

[İstatistikler](docs/stats.md)      [Tuple'lar](docs/scripting/tuples.md)      [Listeler](docs/scripting/lists.md)

[change_hat()](functions/change_hat)      [move()](functions/move)      [measure()](functions/measure)
