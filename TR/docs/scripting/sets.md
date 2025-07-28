# Set'ler
Set'ler [dictionary'lere](docs/scripting/dicts.md) benzer, ama değerleri yoktur. Sadece sırasız bir anahtar kümesidirler. 

Dictionary'ler gibi oluşturulurlar, ama değerleri yoktur.
`set = {North, East, West}`

Boş bir set oluşturmak için `set()` kullan. `{}`'nin boş bir dictionary oluşturduğunu unutma.

Set'e yeni bir eleman eklemek için `set.add(elem)` kullan.

Bir set'ten bir eleman kaldırmak için `set.remove(elem)` kullan.

Set'in bir eleman içerip içermediğini kontrol etmek için `if elem in set:` kullan.

Set'teki tüm elemanları yinelemek için `for elem in set:` kullan.
Daha büyük set'ler için `in` operatörü, bir list üzerinde olacağından çok daha hızlı performans gösterir.

Tıpkı dictionary'ler gibi, set'ler de sırasızdır, bu nedenle elemanların hangi sırayla yineleneceği konusunda hiçbir garanti yoktur.

Ayrıca, set'lerdeki elemanlar benzersizdir, bu yüzden sette zaten bulunan bir elemanı eklemek seti değiştirmez.