# While Döngüsü
Artık `while` döngüsünü ve `True` ve `False` değerlerini açtınız. `while` döngüsü, koşul `True` olduğu sürece döngü gövdesini çalıştırmaya devam eder.

`while condition:
	#döngü gövdesi`

Sonsuz döngüler oluşturma konusunda endişelenme. Yürütme sırasında gecikmeler, programın donmasını önleyecektir.

## Yeni Başlayanlar İçin
Belki de zaten birkaç `harvest()` çağrısını arka arkaya yazmayı denemişsindir:

`harvest()
harvest()
harvest()`

Bu, bir program çalıştırmasında birden fazla kez hasat yapmanı sağlar.
Ancak, üçten fazla hasat etmek ve aynı kodu tekrar tekrar yazmak kötü bir pratiktir.
Çözüm bir döngü kullanmaktır.
Bir döngü, aynı kodu birçok kez çalıştırmanı sağlar.

While döngüsü, yalnızca iki durumda olabilen mantıksal bir değer olan bir koşul alır: `True` veya `False`.
Bu tür bir değere Boolen değeri denir.

Döngü, koşul `False` olana kadar döngü içindeki kodu çalıştırır.
While döngüsü şu şekilde görünür:

`while condition:
	#döngü gövdesi
	#döngü gövdesi
	#...`
	
Burada "condition" ifadesini bir boolen değerle, `#döngü gövdesi` kısmını ise döngüde yapmak istediğiniz işlemlerle değiştirmelisiniz.

İki tane sabit boolen değeri vardır. Sabitler, program süresince değişmeyen değerlerdir.

Her zaman `True` olan sabit bir boolen değer oluşturmak için sadece `True` yazabilirsiniz. Her zaman `False` olacak sabit bir boolen değer oluşturmak için de `False` yazın.
Bu yüzden şunları yazabilirsiniz


`while False:
	do_a_flip()`

veya

`while True:
	do_a_flip()`

İlk örnek hiçbir zaman takla atmayacak, ikinci ise sonsuza kadar takla atacak (sonsuz döngü).

Normalde bir sonsuz döngü oluşturmak kötü bir fikirdir çünkü programı dondurur ama bu oyunda döngünün her yinelemesi arasında bir gecikme vardır, böylece dronenin takla atmasını sürdürmesini sağlarken, sen yürütme düğmesine tekrar basarak manuel olarak durdurabilirsin.

Dikkat et, iki nokta üst üste (:)'dan sonra gelen satır girintili. Bu tür bir girinti, kod bloklarını ayırmak için kullanılır.
Girinti eklemek için Tab tuşuna bas ve girintiyi kaldırmak için Shift + Tab (veya Backspace) tuşlarına bas.

Döngü, iki nokta üst üste (:) işaretinden sonra girintili olan tüm emirleri tekrar eder.
Girintili bloktan sonraki emirler, döngü tamamlandıktan sonra yürütülür.