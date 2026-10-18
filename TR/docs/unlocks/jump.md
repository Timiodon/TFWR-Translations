[<- Kömür](docs/unlocks/coal.md)
---
# Zıplama

Dronun `jump()` komutunun kilidini açtı.

Bu komut belirli kilit açmaları hedef alıp ileriye, onlara doğru zıplamanı sağlar. Özellikle hata ayıklarken ya da kısa süre önce kaçırdığın bir cevher damarına ileri zıplamak için çok işe yarar. Kullanmak için ona argüman olarak `Unlocks.Iron` gibi bir kilit açma verirsin.

`jump()` yalnızca yeraltında ortaya çıkan kilit açmalar için çalışır; örneğin `jump(Unlocks.Rice)` ya da `jump(Unlocks.Iron)`.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 3,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms"],
    "starting_chunk": 0
}
#CODE
dig()
dig()
dig()
jump(Unlocks.Iron)
do_a_flip()
}}

Zıplamanın seni doğrudan hedef kilit açmaya götüreceği garanti değildir, bu yüzden yine de biraz etrafa bakman gerekebilir; ama hedefin yakınlarda olduğu garantidir.

`jump()` program her çalıştırıldığında yalnızca bir kez kullanılabilir.

---

[jump()](functions/jump)
