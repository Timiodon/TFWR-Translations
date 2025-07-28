# Labirentler
Bitkileri [gübreleyerek](docs/unlocks/fertilizer.md) elde edilen `Items.Weird_Substance`, çalılarda garip bir etkiye sahiptir. Eğer drone bir çalının üzerindeyse ve `use_item(Items.Weird_Substance, amount)` çağırırsan, çalı bir çit labirentine dönüşür.
Labirentin boyutu, kullanılan `Items.Weird_Substance` miktarına bağlıdır (`use_item()` çağrısının ikinci argümanı).
Labirent yükseltmeleri olmadan, `n` `Items.Weird_Substance` kullanmak `n`x`n` boyutunda bir labirentle sonuçlanır. Her labirent yükseltme seviyesi hazineyi ikiye katlar, ancak aynı zamanda gereken `Items.Weird_Substance` miktarını da ikiye katlar. 
Dolayısıyla tam bir tarla labirenti yapmak için:

`plant(Entities.Bush)
n_substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, n_substance)`


Nedense drone, çitlerin üzerinden uçamıyor, çok yüksek görünmeseler bile.

Çitin içinde bir yerlerde bir hazine gizlidir. Labirentin alanına eşit altın almak için hazine üzerinde `harvest()` kullan. (Örneğin, 5x5 bir labirent 25 altın verir.)

Başka bir yerde `harvest()` kullanırsan, labirent einfach kaybolur.

Drone hazinenin üzerindeyse `get_entity_type()` `Entities.Treasure`'a, labirentin diğer her yerinde ise `Entities.Hedge`'e eşittir.

Labirentler, labirenti yeniden kullanmadığın sürece döngü içermez (bir labirenti nasıl yeniden kullanacağını aşağıda gör). Bu yüzden drone'un geri gitmeden aynı pozisyona tekrar gelmesinin bir yolu yoktur.

Bir duvar olup olmadığını içinden geçmeye çalışarak kontrol edebilirsin. 
`move()` başarılı olursa `True`, aksi takdirde `False` döndürür.

Hazineye nasıl gideceğin hakkında hiçbir fikrin yoksa, İpucu 1'e bir göz at. Sana böyle bir sorunu nasıl ele alacağını gösterir.


Ekstra bir meydan okuma için, hazine üzerinde tekrar aynı miktarda `Items.Weird_Substance` kullanarak labirenti yeniden de kullanabilirsin. 
Bu, hazinedeki altın miktarını tam bir labirent kadar artıracak ve onu labirentte rastgele bir konuma taşıyacaktır.

Bir hazine üzerinde `measure()` kullanmak, gideceği pozisyonu bir tuple olarak döndürür.
`next_x, next_y = measure()`

Hazine her hareket ettirildiğinde, labirentten rastgele bir duvar kaldırılabilir. Bu yüzden yeniden kullanılan labirentler döngüler içerebilir.

Labirentteki döngülerin işi çok daha zorlaştırdığını unutma, çünkü bu, geri hareket etmeden aynı konuma tekrar gelebileceğin anlamına gelir.
Bir labirenti yeniden kullanmak, sadece hasat edip yeni bir labirent oluşturmaktan daha fazla altın vermez.
Bu, sadece atlayabileceğin %100 ekstra bir meydan okumadır.
Sadece ekstra bilgi ve kısayollar labirenti daha hızlı çözmene yardımcı olursa buna değer.

Aynı labirent en fazla 300 kez çözülebilir. Bu, 299 yer değiştirmeye karşılık gelir. Bundan sonra, hazine üzerinde tuhaf madde kullanmak artık içindeki altını artırmaz ve `measure()` `None` döndürür.

<spoiler=ipucu 1'i göster>İşte sorunu çözmek için genel bir yaklaşım:

Bir labirent oluştur ve drone'un sen olduğunu hayal et.

Labirentte olsaydın hazineyi bulmaya nasıl çalışacağını düşün.

Stratejini adım adım yaz, böylece başka biri düşünmeden onu takip edebilir.

Şimdi adımlarını koda çevirmeye çalış.
</spoiler>
<spoiler=ipucu 2'yi göster>Döngü olmadığı sürece: Tüm duvarlar aslında tek bir büyük bağlantılı duvardır. Duvarı takip edersen, seni tüm labirentten geçirir.
Bu yaklaşım çok az kod gerektirir ve daha önce nerede olduğunu takip etmene gerek yoktur. Yaklaşık 10 satır kod yeterlidir.</spoiler>
<spoiler=ipucu 3'ü göster>Drone'u doğu veya batı gibi mutlak yönlerde hareket ettirmek yerine, "sağa dön" veya "sola dön" gibi göreceli yönlerde hareket ettirmek çok faydalı olabilir. Bunu yapmak için, drone'un şu anda hangi yöne hareket ettiğini takip etmen gerekir. Drone aslında hiç dönmez, ama yine de kodda "sanal" bir dönüş tutabilirsin.
Aşağıdaki indeks hilesi bunun için faydalıdır:

`directions = [North, East, South, West]
index = 0`

`West`'ten sonra `North`'a geri dönmesi için "daire etrafında" dönmesine izin vermek için `% 4` kullan.
`# sağa dön
index = (index + 1) % 4`

`# sola dön
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=ipucu 4'ü göster>Eğer çözemiyorsan, hayatını her zaman kolaylaştırabilir ve daha az verimli bir şekilde yapabilirsin. 
Bir `1`x`1` labirentini çözmek basittir.</spoiler>