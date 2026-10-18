[<- Genişletme 1](docs/unlocks/expand_1.md) <right>[Yeraltı Duyuları ->](docs/unlocks/underground_senses.md)
<right>[Pirinç ->](docs/unlocks/rice.md)
<right>[Kömür ->](docs/unlocks/coal.md)
---
# Madencilik

Dronun ilkel bir matkaba kavuştu; bu matkapla yeraltında hazine arayabilir.

Altındaki bloğu kazmak için `dig()` komutunu kullanabilirsin.

Şimdilik biraz blok toplayalım:

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
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "special_soils"]
}
#SETUP
move(North)
move(East)
#CODE
dig()
do_a_flip()
dig()
do_a_flip()
dig()
do_a_flip()
clear()
}}

Yüzeye geri dönmek istersen istediğin an `clear()` kullanabilirsin. Bu, çiftliğini de eski haline getirir.

İmleci bir bloğun üzerine getirdiğinde bloğun adı, sağlamlığı ve sertliği gösterilir.

# Matkap

Daha derine kazdıkça blokların sertleştiğini ve bu yüzden kazmanın daha uzun sürdüğünü fark edeceksin. Neyse ki bu konuda yardımı olsun diye matkabımızı yükseltebiliyoruz!

Altındaki bloğun sertliğini kontrol etmek için `get_hardness()` kullanabilirsin. Özellikle sert bloklardan oluşan bir bölgeye denk gelirsen, daha hızlı ilerleyebilmek için etrafından dolaşmak akıllıca olabilir:

`while True:
        if get_hardness() < 5:
                dig()
        else:
                move(East)`

Elbette aşağı indikçe bloklar giderek sertleşir; bu strateji işe yarasa da seni ancak bir yere kadar götürebilir.

## Göçükler

Aşağı kazmak çevredeki blokların göçmesine neden olur. Dronun yanındaki dört blok her zaman yok olur. Ardından göçük, zeminin sağlamlığına göre yayılır. Çayır gibi sağlamlığı 1 olan bir blok en fazla 1 blokluk yükseklik farkına dayanabilir. Başka bir deyişle, çayırın dikey ya da yatay komşularından birinin z koordinatı 2 ya da daha fazla blok daha derindeyse çayır yok olur.

Bir bloğun sağlamlığı, üzerine gelindiğinde açılan ipucu kutusunda yazar.

Bir blok göçtüğünde üstündeki tüm bloklar da yok olur. Kaynakları yalnızca dronun doğrudan kazdığı bloklardan alırsın; göçükte kaybolan bloklar hiçbir kaynak vermeden yok olur.

---

[Yeraltı Duyuları](docs/unlocks/underground_senses.md)      [While Döngüsü](docs/scripting/while.md)

[move()](functions/move)      [dig()](functions/dig)
