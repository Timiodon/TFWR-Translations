# Hız Yükseltmesi
Çalışma hızı iki katına çıktı. Sorun şu ki, drone artık çimi büyüyebileceğinden daha hızlı biçiyor, bu da hiç hasat yapılamamasıyla sonuçlanıyor. Bu durumu kontrol etmek için [if](docs/scripting/if.md) dalları ve [can_harvest](functions/can_harvest) fonksiyonu artık kullanılabilir durumda.

## Hasattan Önce Kontrol Etmek
Şu ana kadar `if` ile birlikte çok da kullanışlı olmayan `True` ve `False` gibi koşullar kullanıyorduk.

Yeni can_harvest() fonksiyonu daha iyi bir koşul sunuyor. `can_harvest()` fonksiyonu, drone altındaki bitki biçilebilir durumda ise `True`, aksi takdirde `False` döndürür.

`if can_harvest():
	# bir şey yap`

Bu fonksiyonu bir koşul olarak kullanabilmenizin nedeni, boolean bir değer döndürmesidir.

Bir return değeri esasen, fonksiyon çağrısı tamamlandıktan sonra ifadeyi döndürülen değere değerlendirmek anlamına gelir.

Yukarıdaki kod çalıştığında ne olur:
	- if çalışır
	-`can_harvest()` çağrılır
	-`can_harvest()` gerekli işlemleri yapar
	-`can_harvest()` `True` veya `False` döndürür
	- ifadenin şekli `if True:` veya `if False:` olur
	- kod bloğu ancak biçme işlemi yapılabiliyorsa çalıştırılır

Artık dronenin çok erken biçmesini önlemek için `if` kullanabiliriz.