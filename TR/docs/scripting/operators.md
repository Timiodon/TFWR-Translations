# Operatörler
aritmetik operatörler: `+, -, *, /, //, %, **`
karşılaştırma operatörleri: `==, !=, <=, >=, <, >`
boolean operatörleri: `not, and, or`

Not: Oyundaki tüm sayılar floating point sayılardır. Bu nedenle tüm aritmetik operatörler floating point operatörleridir.
`//`, bölmeden sonra sayıyı aşağı yuvarlamak (floor) için tanımlanmıştır.

Atama operatörleri için "Değişkenler" kilidini açman gerekir.

## Giriş
Operatörler değerleri karşılaştırmana, değiştirimene ve birleştirimene olanak tanır. 
Aritmetik operatörler `+, -, *, /, //, %, **` sayılar üzerinde yaygın matematiksel işlemleri gerçekleştirmek için kullanılır. 
Karşılaştırma operatörleri `==, !=, <=, >=, <, >` değerleri karşılaştırmak için kullanılır. Sonuç her zaman ya `True` ya da `False` olur.
Mantık operatörleri (boolean operatörleri olarak da adlandırılır) `not, and, or` doğruluk değerlerini birleştirmek için kullanılır.

## Aritmetik Operatörler
`+` ve `-` toplama ve çıkarma için kullanılır.

`2 + 3` ifadesi `5` olarak değerlendirilir
`3 - 2` ifadesi `1` olarak değerlendirilir

`*`, `/` ve `//` çarpma ve bölme için kullanılır.

`2 * 3` ifadesi `6` olarak değerlendirilir
`5 / 2` ifadesi `2.5` olarak değerlendirilir

`//` ile `/` aynı şeyi yapar, ancak sonuç aşağı yuvarlanır (bir sonraki tam sayıya yuvarlanır).

`5 // 2` ifadesi `2` olarak değerlendirilir

`%`, modülo operatörüdür, kalan operatörü olarak da bilinir. Temelde iki sayıyı böler ve sonra kalanı döndürür. Sağdaki sayıyı soldaki sayıdan, kalan sağdaki sayıdan küçük olana kadar tekrar tekrar çıkarmak olarak da düşünebilirsin.

`4 % 2` ifadesi `0` olarak değerlendirilir
`5 % 2` ifadesi `1` olarak değerlendirilir
`6 % 2` ifadesi `0` olarak değerlendirilir
`2 % 6` ifadesi `2` olarak değerlendirilir
`1.5 % 1` ifadesi `0.5` olarak değerlendirilir

`**`, üs alma operatörüdür.

`2**2` ifadesi `4` olarak değerlendirilir
`(-5)**3` ifadesi `-125` olarak değerlendirilir

## Karşılaştırma Operatörleri
`==` ve `!=` iki değerin "eşit"(`==`) veya "eşit değil"(`!=`) olup olmadığını kontrol etmek için kullanılır. Her tür değer üzerinde kullanılabilirler.

`2 == 2` ifadesi `True` olarak değerlendirilir
`Entities.Bush != Entities.Bush` ifadesi `False` olarak değerlendirilir
`3 != 3 + 1` ifadesi `True` olarak değerlendirilir

`<=, >=, <, >` sadece sayılar üzerinde kullanılabilir. Sol sayının sağ sayıdan "küçük veya eşit"(`<=`), "büyük veya eşit"(`>=`), "küçük" (`<`) veya "büyük" (`>`) olup olmadığını kontrol ederler.

`1 <= 1` ifadesi `True` olarak değerlendirilir
`2 >= 3` ifadesi `False` olarak değerlendirilir
`-2 < -1` ifadesi `True` olarak değerlendirilir
`6 > 6` ifadesi `False` olarak değerlendirilir

## Mantık Operatörleri
`not` sadece değeri tersine çevirir:

`not False` ifadesi `True` olarak değerlendirilir
`not True` ifadesi `False` olarak değerlendirilir

`and` sadece her iki değer de `True` ise `True` olarak değerlendirilir

`True and True` ifadesi `True` olarak değerlendirilir
`True and False` ifadesi `False` olarak değerlendirilir
`False and False` ifadesi `False` olarak değerlendirilir

`or` en az bir değer `True` ise `True` olarak değerlendirilir

`True or True` ifadesi `True` olarak değerlendirilir
`True or False` ifadesi `True` olarak değerlendirilir
`False or False` ifadesi `False` olarak değerlendirilir