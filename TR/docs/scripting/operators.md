# Operatörler
aritmetik operatörler: `+, -, *, /, //, %, **`
karşılaştırma operatörleri: `==, !=, <=, >=, <, >`
mantıksal operatörler: `not, and, or`

Not: Oyundaki tüm sayılar floating point (kayan nokta) sayılardır. Dolayısıyla tüm aritmetik operatörler floating point operatörleridir.
`//` bölme işleminden sonra sadece sonucu aşağıya yuvarlamak olarak tanımlanmıştır.

Atama operatörlerini kullanabilmek için "Değişkenler" kilidini açmanız gerekiyor.

## Giriş
Operatörler, değerleri karşılaştırmanıza, değiştirmenize ve birleştirmenize olanak tanır.
Aritmetik operatörler `+, -, *, /, //, %, **`, sayılar üzerinde yaygın matematiksel işlemleri gerçekleştirmek için kullanılır.
Karşılaştırma operatörleri `==, !=, <=, >=, <, >` değerleri karşılaştırmak için kullanılır. Sonuç her zaman ya `True` ya da `False` olur.
Mantıksal operatörler (boolean operatörler olarak da adlandırılır) `not, and, or`, doğru değerlerini birleştirmek için kullanılır.

## Aritmetik Operatörler
`+` ve `-` toplama ve çıkarma için kullanılır.

`2 + 3` değeri `5` olur
`3 - 2` değeri `1` olur

`*`, `/` ve `//` çarpma ve bölme için kullanılır.

`2 * 3` değeri `6` olur
`5 / 2` değeri `2.5` olur

`//` `/` ile aynı işi yapar ama sonuç aşağıya yuvarlanmış (en yakın tam sayıya aşağı doğru) olur.

`5 // 2` değeri `2` olur

`%` modulo operatörü, yani kalan operatörüdür. İki sayıyı böler ve ardından kalanı döndürür. Sağdaki sayıyı soldaki sayıdan defalarca çıkarıp geriye kalan, sağdaki sayıdan küçük olana kadar devam eder.

`4 % 2` değeri `0` olur
`5 % 2` değeri `1` olur
`6 % 2` değeri `0` olur
`2 % 6` değeri `2` olur
`1.5 % 1` değeri `0.5` olur

`**` üslü sayı operatörüdür.

`2**2` değeri `4` olur
`(-5)**3` değeri `-125` olur

## Karşılaştırma Operatörleri
`==` ve `!=`, iki değerin "eşit" (`==`) veya "eşit değil" (`!=`) olup olmadığını kontrol etmek için kullanılır. Bu, her tür değerde kullanılabilir.

`2 == 2` değeri `True` olur
`Entities.Bush != Entities.Bush` değeri `False` olur
`3 != 3 + 1` değeri `True` olur

`<=, >=, <, >` operatörleri sadece sayılar üzerinde kullanılabilir. Soldaki sayının, sağdaki sayıdan "küçük veya eşit" (`<=`), "büyük veya eşit" (`>=`), "küçük" (`<`) veya "büyük" (`>`) olup olmadığını kontrol eder.

`1 <= 1` değeri `True` olur
`2 >= 3` değeri `False` olur
`-2 < -1` değeri `True` olur
`6 > 6` değeri `False` olur

## Mantıksal Operatörler
`not` sadece değeri tersine çevirir:

`not False` değeri `True` olur
`not True` değeri `False` olur

`and` her iki değer de `True` olduğunda `True` döner.

`True and True` değeri `True` olur
`True and False` değeri `False` olur
`False and False` değeri `False` olur

`or` en az bir değer `True` olduğunda `True` döner.

`True or True` değeri `True` olur
`True or False` değeri `True` olur
`False or False` değeri `False` olur