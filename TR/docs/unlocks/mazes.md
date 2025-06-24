# Labirentler
`Items.Weird_Substance`, bitkileri [gübreleyerek](docs/unlocks/fertilizer.md) elde edilebilen bir maddedir ve çalılarda garip bir etkiye sahiptir. Eğer drone bir çalının üzerinde ise ve `use_item(Items.Weird_Substance, amount)` fonksiyonunu çağırırsanız, çalı bir çit labirentine dönüşür.
Labirentin boyutu, kullanılan `Items.Weird_Substance` miktarına (yani, `use_item()` çağrısının ikinci argümanı) bağlıdır.
Labirent yükseltmeleri olmadan, `n` `Items.Weird_Substance` kullanmak bir `n`x`n` labirent oluşturur. Her labirent yükseltme seviyesi, hazine miktarını iki katına çıkarır ancak aynı zamanda gereken `Items.Weird_Substance` miktarını da iki katına çıkarır.
Bu şekilde tam bir alan labirenti yapmak için:

`plant(Entities.Bush)
n_substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, n_substance)`

Nedense drone çitin üzerinden uçamıyor, oysa çitler pek yüksek görünmüyor.

Çitin içinde bir yerde hazine gizlidir. Hazine üzerinde `harvest()` fonksiyonunu kullanarak labirentin alanına eşit miktarda altın alırsınız. (Örneğin, 5x5'lik bir labirent 25 altın verir.)

Başka bir yerde `harvest()` kullanırsanız, labirent basitçe kaybolur.

Eğer drone hazine üzerindeyse `get_entity_type()` `Entities.Treasure` ve labirentin diğer her yerinde `Entities.Hedge` ile eşittir.

Labirentler, yeniden kullanılmadıkça döngüler içermez (labirenti nasıl yeniden kullanabileceğinizi görmek için aşağıya bakın). Yani drone’un aynı konuma geri gitmeden ulaşması mümkün değildir.

Bir duvar olup olmadığını denemek için hareket edebilirsiniz.
`move()` başarılı olursa `True`, yoksa `False` döndürür.

Eğer hazineye nasıl ulaşacağınız hakkında hiçbir fikriniz yoksa, birinci ipucuna göz atın. Bu tür bir sorunu nasıl ele alabileceğinizi gösterir.

Ekstra bir meydan okuma arıyorsanız aynı miktarda `Items.Weird_Substance` ile tekrar hazineyi kullanarak labirenti yeniden kullanabilirsiniz.
Bu işlem, hazine içindeki altın miktarını bir tam labirent kadar artırır ve onu labirentin rastgele bir konumuna taşır.

Hazine üzerinde `measure()` kullanmak, onun hareket edeceği konumu bir demet olarak döndürür.
`next_x, next_y = measure()`

Her seferinde hazine taşındığında, labirentten rastgele bir duvar kaldırılabilir. Yani, yeniden kullanılan labirentler döngüler içerebilir.

Labirentteki döngülerin bulunması işinizi zorlaştırır çünkü aynı konuma geri dönebilir ve bu, geriye gitmeden tekrar aynı konumda olabileceğiniz anlamına gelir.
Bir labirenti yeniden kullanmak, sadece hasat yapıp yeni bir labirent oluşturmaktan daha fazla altın kazandırmaz.
Bu tamamen ekstra bir meydan okumadır ve atlayabilirsiniz.
Yalnızca ekstra bilgiler ve kestirmeler, labirenti daha hızlı çözmenize yardımcı olursa buna değer.

Aynı labirenti en fazla 300 kez çözebilirsiniz. Bu, 299 kez taşınmasına karşılık gelir. Bundan sonra, hazine üzerinde garip madde kullanmak daha fazla altın sağlamaz ve `measure()` `None` döndürecektir.

<spoiler=ipuçunu göster 1>Sorunu çözmek için genel bir yaklaşım:

Bir labirent oluşturun ve kendinizi drone gibi hayal edin.

Labirentin içinde olsaydınız hazineyi nasıl bulmak isterdiniz diye düşünün.

Adım adım stratejinizi yazın ki başkası düşünmeden uygulayabilsin.

Şimdi adımlarınızı koda çevirmeyi deneyin.
</spoiler>
<spoiler=ipuçunu göster 2>Döngü olmadığı sürece: Tüm duvarlar aslında büyük bir bağlı duvardan ibarettir. Eğer duvarı takip ederseniz, bu sizi tüm labirentin içinden geçirir.
Bu yaklaşım çok az kod gerektirir ve nerede olduğunuzu takip etmenize gerek yoktur. Yaklaşık 10 satır kod yeterlidir.</spoiler>
<spoiler=ipuçunu göster 3>Drone'u doğu veya batı gibi mutlak yönlerde hareket ettirmek yerine "sağa dön" veya "sola dön" gibi göreceli yönlerde hareket ettirmek çok daha yararlıdır. Bunu yapmak için drone'un hangi yöne doğru hareket ettiğini takip etmelisiniz. Drone aslında hiç dönmez, ancak yine de kodda "sanal" bir dönüş oluşturabilirsiniz.
Şu index hilesi bu konuda yardımcıdır:

`directions = [North, East, South, West]
index = 0`

`% 4` kullanarak "çember etrafında" dönmesini sağlayabilirsiniz, böylece `West`'ten sonra tekrar `North`'e döner.
`# sağa dön
index = (index + 1) % 4`

`# sola dön
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=ipuçunu göster 4>Eğer çözemezseniz her zaman işleri kolaylaştırabilir ve daha az verimli bir şekilde yapabilirsiniz.
Bir `1`x`1` labirenti çözmek oldukça basittir.</spoiler>