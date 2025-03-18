# Ağaçlar
[Ağaçlar](objects/tree) çalılardan daha iyi bir şekilde odun elde etmenizi sağlar. Her biri 5 odun verir. Çalılar gibi, çim veya toprağa dikilebilir.

Ağaçlar biraz alana ihtiyaç duyar ve yan yana dikildiklerinde büyümeleri yavaşlar. Kuzey, doğu, batı veya güney taraflarında doğrudan bir karoda ağaç olduğunda büyüme süresi iki katına çıkar. Yani her karoya ağaç dikerseniz, büyümeleri `2*2*2*2 = 16` kat daha uzun sürer.

<spoiler=show> Burada `%` operatörü kullanışlı olabilir. `%` operatörünün bölme işleminden kalan sayıyı döndürdüğünü unutmayın. `2`'ye bölünen çift sayılar `0` kalanına sahiptir ve `2`'ye bölünen tek sayılar `1` kalanına sahiptir.
Bu şekilde bir sayının çift olup olmadığını kontrol edebilirsiniz:

`def is_even(n):
	return n % 2 == 0`

Eğer n çift ise `True` döndürür, değilse `False` döndürür.
</spoiler>