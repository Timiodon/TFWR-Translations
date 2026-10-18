[<- Hata Ayıklama](docs/scripting/debug.md) <right>[Simülasyon ->](docs/unlocks/simulation.md)
---
# Zamanlama
Yöntemlerini gerçekten optimize etmek istiyorsan, bu oyunda zamanın nasıl ölçüldüğünü anlaman gerekir. Bu kilit açma tamamen bununla ilgili.

## Yeni Fonksiyonlar
İşlerin ne kadar sürdüğünü ölçmek için iki kullanışlı fonksiyon var:

`get_time()` oyunun başından beri geçen süreyi saniye cinsinden döndürür.

`get_tick_count()` yürütmenin başından beri gerçekleşen tik sayısını döndürür.

Bu iki fonksiyon ve `quick_print()` tamamen ücretsizdir. Bunları çağırma işlemi bile ücretsizdir.

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
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
start_time, start_ticks = get_time(), get_tick_count()
harvest()
time, ticks = get_time(), get_tick_count()
quick_print(time - start_time, ticks - start_ticks)
}}

## Çalışma Zamanı Ayrıntıları

### Bilgin Olsun
Gerçek dünyada performans böyle işlemez. Bunlar, tutarlı ve anlaşılır bir zamanlama modeli olsun diye bu oyun için uydurulmuş kurallardır.
Büyük ihtimalle bunlarla yalnızca kodunu son noktasına kadar optimize etmek istiyorsan ilgilenirsin.


Kod yürütmenin temel zaman birimine "tik" denir. Hız yükseltmeleri ve güç olmadan yürütme saniyede `400` tik hızında ilerler.

Genel olarak `+, -, *, /, //, %, and, or, ...` gibi iki değeri birleştiren işlemlerin çalışması bir tik sürer.
Tek değerle kullanılan `-` ve `not` ücretsizdir.
Bir `if` dalının çalışması da bir tik sürer (koşul ifadesini değerlendirmek için geçen süreye ek olarak).
Fonksiyon çağrıları ve değişken okuma/yazma işlemleri ücretsizdir, ancak fonksiyon tanımları 1 tik sürer.
`import` ifadeleri ücretsizdir.
İçe aktarılmış bir modüle `.` operatörüyle erişmek ücretsizdir.
Bir fonksiyon ya da modül argümanlar veya değişken atamaları yoluyla aktarıldıysa, onu kullanmak 0 yerine 1 tik tutar.
`for` ve `while` döngülerinin başlaması bir tik sürer, ancak yinelemeler ücretsizdir (koşul/dizi ifadelerini değerlendirme süresi hariç).
`return`, `break` ve `continue` ifadelerinin hepsi ücretsizdir.
`pass` bir tik sürer, bu yüzden hassas gecikmeler oluşturmak için kullanılabilir.
Bir veri yapısında indeksleme, indeks operatörü için bir tik sürer; dictionary ya da set söz konusuysa anahtarın boyutuna bağlı olarak ek tikler de harcanır.

Yerleşik fonksiyonların çalışmasının kaç tik sürdüğü, her fonksiyonun kendi sayfasında belirtilmiştir.

---

[Hata Ayıklama](docs/scripting/debug.md)      [Simülasyon](docs/unlocks/simulation.md)      [Sıralama Tablosu](docs/unlocks/leaderboard.md)

[get_time()](functions/get_time)      [get_tick_count()](functions/get_tick_count)      [quick_print()](functions/quick_print)
