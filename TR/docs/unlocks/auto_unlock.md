# Otomatik Kilit Açmalar
Oyunu tamamen otomatikleştirmek için, özellikleri otomatik olarak açmak üzere `unlock()` fonksiyonunu kullanabilirsin.
Örneğin, hız ve genişleme özelliklerini açmak için `unlock(Unlocks.Speed)` ve `unlock(Unlocks.Expand)` kullanabilirsin.

Bir kilit açmanın maliyetini belirlemek için, bir bitki veya eşya için yaptığın gibi `get_cost()` fonksiyonunu kullanman yeterlidir.
Örnek:
`get_cost(Unlocks.Loops)`
`{Items.Hay:5}` döndürür

Belirli bir kilit açmadan kaç tane olduğunu öğrenmek istiyorsan, `num_unlocked(unlock)` fonksiyonunu kullan.

Örneğin, `num_unlocked(Unlocks.Speed)`, sahip olduğun hız yükseltmelerinin sayısını döndürür.

`num_unlocked(Unlocks.Senses)`, duyular açılmışsa `1`, değilse `0` döndürür.

Ayrıca `num_unlocked()`'ı Eşyalar, Varlıklar veya Zeminler üzerinde de kullanabilirsin. Bu, kilidi açıksa `1`, aksi takdirde `0` döndürür.

Dikkatli ol, `num_unlocked(Unlocks.Carrots)` kaç kez kilidinin açıldığını/yükseltildiğini döndürür.
`num_unlocked(Items.Carrot)` sadece `0` veya `1` döndürür. (Diğer bitkiler için de aynı)