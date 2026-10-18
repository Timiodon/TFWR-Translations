[<- Ekim](docs/unlocks/plant.md) <right>[Hata Ayıklama 2 ->](docs/unlocks/debug2.md)
<right>[Zamanlama ->](docs/unlocks/timing.md)
---
# Hata Ayıklama
Bazen kodun bir türlü çalışmaz ve nedenini bulman gerekir. Bunu yapmana yardımcı olacak birkaç araç var.

İlki, programı adım adım çalıştırmaktır. 
Adım adım moduna Çalıştır düğmesinin yanındaki düğmeyle ya da bir kesme noktası koyarak geçebilirsin.

Kesme noktaları, kodun solundaki kesme noktası paneline tıklanarak eklenebilir.
![|x227](Breakpoints)
Yürütme, kesme noktasının bulunduğu satıra ulaştığında otomatik olarak adım adım moduna geçilir.

Fareyi bir değişkenin üzerine getirdiğinde o değişkenin o anki değeri gösterilir.

`print()` fonksiyonu da çok işe yarayabilir. Kendisine verilen her değeri doğrudan havaya yazar.

Örnekler:

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(0.24)
}}

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(can_harvest())
}}

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(get_pos_x(), get_pos_y())
}}

`print()` fonksiyonu değeri doğrudan havaya ve [Çıktı](docs/output.md) sayfasına yazar.

Çok sayıda değer yazdırmak istediğinde havaya yazmak bazen biraz yavaş kalabilir.
Bu durumda yalnızca çıktı penceresine yazdıran `quick_print()` fonksiyonunu kullanabilirsin.

Çıktı penceresi uyarıları ve hataları da kaydeder; bir şey beklediğin gibi çalışmıyorsa oraya göz atmak işine yarayabilir.

Yürütme durduğunda çıktı, oyun klasöründeki [output.txt](persistent_data_path/output.txt) dosyasına da yazılır.

---

[Çıktı](docs/output.md)      [Yorumlar](docs/scripting/comments.md)      [Hata Ayıklama 2](docs/unlocks/debug2.md)      [Renkli Bloklar](docs/unlocks/debug_place.md)      [Simülasyon](docs/unlocks/simulation.md)

[print()](functions/print)      [quick_print()](functions/quick_print)
