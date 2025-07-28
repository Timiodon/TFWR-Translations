# Ayçiçekleri
[Ayçiçekleri](objects/sunflower) güneşin gücünü toplar. Bu gücü hasat edebilirsin.

Onları ekmek, tıpkı havuç veya balkabağı ekmek gibi işler.

Büyümüş bir ayçiçeğini hasat etmek güç verir.
Eğer çiftlikte en az 10 ayçiçeği varsa ve en çok yaprağı olanı hasat edersen, `5` kat daha fazla güç kazanırsın!

`measure()`, drone'un altındaki ayçiçeğinin yaprak sayısını döndürür.
Ayçiçeklerinin en az `7`, en fazla `15` yaprağı vardır.
Tamamen büyümeden önce de ölçülebilirler.

Birden fazla ayçiçeği aynı sayıda yaprağa sahip olabilir, bu yüzden en çok yaprağı olan birkaç ayçiçeği de olabilir. Bu durumda, hangisini hasat ettiğinin bir önemi yoktur.

Gücün olduğu sürece drone, iki kat daha hızlı çalışmak için onu kullanır.
Her 30 eylemde (hareket, hasat, ekme gibi...) 1 güç tüketir.
Diğer kod ifadelerini çalıştırmak da güç kullanabilir, ancak drone eylemlerinden çok daha az.

Genel olarak, hız yükseltmeleriyle hızlandırılan her şey, güçle de hızlandırılır.
Güçle hızlandırılan her şey, hız yükseltmelerini göz ardı ederek, çalışması için gereken süreyle orantılı olarak güç kullanır.