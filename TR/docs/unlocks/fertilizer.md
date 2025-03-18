# Gübre
Bir noktada, bitkilerin büyümesini beklemek artık yeterince verimli değildir. 
Suya benzer şekilde, her 10 saniyede bir otomatik olarak 1 gübre alırsınız, ayrıca her yükseltme için ekstra bir tane daha.

Gübre, bitkilerin anında büyümesini sağlar. `use_item(Items.Fertilizer)`, dronun altındaki bitkinin kalan büyüme süresini 2 saniye azaltır.

Bunun bazı yan etkileri vardır.
Gübreyle büyütülen bitkiler enfekte olacaktır.

Bir bitki enfekte olduysa, hasat edildiğinde veriminin yarısı `Items.Weird_Substance`'e dönüşür.
Tuhaf Madde de bitkilerde kullanılabilir ve bu, bitkinin ve tüm komşu bitkilerin enfekte olma durumunu değiştirir.

Yani, `use_item(Items.Weird_Substance)` komutunu enfekte bir bitki üzerine kullanırsanız, onu tedavi edersiniz, ama sağlıklı bir bitki üzerine kullanırsanız enfekte edersiniz.

Eğer sağlıklı komşulara sahip enfekte bir bitki üzerine kullanırsanız, bitkiyi tedavi eder ama komşuları enfekte eder ve tam tersi.