# Demetler
Demetler, birden fazla değeri tek bir değer olarak birleştirmenin harika bir yoludur.
Bir demet oluşturmak için, değerleri virgülle ayırmanız yeterlidir:

`tuple = 1, 2`

Ayrıca, demetleri yeniden birkaç değişkene ayırabilirsiniz. Aşağıdaki kodda, `(1,2)` demeti `a` ve `b` olmak üzere iki değişkene ayıklanıyor.

`a, b = 1, 2`

Demetler, listeler gibi indekslenebilir ama oluşturulduktan sonra değiştirilemezler.

`tuple = 1, 2`

`print(tuple[1])`
çıktısı `2`

`tuple[0] = 3`
bir hata verir
<unlock=dicts>
Listelerden farklı olarak demetler, dictionary içinde anahtar olarak kullanılabilir.

`d = {(1,2):(4,5)}

print(d[(1,2)])`
`çıktısı` (4,5)</unlock>

Ayrıca bir fonksiyondan birden fazla değer döndürmek için faydalı olabilirler.

`def f():
    return 1, 2

a, b = f()`