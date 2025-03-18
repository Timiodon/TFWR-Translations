# Sulama
Bitkiler sulandığında daha hızlı büyür. Toprağın su seviyesi `0` ile `1` arasında değişir.
`get_water()` fonksiyonu, bulunduğu yerin su seviyesini döner.

Bir bitkinin büyüme hızı, su seviyesi `0` iken 1 kat hızdan, su seviyesi `1` iken 5 kat hıza doğrusal olarak artar.

Toprak zamanla kurur: Ortalama olarak her saniyede mevcut suyunun %1'ini kaybeder, fakat bunda biraz rastgelelik de vardır. Yüksek bir su seviyesini korumak, düşük bir su seviyesini korumaktan çok daha fazla su tüketir.

Bitkilerinizi sulamak için su tanklarını kullanabilirsiniz. Her 10 saniyede bir envanterinize otomatik olarak bir su tankı eklenir.
`Unlocks.Watering`'i yükseltmek, her 10 saniyede size ek bir su tankı sağlar.

Bir tank `0.25` su taşır.

Herhangi bir toprağı sulamak için o yerin üzerinde `use_item(Items.Water)` fonksiyonunu çağırın.