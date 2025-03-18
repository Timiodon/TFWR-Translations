# Labirentler
`Items.Weird_Substance`, bitkilerin [gübrelenmesi](docs/unlocks/fertilizer.md) sırasında elde edilir ve çalılar üzerinde garip bir etkisi vardır. Eğer drone bir çalının üzerinde ise ve `use_item(Items.Weird_Substance, amount)` çağrısı yaparsanız, çalı bir çit labirentine dönüşür.
Labirentin boyutu kullanılan `Items.Weird_Substance` miktarına bağlıdır (`use_item()` çağrısının ikinci argümanı).
Labirent yükseltmeleri olmadan, `n` adet `Items.Weird_Substance` kullanmak `n`x`n` boyutunda bir labirent oluşturur. Her bir labirent yükseltme seviyesi için aynı etkiyi almak adına ekstra bir adet `n` `Items.Weird_Substance` kullanmanız gerekir.
Dolayısıyla tam bir alan labirenti yapmak için:

`plant(Entities.Bush)
n_substance = get_world_size() * num_unlocked(Unlocks.Mazes)
use_item(Items.Weird_Substance, n_substance)`

Her ne sebepten olursa olsun, drone çitlerin üzerinden uçamıyor, sanki çok yüksek görünmeseler de.

Çitin içinde bir yerde bir hazine gizli. Hazineye `harvest()` kullanarak labirentin alanına eşit bir miktarda altın alırsınız. (Örneğin, 5x5'lik bir labirent 25 altın verecektir.)

Başka bir yerde `harvest()` kullanırsanız, labirent basitçe kaybolur.

Eğer drone hazine üzerinde bulunuyorsa `get_entity_type()` `Entities.Treasure` ile eşit olur, labirentte başka yerlerde ise `Entities.Hedge` olur.

Labirentler, yeniden kullanılmadıkları sürece döngü içermezler (aşağıda, bir labirenti nasıl tekrar kullanacağınızı görün). Bu yüzden drone'un aynı konuma tekrar geri dönmeden gitmesi mümkün değil.

Bir duvarın olup olmadığını kontrol etmek için, onun içinden geçmeye çalışabilirsiniz.
`move()` başarılı olursa `True` döner, yoksa `False` döner.

Hazineye nasıl ulaşacağınızı bilmiyorsanız, İpucu 1'e göz atın. Bu tür bir soruna nasıl yaklaşmanız gerektiğini gösterir.

Ekstra bir zorluk için, aynı miktarda `Items.Weird_Substance` kullanarak labirenti tekrar kullanabilirsiniz.
Bu, hazinedeki altın miktarını bir tam labirent kadar arttırır ve hazinenin labirent içinde rastgele bir konuma taşınmasına neden olur.

Bir hazineye `measure()` kullanmak, taşınacağı pozisyonu bir demet olarak döndürür.
`next_x, next_y = measure()`

Her hazine taşındığında, labirentten rastgele bir duvar kaldırılabilir. Dolayısıyla yeniden kullanılan labirentler döngüler içerebilir.

Labirentteki döngüler dikkat edilmesi gereken bir nokta çünkü aynı yere tekrar geri dönebilirsiniz.
Bir labirenti tekrar kullanmak, sadece hasat etmek ve yeni bir labirent oluşturmak kadar fazla altın vermez.
Bu %100'lük bir ekstra zorluk ve geçebilirsiniz.
Ekstra bilgi ve kısayollar labirenti daha hızlı çözmenize yardımcı oluyorsa, o zaman değerlidir.

Aynı labirent maksimum 300 kez çözülebilir. Bu, 299 taşınmaya karşılık gelir. Bundan sonra, hazineye tuhaf madde kullanmak altını arttırmaz ve `measure()` `None` döner.

<spoiler=ipucu 1'i göster>Problemi çözmek için genel bir yaklaşım buraya getir:

Bir labirent oluşturun ve kendinizin drone olduğunu hayal edin.

Labirentin içindeyken hazineyi nasıl bulmak isteyebileceğinizi düşünün.

Başka birinin düşünmeden takip edebileceği şekilde adım adım stratejinizi yazın.

Şimdi, adımlarınızı koda dönüştürmeyi deneyin.
</spoiler>
<spoiler=ipucu 2'yi göster>Döngüler olmadığı sürece: Tüm duvarlar aslında sadece büyük bir bağlı duvardır. Duvarı takip ederseniz, sizi tüm labirent boyunca yönlendirecektir.
Bu yaklaşım çok az kod gerektirir ve daha önce bulunduğunuz yeri takip etmeniz gerekmez. Yaklaşık 10 satır kod yeterli olacaktır.</spoiler>
<spoiler=ipucu 3'ü göster>Drone'u doğu veya batı gibi mutlak yönlerle hareket ettirmek yerine, "sağa dön" veya "sola dön" gibi göreceli yönlerle hareket ettirmek çok yararlı olabilir. Bunu yapmak için drone'un şu anda hangi yöne hareket ettiğini takip etmelisiniz. Drone asla gerçekten dönmez, ama yine de koda "sanaldan" bir dönüş ekleyebilirsiniz.
Aşağıdaki indeks hilesi bunun için faydalıdır:

`directions = [North, East, South, West]
index = 0`

"x`% 4`" kullanarak "çemberin etrafında" dönmelerine izin verin, böylece `West`'den sonra `North`'a geri döner.
`# sağa dön
index = (index + 1) % 4`

`# sola dön
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=ipucu 4'ü göster>Eğer çözemezseniz, her zaman işleri kolaylaştırabilir ve daha az verimli yapabilirsiniz.
Bir `1`x`1` labirenti çözmek önemsizdir.</spoiler>