# Leaderboard
Eğer bu kadar ileri geldiysen, birçok zorluğun üstesinden geldin. Ama onları verimli bir şekilde çözdün mü? 
En verimli çiftçilik yöntemleri için çeşitli leaderboard'larda diğer oyuncularla rekabet edebilirsin.

`leaderboard_run(leaderboard, filename, speedup)` çağırarak bir leaderboard koşusu başlatabilirsin.
Bu, başlangıç koşullarının sabit olması dışında `simulate()`'e benzer bir [simülasyon](docs/unlocks/simulation.md) başlatır. Her leaderboard kategorisinin farklı başlangıç ve başarı koşulları vardır.

Simülasyon sona erdiğinde başarı koşulu `True` ise leaderboard koşusu başarılı olur. Hedefe ulaşıldığında simülasyon otomatik olarak sona ermez. Programın sonlandığından emin olmalısın.
Eğer koşu başarılı olursa, süren leaderboard'a eklenecektir.

Varyansı azaltmak için, tüm koşuların en az 2 saat sürmesi gerekir (Hızlandırabilirsin, bu yüzden o kadar uzun sürmez). Bir koşu daha erken tamamlanırsa, toplam 2 saatlik bir süreye ulaşılana kadar tekrarlanır. Ardından tüm koşuların ortalaması puanın olarak yüklenir.

İşte seni saman leaderboard'una sokacak bir örnek kurulum.
![](LeaderboardSetup400)

## En Hızlı Sıfırlama
En hızlı sıfırlama en prestijli kategoridir. Tek bir çiftlik parselinden başlayarak leaderboard'ları tekrar açmaya kadar oyunu tamamen otomatikleştir.

Her şeyin kilidini açmak zorunda değilsin, sadece `Unlocks.Leaderboard`'u olabildiğince hızlı açmaya çalış.

Bir şeyin kilidinin açık olup olmadığını kontrol etmek için `num_unlocked(unlock) > 0` kullanabileceğini ve ne kadara mal olduklarını görmek için kilit açmalarda `get_cost()` kullanabileceğini unutma, böylece doğru eşyaları otomatik olarak toplayabilirsin.

Fonksiyon Çağrısı:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Eşdeğer Simülasyon:
`unlocks = {}
items = {}
globals = {}
#negatif bir tohum değeri rastgele bir tohum anlamına gelir
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Başarı Koşulu:
`num_unlocked(Unlocks.Leaderboard) > 0`

## Labirent
Her şeyin kilidi açık olarak başla ve olabildiğince hızlı `300000` altın topla. Bu, bir labirenti `300` kez çözerek kazanacağın altın miktarıdır.

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
Her şeyin kilidi açık olarak başla ve olabildiğince hızlı `98010` kemik topla. Bu, 10x10'luk bir alanı dinozor kuyruğu ile doldurursan alacağın kemik sayısıdır.

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

## Diğer Kaynak Leaderboard'ları
Her bitkinin, o bitkiyi olabildiğince hızlı bir şekilde toplamak için kendi leaderboard'u vardır. Tüm kilit açmalarla, bitkiyi yetiştirmek için ihtiyacın olan kaynaklarla ve bolca güçle başlarsın. Amaç, bitkinin ürettiği kaynaktan `100000` tane toplamaktır.

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

`Leaderboards.Polyculture`, üç polikültür kaynağından da `100000` tane toplamayı gerektirir.