# Simülasyon

Simülasyonlar, gerçek çiftliğin durumunu değiştirmeden kodu hızlıca test etmenizi sağlar. Simülasyonun başlangıç durumu serbestçe seçilebilir ve simülasyon bittiğinde, gerçek çiftlik simülasyon başlamadan önceki tam durumunda olacaktır.

Simülasyonu başlatmak için `simulate()` fonksiyonu kullanılır.

Çalıştırmanın başlaması gereken dosya
`filename = "f1"`

Her şey kilitsiz ve tamamen geliştirilmiş olarak başla
`sim_unlocks = Unlocks`

10000 havuç ve 50 saman ile başla
`sim_items = {Items.Carrot : 10000, Items.Hay : 50}`

Değeri 13 olan global "a" değişkeni ile başla
`sim_globals = {"a" : 13}`

Sabit bir rastgele tohum kullan
`seed = 0`

Simülasyonu 64 kat hızlandır
`speedup = 64`

Simülasyonu çalıştır
`run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)`

`simulate()` fonksiyonu, belirtilen başlangıç dosyasını simüle etmenin ne kadar sürdüğünü saniye cinsinden geri döner.

### Dosya Adı
Simülasyon fonksiyonunun ilk argümanı dosya adıdır. Bu, kod penceresinin üst kısmında gösterilen addır. Simülasyon belirlediğiniz dosyayı, tıpkı Execute butonuna tıklamışsınız gibi çalıştırır.

### Başlangıç Kilitleri
Döngüler, if yapıları, listeler, dictler gibi tüm programlama özellikleri her zaman kilitsiz kalacaktır.

İkinci argüman, simülasyonun programlama özelliklerine ek olarak hangi kilitlerle/güncellemelerle başlaması gerektiğini belirtmenizi sağlar. Bu, kilitlerin bir dizisi olmalıdır. Simülasyon, dizide bulunan tüm kilitlerin maksimum seviyeye yükseltildiği bir şekilde başlayacaktır.

Eğer maksimumdan farklı bir seviyeyi belirtmek isterseniz, kilitleri seviye haritasına dönüştüren bir dictionary iletebilirsiniz. Bu durumda, negatif değerler maksimum kilit seviyesine karşılık gelir.

### Başlangıç Eşyaları
Üçüncü argüman, eşyaları sayılara dönüştüren bir dictionary iletmenizi sağlar. Bu, simülasyonun hangi eşyalarla başlaması gerektiğini belirtir.

### Başlangıç Globalleri
Simülasyon tamamen yeni bir program yürütmesi başlattığı için, simülasyonu başlatan programdan değişkenlere erişemezsiniz. Ancak, dördüncü argümanı kullanarak simülasyona değerler iletmek mümkündür. Bu, değişken adlarının string şeklinde değerlere eşlendiği bir dict'tir. Bu değişkenler ardından simülasyon içindeki yürütmenin global scope'una eklenir.

Bu değerlerin tamamının kopyalandığını unutmayın, bu yüzden simülasyon içinde onları değiştirmeniz orijinal değerleri etkilemez. Çalıştırma süresi dışında simülasyondan değer döndürmek mümkün değildir.

### Rastgele Tohum 
Beşinci argüman, simülasyonda kullanılacak rastgele tohumun belirtilmesini sağlar. Bu, pozitif bir tamsayı olmalıdır. Negatif değerler rastgele bir tohum kullanılmasına neden olur.

Rastgele tohum, bitkilerin büyüme sürelerinden labirent düzenlerine ve suyun bozulma zamanlarına kadar her şeyi etkiler. Aynı rastgele tohum ve aynı başlangıç koşullarıyla aynı simülasyonu birçok kez başlattığınızda, sonucun her zaman aynı olması gerekir.

### Hızlandırma
Altıncı argüman, simülasyonun başlangıç hızlandırmasıdır. Bu, şeyleri hızlıca test etmenizi sağlar. Oyun ayarlanan hıza yetişemezse otomatik olarak yavaşlayacaktır.

Hızlandırma, simülasyon sonucunu hiçbir şekilde etkilemez. Yalnızca bekleme süresini azaltmak için bulunur.