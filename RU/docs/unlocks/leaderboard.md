# Рейтинг
Раз ты здесь, значит, тебе удалось решить немало трудных задач. Но насколько эффективно?
Ты можешь соревноваться с другими игроками в разных рейтингах и смотреть, кто ведет сельское хозяйство наиболее эффективно.

Чтобы запустить рейтинг, вызови `leaderboard_run(leaderboard, filename, speedup)`.
Это начнет [симуляцию](docs/unlocks/simulation.md), похожую на `simulate()`. Разница в том, что начальные условия здесь фиксированы. Каждая категория рейтинга имеет разные начальные условия и условия успеха.

Запуск рейтинга считается успешным, если условие успеха равно `True` в момент окончания симуляции.

Симуляция НЕ закончится автоматически при достижении цели. Тебе необходимо проследить, чтобы программа завершилась.
Если запуск прошел успешно, твое время будет добавлено в рейтинг.

Чтобы уменьшить разброс, каждый запуск должен длиться не менее 2 часов (его можно ускорить, так что он не займет так много времени). Если запуск завершается раньше, он будет повторяться до тех пор, пока общая продолжительность не достигнет 2 часов. Среднее значение всех запусков затем загрузится как твой результат.

Вот пример настройки, который поможет попасть в рейтинг по сену.
![](LeaderboardSetup400)

## Самый быстрый сброс
Самый быстрый сброс — наиболее престижная категория. Необходимо полностью автоматизировать игру от одной клетки фермы до повторной разблокировки рейтинга.

Не обязательно разблокировать все технологии. Главное — постарайся как можно быстрее разблокировать `Unlocks.Leaderboard`.

Помни: ты можешь использовать `num_unlocked(unlock) > 0`, чтобы проверить, разблокировано ли что-то, а также `get_cost()` для технологий — чтобы узнать их стоимость и автоматически собирать нужные предметы.

Вызов функции:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Эквивалентная симуляция:
`unlocks = {}
items = {}
globals = {}
#отрицательное значение seed означает, что используется случайное значение seed
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Условие успеха:
`num_unlocked(Unlocks.Leaderboard) > 0`

## Лабиринт
Начни со всеми разблокированными технологиями и как можно быстрее собери `9863168` золота. Это ровно столько золота, сколько ты заработаешь, повторно использовав один лабиринт 32x32 `300` раз.

Вызов функции:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Эквивалентная симуляция:
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Условие успеха:
`num_items(Items.Gold) >= 9863168`

## Динозавр
Начни со всеми разблокированными технологиями и как можно быстрее собери `33488928` костей. Это ровно столько костей, сколько ты получишь, если заполнишь хвостом динозавра область 32x32.

Вызов функции:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Эквивалентная симуляция:
`unlocks = Unlocks
items = {Items.Cactus : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Условие успеха:
`num_items(Items.Bone) >= 33488928`

## Другие рейтинги по ресурсам
Для каждого растения есть свой рейтинг по скорости сбора. Ты начинаешь со всеми разблокированными технологиями, ресурсами, необходимыми для выращивания растения, и большим количеством энергии. Цель — собрать определенное количество ресурса, производимого растением.

Как и всегда, тебе необходимо проследить, чтобы программа завершилась при достижении цели. Запуск не будет считаться завершенным, пока программа не остановится, даже если цель достигнута.

### `Leaderboards.Cactus`
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
Условие успеха: `num_items(Items.Cactus) >= 33554432`

### `Leaderboards.Sunflowers`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
Условие успеха: `num_items(Items.Sunflower) >= 100000`

### `Leaderboards.Pumpkins`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
Условие успеха: `num_items(Items.Pumpkin) >= 200000000`

### `Leaderboards.Wood`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
Условие успеха: `num_items(Items.Wood) >= 10000000000`

### `Leaderboards.Carrots`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
Условие успеха: `num_items(Items.Carrot) >= 2000000000`

### `Leaderboards.Hay`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
Условие успеха: `num_items(Items.Hay) >= 2000000000`

## Рейтинги для одного дрона
Также есть рейтинги по сбору ресурсов одним дроном. Ты получаешь только одного дрона и ферму 8x8, и тебе нужно как можно быстрее собрать определенное количество ресурсов.

### `Leaderboards.Maze_Single`
`leaderboard_run(Leaderboards.Maze_Single, filename, speedup)`
Условие успеха: `num_items(Items.Gold) >= 616448`

### `Leaderboards.Cactus_Single`
`leaderboard_run(Leaderboards.Cactus_Single, filename, speedup)`
Условие успеха: `num_items(Items.Cactus) >= 131072`

### `Leaderboards.Sunflowers_Single`
`leaderboard_run(Leaderboards.Sunflowers_Single, filename, speedup)`
Условие успеха: `num_items(Items.Sunflower) >= 10000`

### `Leaderboards.Pumpkins_Single`
`leaderboard_run(Leaderboards.Pumpkins_Single, filename, speedup)`
Условие успеха: `num_items(Items.Pumpkin) >= 10000000`

### `Leaderboards.Wood_Single`
`leaderboard_run(Leaderboards.Wood_Single, filename, speedup)`
Условие успеха: `num_items(Items.Wood) >= 500000000`

### `Leaderboards.Carrots_Single`
`leaderboard_run(Leaderboards.Carrots_Single, filename, speedup)`
Условие успеха: `num_items(Items.Carrot) >= 100000000`

### `Leaderboards.Hay_Single`
`leaderboard_run(Leaderboards.Hay_Single, filename, speedup)`
Условие успеха: `num_items(Items.Hay) >= 100000000`