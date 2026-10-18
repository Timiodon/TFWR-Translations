[<- Labirentler](docs/unlocks/mazes.md)
---
# Mega Çiftlik
Bu inanılmaz güçlü kilit açma, sana birden fazla drona erişim sağlar. 
{{codeexample 
{
    "camera_position": {"x": -3, "y": 2.1, "z": 7},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": true,
    "collapsing": false,
    "autoplay": true,
    "items": [],
    "world_size": {"x": 7, "y": 7},
    "execution_speed": 21,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(North)
move(North)
move(North)
move(East)
move(East)
move(East)
change_hat(Hats.Wizard_Hat)
#CODE
def harvest_spiral(radius):
    for i in range(1, radius, 2):
        harvest()
        move(West)
        for j in range(i):
            harvest()
            move(South)
        for j in range(i+1):
            harvest()
            move(East)
        for j in range(i+1):
            harvest()
            move(North)
        for j in range(i+1):
            harvest()
            move(West)

while True:
    spawn_drone(harvest_spiral, 7)
    do_a_flip()
}}

Eskiden olduğu gibi yine tek bir dronla başlarsın. Ek dronların önce oluşturulması gerekir ve program sonlandıktan sonra yok olurlar.
Her dron kendi ayrı programını çalıştırır. Yeni dronlar `spawn_drone(function)` fonksiyonuyla oluşturulabilir.

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
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
def drone_function():
    move(East)
    do_a_flip()

spawn_drone(drone_function)
do_a_flip()
}}

Bu, `spawn_drone(function)` komutunu çalıştıran dronla aynı konumda yeni bir dron oluşturur. Yeni dron ardından belirtilen fonksiyonu çalıştırmaya başlar. İşi bittiğinde, var olan son dron değilse kendiliğinden yok olur.

Dronlar birbirleriyle çarpışmaz. 

Aynı anda var olabilecek en fazla dron sayısını öğrenmek için `max_drones()` kullan.
Çiftlikte şu anda kaç dron bulunduğunu öğrenmek için `num_drones()` kullan.


## Örnek
{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)
}}

Bu, ilk dronunun yatay olarak ilerleyip yeni dronlar oluşturmasını sağlar. Oluşturulan dronlar ise dikey olarak ilerleyip yollarındaki her şeyi hasat eder.

Kullanılabilir tüm dronlar zaten oluşturulmuşsa `spawn_drone()` hiçbir şey yapmaz ve `None` döndürür.

Her drona farklı bir yön aktaran başka bir örnek:
{{codeexample 
{
    "camera_position": {"x": -1, "y": 2, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(North)
move(East)
#CODE
for dir in [North, East, South, West]:
    def task():
        move(dir)
        do_a_flip()
    spawn_drone(task)
}}

## Tüm Dronlar Eşittir
Özel bir "ana" dron yoktur. Tüm dronlar başka dronlar oluşturabilir ve hepsi dron sınırına dahil edilir. Tüm dronlar sonlandığında yok olur. İlk dron programını erken bitirirse, yürütmesi kod vurgularıyla gösterilen dron başka bir dron olur. Tüm dronlar kesme noktalarını (breakpoint) tetikleyebilir. Bu olduğunda kod vurgulaması o drona geçer.

<spoiler=ipucunu göster> 
Her fonksiyonu alıp çiftliğin her karesinde çalıştıran bu süper kullanışlı paralel `for_all` fonksiyonuna bir göz at. Bunu yapmak için kullanılabilir tüm dronlardan yararlanır.

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def for_all(f):
	def row():
		for _ in range(get_world_size()-1):
			f()
			move(East)
		f()
	for _ in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(North)

for_all(harvest)
}}

Özellikle kullanışlı bir kalıp şudur: Uygun bir dron varsa onu oluştur, yoksa işi kendin yap.

`if not spawn_drone(task):
	task()`
</spoiler>

## Başka Bir Dronu Beklemek
Başka bir dronun işini bitirmesini beklemek için `wait_for(drone)` fonksiyonunu kullan. `drone` tanıtıcısını (handle), dronu oluşturduğunda alırsın.
`wait_for(drone)`, diğer dronun çalıştırdığı fonksiyonun dönüş değerini döndürür.

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
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
move(East)
plant(Entities.Tree)
move(West)
#CODE
def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

drone = spawn_drone(get_entity_type_in_direction, East)
print(wait_for(drone))
}}

Dron oluşturmanın zaman aldığını unutma; bu yüzden her küçük iş için yeni bir dron oluşturmak iyi bir fikir değildir.

Dronu beklemeden işini bitirip bitirmediğini kontrol etmek için `has_finished(drone)` kullanabilirsin.

## Ortak Bellek Yok
Her dronun kendi belleği vardır ve başka bir dronun global değişkenlerini doğrudan okuyamaz ya da onlara yazamaz.

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": false,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
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
x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)
}}

Bu, `0` yazdırır; çünkü yeni dron global `x`'in kendi kopyasını artırmıştır ve bu, ilk dronun `x`'ini etkilemez.

## Argüman Aktarmak

`spawn_drone()`, çağrılan fonksiyona aktarılacak isteğe bağlı ek argümanlar da kabul eder:

"Ortak bellek yok" kuralının burada da geçerli olduğunu unutma. Yani çağrılan fonksiyon, argümanların bir kopyası üzerinde çalışır:

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": false,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
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
def modify(list):
	list.append('green')
	print(list)

l = ['red']
wait_for(spawn_drone(modify, l))
print(l)
}}

## Yarış Durumları
Birden fazla dron aynı anda aynı çiftlik karesiyle etkileşime girebilir. İki dron aynı tik içinde aynı kareyle etkileşime girerse her iki etkileşim de gerçekleşir, ancak sonuçlar etkileşimlerin sırasına göre değişebilir.

Örneğin `0` ve `1` numaralı dronların, neredeyse tamamen büyümüş aynı ağacın üzerinde olduğunu düşün.
`0` numaralı dron şunu çağırır:
`use_item(Items.Fertilizer)`
`1` numaralı dron şunu çağırır:
`harvest()`

Bu eylemler aynı anda gerçekleşirse ağaç önce gübrelenir, sonra hasat edilir. Bu durumda ağaçtan odun alırsın. Ancak `1` numaralı dron biraz daha hızlı davranırsa ağaç gübrelenmeden önce hasat edilir ve odun alamazsın.
Buna "yarış durumu" (race condition) denir. Sonucun işlemlerin hangi sırayla yapıldığına bağlı olduğu, paralel programlamada sık karşılaşılan bir sorundur.

Aynı kodu aynı anda aynı konumda çalıştıran birden fazla dron olduğunda yaşanabilecek başka bir sorunlu durum:
`if get_water() < 0.5:
    use_item(Items.Water)`

Birden fazla dron bunu aynı anda çalıştırırsa hepsi ilk satırı çalıştırır ve bu da hepsini `if` bloğunun içine sokar. Ardından hepsi su kullanır ve bir sürü suyu boşa harcar.
Oysa bir dron ikinci satıra ulaştığında `get_water()` artık `0.5`'ten küçük olmayabilir, çünkü bu arada başka bir dron kareyi sulamış olabilir.

---

[Fonksiyonlar](docs/scripting/functions.md)      [Ad Kapsamları](docs/scripting/scopes.md)      [Simülasyon](docs/unlocks/simulation.md)

[spawn_drone()](functions/spawn_drone)      [num_drones()](functions/num_drones)      [max_drones()](functions/max_drones)      [wait_for()](functions/wait_for)      [has_finished()](functions/has_finished)
