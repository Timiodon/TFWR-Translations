# Ayçiçekleri
[Ayçiçekleri](objects/sunflower) güneşin enerjisini toplar. Bu enerjiyi hasat edebilirsin.

Onları dikmek, havuç veya kabak dikmekle tamamen aynıdır.

Olgunlaşmış bir ayçiçeğini hasat etmek enerji kazandırır.
Eğer çiftlikte en az 10 ayçiçeği varsa ve en çok yaprağı olanı hasat edersen `5` kat daha fazla enerji alırsın!

`measure()` dronun altındaki ayçiçeğinin yaprak sayısını döndürür.
Ayçiçekleri en az `7` ve en fazla `15` yaprağa sahiptir.
Tamamen büyümeden önce bile ölçülebilirler.

Birden fazla ayçiçeğinin aynı sayıda yaprağı olabilir, bu yüzden en çok yaprağa sahip birkaç ayçiçeği de bulunabilir. Bu durumda hangisini hasat ettiğin önemli değildir.

Enerjin olduğu sürece drone iki kat hızlı çalışacaktır.
Her 30 hareket (hareket etme, hasat, ekim gibi) için 1 enerji tüketir.
Diğer kod ifadelerinin çalıştırılması da enerji kullanabilir ama drone eylemlerine göre çok daha az.

Genel olarak, hız güncellemeleriyle hızlandırılan her şey enerjiyle de hızlanır.
Enerji ile hızlandırılan her şey, gerçekleştirmenin aldığı süreye orantılı olarak enerji kullanır, hız güncellemeleri yok sayılır.