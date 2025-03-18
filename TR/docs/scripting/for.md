# For Döngüsü
`for` döngüsü Python'daki gibi çalışır. (Bazı dillerde foreach döngüsü olarak adlandırılır, C tarzı for döngüsü ile karıştırılmamalıdır.)

`for i in sequence:
	#do something with i`

`while` döngüsüne benzer şekilde, `for` döngüsü de bir kod bloğunu tekrar tekrar çağırır. Ancak bir koşula dayalı tekrar yerine, bir dizideki her bir eleman için döngü gövdesini bir kez çalıştırır.

## Sözdizimi
Bir for döngüsü şöyle görünür:

`for variable_name in sequence:
	#code block`

`variable_name` istediğiniz herhangi bir isim olabilir. Bu, dizideki mevcut elemanı saklayan bir değişkendir. `sequence` ise bir aralık veya sayılar gibi üzerine yinelenebilecek bir değer olmalıdır. Kod bloğu, döngü değişkeni her bir elemana atanarak çalıştırılır.

## Diziler
[Alanlar](functions/range)      <unlock=lists>[Listeler](docs/scripting/lists.md)      </unlock><unlock=functions>[Demetler](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Sözlükler](docs/scripting/dicts.md)      </unlock><unlock=sets>[Kümeler](docs/scripting/sets.md)</unlock>

## Örnek
`for i in range(5):
    harvest()`

Bu döngü, gövdesini sabit sayıda çalıştırır. Esasen şu şekilde yazmaya eşdeğerdir:

`i = 0
harvest()
i = 1
harvest()
i = 2
harvest()
i = 3
harvest()
i = 4
harvest()`

Yani `harvest()` fonksiyonunu 5 kez çağırır.

Ayrıca bakınız [Break](docs/scripting/break.md) ve [Continue](docs/scripting/continue.md)