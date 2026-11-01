# Подземный рейтинг
Под землей ждут еще более сложные испытания. Готов оптимизировать свои программы добычи и земледелия?
С этой технологией можно соревноваться за самые эффективные методы на глубине.

Подземный рейтинговый забег можно начать вызовом `leaderboard_run(leaderboard, filename, speedup)`.
Это начнет [симуляцию](docs/unlocks/simulation.md), похожую на `simulate()`. Разница в том, что начальные условия здесь фиксированы. Каждая категория рейтинга имеет разные начальные условия и условия успеха.

Запуск рейтинга считается успешным, если условие успеха равно `True` в момент окончания симуляции.

Симуляция НЕ закончится автоматически при достижении цели. Тебе необходимо проследить, чтобы программа завершилась.
Если запуск прошел успешно, твое время будет добавлено в рейтинг.

Чтобы уменьшить разброс, запуски должны в сумме охватывать не менее 2 часов симулированного времени. Симуляцию можно ускорить, поэтому в реальном времени ждать так долго не придется. Если отдельный запуск завершается раньше, он будет повторяться, пока суммарное симулированное время всех запусков не достигнет 2 часов. В рейтинг загружается среднее время этих запусков.

Вот пример настройки для попадания в рейтинг `Leaderboards.Rice_Single`.

![|x400](UndergroundLeaderboardSetup)

## Самый быстрый подземный сброс
Подземный сброс — самая престижная категория. В ней ты полностью автоматизируешь дерево добычи, начиная с одной клетки и заканчивая повторным открытием `Unlocks.Underground_Leaderboard`.

Не нужно открывать все — просто как можно быстрее открой `Unlocks.Underground_Leaderboard`.

Помни: ты можешь использовать `num_unlocked(unlock) > 0`, чтобы проверить, разблокировано ли что-то, а также `get_cost()` для технологий — чтобы узнать их стоимость и автоматически собирать нужные предметы.

`unlock()` не учитывает зависимости в дереве технологий. Например, можно разблокировать `Unlocks.Fertilizer` раньше `Unlocks.Water`.

Вызов функции:
`leaderboard_run(Leaderboards.Fastest_Underground_Reset, filename, speedup)`

Эквивалентная симуляция:
`unlocks = {}
items = {}
globals = {}
#отрицательное значение seed означает, что используется случайное значение seed
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Условие успеха:
`num_unlocked(Unlocks.Underground_Leaderboard) > 0`

## Руды
Этот рейтинг проверяет навыки добычи руд, прежде всего кварца. Генерация земли изменена так, чтобы пласты давали сначала уголь, затем железо, затем кварц.

Начни со всеми разблокированными технологиями и как можно быстрее собери `20000` кварца.

Вызов функции:
`leaderboard_run(Leaderboards.Ores, filename, speedup)`

Эквивалентная симуляция:
`unlocks = Unlocks
items = {Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Условие успеха:
`num_items(Items.Quartz) >= 20000`

## Карта сокровищ
В этом рейтинге все открыто с самого начала, и у тебя много энергии. Генерация земли изменена так, чтобы карт сокровищ было много.

Соревнование проходит в мире 8x8 с одним дроном. Цель — как можно быстрее собрать `115000` золота.

Вызов функции:
`leaderboard_run(Leaderboards.Treasure_Map, filename, speedup)`

Эквивалентная симуляция:
`unlocks = Unlocks
items = {Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Условие успеха:
`num_items(Items.Gold) >= 115000`

## Ресурсные рейтинги
В этих рейтингах нужно как можно быстрее собирать определенные ресурсы. Все открыто с самого начала, и у тебя много энергии. Исключение — рейтинг пирамид, где энергию нужно добывать самостоятельно, восстанавливая пирамиды.

Цель — собрать заданное количество ресурсов.

Как и всегда, тебе необходимо проследить, чтобы программа завершилась при достижении цели. Запуск не будет считаться завершенным, пока программа не остановится, даже если цель достигнута.

Эти рейтинги меняют генерацию земли так, чтобы нужный ресурс встречался снова и снова. Поэтому использовать `clear()` не нужно. Например, в рисовом рейтинге есть только глиняные пласты.

### `Leaderboards.Rice`
`leaderboard_run(Leaderboards.Rice, filename, speedup)`
Условие успеха: `num_items(Items.Rice) >= 2000000`

### `Leaderboards.Bamboo`
В бамбуковом рейтинге нельзя копать.

`leaderboard_run(Leaderboards.Bamboo, filename, speedup)`
Условие успеха: `num_items(Items.Bamboo) >= 500000000`

### `Leaderboards.Dynamite`
`leaderboard_run(Leaderboards.Dynamite, filename, speedup)`
Условие успеха: `num_items(Items.Dynamite) >= 10000000`

### `Leaderboards.Mushrooms`
`leaderboard_run(Leaderboards.Mushrooms, filename, speedup)`
Условие успеха: `num_items(Items.Mushroom) >= 240000`

### `Leaderboards.Pyramids`
`leaderboard_run(Leaderboards.Pyramids, filename, speedup)`
Условие успеха: `num_items(Items.Power) >= 150000`

## Подземные рейтинги с одним дроном
Также есть рейтинги по сбору ресурсов одним дроном. Ты получаешь только одного дрона и ферму 8x8, и тебе нужно как можно быстрее собрать определенное количество ресурсов.

### `Leaderboards.Rice_Single`
`leaderboard_run(Leaderboards.Rice_Single, filename, speedup)`
Условие успеха: `num_items(Items.Rice) >= 100000`

### `Leaderboards.Ores_Single`
`leaderboard_run(Leaderboards.Ores_Single, filename, speedup)`
Условие успеха: `num_items(Items.Quartz) >= 4000`

### `Leaderboards.Bamboo_Single`
`leaderboard_run(Leaderboards.Bamboo_Single, filename, speedup)`
Условие успеха: `num_items(Items.Bamboo) >= 25000000`

### `Leaderboards.Dynamite_Single`
`leaderboard_run(Leaderboards.Dynamite_Single, filename, speedup)`
Условие успеха: `num_items(Items.Dynamite) >= 100000`

### `Leaderboards.Mushrooms_Single`
`leaderboard_run(Leaderboards.Mushrooms_Single, filename, speedup)`
Условие успеха: `num_items(Items.Mushroom) >= 30000`

### `Leaderboards.Pyramids_Single`
`leaderboard_run(Leaderboards.Pyramids_Single, filename, speedup)`
Условие успеха: `num_items(Items.Power) >= 30000`

