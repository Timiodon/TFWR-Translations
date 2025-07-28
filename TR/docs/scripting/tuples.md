# Tuple'lar
Tuple'lar, birden fazla değeri tek bir değerde birleştirmenin harika bir yoludur.
Bir tuple oluşturmak için, değerleri virgülle ayırman yeterli:

`tuple = 1, 2`

Onları tekrar birkaç değişkene de açabilirsin. Aşağıdaki kodda, `(1,2)` tuple'ı `a` ve `b` adlı iki değişkene açılır.

`a, b = 1, 2`

Tuple'lar list'ler gibi indekslenebilir, ancak değiştirilemezler (immutable) ve oluşturulduktan sonra değiştirilemezler.

`tuple = 1, 2`

`print(tuple[1])`
`2` yazdırır

`tuple[0] = 3`
error verir
<unlock=dicts>
List'lerin aksine tuple'lar dictionary'lerde anahtar olarak kullanılabilir.

`d = {(1,2):(4,5)}

print(d[(1,2)])`
`(4,5)` yazdırır</unlock>

Ayrıca bir fonksiyonda birden fazla değer döndürmek için de yararlı olabilirler.

`def f():
    return 1, 2

a, b = f()`