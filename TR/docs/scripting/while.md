# While Döngüsü
`while` döngüsünü ve `True` ile `False` değerlerini açtın. `while` döngüsü, koşul `True` olduğu sürece döngü gövdesini yürütmeye devam eder.

`while koşul:
	#döngü gövdesi`

Sonsuz döngüler oluşturma konusunda endişelenme. Yürütmedeki gecikmeler programın donmasını önleyecektir.

## Yeni Başlayanlar İçin
Belki de zaten birkaç `harvest()` çağrısını arka arkaya koymayı denedin:

`harvest()
harvest()
harvest()`

Bu, bir program çalıştırmasında birkaç kez hasat yapmanı sağlar. 
Ancak, üç defadan fazla hasat yapmak güzel olurdu ve aynı kodu birden çok kez yazmak kötü bir uygulamadır. 
Çözüm bir döngüdür. 
Bir döngü, aynı kodu birden çok kez çalıştırmana olanak tanır.

While döngüsü, yalnızca iki durumda olabilen mantıksal bir değer olan bir koşul alır: `True` veya `False`. 
Böyle bir değere Boolean değeri denir.

Döngü daha sonra, koşul False olana kadar döngü içindeki kodu yürütür.
While döngüsü şöyle görünür:

`while koşul:
	#döngü gövdesi
	#döngü gövdesi
	#...`
	
Burada "koşul" yerine bir boolean değeri ve `#döngü gövdesi` yerine döngüde yapmak istediğin her şeyi koyman gerekir.

İki sabit boolean değeri mevcuttur. Sabitler, program sırasında asla değişmeyen değerlerdir.

Her zaman `True` olan bir sabit boolean değeri oluşturmak için, sadece `True` yazabilirsin. Her zaman `False` olacak bir sabit boolean değeri için `False` yaz.
Dolayısıyla ya şöyle yazabilirsin


`while False:
	do_a_flip()`

ya da

`while True:
	do_a_flip()`

İlki asla takla atmaz ve ikincisi sonsuza kadar takla atar (sonsuz bir döngü). 

Normalde sonsuz bir döngü oluşturmak kötü bir fikirdir çünkü programı dondurur, ancak bu oyunda döngünün her yinelemesi arasında gecikmeler vardır, bu yüzden drone'un, sen yürüt düğmesine tekrar basarak manuel olarak durdurana kadar takla atmaya devam etmesine neden olur.

İki nokta üst üste işaretinden sonraki satırın nasıl girintili olduğuna dikkat et. Bunun gibi girintileme, kod bloklarını ayırmak için kullanılır.
Girinti eklemek için Tab'a, kaldırmak için Shift + Tab'a (veya Backspace'e) bas.

Döngü, iki nokta üst üste işaretinden sonraki tüm girintili ifadeleri tekrarlayacaktır.
Girintili bloktan sonraki ifadeler, döngü bittikten sonra yürütülecektir.
