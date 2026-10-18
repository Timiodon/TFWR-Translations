[<- Başlarken](docs/getting_started.md) <right>[While Döngüsü ->](docs/scripting/while.md)
---
# İlk Program
## Metin Düzenleyici
Tüm programlama kod pencerelerinde yapılır. Her kod penceresi, kod içeren bir metin dosyasına karşılık gelir.
Dosyanın adını, pencerenin üst kısmındaki adına tıklayarak değiştirebilirsin.

Kod çalışmadığı sürece onu herhangi bir metin düzenleyicideki gibi düzenleyebilirsin.
Programı, kod penceresindeki yeşil oynat düğmesine basarak doğrudan çalıştırabilirsin.
![|x50](PlayButton)

Ekranın sağ üst köşesindeki "+" düğmesiyle daha fazla kod dosyası oluşturabilirsin.
Bir pencereyi başka bir pencerenin üzerine sürükleyerek ona yerleştirebilirsin.

Yazmaya başladığında basit bir kod tamamlama penceresinin açıldığını fark edeceksin.
Seçili tamamlamayı eklemek için Tab tuşuna bas.
Tamamlama seçenekleri arasında gezinmek için ok tuşlarını kullan.

İlk kez programlama yapıyorsan endişelenme. Dilin özellikleri adım adım açılır, böylece yapabileceğin onca şey karşısında bunalmazsın.
Sözdizimi de dünyada en yaygın kullanılan programlama dillerinden biri olan Python'a benzer, yani burada öğrendiklerin başka yerlerde de işine yarar.

Python'u zaten biliyorsan bu da sorun değil; oyunun başlangıç kısmını hızla geçip daha ilginç şeylere ulaşabilirsin.

Şu anda kullanabileceğin iki dron komutu var.

`harvest()`

ve

`do_a_flip()`

Bunlar fonksiyon çağrılarıdır. Bir fonksiyonu, çalıştırılabilen bir komut olarak düşünebilirsin. `()` parantezleri onu çalıştırır.

Bu ifadeleri kod penceresine yazmayı ve çalıştır düğmesine basmayı dene.

Kodunu bir dizi ifade olarak düşünebilirsin. Birden fazla ifadeyi alt alta satırlara yazarak art arda çalıştırabilirsin.
Kodun nasıl çalıştığını görmek için bu gömülü kod penceresindeki oynat düğmesine basmayı dene:

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
do_a_flip()
harvest()
harvest()
}}

## Kilit Açmalar
Çim toplamak sana saman kazandırır. Saman, teknoloji ağacında döngülerin kilidini açmak için kullanılabilir. Teknoloji ağacını ekranın sağ üst köşesindeki düğmeyle aç.

---

[Harici Düzenleyici](docs/external_editor.md)      [Yorumlar](docs/scripting/comments.md)      [While Döngüsü](docs/scripting/while.md)

[harvest()](functions/harvest)      [do_a_flip()](functions/do_a_flip)
