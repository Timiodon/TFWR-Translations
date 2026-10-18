[<- İlk Program](docs/first_program.md) <right>[Hız Yükseltmesi ->](docs/unlocks/speed.md)
---
# While Döngüsü
`while` döngüsünün ve `True` ile `False` değerlerinin kilidini açtın. `while` döngüsü, koşul `True` olduğu sürece döngü gövdesini çalıştırmaya devam eder.

`while condition:
	#loop body`

Sonsuz döngü oluşturmaktan endişelenme. Yürütmedeki gecikmeler programın donmasını engeller.

## Yeni Başlayanlar İçin
Belki de birkaç `harvest()` çağrısını art arda yazmayı zaten denemişsindir:

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
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
harvest()
harvest()
harvest()
}}
Bu sayede programı bir kez çalıştırarak birkaç kez hasat edebilirsin.
Ama üç kereden fazla hasat edebilmek güzel olurdu; üstelik aynı kodu defalarca yazmak kötü bir alışkanlıktır.
Çözüm bir döngüdür.
Döngü, aynı kodu birden çok kez çalıştırmanı sağlar.

while döngüsü bir koşul alır. Koşul, yalnızca iki durumdan birinde olabilen mantıksal bir değerdir: `True` ya da `False`. 
Böyle bir değere Boolean değer denir.

Döngü, koşul False olana kadar içindeki kodu çalıştırır.
while döngüsü şöyle görünür:

`while condition:
	#loop body
	#loop body
	#...`
	
Burada "condition" yerine bir boolean değer, `#loop body` yerine de döngüde yapmak istediğin şeyi yazman gerekir.

Kullanabileceğin iki sabit boolean değer vardır. Sabitler, program boyunca hiç değişmeyen değerlerdir.

Sabit bir Boolean değer oluşturmak için sadece `True` ya da `False` yazman yeterli.
Yani ya şunu yazabilirsin

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
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while False:
	do_a_flip()
}}
ya da şunu

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
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	do_a_flip()
}}
İlki hiç takla atmaz, ikincisi ise sonsuza dek takla atar (sonsuz döngü).

Normalde sonsuz döngü oluşturmak kötü bir fikirdir, çünkü programı dondurur. Ama bu oyunda yinelemeler arasında gecikmeler olduğundan dron, sen Çalıştır düğmesine tekrar basıp onu elle durdurana kadar takla atmaya devam eder.

İki nokta üst üsteden sonraki satırın içeriden başladığına (girintili olduğuna) dikkat et. Bu tür girintiler kod bloklarını birbirinden ayırmak için kullanılır.
Girinti eklemek için Tab tuşuna, kaldırmak için Shift + Tab (ya da Backspace) tuşlarına basman yeterli. Birkaç satır seçiliyse Tab ve Shift + Tab hepsine birden uygulanır.

Not: Oyunu Steam üzerinden oynuyorsan Shift + Tab bunun yerine Steam arayüzünü (overlay) açar. Girintiyi kaldırma kısayolunu oyun seçeneklerinden, Steam arayüzü kısayolunu da Steam arayüzü seçeneklerinden değiştirebilirsin.

Burada `do_a_flip()` ve `pet_the_piggy()` girintili `while` bloğunun içinde oldukları için tekrar tekrar çağrılır. Ancak `harvest()` bu bloktan sonra geldiği için hiç çalışmaz.
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
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	do_a_flip()
	pet_the_piggy()
harvest()
}}

---

[For Döngüsü](docs/scripting/for.md)      [If](docs/scripting/if.md)      [Break](docs/scripting/break.md)      [Continue](docs/scripting/continue.md)      [Harici Düzenleyici](docs/external_editor.md)
