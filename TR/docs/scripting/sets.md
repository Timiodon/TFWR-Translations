# Setler
Setler [sözlükler](docs/scripting/dicts.md) gibidir, ama değerleri yoktur. Sadece sırasız bir anahtarlar kümesi.

Setler, sözlükler gibi oluşturulur ama değerleri olmaz.
`set = {North, East, West}` 

Boş bir set oluşturmak için `set()` kullanın. Unutmayın, `{}` boş bir sözlük oluşturur.

Sete yeni bir eleman eklemek için `set.add(elem)` kullanın.

Setten bir eleman çıkarmak için `set.remove(elem)` kullanın.

Setin bir eleman içerip içermediğini kontrol etmek için `if elem in set:` kullanın.

Set içerisindeki tüm elemanları tekrarlamak için `for elem in set:` kullanın.
Daha büyük setler için `in` operatörü, listeye göre çok daha hızlı çalışır.

Sözlükler gibi, setler de sırasızdır, bu yüzden elemanların hangi sırada tekrarlanacağının garantisi yoktur.

Ayrıca, setlerdeki elemanlar benzersizdir, bu yüzden sete zaten bulunan bir eleman eklemek seti değiştirmez.