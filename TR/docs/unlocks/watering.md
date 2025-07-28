# Sulama
Bitkiler sulandığında daha hızlı büyür. Zeminin `0` ile `1` arasında değişen bir su seviyesi vardır.
`get_water()` fonksiyonu, üzerinde bulunduğu zeminin su seviyesini döndürür.

Bir bitkinin büyüme hızı, su seviyesi 0'da 1 kat hızdan su seviyesi 1'de 5 kat hıza doğrusal olarak artar.

Zemin zamanla kurur: Ortalama olarak, saniyede mevcut suyunun %1'ini kaybeder, ancak bunda biraz rastgele değişkenlik vardır. Yüksek bir su seviyesini korumak, düşük bir su seviyesini korumaktan çok daha fazla su tüketecektir.

Bitkilerinde su kullanabilirsin. Her 10 saniyede bir, envanterine otomatik olarak bir su tankı eklenir.
`Unlocks.Watering`'i yükseltmek sana her 10 saniyede bir ek bir su tankı verir.

Bir tank `0.25` su alır.

Zemini sulamak için herhangi bir zeminin üzerinde `use_item(Items.Water)` çağır.