[<- Mantar](docs/unlocks/mushroom.md)
---
# Dinamit

Önceki maden keşif seferlerinden geriye kalmış devrim niteliğinde bir patlayıcı. Ne yazık ki (ya da neyse ki) matkabın dinamiti patlatmak için biçilmiş kaftan; patlama etrafındaki tüm blokları havaya uçurur.

Dinamiti güvenle kazmak için `Grounds.Dynamite` ve `Grounds.Soot` zeminlerinden oluşan çift katmanı bulman gerekecek. Üstteki dinamit zemini biraz eskimiş ve bazı bloklarını kazmak güvenli. Ancak dinamitin bir kısmı hâlâ aktif ve kazıldığında patlar.

{{codeexample 
{
    "camera_position": {"x": -3, "y": -3, "z": 12},
    "show_image": true,
    "image_size": {"x": 900, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "hay", "n": 100}],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 8,
    "digging_speed": 8,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 4,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz", "petrified_pumpkins"]
}
#SETUP
jump(Unlocks.Dynamite)
#CODE
while get_ground_type() != Grounds.Soot:
    dig()
dig()
dig()
}}

Tüm sönük blokları bulup kazarak geride yalnızca aktif blokları bırakabilir misin? Dinamit katmanı ortadan kalktığında, yalnızca başka aktif bloklarla ya da is bloklarıyla çevrili olan her aktif blok sana ekstra dinamit kazandırır.

Neyse ki alttaki is blokları sana yardım edecek: komşu dinamit bloklarından kaçında aktif dinamit olduğunu algılayabilirler. Tam olarak hangi blokların aktif olduğunu söylemezler, yalnızca toplam sayıyı verirler; bu yüzden birden fazla is bloğundan aldığın değerleri birleştirip sonucu kendin çıkarman gerekir.

Bir is bloğunda `measure()` çağırmak, üstteki dinamit katmanında komşu sekiz karedeki mayın sayısını döndürür. Bu sayı `0` (hiç aktif mayın yok) ile `8` (tüm komşularda aktif mayın var) arasında olabilir.

Dinamit katmanına yapılan ilk kazı her zaman sönük bir bloğa denk gelir. Kazılan her dinamit bloğu biraz dinamit verir. Dinamit katmanı yok olduğunda (ister tüm sönük blokları başarıyla kazarak, ister yanlışlıkla aktif bir dinamiti kazarak), ayrıca tamamen açığa çıkarılmış aktif blok sayısının karesi kadar dinamit kazanırsın.

Aktif bir dinamiti kazarsan iki katman birden patlar. Bunu `Grounds.Dynamite` zeminini kazdıktan sonra `get_ground_type()` ile kontrol edebilirsin. Zemin `Grounds.Soot` değilse bulmacayı çözemedin demektir. Öte yandan aktif olmayan son dinamit bloğunu da kazarsan tüm dinamit blokları kaybolur ve bu bulmacadan alınabilecek en yüksek verimi kazanırsın. İs katmanı yerinde kalır ama `measure()` artık `None` döndürür; bu da bulmacanın başarıyla çözüldüğünü gösterir.

`# Dig into a dynamite block and check the puzzle state
def dig_dynamite():
    dig()
    if get_ground_type() != Grounds.Soot:
        # Dug into live dynamite, puzzle failed
        return False
    elif measure() == None:
        # Dug up final dud block, puzzle solved
        return True
    else:
        # Got a count from measuring, puzzle still ongoing
        return None
`

Dinamit katmanındaki aktif mayın sayısı, dolayısıyla onları bulmanın zorluğu, derinlikle birlikte artar.

Topladığın dinamiti `use_item(Items.Dynamite)` ile kullanabilirsin; dinamit dronun hemen altında anında patlar.

Dinamit bloklarını kazmaktan ve aktif blokları tamamen açığa çıkarmaktan elde ettiğin verimi artırmak için dinamiti yükselt. Yükseltme ayrıca dinamit patlamalarının enerjisini %30 artırır.

---

[İstatistikler](docs/stats.md)      [Yeraltı Duyuları](docs/unlocks/underground_senses.md)      [Dictionary'ler](docs/scripting/dicts.md)      [Set'ler](docs/scripting/sets.md)

[move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)      [use_item()](functions/use_item)
