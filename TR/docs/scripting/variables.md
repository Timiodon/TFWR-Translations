# Değişkenler
Değişkenler, bir değer tutabilen isimlendirilmiş kaplar olarak düşünülebilir.
`=` operatörü, bir değişken bildirmek ve içinde bir değer saklamak için kullanılır.

`degisken_adi = deger`

Operatörün sol tarafı değişken adıdır. İstediğin herhangi bir adı verebilirsin.
Sağ taraf, sonuç değeri değişkende saklanacak olan bir ifadedir.

`a` adında bir değişken bildir ve içine `5` değerini sakla:
`a = 5`
`b` adında bir değişken bildir ve içine `can_harvest()` fonksiyonunun dönüş değerini sakla:
`b = can_harvest()`

`=` operatörünü `==` operatörüyle karıştırma. 
`==` operatörü iki değerin eşit olup olmadığını kontrol eder ve `True` veya `False` döndürür.
`=` operatörü sağdaki değeri soldaki isme atar.

Bir değişken atandıktan sonra, içerdiği değeri almak için kodda kullanabilirsin

`a = 5
for i in range(a):
	do_a_flip()`

Yukarıdaki döngü, `a` `5`'e ayarlandığı için 5 kez yürütülür.
`for` döngüsündeki `i` de, döngünün her yinelemesinde dizinin mevcut değerini otomatik olarak atanan bir değişkendir. (`i` olarak adlandırılması gerekmez, ona herhangi bir geçerli değişken adı verebilirsin.)

Değişkenler ayrıca bir while döngüsüyle aynı şeyi yapmanı sağlar:

`a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1`

Bu, yukarıdaki for döngüsüyle aynı şeyi yapar. Sadece i'yi manuel olarak artırmamız gerekiyor.
i'yi artırmak için, onu kendi değerine artı `1` olarak ayarladığımızı unutma. Bir değişkenin değerini önceki değerine göre değiştirmek çok yaygın bir şeydir. 
Bu operatörler kullanılarak kısaltılabilir: `+=, -=, *=, /=, %=`

`i = i + 1` ile `i += 1` aynıdır
`a = a / 3` ile `a /= 3` aynıdır
