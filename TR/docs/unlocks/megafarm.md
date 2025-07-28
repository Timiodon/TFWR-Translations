# Mega Çiftlik
Bu inanılmaz derecede güçlü kilit açma, çiftlik boyutunu önemli ölçüde artırır ve sana birden fazla drone'a erişim sağlar. 

İşleri kolaylaştırmak için, her yeni drone için her zaman tam olarak 36 yeni karo alırsın. Drone'ların karolara oranı sabit kalır.

## Birden Fazla Drone
Daha önce olduğu gibi, yine sadece bir drone ile başlarsın. Ek drone'lar önce oluşturulmalı ve program sona erdikten sonra kaybolacaktır.
Her drone kendi ayrı program örneğini çalıştırır. Drone'lar şunları kullanarak yeni drone'lar oluşturabilir
`new_drone_id = spawn_drone("filename")`

Bu, `spawn_drone("filename")` komutunu çalıştıran drone ile aynı pozisyonda yeni bir drone oluşturur. Yeni drone, `filename` adlı dosyadaki programı yürütmeye başlayacaktır, bu yüzden `"filename"` yerine çalıştırmak istediğin dosyanın adını yaz.

Bunu, drone'una `filename` adlı dosyaya gitmesini ve bir sonraki drone için yürüt düğmesine basmasını söylediğin gibi düşünebilirsin.

Drone'lar birbirleriyle çarpışmaz. 

Oluşturulabilecek maksimum drone sayısını almak için `max_drones()` kullan.
Çiftlikte zaten bulunan drone sayısını almak için `num_drones()` kullan.
Kodu hangi drone'un çalıştırdığını öğrenmek için `get_drone_id()` kullan.

Örnek:

`farming routine` adlı bir dosyada:
`if get_drone_id() == 0:
    # Bunu sadece ilk drone çalıştıracak
    while num_drones() < max_drones():
        spawn_drone("farming routine")
        move(East)

while True:
    if can_harvest():
        harvest()
    move(North)`

Bu, ilk drone'unun yatay olarak hareket etmesine ve daha fazla drone oluşturmasına neden olur. Oluşturulan drone'lar daha sonra dikey olarak hareket eder ve yollarındaki her şeyi hasat eder.

<spoiler=ipucu göster>
Birden fazla drone kullanmanın en kolay yolu, çiftliğini aralarında bölmektir. Yükseltmeler, her drone'un her zaman 6x6'lık bir alana sahip olabileceği şekilde tasarlanmıştır.
</spoiler>

Buradan sonraki her şey oldukça gelişmiş ve temel çiftçilik için gerekli değil

## Yarış Koşulları (Race Conditions)
Birden fazla drone aynı çiftlik karosuyla aynı anda etkileşime girebilir. Eğer iki drone aynı kareyle tam olarak aynı tick sırasında etkileşime girerse, daha düşük drone ID'sine sahip drone'un eylemi önce gerçekleşir.

Örneğin, `0` ve `1` numaralı drone'ların her ikisinin de neredeyse tamamen büyümüş aynı ağacın üzerinde olduğunu hayal et.
Drone `0` çağırır
`use_item(Items.Fertilizer)`
Drone `1` çağırır
`harvest()`

Eğer bu eylemler aynı anda gerçekleşirse, ağaç önce gübrelenir ve sonra hasat edilir. Bu durumda, ondan odun alırsın. Ancak, Drone `1` biraz daha hızlıysa, ağaç gübrelenmeden önce hasat edilir ve odun alamazsın.
Buna "yarış koşulu" (race condition) denir. Bu, sonucun işlemlerin gerçekleştirilme sırasına bağlı olduğu paralel programlamada yaygın bir sorundur.

İşte birden fazla drone aynı kodu aynı pozisyonda aynı anda çalıştırdığında ortaya çıkabilecek başka bir sorunlu durum.
`if get_water() < 0.5:
    use_item(Items.Water)`

Eğer birden fazla drone bunu aynı anda çalıştırırsa, hepsi ilk satırı çalıştırır ve bu da onları `if` bloğuna sokar. Sonra hepsi su kullanır ve bir sürü su israf eder.
Bir drone ikinci satıra ulaştığında, başka bir drone bu arada karoyu suladığı için `get_water()` artık `0.5`'ten küçük olmayabilir.

## Drone İletişimi
Daha gelişmiş stratejilerle ilgileniyorsan, drone'larının mesaj geçişi fonksiyonlarını kullanarak birbirleriyle iletişim kurmasını isteyebilirsin.

Başka bir drone'a herhangi bir değer gönder:
`send(data, receiver_drone_id)`

Herhangi bir drone tarafından gönderilen bir sonraki değeri al:
`data = receive()`

Belirli bir drone tarafından gönderilen bir sonraki değeri al:
`data = receive(sender_drone_id)`

`send()`'in yürütme süresi, gönderilen verinin boyutuna bağlıdır. Örneğin, büyük bir dictionary göndermek kopyalama gerektirir, bu da biraz zaman alabilir.

`receive()` bir mesajın gelmesini beklemez. Henüz bir mesaj gönderilmediyse, `None` döndürür.

Bir mesajı bekleyen bir fonksiyonu şu şekilde oluşturabilirsin:
`def blocking_receive(sender_drone_id = -1):
    while True:
        data = receive(sender_drone_id)
        if data != None:
            return data`

Mesaj geçişinin yararlı bir uygulaması, bir drone oluşturan ve ona yürütülecek bir fonksiyon gönderen bir fonksiyona sahip olmaktır.
`drone_spawning` adlı bir dosyada:
`def run_on_new_drone(f):
    id = spawn_drone("drone_spawning")
    send(f, id)

if __name__ == "__main__":
    f = blocking_receive()
    f()`

Bu şekilde fonksiyonlar göndermek çok yavaş olabilir çünkü fonksiyonun yakalanan tüm durumu, tüm global değişkenler dahil, kopyalanmalıdır.
