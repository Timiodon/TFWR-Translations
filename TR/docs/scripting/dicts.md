# Dictionary'ler
Dictionary'ler, gerçek bir sözlüğün kelimeleri tanımlarına eşlemesi gibi, anahtarları değerlere eşlemenizi sağlayan bir veri yapısıdır ve bunları çok hızlı bir şekilde arayabilirsiniz.

Bir dictionary şöyle oluşturulabilir:
`rotation = {North:East, East:South, South:West, West:North}`

İki nokta üst üste öncesindeki ifade anahtardır ve iki nokta üst üste sonrasındaki ifade, anahtarın eşlendiği değerdir. Yukarıdaki dictionary, her yönü sağındaki yöne eşler.

Drone'un pozisyonunu olduğu entity'ye eşleyen başka bir örnek:
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

Bir anahtara eşlenen değere erişmek, bir listedeki bir elemana erişmeye benzer:
`value = dict[key]`

Örnek:
`orientation = rotation[South]`
Bu, `orientation` değerini `West` yapar.

Yeni bir anahtar-değer çifti eklemek için:
`dict[key] = value`

Örnek:
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
Bu, mevcut pozisyon için kaydedilen entity'yi günceller.

Anahtarlar özeldir, bu yüzden dictionary içinde zaten var olan bir anahtarı eklemek, önceki değeri üzerine yazar.

Bir anahtar-değer çiftini dictionary'den çıkarmak için `dict.pop(key)` kullanabilirsiniz.

`key in dict`, `key` dictionary'de bir anahtar ise `True`, aksi takdirde `False` olur.
Bu yüzden `if key in dict:` kullanarak dictionary'nin anahtarı içerip içermediğini kontrol edebilirsiniz.

Bir for döngüsünde dictionary kullanmak, tüm anahtarlar üzerinde gezinmenizi sağlar:
`for key in dict:
	value = dict[key]`

Anahtarların hangi sırada döneceği konusunda bir garanti yoktur.

Ayrıca bkz. [Sets](docs/scripting/sets.md)