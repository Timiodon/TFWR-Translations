# Zamanlama
Eğer yöntemlerini gerçekten optimize etmek istiyorsan, bu oyunda zamanın nasıl ölçüldüğünü anlaman gerekir. Bu kilit açma tamamen bununla ilgili.

## Yeni Fonksiyonlar
İşlerin ne kadar sürdüğünü ölçmek için iki yararlı fonksiyon var:

`get_time()`, oyunun başlangıcından bu yana geçen süreyi saniye cinsinden döndürür.

`get_tick_count()`, yürütmenin başlangıcından bu yana gerçekleştirilen tick sayısını döndürür.

Bu iki fonksiyon ve `quick_print()` tamamen ücretsizdir. Hatta çağrı işlemi bile onlar için ücretsizdir.

## Çalışma Zamanı Detayları

### Dikkat
Gerçek dünyada performans böyle çalışmaz. Bunlar sadece bu oyun için tutarlı ve anlaşılır bir zamanlama modeline sahip olmak amacıyla uydurulmuş kurallardır.
Muhtemelen bunu sadece kodunu aşırı optimize etmek istiyorsan umursarsın.


Kod yürütme için temel zaman birimi "tick" olarak adlandırılır. Hız yükseltmeleri ve güç olmadan, yürütme saniyede `400` tick hızında ilerler.

Genel olarak, `+, -, *, /, //, %, and, or, ...` gibi iki değeri birleştiren işlemlerin çalışması bir tick sürer.
Tek değerli `-` ve `not` ücretsizdir.
Bir `if` dalı da (koşul ifadesini değerlendirmek için geçen süreye ek olarak) çalışmak için bir tick alır.
Fonksiyon çağrıları ve değişken okuma ve yazmaları ücretsizdir ancak fonksiyon tanımları 1 tick alır.
`import` ifadeleri ücretsizdir.
İçe aktarılmış bir modüle `.` operatörü ile erişmek ücretsizdir.
Eğer bir fonksiyon veya modül argümanlar veya değişken atamaları yoluyla geçirilmişse, onu kullanmak 0 yerine 1 tick'e mal olur.
`for` ve `while` döngülerinin başlaması bir tick alır, ancak yinelemeler ücretsizdir (koşul/dizi ifadelerini değerlendirme süresi hariç).
`return`, `break` ve `continue` hepsi ücretsizdir.
`pass` bir tick alır, bu yüzden hassas gecikmeler oluşturmak için kullanılabilir.
Bir veri yapısına indeksleme, indeks operatörü için bir tick ve bir dictionary veya set durumunda, anahtarın boyutuna bağlı olarak ek tick'ler alır.

Yerleşik fonksiyonların çalışmasının kaç tick sürdüğü, her fonksiyonun dokümantasyonunda ayrı ayrı belgelenmiştir.