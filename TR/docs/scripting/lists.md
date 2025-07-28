# List'ler
List'ler, birden çok değeri tek bir değişkende saklamanın kolay bir yoludur.
Yeni list'ler şu şekilde oluşturabilirsin:

`list = [2, True, Items.Hay]`

list şimdi `2`, `True` ve `Items.Hay` değerlerini içerir.
Bir list boş da olabilir:

`empty_list = []`

Bir list'in bir elemanına indeksi ile erişebilirsin. İndeks ilk eleman için `0`, ikinci eleman için `1`, üçüncü için `2`'dir...

havuç eker
`list = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(list[1])`

Bir for döngüsü kullanarak bir list üzerinde yineleme yapabilirsin. Aşağıdaki örnek, listedeki tüm elemanları toplar.

`list = [4, 7, 2, 5]
sum = 0
for number in list:
	sum += number`
`sum` şimdi `18`

Aşağıdaki list metotları eleman eklemeni ve kaldırmanı sağlar:

`list.append(elem)` list'in sonuna bir eleman ekler:

`list = [2, 6, 12]
list.append(7)`
`list` şimdi `[2, 6, 12, 7]`

`list.remove(elem)` bir listeden bir elemanın ilk geçtiği yeri kaldırır:

`list = [1, 2, 4, 2]
list.remove(2)`
`list` şimdi `[1, 4, 2]`

`list.insert(index, elem)` verilen indekse bir eleman ekler:

`list = [Entities.Tree, Items.Hay]
list.insert(1, Items.Wood)`
`list` şimdi `[Entities.Tree, Items.Wood, Items.Hay]`

`list.pop(index)` belirtilen indeksteki elemanı kaldırır.
Eğer bir indeks belirtilmezse, son eleman kaldırılır.

`list = [3, 5, 8, 25]
list.pop()`
`list` şimdi `[3, 5, 8]`
`list.pop(1)`
`list` şimdi `[3, 8]`

`len()` fonksiyonu list'in uzunluğunu döndürür.
`list = [3, 2, 1]
x = len(list)`
`x` şimdi `3`

List'ler referans semantiğine sahiptir. Bu, bir list'i bir değişkene atamanın, list'in bir kopyasını oluşturmak yerine, aynı list nesnesini o değişkene atadığı anlamına gelir.
Eğer iki değişken aynı list'e referans veriyorsa, list'teki değişiklikler her ikisi tarafından da görülecektir.

`a = [1,2]
b = a
b.pop()`
`a` ve `b` şimdi her ikisi de `[1]`
