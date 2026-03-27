# Таблиця лідерів
Якщо ви зайшли так далеко, то вже подолали багато викликів. Але чи зробили ви це ефективно?
Ви можете змагатися з іншими гравцями в різних таблицях лідерів за найефективніші методи фермерства.

Ви можете почати забіг у таблиці лідерів, використавши: `leaderboard_run(leaderboard, filename, speedup)`.
Це запускає [симуляцію](docs/unlocks/simulation.md) подібно до `simulate()` , але з фіксованими початковими умовами. Кожна категорія має власні стартові умови та умови для успіху.

Забіг вважається успішним, якщо умова для успіху дорівнює `True` на момент завершення симуляції. 

Симуляція НЕ завершується автоматично, коли ціль досягнута. Ви повинні самі подбати про завершення програми.
Якщо забіг успішний, ваш час буде додано до таблиці лідерів.

Щоб зменшити випадковість результатів, кожен забіг має тривати щонайменше 2 години (можна прискорити, тому це не займе реального часу). Якщо забіг завершується раніше, його буде повторено, доки загальний час не досягне 2 годин. Потім завантажується середній результат усіх спроб.

Ось приклад налаштування, який дозволить вам потрапити в таблицю лідерів сіна.
![](LeaderboardSetup400)

## Швидке скидання
Швидке скидання – це найпрестижніша категорія. Повністю автоматизуйте гру від однієї фермерської ділянки до повторного розблокування таблиці лідерів.

Вам не потрібно розблоковувати все, просто спробуйте розблокувати `Unlocks.Leaderboard` якомога швидше.

Пам'ятайте, що ви можете використовувати  `num_unlocked(unlock) > 0`, щоб перевірити, чи щось розблоковано, а також `get_cost()`, щоб подивитися вартість відкриття для автоматичного збирання потрібних ресурсів.

Виклик функції:

`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Еквівалентна симуляція:

`unlocks = {}
items = {}
globals = {}
#негативне значення сіда означає випадковий сід
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Умова для успіху:

`num_unlocked(Unlocks.Leaderboard) > 0`

## Лабіринт
Почніть з усіма відкритими можливостями та назбирайте `9863168` золота якнайшвидше. Саме стільки золота ви назбираєте, використовуючи один лабіринт 32x32 `300` разів.

Виклик функції:

`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Еквівалентна симуляція:

`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Умова для успіху:

`num_items(Items.Gold) >= 9863168`

## Динозавр
Почніть з усіма відкритими можливостями та назбирайте `33488928` кісток якнайшвидше. Саме стільки кісток ви отримаєте, якщо заповните область 32x32 хвостом динозавра.

Виклик функції:

`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Еквівалентна симуляція:

`unlocks = Unlocks
items = {Items.Cactus : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Умова для успіху:

`num_items(Items.Bone) >= 33488928`

## Таблиці лідерів для інших ресурсів
Кожна рослина має власну таблицю лідерів. Ви стартуєте з усіма відкритими можливостями, необхідними ресурсами та великою кількістю енергії. Мета — назбирати визначену кількість ресурсу.

Як завжди, ви повинні завершити програму, коли досягаєте мети. Виконання умов не вважається завершеним, доки програма не завершиться, навіть якщо мету досягнуто.

### `Leaderboards.Cactus`

`leaderboard_run(Leaderboards.Cactus, filename, speedup)`

Умова для успіху: `num_items(Items.Cactus) >= 33554432`

### `Leaderboards.Sunflowers`

`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`

Умова для успіху: `num_items(Items.Power) >= 100000`

### `Leaderboards.Pumpkins`

`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`

Умова для успіху: `num_items(Items.Pumpkin) >= 200000000`

### `Leaderboards.Wood`

`leaderboard_run(Leaderboards.Wood, filename, speedup)`

Умова для успіху: `num_items(Items.Wood) >= 10000000000`

### `Leaderboards.Carrots`

`leaderboard_run(Leaderboards.Carrots, filename, speedup)`

Умова для успіху: `num_items(Items.Carrot) >= 2000000000`

### `Leaderboards.Hay`

`leaderboard_run(Leaderboards.Hay, filename, speedup)`

Умова для успіху: `num_items(Items.Hay) >= 2000000000`

## Таблиці лідерів для одного дрона
Також є таблиці лідерів для фермерства з одним дроном. Ви отримуєте лише один дрон та ферму 8x8, і вам потрібно якомога швидше зібрати певну кількість ресурсів.

### `Leaderboards.Maze_Single`

`leaderboard_run(Leaderboards.Maze_Single, filename, speedup)`

Умова для успіху: `num_items(Items.Gold) >= 616448`

### `Leaderboards.Cactus_Single`

`leaderboard_run(Leaderboards.Cactus_Single, filename, speedup)`

Умова для успіху: `num_items(Items.Cactus) >= 131072`

### `Leaderboards.Sunflowers_Single`

`leaderboard_run(Leaderboards.Sunflowers_Single, filename, speedup)`

Умова для успіху: `num_items(Items.Power) >= 10000`

### `Leaderboards.Pumpkins_Single`

`leaderboard_run(Leaderboards.Pumpkins_Single, filename, speedup)`

Умова для успіху: `num_items(Items.Pumpkin) >= 10000000`

### `Leaderboards.Wood_Single`

`leaderboard_run(Leaderboards.Wood_Single, filename, speedup)`

Умова для успіху: `num_items(Items.Wood) >= 500000000`

### `Leaderboards.Carrots_Single`

`leaderboard_run(Leaderboards.Carrots_Single, filename, speedup)`

Умова для успіху: `num_items(Items.Carrot) >= 100000000`

### `Leaderboards.Hay_Single`

`leaderboard_run(Leaderboards.Hay_Single, filename, speedup)`

Умова для успіху: `num_items(Items.Hay) >= 100000000`