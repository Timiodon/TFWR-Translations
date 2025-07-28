# Duyular
Drone artık görebiliyor! 

`get_pos_x()` ve `get_pos_y()` fonksiyonları, drone'un mevcut x ve y pozisyonunu döndürür. Başlangıç pozisyonunda her ikisi de `0`'dır. x pozisyonu `East` yönüne doğru her karoda `1` artar ve y pozisyonu `North` yönüne doğru her karoda `1` artar.

`num_items(item)` bir eşyadan ne kadar olduğunu döndürür.
Örneğin `num_items(Items.Hay)` ne kadar samanın olduğunu döndürür.

`get_entity_type()` ve `get_ground_type()`, drone'un altındaki varlık veya zemin türünü döndürür.

Eğer bir çalının üzerindeyse takla at:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

`None` anahtar kelimesi de artık açıldı! `None`, bir değer olmadığını temsil eden bir değerdir.
Örneğin, `return` ifadesi olmayan bir fonksiyon aslında `None` döndürür.

Drone'un altında bir varlık yoksa `get_entity_type()` `None` döndürür.
