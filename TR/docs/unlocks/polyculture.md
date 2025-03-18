# Polikültür
Belki fark ettin, bazen bitkiler bir arada dikildiğinde daha fazla verim sağlıyor. Çimenler, çalılar, ağaçlar ve havuçlar doğru bitki arkadaşı olduğu zaman daha fazla verim sağlar. Her bitkinin tercih ettiği bitki arkadaşı farklıdır ve tahmin edilemez. Neyse ki, drone'un altındaki bitkinin tercih ettiği bitki arkadaşı `get_companion()` fonksiyonu ile ölçülebilir. Bu fonksiyon, ilk elemanı bitkinin yanındaki bitki türünü ve ikinci elemanı ise bu bitkinin bulunmasını istediği konumu içeren bir tuple döner.

`plant, (x, y) = get_companion()`

Örneğin, bir çalı diktiysen ve ardından `get_companion()` fonksiyonunu çağırırsan, bu fonksiyon `(Entities.Carrot, (3, 5))` gibi bir değer dönebilir. Bu, çalının `(3,5)` konumunda havuç olmasını istediğini belirtir. Yani, `(3,5)` konumuna havuç dikersen ve ardından çalıyı hasat edersen, daha fazla odun alırsın. Havuçun büyüme aşaması önemli değildir.

Bir bitkinin tercih ettiği bitki arkadaşı `Entities.Grass`, `Entities.Bush`, `Entities.Tree` veya `Entities.Carrot` olabilir. Her bitki bunu rastgele seçer, ancak her zaman kendisinden farklı bir bitki seçer. Konum da bitkinin kendisi dışında 3 hareket mesafesi içerisindeki herhangi bir konum olabilir.

Eğer drone'un altında tercih ettiği bir bitki arkadaşı olmayan bir bitki varsa, `get_companion()` fonksiyonu `None` dönecektir.

Verim çarpanı `5` artı çoklu tarım iyileştirmelerinin sayısıdır.