# Kaktüs
Diğer bitkiler gibi, [kaktüsler](objects/cactus) de toprakta yetiştirilebilir ve her zamanki gibi hasat edilebilir.

Ancak, çeşitli boyutlarda gelirler ve garip bir düzen anlayışları vardır.

Tamamen büyümüş bir kaktüsü hasat edersen ve tüm komşu kaktüsler sıralı düzende ise, tüm komşu kaktüsleri de özyinelemeli olarak hasat eder.

Bir kaktüs, `North` ve `East` yönündeki tüm komşu kaktüsler tamamen büyümüş ve boyut olarak daha büyük veya eşitse ve `South` ve `West` yönündeki tüm komşu kaktüsler tamamen büyümüş ve boyut olarak daha küçük veya eşitse sıralı düzende kabul edilir.

Hasat, yalnızca bitişik tüm kaktüsler tamamen büyümüş ve sıralı düzende ise yayılır.
Bu, büyümüş bir kaktüs karesi boyuta göre sıralanmışsa ve bir kaktüsü hasat edersen, tüm kareyi hasat edeceği anlamına gelir.

Tamamen büyümüş bir kaktüs, sıralı değilse kahverengi görünür. Sıralandıktan sonra tekrar yeşile döner.

Hasat edilen kaktüs sayısının karesine eşit kaktüs alırsın. Yani aynı anda `n` kaktüs hasat edersen `n**2` `Items.Cactus` alırsın.

Bir kaktüsün boyutu `measure()` ile ölçülebilir.
Her zaman şu sayılardan biridir: `0,1,2,3,4,5,6,7,8,9`.

Ayrıca, drone'un o yöndeki komşu karoyu ölçmek için `measure(direction)`'a bir yön de geçirebilirsin.

`swap()` komutunu kullanarak bir kaktüsü herhangi bir yöndeki komşusuyla takas edebilirsin.
`swap(direction)`, drone'un altındaki nesneyi, drone'un `direction` yönünde bir kare ötedeki nesneyle değiştirir.

## Örnekler
Bu ızgaraların her birinde, tüm kaktüsler sıralı düzendedir ve hasat tüm tarlaya yayılacaktır:
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

Bu ızgarada, sadece sol alttaki kaktüs sıralı düzendedir, bu da yayılması için yeterli değildir:
`1 5 3
4 9 7
3 3 2`

<spoiler=ipucu 1'i göster>
Eğer satırlar zaten sıralıysa, sütunları sıralamak satırları bozmaz.
</spoiler>
<spoiler=ipucu 2'yi göster>
Sıralama algoritmalarına aşina değilsen, internette onlara göz atmak ve hangilerinin bu probleme uyarlanabileceğini düşünmek isteyebilirsin. Hepsinin işe yaramadığını unutma çünkü sadece komşu kaktüsleri takas edebilirsin.
</spoiler>