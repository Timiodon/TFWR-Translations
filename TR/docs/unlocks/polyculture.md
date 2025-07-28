# Polikültür
Bazen bitkilerin birlikte ekildiğinde daha fazla verim verdiğini zaten fark etmiş olabilirsin.
Çimen, çalılar, ağaçlar ve havuçlar, doğru bitki yoldaşına sahip olduklarında daha fazla verim verir. Yoldaş tercihi her bir bitki için farklıdır ve tahmin edilemez. Neyse ki, drone'un altındaki bitkinin yoldaş tercihi `get_companion()` kullanılarak ölçülebilir. İlk elemanı yoldaş olarak istediği bitki türü ve ikinci elemanı yoldaşını istediği pozisyon olan bir tuple döndürür.

`plant_type, (x, y) = get_companion()`

Örneğin bir çalı ekersen ve sonra `get_companion()` çağırırsan, `(Entities.Carrot, (3, 5))` gibi bir şey döndürür. Bu, bu çalının `(3,5)` pozisyonunda havuç olmasını istediği anlamına gelir. Yani `(3,5)` pozisyonuna havuç ekersen ve sonra çalıyı hasat edersen, daha fazla odun verir. Havucun büyüme aşaması önemli değildir.

Bir bitkinin yoldaş tercihi `Entities.Grass`, `Entities.Bush`, `Entities.Tree` veya `Entities.Carrot` olabilir. Her bitki bunu rastgele seçer, ancak her zaman kendisinden farklı bir bitki seçecektir. Pozisyon ayrıca, bitkinin kendi pozisyonu hariç, bitkinin 3 hamle mesafesindeki herhangi bir pozisyon olabilir.

Drone'un altında bir yoldaş tercihi olan bir bitki yoksa `get_companion()` `None` döndürür.

Polikültür açılmadan önce, verim çarpanı `5`'tir. Her yükselttiğinde ikiye katlanır.