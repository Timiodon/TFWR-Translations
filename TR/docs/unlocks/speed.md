# Hız Yükseltmesi
Yürütme hızı iki katına çıktı. Sorun şu ki, drone artık çimenlerin büyüyebileceğinden daha hızlı hasat yapıyor, bu da hiç hasat yapılamamasına neden oluyor. Bununla başa çıkmak için [if](docs/scripting/if.md) dallanmaları ve [can_harvest](functions/can_harvest) fonksiyonu artık açık.

## Hasattan Önce Kontrol Etme
Şimdiye kadar koşul olarak sadece `True` ve `False` kullandık, bu da `if` ile pek kullanışlı değil.

Yeni `can_harvest()` fonksiyonu daha iyi bir koşul sağlar. `can_harvest()`, drone'un altındaki bitki hasat edilebiliyorsa `True`, aksi takdirde `False` döndürür.

`if can_harvest():
	#bir şeyler yap`

Bu fonksiyonu bu şekilde bir koşul olarak kullanabilmenin sebebi, bir boolean değeri döndürmesidir.

Bir dönüş değeri, temel olarak, fonksiyon yürütüldükten sonra, fonksiyon çağrı ifadesinin döndürülen değere dönüştüğü anlamına gelir.

Yukarıdaki kod çalıştığında ne olur:
	-if çalışır
	-`can_harvest()` çağrılır
	-`can_harvest()` kendi işini yapar
	-`can_harvest()` `True` veya `False` döndürür
	-ifade şimdi `if True:` veya `if False:` olur
	-kod bloğu sadece hasat yapılabiliyorsa çalıştırılır

Artık drone'un çok erken hasat yapmasını önlemek için `if` kullanabiliriz.