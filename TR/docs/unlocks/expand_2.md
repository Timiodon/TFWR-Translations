# Genişleme 2
Çiftliğin tekrar genişledi! Artık kareler düzgün bir sıra halinde değil, bu yüzden kare bir ızgarada dolaşmanın bir yolunu bulmalısın.

`while` döngüsü ile bu, duyular ve operatörler açılana kadar mümkün değil.
Artık `for` döngüsünü tanıtmanın zamanı geldi.

[For Döngüsü](docs/scripting/for.md) sayfasında `for` döngüsü hakkında her şeyi okuyabilirsin, ama şimdilik sadece kodu sabit bir sayıda tekrarlamak için ihtiyacın olacak.

`#do n flips
for i in range(5):
	do_a_flip()`

`range(n)`, içinde `n` öğesi olan `0`'dan `n-1`'e kadar bir sayı aralığı oluşturur. `for` döngüsü, dizideki her öğe için döngü gövdesini bir kez çalıştırır. Bu örnekte `do_a_flip()` `5` kez çağrılacaktır.

`get_world_size()` fonksiyonu da şimdi kullanılabilir. Bu, çiftliğinin kenar uzunluğunu döndürüyor. Böylece bir sonraki genişleme yükseltmesinde kodunun bozulmaması için kod yazabilirsin.

`for i in range(get_world_size()):
	harvest()
	move(North)`

Bu örnek, her çiftlik boyutu için çiftliğin bir sütununu hasat eder.

Drone'u çiftlikte nasıl hareket ettireceğin konusunda sıkıştıysanız aşağıdaki ipucuna bakın.
<spoiler=ipucunu göster> Çiftlikte dolaşmanın birkaç yolu elbette var.
Aradığımız, çiftlik tekrar büyüdüğünde bozulmayan, sistematik bir şekilde dolaşmanın bir yoludur.
Çiftlikteki her yere ulaşmanın sistematik bir yolu, aşağıdaki 2 adımı sonsuza kadar tekrarlamaktır:

1. `North` yönünde geri sarılana kadar hareket et.
2. `East` yönünde hareket et.

`for i in range(get_world_size()):` bu fikri koda dökmek için yararlı olabilir.
</spoiler>
<spoiler=olası çözümü göster> Temel dolaşım şöyle görünebilir:

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		#her karede bir flip yap
		do_a_flip()
		move(North)
	move(East)`
</spoiler>