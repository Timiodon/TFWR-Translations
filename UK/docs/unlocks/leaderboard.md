# Таблиця лідерів (Leaderboard)
Якщо ви дійшли до цього моменту, ви подолали багато викликів. Але чи розв'язали ви їх ефективно? 
Ви можете змагатися з іншими гравцями в різних таблицях лідерів за найефективніші методи фермерства.

Ви можете почати забіг для таблиці лідерів, викликавши `leaderboard_run(leaderboard, filename, speedup)`.
Це запустить [симуляцію](docs/unlocks/simulation.md), подібну до `simulate()`, за винятком того, що початкові умови фіксовані. Кожна категорія таблиці лідерів має різні умови старту та успіху.

Забіг вважається успішним, якщо умова успіху є `True` на момент завершення симуляції. 

Симуляція НЕ завершиться автоматично після досягнення мети. Ви повинні переконатися, що програма завершує роботу.
Якщо забіг успішний, ваш час буде додано до таблиці лідерів.

Щоб зменшити похибку, усі забіги мають тривати щонайменше 2 години (ви можете прискорити процес, тож це не займе так багато реального часу). Якщо забіг завершується раніше, він буде повторюватися, доки загальний час не сягне 2 годин. Середній результат усіх забігів буде завантажено як ваш рахунок.

Ось приклад налаштування, яке допоможе вам потрапити в таблицю лідерів по сіну.
![](LeaderboardSetup400)

## Найшвидше скидання (Fastest Reset)
Найшвидше перезавантаження — найпрестижніша категорія. Повністю автоматизуйте гру від однієї ділянки ферми до повторного розблокування таблиць лідерів.

Вам не обов'язково розблоковувати все, просто спробуйте розблокувати `Unlocks.Leaderboard` якомога швидше.

Пам'ятайте, що ви можете використовувати `num_unlocked(unlock) > 0`, щоб перевірити, чи розблоковано щось, і ви можете використовувати `get_cost()` для розблокувань, щоб побачити їхню вартість і автоматично вирощувати потрібні предмети.

Виклик функції:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Еквівалентна симуляція:
`unlocks = {}
items = {}
globals = {}
#від'ємне значення seed означає випадковий seed
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Умова успіху:
`num_unlocked(Unlocks.Leaderboard) > 0`

## Лабіринт (Maze)
Почніть з усім розблокованим і зберіть `9863168` золота якомога швидше. Це саме та кількість золота, яку ви заробите, повторно використовуючи один лабіринт розміром 32x32 `300` разів.

Виклик функції:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Еквівалентна симуляція:
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Умова успіху:
`num_items(Items.Gold) >= 9863168`

## Динозавр (Dinosaur)
Почніть з усім розблокованим і зберіть `33488928` кісток якомога швидше. Це саме та кількість кісток, яку ви отримаєте, якщо заповните ділянку 32x32 хвостом динозавра.

Виклик функції:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Еквівалентна симуляція:
`unlocks = Unlocks
items = {Items.Cactus : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Умова успіху:
`num_items(Items.Bone) >= 33488928`

## Інші таблиці лідерів ресурсів
Кожна рослина має власну таблицю лідерів для вирощування цієї конкретної рослини якомога швидше. Ви починаєте з усіма розблокуваннями, ресурсами, необхідними для вирощування рослини, і великою кількістю енергії (power). Мета — зібрати певну кількість ресурсу, який виробляє рослина.

Як завжди, вам потрібно переконатися, що ваша програма завершується, коли ви досягаєте мети. Забіг не вважається завершеним, поки програма не закінчиться, навіть якщо мета досягнута.

### `Leaderboards.Cactus`
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
Умова успіху: `num_items(Items.Cactus) >= 33554432`

### `Leaderboards.Sunflowers`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
Умова успіху: `num_items(Items.Power) >= 100000`

### `Leaderboards.Pumpkins`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
Умова успіху: `num_items(Items.Pumpkin) >= 200000000`

### `Leaderboards.Wood`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
Умова успіху: `num_items(Items.Wood) >= 10000000000`

### `Leaderboards.Carrots`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
Умова успіху: `num_items(Items.Carrot) >= 2000000000`

### `Leaderboards.Hay`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
Умова успіху: `num_items(Items.Hay) >= 2000000000`

## Таблиці лідерів для одного дрона
Існують також таблиці лідерів для фермерства одним дроном. Ви отримуєте лише одного дрона та ферму 8x8 і маєте зібрати певну кількість ресурсів якомога швидше.

### `Leaderboards.Maze_Single`
`leaderboard_run(Leaderboards.Maze_Single, filename, speedup)`
Умова успіху: `num_items(Items.Gold) >= 616448`

### `Leaderboards.Cactus_Single`
`leaderboard_run(Leaderboards.Cactus_Single, filename, speedup)`
Умова успіху: `num_items(Items.Cactus) >= 131072`

### `Leaderboards.Sunflowers_Single`
`leaderboard_run(Leaderboards.Sunflowers_Single, filename, speedup)`
Умова успіху: `num_items(Items.Power) >= 10000`

### `Leaderboards.Pumpkins_Single`
`leaderboard_run(Leaderboards.Pumpkins_Single, filename, speedup)`
Умова успіху: `num_items(Items.Pumpkin) >= 10000000`

### `Leaderboards.Wood_Single`
`leaderboard_run(Leaderboards.Wood_Single, filename, speedup)`
Умова успіху: `num_items(Items.Wood) >= 500000000`

### `Leaderboards.Carrots_Single`
`leaderboard_run(Leaderboards.Carrots_Single, filename, speedup)`
Умова успіху: `num_items(Items.Carrot) >= 100000000`

### `Leaderboards.Hay_Single`
`leaderboard_run(Leaderboards.Hay_Single, filename, speedup)`
Умова успіху: `num_items(Items.Hay) >= 100000000`