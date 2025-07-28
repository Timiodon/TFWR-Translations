# Gübre
Bir noktada, bitkilerin büyümesini beklemek artık yeterince verimli değil. 
Su gibi, her 10 saniyede bir otomatik olarak 1 gübre ve her yükseltme için ekstra bir tane alacaksın.

Gübre, bitkilerin anında büyümesini sağlayabilir. `use_item(Items.Fertilizer)`, drone'un altındaki bitkinin kalan büyüme süresini 2 saniye azaltır.

Bunun bazı yan etkileri var.
Gübre ile büyütülen bitkiler enfekte olacaktır.

Bir bitki enfekte olduğunda, hasat edildiğinde veriminin yarısı `Items.Weird_Substance`'e dönüşür.
Tuhaf Madde ayrıca bitkiler üzerinde de kullanılabilir, bu da bitkinin ve tüm bitişik bitkilerin enfekte durumunu değiştirme etkisine sahiptir.

Yani `use_item(Items.Weird_Substance)`'ı enfekte bir bitki üzerinde kullanırsan onu iyileştirir, ancak sağlıklı bir bitki üzerinde kullanırsan onu enfekte eder.

Sağlıklı komşuları olan enfekte bir bitki üzerinde kullanırsan, bitkiyi iyileştirir ama komşuları enfekte eder ve tam tersi.