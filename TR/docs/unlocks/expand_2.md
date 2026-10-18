[<- Genişletme 1](docs/unlocks/expand_1.md)
---
# Genişletme 2
Çiftliğin yeniden genişledi! Kareler artık düzgün bir sıra hâlinde değil, bu yüzden kare biçimli bir ızgarada dolaşmanın bir yolunu bulman gerekiyor.

Duyuların ve operatörlerin kilidini açana kadar bunu `while` döngüsüyle yapmak mümkün değil.
`for` döngüsüyle tanışma zamanı.

`for` döngüsüyle ilgili her şeyi [For Döngüsü](docs/scripting/for.md) sayfasında okuyabilirsin, ama şimdilik ona yalnızca bir kodu belirli sayıda tekrarlamak için ihtiyacın olacak.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
for i in range(5):
	do_a_flip()
}}

`range(n)`, `0` ile `n - 1` arasındaki `n` sayıdan oluşan bir dizi oluşturur. `for` döngüsü, dizideki her eleman için döngü gövdesini bir kez çalıştırır. Bu örnekte `do_a_flip()` fonksiyonu `5` kez çağrılır.

`get_world_size()` fonksiyonu da artık kullanılabilir. Bu fonksiyon çiftliğinin kenar uzunluğunu döndürür. Böylece bir sonraki genişleme yükseltmesinde bozulmayacak kod yazabilirsin.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
for i in range(get_world_size()):
	harvest()
	move(North)
}}

Bu örnek, çiftliğin boyutu ne olursa olsun çiftliğin bir sütununu hasat eder.

Dronu çiftlikte nasıl dolaştıracağını bulmaya çalışırken takıldıysan aşağıdaki ipucuna bak.
<spoiler=ipucunu göster>Çiftlikte dolaşmanın elbette birkaç yolu var.
Aradığımız şey, çiftliği sistemli bir şekilde dolaşan ve çiftlik yeniden büyüdüğünde bozulmayan bir yol.
Çiftlikteki her yere ulaşmanın sistemli bir yolu, şu iki adımı sonsuza kadar tekrarlamak olabilir:

1. Dron kenardan sarıp başa dönene kadar `North` yönünde ilerle.
2. `East` yönünde ilerle.

`for i in range(get_world_size()):` bu fikri koda dökerken işine yarayabilir.
</spoiler>
<spoiler=olası çözümü göster>
{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
for i in range(get_world_size()):
	for j in range(get_world_size()):
		#do a flip on every tile
		do_a_flip()
		move(North)
	move(East)
}}
</spoiler>

---

[For Döngüsü](docs/scripting/for.md)      [While Döngüsü](docs/scripting/while.md)      [Değişkenler](docs/scripting/variables.md)

[move()](functions/move)      [get_world_size()](functions/get_world_size)
