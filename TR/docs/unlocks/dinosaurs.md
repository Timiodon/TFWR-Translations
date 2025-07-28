# Dinozorlar
Dinozorlar, antik kemikler için çiftçiliği yapılabilen antik, görkemli yaratıklardır.

Maalesef dinozorlar uzun zaman önce yok oldu, bu yüzden şimdi yapabileceğimiz en iyi şey onlardan biri gibi giyinmek.
Bu amaçla yeni dinozor şapkasını aldın.

Şapka şununla kuşanılabilir
`change_hat(Hats.Dinosaur_Hat)`

Maalesef reklamlardaki gibi görünmüyor...

Dinozor şapkasını takarsan ve yeterli balkabağın varsa, bir [elma](objects/apple) otomatik olarak satın alınacak ve drone'un altına yerleştirilecektir.
Drone bir elmanın üzerindeyken tekrar hareket ettiğinde, elmayı yiyecek ve kuyruğunu bir birim uzatacaktır. Eğer karşılayabiliyorsan, yeni bir elma satın alınacak ve rastgele bir konuma yerleştirilecektir.
Elma, olmak istediği yerde başka bir şey ekiliyse ortaya çıkamaz.

Dinozorun kuyruğu, drone'un arkasında sürüklenerek drone'un daha önce hareket ettiği karoları doldurur. Eğer bir drone kuyruğun üzerine çıkmaya çalışırsa `move()` başarısız olur ve `False` döndürür. 
Kuyruğun son segmenti hareket sırasında yoldan çekilir, böylece üzerine hareket edebilirsin. Ancak, yılan tüm çiftliği doldurursa, artık hareket edemezsin. Bu yüzden, artık hareket edip edemediğini kontrol ederek yılanın tamamen büyüyüp büyümediğini kontrol edebilirsin.

Bir elma üzerinde `measure()` kullanmak, bir sonraki elmanın pozisyonunu bir tuple olarak döndürür.

`sonraki_x, sonraki_y = measure()`

Farklı bir şapka takılarak şapka tekrar çıkarıldığında, kuyruk hasat edilir.
Kuyruk uzunluğunun karesine eşit kemik alırsın. Yani `n` uzunluğunda bir kuyruk için `n**2` `Items.Bone` alırsın. 
Örneğin:
uzunluk 1 => 1 kemik
uzunluk 2 => 4 kemik
uzunluk 3 => 9 kemik
uzunluk 4 => 16 kemik
uzunluk 16 => 256 kemik
uzunluk 100 => 10000 kemik

Dinozor Şapkası çok ağırdır, bu yüzden takarsan, `move()`'un 200 yerine 800 tick sürmesine neden olur. Ancak, her elma aldığında, `move()` tarafından kullanılan tick sayısı %3 (aşağı yuvarlanarak) azalır, çünkü daha uzun bir kuyruk hareket etmene yardımcı olabilir.

Aşağıdaki döngü, herhangi bir sayıda elmadan sonra `move()` tarafından kullanılan tick sayısını yazdırır:

`ticks = 800
for i in range(100):
    print(i, " elmadan sonraki tick sayısı: ", ticks)
    ticks -= ticks * 0.03 // 1`

<spoiler=ipucu 1'i göster>Eğer tüm tarlayı kaplayan aynı yol boyunca hareket etmeye devam edersen, her seferinde tüm tarlayı kaplayan bir yılanı kolayca elde edebilirsin, çünkü kuyruğunun olduğu yere geri dönmeden önce her boş noktayı kaplayacaksın. Çok verimli değil, ama işe yarıyor.
Tek sayılı alanlar daha zor olabilir. Eğer `Unlocks.Debug2` kilidin açıksa, tarlanın boyutunu daha uygun bir şeye değiştirebilirsin.</spoiler>