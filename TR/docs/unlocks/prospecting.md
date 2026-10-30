[<- Demir](docs/unlocks/iron.md)
---
# Demir Arama

Demir damarlarını bulmanın bazen zor olduğunu fark etmiş olabilirsin. Etrafı kazıp onlara şans eseri denk gelmeyi umabilirsin ama daha iyi bir yol var: demir manyetik olduğu için onu uzaktan bulabiliriz.

`prospect_iron()` komutu tam olarak bunu yapar. `prospect_iron()`, en yakın demir cevherine doğru bir adım atmak için dronun hareket etmesi gereken ana yönü (`North`, `East`, `South` ya da `West`) döndürür. Bu komutu çalıştırmak 1 kömüre mal olur.

Dron zaten en yakın demir cevherinin tam üstündeyse, komutu çalıştırmaya yetecek kadar kömürün yoksa ya da menzilde hiç demir yoksa `prospect_iron()` `None` döndürür.

Bir sonraki demir cevherine bir adım yaklaşmak için şu kodu kullanabilirsin:

`if prospect_iron() != None:
    move(prospect_iron())
`

Bu kod şu anda `prospect_iron()` fonksiyonunu iki kez çağırıp 2 kömür harcıyor; bu yüzden onu bir değişken kullanarak optimize etmek isteyebilirsin.

En yakın demir cevheri, dronun atması gereken adım sayısına göre belirlenir. Dronun 2 blok doğusunda ve 3 blok kuzeyinde bir demir cevheri varsa bu 5 birimlik bir mesafe sayılır, çünkü dronun oraya gitmesi beş adım sürer.

Kazmak da bir adım sayılır. Yani buna ek olarak demir yerin 7 blok altına gömülüyse bu 12 birimlik bir mesafe sayılır, çünkü dronun demirin üstüne gelmesi beş adım, ona ulaşması da yedi kazı sürer.

---

[Demir](docs/unlocks/iron.md)      [Yeraltı Duyuları](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [prospect_iron()](functions/prospect_iron)
