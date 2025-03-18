# Dinozorlar
Dinozorlar, eski zamanlardan kalma, görkemli yaratıklardır ve antik kemikler için yetiştirilebilirler.

Maalesef dinozorlar çok uzun zaman önce yok olmuşlardır, bu yüzden yapabileceğimiz en iyi şey dinozor gibi giyinmektir.
Bu amaçla yeni bir dinozor şapkası aldın.

Şapka, `change_hat(Hats.Dinosaur_Hat)` ile takılabilir.

Ne yazık ki, reklamda göründüğü gibi görünmüyor...

Eğer dinozor şapkasını takar ve yeterli miktarda balkabağınız varsa, bir [apple](objects/apple) otomatik olarak satın alınır ve dronun altına yerleştirilir.
Dron bir elmanın üzerine gelip tekrar hareket ettiğinde, elmayı yer ve kuyruğunu bir birim uzatır. Eğer karşılayabiliyorsan, yeni bir elma satın alınır ve rastgele bir yere yerleştirilir.
Elma, başka bir şeyin ekili olduğu bir yere doğamaz.

Dinozorun kuyruğu, dronun hareket ettiği önceki kareleri doldurarak dronun arkasında sürüklenir. Eğer bir dron kuyruk üzerine hareket etmeye çalışırsa, `move()` başarısız olur ve `False` döner.
Kuyruğun son parçası hareket sırasında yolun dışına çıkar, bu nedenle üzerine hareket edebilirsin. Ancak, yılan tüm çiftliği doldurduğunda daha fazla hareket edemezsin. Dolayısıyla yılanın tamamen büyüdüğünü kontrol ederek daha fazla hareket edemediğini görebilirsin.

Bir elmada `measure()` kullanmak, bir sonraki elmanın pozisyonunu bir demet olarak döner.

`next_x, next_y = measure()`

Başka bir şapka takarak şapka tekrar çıkarıldığında, kuyruk hasat edilir.
Kuyruğun uzunluğunun karesi kadar kemik alırsın. Yani uzunluğu `n` olan bir kuyruk için `n**2` `Items.Bone` alırsın.
Örneğin:
uzunluk 1 => 1 kemik
uzunluk 2 => 4 kemik
uzunluk 3 => 9 kemik
uzunluk 4 => 16 kemik
uzunluk 16 => 256 kemik
uzunluk 100 => 10000 kemik

Dinozor Şapkası çok ağırdır, bu nedenle şapkayı takarsan, `move()` 200 yerine 800 tick alır. Bununla birlikte, her elma toplandığında, `move()` tarafından kullanılan tick sayısı %3 oranında (aşağıya yuvarlanmış) azalır çünkü daha uzun bir kuyruk hareket etmene yardımcı olabilir.

Aşağıdaki döngü, birkaç elmanın ardından `move()` tarafından kullanılan tick sayısını yazdırır:

`ticks = 800
for i in range(100):
    print("ticks after ", i, " apples: ", ticks)
    ticks -= ticks * 0.03 // 1`

<spoiler=show hint 1>Eğer tüm alanı kaplayan aynı yolda devam edersen, kuyruğun her zaman tüm alanı kaplayacak şekilde bir yılan yapabilirsin, çünkü kuyruk olduğun yere geri dönmeden önce tüm boş noktaları kaplayacaksın. Çok verimli değil, ama işe yarıyor.
Tek sayılı alanlar daha zor olabilir. Eğer `Unlocks.Debug2`'yi açtıysan, alanın boyutunu daha uygun bir şeye değiştirebilirsin.</spoiler>