# Değişkenler
Değişkenler, bir değeri tutabilen isimlendirilmiş kaplar olarak düşünülebilir. 
Bir değişken tanımlamak ve içine bir değer depolamak için `=` operatörü kullanılır.

`variable_name = value`

Operatörün sol tarafı değişkenin adı olur. Ona istediğin herhangi bir ismi verebilirsin. 
Sağ taraf ise, elde edilen değerin değişkende saklanacağı bir ifadedir.

Adı `a` olan bir değişken tanımla ve içine `5` değerini depola:
`a = 5`
Adı `b` olan bir değişken tanımla ve içine `can_harvest()` fonksiyonunun dönüş değerini depola:
`b = can_harvest()`

`=` operatörünü `==` operatörü ile karıştırma. 
`==` operatörü iki değerin eşit olup olmadığını kontrol eder ve sonuç olarak `True` ya da `False` döner. 
`=` operatörü ise sağdaki değeri, soldaki isme atar.

Bir değişkene değer atandıktan sonra, o değişkeni kodda içeriğini yani değerini elde etmek için kullanabilirsin.

`a = 5
for i in range(a):
	do_a_flip()`

Yukarıdaki döngü 5 kez çalıştırılır çünkü `a` değeri `5` olarak ayarlanmıştır. 
`for` döngüsündeki `i` de otomatik olarak döngüdeki her bir adımda sıradaki değeri alan bir değişkendir. (İlla ki `i` olmak zorunda değil, ona geçerli herhangi bir değişken adı verebilirsin.)

Değişkenlerle aynı şeyi bir while döngüsüyle de yapabilirsin:

`a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1`

Bu da yukarıdaki for döngüsüyle aynı işi yapar. Sadece bu sefer i'yi elle artırmamız gerekiyor.
i'yi artırmak için kendi değerine `1` eklediğimize dikkat et. Bir değişkenin değerini, önceki değerine dayalı olarak değiştirmek oldukça yaygındır. 
Bu işlem şu operatörlerle kısaltılabilir: `+=, -=, *=, /=, %=`

`i = i + 1` ifadesi `i += 1` ile aynıdır
`a = a / 3` ifadesi `a /= 3` ile aynıdır.