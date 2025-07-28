# For Döngüsü
`for` döngüsü Python'daki gibi çalışır. (Bazı dillerde foreach döngüsü olarak adlandırılır, C tarzı for döngüsü ile karıştırılmamalıdır, o farklı bir şeydir).

`for i in sequence:
	#i ile bir şeyler yap`

`while` döngüsüne benzer şekilde, `for` döngüsü de tekrar tekrar bir kod bloğunu çağırır. Bir koşula göre döngü yapmak yerine, bir dizideki her eleman için döngü gövdesini bir kez yürütür.

## Syntax
Bir for döngüsü şuna benzer:

`for variable_name in sequence:
	#kod bloğu`

`variable_name` seçtiğin herhangi bir ad olabilir. Bu, dizideki mevcut elemanı depolayan bir değişkendir. `sequence`, bir sayı aralığı gibi yinelenebilen bir değer olmalıdır. Kod bloğu, döngü değişkeni o elemana atanmış olarak her eleman için yürütülür.

## Diziler
[Aralıklar](functions/range)      <unlock=lists>[Listeler](docs/scripting/lists.md)      </unlock><unlock=functions>[Tuple'lar](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Dictionaries](docs/scripting/dicts.md)      </unlock><unlock=sets>[Sets](docs/scripting/sets.md)</unlock>

## Örnek
`for i in range(5):
    harvest()`

Bu döngü, gövdeyi sabit sayıda yürütür. Esasen şununla aynıdır:

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

Bu yüzden `harvest()`'ı 5 kez çağırır.

Ayrıca bakınız [Break](docs/scripting/break.md) ve [Continue](docs/scripting/continue.md)