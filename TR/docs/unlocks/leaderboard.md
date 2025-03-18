# Lider Tablosu
Buraya kadar geldiysen, birçok zorluğun üstesinden geldin demektir. Ama onları verimli bir şekilde çözdün mü? 
En verimli tarım yöntemleri için diğer oyuncularla çeşitli lider tablolarında yarışabilirsin.

Lider tablosu koşusuna `leaderboard_run(leaderboard, filename, speedup)` işlevini çağırarak başlayabilirsin.
Bu, başlangıç koşullarının sabit olduğu bir [simülasyon](docs/unlocks/simulation.md) başlatır. Her lider tablosu kategorisinin farklı başlangıç ve başarı koşulları vardır.

Lider tablosu koşusu, simülasyon sona erdiğinde başarı koşulu `True` ise başarıyla tamamlanmış olur. Hedefe ulaşıldığında simülasyon otomatik olarak sona ermez. Programın sonlandığından emin olmalısın.
Koşu başarılı olursa, süren lider tablosuna eklenir.

Varyansı azaltmak için, tüm koşuların en az 2 saat sürmesi gerekiyor (Hızı artırabilirsin, bu yüzden o kadar uzun sürmez). Bir koşu daha erken tamamlanırsa, toplamda 2 saat sürene kadar tekrarlanır. Tüm koşuların ortalaması puanın olarak yüklenir.

İşte seni saman lider tablosuna sokacak bir örnek kurulum.
![](LeaderboardSetup400)

## En Hızlı Reset
En hızlı reset, en prestijli kategoridir. Tek bir çiftlik arsağından tamamen otomatik hale gelerek lider tablolarını tekrar açmak için uğraş.

Her şeyi açmana gerek yok, `Unlocks.Leaderboard` kilidini mümkün olan en hızlı şekilde açmayı dene.

Bir şeyin açılıp açılmadığını kontrol etmek için `num_unlocked(unlock) > 0` kullanabileceğini ve doğru öğeleri otomatik olarak çiftleyebilmen için onların maliyetini görmek amacıyla açılanlar üzerinde `get_cost()` kullanabileceğini unutma.

Fonksiyon Çağrısı:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Eşdeğer Simülasyon:
`unlocks = {}
items = {}
globals = {}
#negatif bir tohum değeri rastgele bir tohum demektir
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Başarı Koşulu:
`num_unlocked(Unlocks.Leaderboard) > 0`

## Labirent
Her şeyin kilidi açılmış olarak başlayın ve mümkün olduğunca hızlı bir şekilde `300000` altın toplayın. Bu miktarda altını, bir labirenti `300` kez çözerek kazanabilirsiniz.

Fonksiyon Çağrısı:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Eşdeğer Simülasyon:
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Başarı Koşulu:
`num_items(Items.Gold) >= 300000`

## Dinozor
Her şeyin kilidi açılmış olarak başlayın ve mümkün olduğunca hızlı `98010` kemik toplayın. Bu, dinozor kuyruğu ile 10x10 bir alanı doldurduğunuzda elde edeceğiniz kemik sayısıdır.

Fonksiyon Çağrısı:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Eşdeğer Simülasyon:
`unlocks = Unlocks
items = {Items.Pumpkin : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Başarı Koşulu:
`num_items(Items.Bone) >= 98010`

## Diğer Kaynak Lider Tabloları
Her bitki, o bitkiden mümkün olduğunca hızlı çiftlemek için kendi lider tablosuna sahiptir. Tüm kilitler açılmış olarak başlarsınız, bitkiyi yetiştirmek için gerekli kaynaklar ve bol miktarda enerji mevcuttur. Amaç, bitkinin ürettiği kaynaktan `100000` çiftlemektir.

Fonksiyon Çağrıları:
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
`leaderboard_run(Leaderboards.Polyculture, filename, speedup)`

Başarı Koşulu:
`num_items(resource) >= 100000`

`Leaderboards.Polyculture` üç poli-kültür kaynağından her birinden `100000` çiftlemeyi gerektirir.