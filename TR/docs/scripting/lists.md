# Listeler
Listeler, bir değişkende birden fazla değeri saklamanın kolay bir yoludur.
Yeni listeler şöyle oluşturulabilir:

`list = [2, True, Items.Hay]`

Liste artık `2`, `True` ve `Items.Hay` değerlerini içeriyor.
Bir liste boş da olabilir:

`empty_list = []`

Bir listenin bir öğesine indeks numarasıyla erişebilirsiniz. İlk öğe için indeks `0`, ikinci öğe için `1`, üçüncü için `2`...

havuçları ek
`list = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(list[1])`

Bir for döngüsü kullanarak bir liste üzerinde iterate edebilirsiniz. Aşağıdaki örnek, listedeki tüm öğelerin toplamını hesaplar.

`list = [4, 7, 2, 5]
sum = 0
for number in list:
	sum += number`
`sum` artık `18` değerini alır

Aşağıdaki liste metodları, öğe ekleyip çıkarmaya olanak tanır:

`list.append(elem)` listeye bir öğeyi sonuna ekler:

`list = [2, 6, 12]
list.append(7)`
`list` artık `[2, 6, 12, 7]`

`list.remove(elem)` bir listedeki bir öğenin ilk bulunuşunu kaldırır:

`list = [1, 2, 4, 2]
list.remove(2)`
`list` artık `[1, 4, 2]`

`list.insert(index, elem)` verilen indekse bir öğe ekler:

`list = [Entities.Tree, Items.Hay]
list.insert(1, Items.Wood)`
`list` artık `[Entities.Tree, Items.Wood, Items.Hay]`

`list.pop(index)` belirli indeksdeki öğeyi kaldırır.
Eğer bir indeks belirtilmemişse, son öğe kaldırılır.

`list = [3, 5, 8, 25]
list.pop()`
`list` artık `[3, 5, 8]`
`list.pop(1)`
`list` artık `[3, 8]`

`len()` fonksiyonu listenin uzunluğunu döndürür.
`list = [3, 2, 1]
x = len(list)`
`x` artık `3`

Listeler referans semantiğine sahiptir. Bu, bir listeyi bir değişkene atamanın, liste kopyası oluşturmak yerine aynı liste nesnesini o değişkene atadığı anlamına gelir.
Eğer iki değişken aynı listeyi referans alıyorsa, listedeki değişiklikler her iki listede de görülür.

`a = [1,2]
b = a
b.pop()`
`a` ve `b` şimdi her ikisi de `[1]` durumunda.