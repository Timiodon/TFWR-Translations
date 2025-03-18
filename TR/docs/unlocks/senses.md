# Algılar
Drone artık görebiliyor!

`get_pos_x()` ve `get_pos_y()` fonksiyonları, dronenin mevcut x ve y pozisyonunu döner. Başlangıç pozisyonunda her ikisi de `0`'dır. X pozisyonu, her kare için `East` yönüne doğru `1` artar ve y pozisyonu her kare için `North` yönüne doğru `1` artar.

`num_items(item)`, bir eşyadan kaç tane olduğunu döner.
Örneğin, `num_items(Items.Hay)` ne kadar samanınız olduğunu döner.

`get_entity_type()` ve `get_ground_type()`, dronenin altında bulunan varlık veya zeminin türünü döner.

Bir çalının üzerindeysen talimatlar:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

`None` anahtar kelimesi de artık kullanılabilir! `None`, bir değerin olmadığını temsil eden bir değerdir.
Örneğin, `return` ifadesi olmayan bir fonksiyon aslında `None` döner.

`get_entity_type()`, dronenin altında bir varlık yoksa `None` döner.