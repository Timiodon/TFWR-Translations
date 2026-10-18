[<- Demir](docs/unlocks/iron.md)
---
# Hazine Haritası

Efsaneler, çoktan ölmüş unutkan bir korsanın sakladığı ve bir türlü bulunamayan bir hazineden söz eder — ya da öyle bir şeyden. Peki ya korsan hazineye giden yolu bir haritaya yazıp sonra haritayı kaybettiyse? Belki de bir lav nehrinin önünde köşeye sıkıştığında haritayı düşürdü ve harita bir bazalt katmanının altında korunarak bugüne kaldı. Bazaltı ölçmek bir şeyler ortaya çıkarabilir.

<spoiler=daha fazlasını anlat>
Bir `Grounds.Basalt` katmanının peşine düşmelisin. Bazaltı ölçmeyi dene ve sana ne söylediğine bak. Bu ipucu seni hazine haritasına götürebilir; haritayı ölçmek de sana hazineye giden yolu mutlaka verecektir – ama haritanın verdiği talimatları çözebilecek misin?
</spoiler>

<spoiler=sadece nasıl yapılacağını söyle>
Peki, durum şu: `Grounds.Basalt` katmanını ve hemen altındaki `Grounds.Treasure_Map` bloğunu bul. Bazalt üzerinde `measure()` çağırarak altındaki harita bloğunun `(x, y)` konumunu öğrenebilirsin.

Hazine yolunu yön harflerinden oluşan bir metin (string) olarak almak için harita bloğunun üzerinde `measure()` çağır. N, E, S ve W sırasıyla `North`, `East`, `South` ve `West` anlamına gelir; D ise "Down" (aşağı) ya da "Dig" (kaz) demektir. Bu harfler, `Grounds.Treasure_Path` bloklarından oluşan ve hazineye giden bir yolu tarif eder.

```
path = measure()
for letter in path:
    do_something(letter)
```

Hazineyi bulması gereken dron, hazine haritası bloğunu kazan dronun kendisidir. Bu dron, yol boyunca her zaman `Grounds.Treasure_Path` bloklarının üzerinde kalmalıdır. Başka bir zemine geçerse yol bozulur ve hazine kaybolur.

Yolun sonunda bir `Grounds.Treasure_Goal` bloğu vardır. Dron yoldan sapmadıysa bu bloğun üzerinde bir `Entities.Underground_Treasure` belirir. Dron, içindeki altını almak için sandığı `harvest()` ile hasat edebilir.

Altın miktarı, hazine yolunun uzunluğuyla orantılıdır. Hazine Haritası kilit açmasını yükseltmek yolun derinliğini artırır; Genişletme'yi yükseltmek ise yola yanlara doğru ilerlemesi için daha fazla alan tanır. Her iki yükseltme de hazine yolunun uzunluğunu ve bulacağın altın miktarını artırır.
</spoiler>

---

[İstatistikler](docs/stats.md)      [For Döngüsü](docs/scripting/for.md)      [Tuple'lar](docs/scripting/tuples.md)      [Yeraltı Duyuları](docs/unlocks/underground_senses.md)

[harvest()](functions/harvest)      [move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)
