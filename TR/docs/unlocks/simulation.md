# Simülasyon

Simülasyonlar, gerçek çiftliğin durumunu değiştirmeden kodu hızlıca test etmeni sağlar.
Simülasyonun başlangıç durumu serbestçe seçilebilir ve simülasyon sona erdiğinde, gerçek çiftlik simülasyon başlamadan öncekiyle birebir aynı durumda olacaktır.

`simulate()` fonksiyonu bir simülasyon başlatmak için kullanılır.

yürütmenin başlayacağı dosya
`filename = "f1"`

her şeyin kilidi açık ve tamamen yükseltilmiş olarak başla
`sim_unlocks = Unlocks`

10000 havuç ve 50 saman ile başla
`sim_items = {Items.Carrot : 10000, Items.Hay : 50}`

değeri 13 olan bir global "a" değişkeni ile başla
`sim_globals = {"a" : 13}`

sabit bir random seed kullan
`seed = 0`

simülasyonu 64 kat hızlandır
`speedup = 64`

simülasyonu çalıştır
`run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)`

`simulate()` fonksiyonu, verilen başlangıç dosyasını simüle etmenin ne kadar sürdüğünü saniye cinsinden döndürür.

### Dosya Adı
Simulate fonksiyonunun ilk argümanı dosya adıdır. Bu, kod penceresinin üstünde görüntülenen isimdir. Simülasyon, belirtilen dosyayı sanki üzerindeki Çalıştır düğmesine tıklamışsın gibi çalıştıracaktır.

### Başlangıç Kilit Açmaları
Döngüler, if ifadeleri, list'ler, dict'ler gibi tüm programlama özellikleri her zaman kilitli açık kalacaktır.

İkinci argüman, programlama özelliklerine ek olarak simülasyonun hangi kilit açmalar/yükseltmeler ile başlaması gerektiğini belirtmeni sağlar. Bu, bir kilit açma dizisi olmalıdır. Simülasyon, dizideki tüm kilit açmalar maksimum seviyelerine yükseltilmiş olarak başlayacaktır.

Maksimumdan farklı bir yükseltme seviyesi belirtmek istiyorsan, kilit açmaları kilit açma seviyelerine eşleyen bir dictionary geçebilirsin. Bu durumda, negatif değerler maksimum kilit açma seviyesine karşılık gelir.

### Başlangıç Eşyaları
Üçüncü argüman, eşyaları sayılara eşleyen bir dictionary geçmeni sağlar. Simülasyonun hangi eşyalarla başlayacağını belirtir.

### Başlangıç Global Değişkenleri
Simülasyon tamamen yeni bir program yürütmesi başlattığı için, simülasyonu başlatan programdaki değişkenlere erişemezsin.
Ancak, dördüncü argümanı kullanarak simülasyona değerler geçirmek mümkündür. Bu, string biçimindeki değişken adlarını değerlere eşleyen bir dict'tir. Bu değişkenler daha sonra simülasyon içindeki yürütmenin global scope'una eklenir.

Bunun tüm değerleri kopyaladığını unutma, bu yüzden onları simülasyon içinde değiştirmek, simülasyon dışındaki orijinal değerleri etkilemez. Simülasyondan, çalışma süresi dışındaki değerleri döndürmek mümkün değildir.

### Random Seed
Beşinci argüman, simülasyonda kullanılan random seed'i belirtmeni sağlar. Bu pozitif bir tam sayı olmalıdır. Negatif değerler rastgele bir seed kullanılmasına neden olur.

Random seed, bitki büyüme sürelerinden labirent düzenlerine ve suyun azalma sürelerine kadar her şeyi etkiler. Aynı simülasyonu, aynı random seed ve aynı başlangıç koşullarıyla birden çok kez başlatırsan, sonuç her zaman aynı olmalıdır.

### Hızlandırma
Altıncı argüman, simülasyonun başlangıçtaki hızlandırmasıdır. Bu, şeyleri hızlıca test etmeni sağlar. Eğer oyun ayarlanan hıza yetişemezse, otomatik olarak yavaşlayacaktır.

Hızlandırma, simülasyonun sonucunu hiçbir şekilde etkilemez. Sadece bekleme süresini azaltmak için vardır.