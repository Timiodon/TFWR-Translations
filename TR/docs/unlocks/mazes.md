[<- Gübre](docs/unlocks/fertilizer.md) <right>[Mega Çiftlik ->](docs/unlocks/megafarm.md)
---
# Labirentler
`Items.Weird_Substance`, çalılar üzerinde tuhaf bir etki yaratır. Dron bir çalının üzerindeyken `use_item(Items.Weird_Substance, amount)` çağırırsan, çalı büyüyüp çitlerden oluşan bir labirente dönüşür.
Labirentin boyutu, kullanılan `Items.Weird_Substance` miktarına (`use_item()` çağrısının ikinci argümanı) bağlıdır.
Labirent yükseltmesi olmadan `n` adet `Items.Weird_Substance` kullanmak `n`x`n` boyutunda bir labirent oluşturur. Her labirent yükseltme seviyesi hazineyi iki katına çıkarır, ama gereken `Items.Weird_Substance` miktarını da iki katına çıkarır.
Yani tüm tarlayı kaplayan bir labirent yapmak için:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": -1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
}}


Nedense dron, pek yüksek görünmeseler de çitlerin üzerinden uçamıyor.

Labirentin bir yerinde gizlenmiş bir hazine var. Labirentin alanı kadar altın almak için hazinenin üzerinde `harvest()` kullan. Örneğin 5x5'lik bir labirent 25 altın verir.

`harvest()`'ı başka herhangi bir yerde kullanırsan labirent öylece yok olur.

Dron hazinenin üzerindeyse `get_entity_type()`, `Entities.Treasure` değerine eşittir; labirentin geri kalan her yerinde ise `Entities.Hedge` değerine eşittir.

Labirentleri yeniden kullanmadığın sürece (aşağıya bak) labirentlerde hiç döngü bulunmaz. Bu yüzden dron, geldiği yoldan geri dönmeden aynı konuma yeniden varamaz.

Bir duvar olup olmadığını, içinden geçmeyi deneyerek kontrol edebilirsin. 
`move()`, başarılı olursa `True`, aksi halde `False` döndürür.

Hareket etmeden duvar olup olmadığını kontrol etmek için `can_move()` kullanılabilir.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(East)
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
#CODE
quick_print(
    can_move(North), 
    can_move(East), 
    can_move(South), 
    can_move(West)
)
if move(North) and get_entity_type() == Entities.Treasure:
    harvest()
}}

Hazineye nasıl ulaşacağın konusunda hiçbir fikrin yoksa 1. İpucu'na bir göz at. Bu tür bir probleme nasıl yaklaşacağını gösteriyor.

Labirentin herhangi bir yerinde `measure()` kullanmak hazinenin konumunu döndürür.
`x, y = measure()`

Ekstra bir meydan okuma istersen, hazinenin üzerinde yine aynı miktarda `Items.Weird_Substance` kullanarak labirenti yeniden kullanabilirsin.
Bu, hazineyi toplar ve labirentte rastgele bir konumda yeni bir hazine oluşturur.

Hazine her yer değiştirdiğinde labirentin bazı duvarları rastgele kaldırılabilir. Bu yüzden yeniden kullanılan labirentlerde döngüler olabilir.

Labirentteki döngülerin işi çok daha zorlaştırdığını unutma, çünkü bu, geri dönmeden de aynı konuma yeniden varabileceğin anlamına gelir.
Labirenti yeniden kullanmak, hasat edip yeni bir labirent oluşturmaktan daha fazla altın kazandırmaz.
Bu tamamen ekstra bir meydan okumadır, istersen atlayabilirsin.
Ancak ek bilgiler ve kısayollar labirenti daha hızlı çözmene yardımcı oluyorsa buna değer.

Hazinenin yeri en fazla 300 kez değiştirilebilir. Ondan sonra hazinenin üzerinde Tuhaf Madde kullanmak, içindeki altını artık artırmaz ve hazinenin yerini de değiştirmez.

<spoiler=1. ipucunu göster>
Bu probleme genel bir yaklaşım şöyle:

Bir labirent oluştur ve kendini dronun yerine koy.

Labirentin içinde olsaydın hazineyi bulmaya nasıl çalışırdın, bir düşün.

Stratejini adım adım, başka biri hiç düşünmeden takip edebilecek şekilde yaz.

Şimdi de bu adımları koda dökmeyi dene.
</spoiler>
<spoiler=2. ipucunu göster>
Hiç döngü olmadığı sürece tüm duvarlar birbirine bağlı tek büyük bir duvar oluşturur. Sol elini duvara koyup duvarı takip edersen seni labirentin tamamında dolaştırır.
Bu yaklaşım çok az kod gerektirir ve daha önce nerelerde bulunduğunu takip etmene gerek kalmaz. Bunun için yaklaşık 10 satır kod yeterlidir.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": true,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": -1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
#CODE
directions = [North, East, South, West]
index = 0
while get_entity_type() != Entities.Treasure:
    index = (index - 1) % 4
    for _ in range(4):
        if move(directions[index]):
            break
        index = (index + 1) % 4
do_a_flip()
harvest()
}}
</spoiler>
<spoiler=3. ipucunu göster>
Dronu doğu ya da batı gibi mutlak yönlerde hareket ettirmek yerine "sağa dön" veya "sola dön" gibi göreli yönlerde hareket ettirmek işine yarayabilir. Bunun için dronun şu anda hangi yöne ilerlediğini takip etmen gerekir. Dron aslında hiç dönmez, ama kodda yine de "sanal" bir yön tutabilirsin.
Bunun için şu indeks numarası işe yarar:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
directions = [North, East, South, West]
index = 0
move(directions[index])

#turn right
index = (index + 1) % 4
move(directions[index])

#turn left
index = (index - 1) % 4
move(directions[index])
}}


"Çember etrafında" dönebilmesi için `% 4` kullanılır; böylece `4 % 4 == 0` ve `-1 % 4 == 3` olduğundan `3 (West) + 1` yeniden `0 (North)` olur.</spoiler>
<spoiler=4. ipucunu göster>
Çözemiyorsan, daha az verimli bir yaklaşım kullanarak problemi her zaman basitleştirebilirsin.
`1`x`1` boyutunda bir labirenti çözmek çocuk oyuncağıdır.</spoiler>

---

[İstatistikler](docs/stats.md)      [Listeler](docs/scripting/lists.md)      [Dictionary'ler](docs/scripting/dicts.md)      [Tuple'lar](docs/scripting/tuples.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [can_move()](functions/can_move)      [move()](functions/move)      [use_item()](functions/use_item)
