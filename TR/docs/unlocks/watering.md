# Sulama
Bitkiler sulandığında daha hızlı büyür. Toprağın su seviyesi `0` ile `1` arasında değişir.
`get_water()` fonksiyonu, bulunduğu yerin su seviyesini döner.

Bir bitkinin büyüme hızı, su seviyesi `0` iken 1 kat hızdan, `1` iken 5 kat hıza kadar lineer olarak artar.

Zamanla toprak kurur: Ortalama olarak, her saniyede mevcut suyunun %1'ini kaybeder, fakat bunda biraz rastgelelik de vardır. Yüksek bir su seviyesini korumak, düşük bir su seviyesini korumaktan çok daha fazla su tüketir.

Bitkilerinize su kullanabilirsiniz. Her 10 saniyede bir tank su otomatik olarak envanterinize eklenir.
`Unlocks.Watering` yükseltmesini yapmak, her 10 saniyede bir ek tank su kazanmanızı sağlar.

Bir tank `0.25` su tutar.

Herhangi bir yere su vermek için `use_item(Items.Water)` çağrısı yapabilirsiniz.