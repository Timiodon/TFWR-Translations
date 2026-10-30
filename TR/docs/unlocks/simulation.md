[<- Zamanlama](docs/unlocks/timing.md) <right>[Sıralama Tablosu ->](docs/unlocks/leaderboard.md)
---
# Simülasyon

Simülasyonlar, gerçek çiftliğin durumunu değiştirmeden kodunu hızlıca test etmeni sağlar.
Simülasyonun başlangıç durumunu dilediğin gibi seçebilirsin ve simülasyon bittiğinde gerçek çiftlik, simülasyon başlamadan önceki durumuna birebir geri döner.

Simülasyon başlatmak için `simulate()` fonksiyonu kullanılır.

yürütmenin başlayacağı dosya
`filename = "f1"`

her şeyin kilidi açık ve tamamen yükseltilmiş olarak başla
`sim_unlocks = Unlocks`

10000 havuç ve 50 samanla başla
`sim_items = {Items.Carrot : 10000, Items.Hay : 50}`

değeri 13 olan "a" adlı bir global değişkenle başla
`sim_globals = {"a" : 13}`

sabit bir rastgelelik tohumu (seed) kullan
`seed = 0`

simülasyonu 64 kat hızlandır
`speedup = 64`

simülasyonu çalıştır
`run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)`

`simulate()` fonksiyonu, verilen başlangıç dosyasının simülasyonunun kaç saniye sürdüğünü döndürür.

### Dosya Adı
`simulate()` fonksiyonunun ilk argümanı dosya adıdır. Bu, kod penceresinin üst kısmında görünen addır. Simülasyon, belirtilen dosyayı sanki o dosyanın Çalıştır düğmesine tıklamışsın gibi çalıştırır.

### Başlangıç Kilit Açmaları
Döngüler, `if` ifadeleri, list'ler ve dictionary'ler gibi tüm programlama özelliklerinin kilidi her zaman açık kalır.

İkinci argüman, simülasyonun programlama özelliklerine ek olarak hangi kilit açmalar/yükseltmelerle başlayacağını belirtmeni sağlar. Bu, kilit açmalardan oluşan bir dizi olmalıdır. Simülasyon, dizideki tüm kilit açmalar en yüksek seviyeye yükseltilmiş olarak başlar.

En yüksek seviye dışında bir yükseltme seviyesi belirtmek istersen, kilit açmaları seviyelerle eşleyen bir dictionary (sözlük) verebilirsin. Bu durumda negatif değerler, en yüksek kilit açma seviyesi anlamına gelir.

### Başlangıç Eşyaları
Üçüncü argümanla, eşyaları sayılarla eşleyen bir dictionary verebilirsin. Bu, simülasyonun hangi eşyalarla başlayacağını belirler.

### Başlangıç Global Değişkenleri
Simülasyon tamamen yeni bir program yürütmesi başlattığı için, simülasyonu başlatan programdaki değişkenlere erişemezsin.
Ancak dördüncü argümanı kullanarak simülasyona değer aktarabilirsin. Bu, metin (string) biçimindeki değişken adlarını değerlerle eşleyen bir dict'tir. Bu değişkenler daha sonra simülasyon içindeki yürütmenin global kapsamına eklenir.

Bunun tüm değerleri kopyaladığını unutma; yani simülasyonun içinde onları değiştirmek, simülasyonun dışındaki asıl değerleri etkilemez. Simülasyondan, çalışmasının ne kadar sürdüğü dışında bir değer döndürmek mümkün değildir.

### Rastgelelik Tohumu
Beşinci argüman, simülasyonda kullanılacak rastgelelik tohumunu (seed) belirtmeni sağlar. Bu pozitif bir tam sayı olmalıdır. Negatif değerler rastgele bir tohum kullanılmasına yol açar.

Rastgelelik tohumu, bitkilerin büyüme sürelerinden labirent düzenlerine ve suyun azalma sürelerine kadar her şeyi etkiler. Aynı simülasyonu aynı tohum ve aynı başlangıç koşullarıyla birden çok kez başlatırsan, sonuç her seferinde aynı olmalıdır.

### Hızlandırma
Altıncı argüman, simülasyonun başlangıçtaki hızlandırma katsayısıdır. Bu, bir şeyleri hızlıca test etmeni sağlar. Oyun ayarlanan hıza yetişemezse kendiliğinden yavaşlar.

Hızlandırma, simülasyonun sonucunu hiçbir şekilde etkilemez. Yalnızca bekleme süresini kısaltmak için vardır.

---

[Dictionary'ler](docs/scripting/dicts.md)      [Zamanlama](docs/unlocks/timing.md)      [Hata Ayıklama](docs/scripting/debug.md)      [Sıralama Tablosu](docs/unlocks/leaderboard.md)

[simulate()](functions/simulate)
