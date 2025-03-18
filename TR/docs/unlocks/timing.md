# Zamanlama
Yöntemlerinizi gerçekten optimize etmek istiyorsanız, bu oyunda zamanın nasıl ölçüldüğünü anlamanız gerekiyor. Bu adım tamamen bununla ilgili.

## Yeni Fonksiyonlar
Nesnelerin ne kadar sürdüğünü ölçmek için iki yararlı fonksiyon var:

`get_time()` oyunun başlangıcından itibaren geçen süreyi saniye cinsinden verir.

`get_tick_count()` çalıştırmanın başlangıcından itibaren gerçekleştirilen tick sayısını verir.

Bu iki fonksiyon ve `quick_print()` tamamen ücretsiz. Hatta çağrı işlemi bile onlar için ücretsizdir.

## Çalışma Zamanı Detayları

### Uyarı
Gerçek dünyada performans böyle çalışmaz. Bunlar sadece oyun için tutarlı ve anlaşılır bir zaman modeli oluşturmak amacıyla oluşturulmuş kurallardır.
Muhtemelen sadece kodunuzu aşırı optimize etmek isterseniz buna dikkat edersiniz.

Kod yürütmenin temel zaman birimi "tick" olarak adlandırılır. Hız yükseltmeleri ve enerji olmadan, yürütme `400` tick saniyede gerçekleşir.

Genel olarak, iki değeri birleştiren işlemler, örneğin `+, -, *, /, //, %, and, or, ...` çalıştırmak için bir tick alır.
Tek değerli `-` ve `not` ise ücretsizdir.
`if` dalı da çalışmak için bir tick alır (koşul ifadesinin değerlendirilmesi süresi hariç).
Fonksiyon çağrıları ve değişken okuma ve yazmaları ücretsizdir ama fonksiyon tanımları 1 tick alır.
`import` ifadeleri ücretsizdir.
İçe aktarılan bir modüle `.` operatörü ile erişmek ücretsizdir.
Eğer bir fonksiyon veya modül argümanlar ya da değişken atamaları yoluyla iletildiyse, kullanmak 0 yerine 1 tick alır.
`for` ve `while` döngüleri başlamak için bir tick alır, ancak yinelemeler ücretsizdir (koşul/dizi ifadelerinin değerlendirilme süresi hariç).
`return`, `break` ve `continue` hepsi ücretsizdir.
`pass` bir tick alır, dolayısıyla kesin gecikmeler yaratmak için kullanılabilir.
Bir veri yapısında indeksleme, indeks operatörü için bir tick alır ve bir dictionary veya set durumunda anahtarın boyutuna bağlı olarak ek tickler alır.

Yerleşik fonksiyonların çalıştırılması için gereken tick sayısı, her bir fonksiyonun dokümantasyonunda ayrı ayrı belgelenmiştir.