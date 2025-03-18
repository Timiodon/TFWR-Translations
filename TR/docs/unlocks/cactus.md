# Kaktüs
Diğer bitkiler gibi, [kaktüsler](objects/cactus) de toprağa ekilip normal şekilde hasat edilebilir.

Ancak, farklı boyutlarda gelirler ve tuhaf bir düzen anlayışına sahiptirler.

Tamamen büyümüş bir kaktüsü hasat ederseniz ve tüm komşu kaktüsler sıralı bir düzende ise, o zaman tüm komşu kaktüsleri de özyinelemeli bir şekilde hasat edecektir.

Bir kaktüs, `Kuzey` ve `Doğu` yöresindeki tüm komşu kaktüsler tamamen büyümüş ve aynı veya daha büyük boyutta ve `Güney` ve `Batı` yöresindekiler tamamen büyümüş ve aynı veya daha küçük boyutta ise sıralı düzende kabul edilir.

Hasat, yalnızca tüm bitişik kaktüsler tamamen büyümüş ve sıralı düzende ise yayılacaktır.
Bu, tamamen büyümüş bir kaktüs karesinin boyutuna göre sıralı olması ve bir kaktüsü hasat ettiğinizde tüm kareyi hasat edeceğiniz anlamına gelir.

Hasat ettiğiniz kaktüs sayısının karesi kadar kaktüs alırsınız. Yani aynı anda `n` kaktüs hasat ederseniz, `n**2` `Items.Cactus` alırsınız.

Bir kaktüsün boyutunu `measure()` ile ölçebilirsiniz.
Bu her zaman şu sayılardan biri olur: `0,1,2,3,4,5,6,7,8,9`.

Ayrıca `measure(direction)` fonksiyonuna bir yön vererek, drone'un o yöndeki komşu karesini ölçebilirsiniz.

`swap()` komutunu kullanarak bir kaktüsü, herhangi bir yönde komşusuyla değiştirebilirsiniz.
`swap(direction)` komutu, drone'un altındaki nesneyi, drone'un `direction` yönünde bir karedeki nesneyle değiştirir.

## Örnekler
Bu ızgaraların her birinde, tüm kaktüsler sıralı düzende ve hasat tüm alanı kaplayacaktır:
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

Bu ızgarada, yalnızca sol alttaki kaktüs sıralı düzen içindedir, yayılması için yeterli değildir:
`1 5 3
4 9 7
3 3 2`

<spoiler=ipucu 1>
Eğer alanın her sütunu ve her satırı sıralı ise, tüm alan sıralıdır.
</spoiler>
<spoiler=ipucu 2>
Sıralama algoritmalarıyla tanışık değilseniz, çevrimiçi olarak araştırmak ve bu probleme adapte edilebileceklerini düşünmek isteyebilirsiniz.
</spoiler>