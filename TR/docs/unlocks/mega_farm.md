# Mega Farm
Bu son derece güçlü açılım, çiftliğin boyutunu önemli ölçüde artırır ve birden fazla drone'a erişim sağlar.

İşleri kolaylaştırmak için, her yeni drone için her zaman tam olarak 36 yeni karoyu alırsınız. Drone ile karo oranı sabit kalır.

## Çoklu Drone
Daha önce olduğu gibi, yine yalnızca tek bir drone ile başlarsınız. Ek drone'ların önce spawn edilmesi gerekir ve program sona erdiğinde kaybolacaklardır. Her bir drone, kendi ayrı program örneğini çalıştırır. Drone'lar, kullanarak yeni drone'lar spawn edebilir:
`new_drone_id = spawn_drone("filename")`

Bu, `spawn_drone("filename")` komutunu çalıştıran drone ile aynı pozisyonda yeni bir drone spawn eder. Yeni drone, `filename` adlı dosyadaki programı çalıştırmaya başlayacağı için, `"filename"` kısmını çalıştırmak istediğiniz dosyanın adıyla değiştirin.

Bunu, drone'unuzdan `filename` adlı dosyaya gitmesini ve bir sonraki drone için çalıştır düğmesine tıklamasını istemiş gibi düşünebilirsiniz.

Drone'lar birbiriyle çarpışmaz.

Spawn edilebilecek maksimum drone sayısını öğrenmek için `max_drones()` kullanın.
Zaten çiftlikte olan drone sayısını öğrenmek için `num_drones()` kullanın.
Hangi drone'nun kodu çalıştırdığını öğrenmek için `get_drone_id()` kullanın.

Örnek:

`farming routine` adlı bir dosyada:
`if get_drone_id() == 0:
    # Yalnızca ilk drone bunu çalıştıracak
    while num_drones() < max_drones():
        spawn_drone("farming routine")
        move(East)`

while True:
    if can_harvest():
        harvest()
    move(North)`

Bu, ilk drone'unuzun yatay olarak hareket etmesine ve daha fazla drone spawn etmesine neden olur. Spawn edilen drone'lar ise dikey olarak hareket edip yollarındaki her şeyi hasat ederler.

<spoiler=show hint>Birden fazla drone kullanmanın en kolay yolu, çiftliğinizi aralarında paylaştırmaktır. Güncellemeler, her drone'un her zaman 6x6 bir alana sahip olmasını sağlamak üzere tasarlanmıştır.
</spoiler>

### Buradan sonraki her şey oldukça ileri düzeydedir ve temel çiftçilik için gerekli değildir

## Yarış Koşulları
Birden fazla drone, aynı zamanda aynı çiftlik karosuyla etkileşime girebilir. İki drone aynı tick sırasında aynı karoyla etkileşime girerse, daha düşük drone kimliği olanın işlemi önce gerçekleşir.

Örneğin, drone `0` ve `1`, neredeyse tamamen büyümüş aynı ağacın üzerinde olduklarını farz edelim.
Drone `0` çağırıyor
`use_item(Items.Fertilizer)`
Drone `1` çağırıyor
`harvest()`

Bu eylemler aynı anda gerçekleşirse, ağaç önce gübrelenir ve sonra hasat edilir. Bu durumda, ağaçtan odun alırsınız. Ancak, eğer Drone `1` biraz daha hızlı olursa, ağaç gübrelemeden önce hasat edilir ve odun almazsınız.
Bu duruma "yarış koşulu" denir. Paralel programlamada yaygın bir sorundur, burada sonucun, işlemlerin hangi sırayla yapıldığına bağlıdır.

Birden fazla dronenun aynı yerde ve aynı zamanda aynı kodu çalıştırırken oluşabilecek başka bir sorunlu durum.
`if get_water() < 0.5:
    use_item(Items.Water)`

Eğer bu kod aynı anda birden fazla drone tarafından çalıştırılırsa, hepsi ilk satırı çalıştırır ve `if` bloğuna girerler. Sonra, hepsi su kullanır ve çok su israf edilir.
Bir drone ikinci satıra ulaştığında, `get_water()` artık `0.5`'den az olmayabilir çünkü bu arada başka bir drone karoyu suladı.

## Drone İletişimi
Eğer daha ileri düzey stratejilerle ilgileniyorsanız, drone'larınızın mesaj geçişi fonksiyonlarını kullanarak birbirleriyle iletişim kurmalarını isteyebilirsiniz.

Başka bir drone'a herhangi bir değeri gönder:
`send(data, receiver_drone_id)`

Herhangi bir drone tarafından gönderilen bir sonraki değeri al:
`data = receive()`

Belirli bir drone tarafından gönderilen bir sonraki değeri al:
`data = receive(sender_drone_id)`

`send()`'in yürütme süresi gönderilen verinin boyutuna bağlıdır. Örneğin, büyük bir dictionary gönderilmesi kopyalama gerektirir ve bu biraz zaman alabilir.

`receive()`, bir mesaj gelmesi için beklemez. Henüz bir mesaj gönderilmediyse, `None` döndürecektir.

Bir mesaj bekleyen bir fonksiyon oluşturabilirsiniz:
`def blocking_receive(sender_drone_id = -1):
    while True:
        data = receive(sender_drone_id)
        if data != None:
            return data`

Mesaj iletmenin yararlı bir uygulaması, bir drone spawn etmek ve ona çalıştırılması için bir fonksiyon göndermek olabilir.
`drone_spawning` adlı bir dosyada:
`def run_on_new_drone(f):
    id = spawn_drone("drone_spawning")
    send(f, id)

if __name__ == "__main__":
    f = blocking_receive()
    f()`

Bu tür işlevleri göndermek çok yavaş olabilir çünkü işlevin yakalanmış tüm durumu, tüm global değişkenler dahil, kopyalanması gerekir.