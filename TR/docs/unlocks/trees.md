# Ağaçlar
[Ağaçlar](objects/tree), çalılardan odun elde etmenin daha iyi bir yoludur. Her biri 5 odun verir. Çalılar gibi, çimen veya toprağa ekilebilirler.

Ağaçlar biraz alana sahip olmayı sever ve onları yan yana ekmek büyümelerini yavaşlatır. Büyüme süresi, hemen kuzeyinde, doğusunda, batısında veya güneyinde bir karoda bulunan her ağaç için iki katına çıkar. Yani her karoya ağaç ekersen, büyümeleri `2*2*2*2 = 16` kat daha uzun sürer.

<spoiler=göster> `%` operatörü burada faydalı olabilir. `%` operatörünün bölmenin kalanını döndürdüğünü unutma. `2`'ye bölünen çift sayıların kalanı `0`, `2`'ye bölünen tek sayıların kalanı `1`'dir.
Yani bir sayının çift olup olmadığını şu şekilde kontrol edebilirsin:

`def is_even(n):
	return n % 2 == 0`

Bu, n çift ise `True`, değilse `False` döndürür.
</spoiler>