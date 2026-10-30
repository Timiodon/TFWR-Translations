[<- Simülasyon](docs/unlocks/simulation.md)
---
# Sıralama Tablosu
Buraya kadar geldiysen pek çok zorluğun üstesinden gelmişsin demektir. Peki onları verimli bir şekilde mi çözdün? 
En verimli tarım yöntemleri için çeşitli sıralama tablolarında diğer oyuncularla yarışabilirsin.

Bir sıralama tablosu denemesini `leaderboard_run(leaderboard, filename, speedup)` fonksiyonunu çağırarak başlatabilirsin.
Bu, `simulate()`'e benzeyen bir [simülasyon](docs/unlocks/simulation.md) başlatır; tek farkı başlangıç koşullarının sabit olmasıdır. Her sıralama tablosu kategorisinin farklı başlangıç ve başarı koşulları vardır.

Simülasyon sona erdiğinde başarı koşulu `True` ise sıralama tablosu denemesi başarılı olur. 

Hedefe ulaşıldığında simülasyon kendiliğinden SONA ERMEZ. Programın sonlandığından emin olman gerekir.
Deneme başarılı olursa süren sıralama tablosuna eklenir.

Sonuçlardaki dalgalanmayı azaltmak için tüm denemelerin simülasyon zamanı olarak en az 2 saati kapsaması gerekir. Simülasyonu hızlandırabilirsin, yani gerçek zamanda o kadar uzun sürmez. Bir deneme daha erken biterse, toplam simülasyon süresi 2 saate ulaşana kadar tekrarlanır. Ardından tüm denemelerin ortalama süresi puanın olarak yüklenir.

Seni saman sıralama tablosuna sokacak örnek bir kurulum:
![|x400](LeaderboardSetup)

## En Hızlı Sıfırlama
En hızlı sıfırlama, en prestijli kategoridir. Bu kategoride oyunu tamamen otomatikleştirirsin: tek bir tarla karesiyle başlar, sıralama tablolarının kilidini yeniden açtığında bitirirsin.

Her şeyin kilidini açman gerekmez; sadece `Unlocks.Leaderboard`'un kilidini olabildiğince hızlı açmaya çalış.

Bir şeyin kilidinin açık olup olmadığını kontrol etmek için `num_unlocked(unlock) > 0` kullanabileceğini unutma. Kilit açmaların neye mal olduğunu görmek için de onlar üzerinde `get_cost()` kullanabilirsin; böylece doğru eşyaları otomatik olarak toplayabilirsin.

`unlock()`, teknoloji ağacındaki bağımlılıkları umursamaz. Örneğin `Unlocks.Fertilizer`'ın kilidini `Unlocks.Water`'dan önce açmak mümkündür.

Fonksiyon Çağrısı:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Eşdeğer Simülasyon:
`unlocks = {}
items = {}
globals = {}
#a negative seed value means a random seed
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Başarı Koşulu:
`num_unlocked(Unlocks.Leaderboard) > 0`

## Labirent
Her şeyin kilidi açık olarak başla ve olabildiğince hızlı `9863168` altın topla. Bu, tek bir 32x32 labirenti `300` kez yeniden kullanarak kazanacağın altın miktarıyla tam olarak aynıdır.

Fonksiyon Çağrısı:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Eşdeğer Simülasyon:
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Başarı Koşulu:
`num_items(Items.Gold) >= 9863168`

## Dinozor
Her şeyin kilidi açık olarak başla ve olabildiğince hızlı `33488928` kemik topla. Bu, 32x32'lik bir alanı dinozor kuyruğuyla doldurduğunda elde edeceğin kemik sayısıyla tam olarak aynıdır.

Fonksiyon Çağrısı:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Eşdeğer Simülasyon:
`unlocks = Unlocks
items = {Items.Cactus : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Başarı Koşulu:
`num_items(Items.Bone) >= 33488928`

## Diğer Kaynak Sıralama Tabloları
Her bitkinin, o bitkiyi olabildiğince hızlı yetiştirmek için kendi sıralama tablosu vardır. Tüm kilit açmalarla, bitkiyi yetiştirmek için gereken kaynaklarla ve bolca güçle başlarsın. Amaç, bitkinin ürettiği kaynaktan belirli bir miktar toplamaktır.

Her zamanki gibi, hedefe ulaştığında programının sonlandığından emin olman gerekir. Hedefe ulaşılmış olsa bile, program bitmeden deneme tamamlanmış sayılmaz.

### `Leaderboards.Cactus`
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
Başarı Koşulu: `num_items(Items.Cactus) >= 33554432`

### `Leaderboards.Sunflowers`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
Başarı Koşulu: `num_items(Items.Power) >= 100000`

### `Leaderboards.Pumpkins`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
Başarı Koşulu: `num_items(Items.Pumpkin) >= 200000000`

### `Leaderboards.Wood`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
Başarı Koşulu: `num_items(Items.Wood) >= 10000000000`

### `Leaderboards.Carrots`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
Başarı Koşulu: `num_items(Items.Carrot) >= 2000000000`

### `Leaderboards.Hay`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
Başarı Koşulu: `num_items(Items.Hay) >= 2000000000`

## Tek Dron Sıralama Tabloları
Tek bir dronla tarım yapmak için de sıralama tabloları vardır. Yalnızca bir dronun ve 8x8'lik bir çiftliğin olur; belirli bir miktar kaynağı olabildiğince hızlı toplaman gerekir.

### `Leaderboards.Maze_Single`
`leaderboard_run(Leaderboards.Maze_Single, filename, speedup)`
Başarı Koşulu: `num_items(Items.Gold) >= 616448`

### `Leaderboards.Cactus_Single`
`leaderboard_run(Leaderboards.Cactus_Single, filename, speedup)`
Başarı Koşulu: `num_items(Items.Cactus) >= 131072`

### `Leaderboards.Sunflowers_Single`
`leaderboard_run(Leaderboards.Sunflowers_Single, filename, speedup)`
Başarı Koşulu: `num_items(Items.Power) >= 10000`

### `Leaderboards.Pumpkins_Single`
`leaderboard_run(Leaderboards.Pumpkins_Single, filename, speedup)`
Başarı Koşulu: `num_items(Items.Pumpkin) >= 10000000`

### `Leaderboards.Wood_Single`
`leaderboard_run(Leaderboards.Wood_Single, filename, speedup)`
Başarı Koşulu: `num_items(Items.Wood) >= 500000000`

### `Leaderboards.Carrots_Single`
`leaderboard_run(Leaderboards.Carrots_Single, filename, speedup)`
Başarı Koşulu: `num_items(Items.Carrot) >= 100000000`

### `Leaderboards.Hay_Single`
`leaderboard_run(Leaderboards.Hay_Single, filename, speedup)`
Başarı Koşulu: `num_items(Items.Hay) >= 100000000`

---

[Simülasyon](docs/unlocks/simulation.md)      [Zamanlama](docs/unlocks/timing.md)      [Otomatik Kilit Açma](docs/unlocks/auto_unlock.md)      [Maliyetler](docs/unlocks/costs.md)      [İstatistikler](docs/stats.md)

[get_cost()](functions/get_cost)      [num_unlocked()](functions/num_unlocked)      [leaderboard_run()](functions/leaderboard_run)
