# Leaderboard
Если вы дошли до этого момента, вы преодолели много трудностей. Но решали ли вы их эффективно? 
Вы можете соревноваться с другими игроками в различных leaderboard за самые эффективные методы ведения сельского хозяйства.

Вы можете запустить прогон для leaderboard, вызвав `leaderboard_run(leaderboard, filename, speedup)`.
Это запускает [симуляцию](docs/unlocks/simulation.md), похожую на `simulate()`, за исключением того, что начальные условия фиксированы. Каждая категория leaderboard имеет разные начальные и успешные условия.

Прогон для leaderboard считается успешным, если условие успеха `True` в момент окончания симуляции. Симуляция не закончится автоматически при достижении цели. Вы должны убедиться, что программа завершается.
Если прогон успешен, ваше время будет добавлено в leaderboard.

Чтобы уменьшить разброс, все прогоны должны длиться не менее 2 часов (вы можете ускорить это, так что это не займёт так много времени). Если прогон завершается раньше, он будет повторяться до тех пор, пока общее время не достигнет 2 часов. Среднее значение всех прогонов затем загружается как ваш результат.

Вот пример настройки, которая выведет вас в leaderboard по сену.
![](LeaderboardSetup400)

## Самый быстрый сброс
Самый быстрый сброс — самая престижная категория. Полностью автоматизируйте игру с одного участка земли до повторной разблокировки leaderboard.

Вам не нужно разблокировать всё, просто постарайтесь разблокировать `Unlocks.Leaderboard` как можно быстрее.

Помните, что вы можете использовать `num_unlocked(unlock) > 0`, чтобы проверить, разблокировано ли что-то, и вы можете использовать `get_cost()` для улучшений, чтобы узнать их стоимость, чтобы вы могли автоматически фармить нужные предметы.

Вызов функции:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Эквивалентная симуляция:
`unlocks = {}
items = {}
globals = {}
#отрицательное значение seed означает случайный seed
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Условие успеха:
`num_unlocked(Unlocks.Leaderboard) > 0`

## Лабиринт
Начните со всеми разблокированными улучшениями и соберите `300000` золота как можно быстрее. Это ровно то количество золота, которое вы заработаете, решив один лабиринт `300` раз.

Вызов функции:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Эквивалентная симуляция:
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Условие успеха:
`num_items(Items.Gold) >= 300000`

## Динозавр
Начните со всеми разблокированными улучшениями и соберите `98010` костей как можно быстрее. Это ровно то количество костей, которое вы получите, если заполните область 10x10 хвостом динозавра.

Вызов функции:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Эквивалентная симуляция:
`unlocks = Unlocks
items = {Items.Pumpkin : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Условие успеха:
`num_items(Items.Bone) >= 98010`

## Другие leaderboard по ресурсам
У каждого растения есть свой leaderboard для максимально быстрого сбора этого конкретного растения. Вы начинаете со всеми улучшениями, ресурсами, необходимыми для выращивания растения, и большим количеством энергии. Цель — собрать `100000` единиц ресурса, производимого растением.

Вызовы функций:
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
`leaderboard_run(Leaderboards.Polyculture, filename, speedup)`

Условие успеха:
`num_items(resource) >= 100000`

`Leaderboards.Polyculture` требует сбора по `100000` всех трёх ресурсов поликультуры.