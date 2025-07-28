# Dictionaries
Dictionary'ler, gerçek bir sözlüğün kelimeleri tanımlarıyla eşlemesi gibi anahtarları değerlerle eşlemenize olanak tanıyan ve onları çok hızlı bir şekilde arayabilmenizi sağlayan bir veri yapısıdır.

Bir dictionary şu şekilde oluşturulabilir:
`right_of = {North:East, East:South, South:West, West:North}`

İki nokta üst üste işaretinden önceki ifade anahtar, sonraki ifade ise anahtarın eşlendiği değerdir.
Yukarıdaki dictionary, her yönü sağındaki yöne eşler.

İşte drone'un pozisyonunu üzerindeki varlıkla eşleyen bir başkası:
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

Bir anahtara eşlenen değere erişim, bir listedeki bir elemana erişime benzer:
`value = dict[key]`

Örnek:
`orientation = right_of[South]`
Bu, `orientation`'ı `West`'e ayarlar.

Bir dictionary'e yeni bir anahtar-değer çifti şu şekilde ekleyebilirsin:
`dict[key] = value`

Örnek:
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
Bu, mevcut pozisyon için depolanan varlığı günceller.

Anahtarlar benzersizdir, bu nedenle dictionary'de zaten var olan bir anahtarı eklemek önceki değeri üzerine yazar.

`dict`'ten bir anahtar-değer çiftini kaldırmak için `dict.pop(key)` kullan.

`key in dict`, `key` `dict`'te bir anahtarsa `True`, aksi takdirde `False` olarak değerlendirilir.
Böylece `dict`'in anahtarı içerip içermediğini kontrol etmek için `if key in dict:` kullanabilirsin.

Bir dictionary'i for döngüsüne koymak, tüm anahtarlar arasında yineleme yapmanı sağlar:
`for key in dict:
	value = dict[key]`

Anahtarların hangi sırayla yineleneceği konusunda hiçbir garanti yoktur.

Ayrıca bakınız [Sets](docs/scripting/sets.md)