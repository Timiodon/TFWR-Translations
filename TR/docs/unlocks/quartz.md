[<- Demir](docs/unlocks/iron.md) <right>[Mantar ->](docs/unlocks/mushroom.md)
---
# Kuvars

Kuvars, taş katmanının alt kısımlarında ve onun altındaki sert toprakta iğne biçimli damarlar hâlinde oluşur. Bu damarlar dikey sütunlar oluşturduğu için deneme yanılmayla bulunmaları oldukça zordur.

Neyse ki demirimizi bükerek yeraltında su aramak için kullanılan çatal çubuklara benzer bir şey yapabilir ve bu kuvars damarlarını çok daha kolay bulabiliriz. Bunun komutu `prospect_quartz()`.

`prospect_quartz()`, `prospect_iron()` fonksiyonundan farklı çalışır. En yakın kuvars cevherinin yönünü döndürmek yerine en yakın kuvarsa olan Öklid uzaklığını (3 boyutlu uzaklık) döndürür. `prospect_quartz()` her çalıştırıldığında 1 demir harcar, bu yüzden komutu idareli kullanmak iyi bir fikir olabilir.

`prospect_quartz()` yakınlarda hiç kuvars bulamazsa ya da aramayı yapmaya yetecek kadar demirin yoksa `None` döndürür.

Aşağıdaki kod parçası, dronunun toprağı geçip kaya katmanının derinlerine kadar kazmasını sağlar. Sonra, biraz şansın varsa yakınlarda bir kuvars damarı olur ve dronun ona olan uzaklığı yazdırır.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 100}, {"item": "iron", "n": 100}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 8,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "dynamite"]
}

#CODE
move(East)
move(North)
while get_ground_type() != Grounds.Rock:
    dig()
for i in range(30):
    dig()
do_a_flip()
do_a_flip()
print(prospect_quartz())
}}

---

[İstatistikler](docs/stats.md)      [Madencilik](docs/unlocks/mining.md)      [Yeraltı Duyuları](docs/unlocks/underground_senses.md)      [Değişkenler](docs/scripting/variables.md)      [Operatörler](docs/scripting/operators.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)      [prospect_quartz()](functions/prospect_quartz)
