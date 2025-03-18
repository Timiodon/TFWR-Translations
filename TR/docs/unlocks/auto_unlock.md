# Otomatik Kilit Açma
Oyunu tamamen otomatikleştirmek için, özellikleri otomatik olarak açmak adına `unlock()` fonksiyonunu kullanabilirsiniz.
Örneğin, hız ve genişleme özelliklerini açmak için `unlock(Unlocks.Speed)` ve `unlock(Unlocks.Expand)` kodlarını kullanabilirsiniz.

Bir kilidin maliyetini belirlemek için, bir bitki veya eşya için olduğu gibi `get_cost()` fonksiyonunu kullanmanız yeterlidir.
Örnek:
`get_cost(Unlocks.Loops)`
`{Items.Hay:5}` döndürür

Belirli bir kilidin kaç tane olduğunu öğrenmek isterseniz, `num_unlocked(unlock)` fonksiyonunu kullanın.

Örneğin, `num_unlocked(Unlocks.Speed)` sahip olduğunuz hız yükseltmelerinin sayısını döndürecektir.

`num_unlocked(Unlocks.Senses)` eğer duyu özelliği açıksa `1`, değilse `0` döner.

Ayrıca, `num_unlocked()` fonksiyonunu Eşyalar, Varlıklar veya Zeminler üzerinde de kullanabilirsiniz. Bu, eğer açıksa `1` aksi takdirde `0` döner.

Dikkat edin, `num_unlocked(Unlocks.Carrots)` kilidin kaç kez açıldığını/yükseltildiğini gösterecektir.
`num_unlocked(Items.Carrot)` yalnızca `0` veya `1` döner. (Diğer bitkiler için de aynı şekilde)