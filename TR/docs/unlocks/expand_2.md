# Genişleme 2
Çiftliğin tekrar genişledi! Artık karolar düzgün bir sırada değil, bu yüzden kare bir ızgarayı dolaşmanın bir yolunu bulman gerekiyor.

`while` döngüsüyle bu, duyuları ve operatörleri açana kadar mümkün değil.
`for` döngüsünü tanıtmanın zamanı geldi.

`for` döngüsü hakkında her şeyi [For Döngüsü](docs/scripting/for.md) sayfasında okuyabilirsin, ama şimdilik sadece kodu belirli sayıda tekrarlamak için ihtiyacın olacak.

`#n kere takla at
for i in range(5):
	do_a_flip()`

`range(n)`, `0`'dan `n-1`'e kadar `n` elemanı olan bir sayı aralığı oluşturur. `for` döngüsü, döngü gövdesini dizideki her eleman için bir kez çalıştırır. Bu örnekte `do_a_flip()` `5` kez çağrılacaktır.

`get_world_size()` fonksiyonu da artık mevcut. Çiftliğinin kenar uzunluğunu döndürür. Bu şekilde, bir sonraki genişletme yükseltmesiyle bozulmayacak kod yazabilirsin.

`for i in range(get_world_size()):
	harvest()
	move(North)`

Bu örnek, herhangi bir çiftlik boyutu için çiftliğin bir sütununu hasat eder.

Drone'u çiftlikte nasıl dolaştıracağını bulmaya çalışırken takılırsan aşağıdaki ipucuna bak.
<spoiler=ipucu göster>Çiftlikte dolaşmanın elbette birkaç yolu var.
Aradığımız şey, çiftlik tekrar büyüdüğünde bozulmayacak sistematik bir şekilde dolaşmanın bir yoludur.
Çiftlikteki her yere ulaşmanın sistematik bir yolu, aşağıdaki 2 adımı sonsuza kadar tekrarlamak olacaktır:

1.Geri dönene kadar `North` yönünde hareket et.
2.`East` yönünde hareket et

`for i in range(get_world_size()):` bu fikri koda dönüştürmek için yardımcı olabilir.
</spoiler>
<spoiler=olası çözümü göster> Temel dolaşım şöyle görünebilir:

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		#her karoda bir takla at
		do_a_flip()
		move(North)
	move(East)`
</spoiler>