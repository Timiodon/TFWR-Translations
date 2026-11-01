# 지하 리더보드
지하에는 더 큰 도전이 기다립니다. 채광과 농사 프로그램을 최적화할 준비가 됐나요?
이 해금 항목으로 깊은 지하에서 가장 효율적인 방법을 겨룰 수 있습니다.

`leaderboard_run(leaderboard, filename, speedup)`을 호출해 지하 리더보드 도전을 시작할 수 있습니다.
이것은 시작 조건이 고정되어 있다는 점을 제외하면 `simulate()`와 유사한 [시뮬레이션](docs/unlocks/simulation.md)을 시작해요. 각 리더보드 카테고리는 다른 시작과 성공 조건을 가지고 있어요.

리더보드 런은 시뮬레이션이 끝날 때 성공 조건이 `True`이면 성공해요. 

목표에 도달해도 시뮬레이션은 자동으로 끝나지 않아요. 프로그램이 종료되도록 해야 해요.
런이 성공하면, 여러분의 시간이 리더보드에 추가될 거예요.

편차를 줄이기 위해 모든 런은 최소 2시간의 시뮬레이션 시간을 포함해야 해요. 시뮬레이션 속도를 높일 수 있으므로 실제로 그렇게 오래 걸리지는 않아요. 런이 더 일찍 끝나면 총 시뮬레이션 시간이 2시간에 도달할 때까지 반복돼요. 그런 다음 모든 런의 평균 시간이 점수로 업로드돼요.

`Leaderboards.Rice_Single` 리더보드에 진입하기 위한 예시 설정입니다.

![|x400](UndergroundLeaderboardSetup)

## 가장 빠른 지하 초기화
지하 초기화는 가장 명예로운 종목입니다. 농장 한 칸에서 시작해 `Unlocks.Underground_Leaderboard`를 다시 해금할 때까지 채광 해금 트리를 완전히 자동화합니다.

전부 해금할 필요는 없습니다. `Unlocks.Underground_Leaderboard`를 최대한 빨리 해금하세요.

`num_unlocked(unlock) > 0`을 사용하여 무언가가 해금되었는지 확인할 수 있고, 해금에 `get_cost()`를 사용하여 비용을 확인하여 올바른 아이템을 자동으로 수확할 수 있다는 것을 기억하세요.

`unlock()`은 기술 트리의 의존 관계를 따지지 않아요. 예를 들어 `Unlocks.Water`보다 `Unlocks.Fertilizer`를 먼저 해금할 수도 있어요.

함수 호출:
`leaderboard_run(Leaderboards.Fastest_Underground_Reset, filename, speedup)`

동등한 시뮬레이션:
`unlocks = {}
items = {}
globals = {}
# 음수 시드 값은 무작위 시드를 의미해요
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

성공 조건:
`num_unlocked(Unlocks.Underground_Leaderboard) > 0`

## 광물
이 리더보드는 광물, 특히 석영을 모으는 실력을 시험합니다. 땅의 층이 석탄, 철, 석영 순으로 제공되도록 생성을 변경합니다.

모두 해금된 상태에서 석영 `20000`개를 최대한 빨리 모으세요.

함수 호출:
`leaderboard_run(Leaderboards.Ores, filename, speedup)`

동등한 시뮬레이션:
`unlocks = Unlocks
items = {Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

성공 조건:
`num_items(Items.Quartz) >= 20000`

## 보물 지도
이 리더보드는 모두 해금되고 파워가 풍부한 상태에서 시작합니다. 보물 지도가 많이 나타나도록 땅 생성을 변경합니다.

8x8 세계에서 드론 한 대로 진행합니다. 목표는 골드 `115000`개를 최대한 빨리 모으는 것입니다.

함수 호출:
`leaderboard_run(Leaderboards.Treasure_Map, filename, speedup)`

동등한 시뮬레이션:
`unlocks = Unlocks
items = {Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

성공 조건:
`num_items(Items.Gold) >= 115000`

## 자원 리더보드
이 리더보드는 특정 자원을 최대한 빨리 모으는 데 초점을 맞춥니다. 모두 해금되고 파워가 풍부한 상태에서 시작합니다. 피라미드 리더보드만 예외로, 직접 피라미드를 복원해 파워를 생산해야 합니다.

목표는 정해진 양의 자원을 모으는 것입니다.

언제나처럼, 목표에 도달하면 프로그램이 종료되도록 해야 해요. 목표에 도달하더라도 프로그램이 끝나기 전까지는 런이 완료된 것이 아니에요.

이 리더보드들은 원하는 자원이 계속 나타나도록 땅 생성을 변경합니다. 따라서 `clear()`가 필요 없습니다. 예를 들어 벼 리더보드에는 점토층만 있습니다.

### `Leaderboards.Rice`
`leaderboard_run(Leaderboards.Rice, filename, speedup)`
성공 조건: `num_items(Items.Rice) >= 2000000`

### `Leaderboards.Bamboo`
대나무 리더보드에서는 굴착이 금지됩니다.

`leaderboard_run(Leaderboards.Bamboo, filename, speedup)`
성공 조건: `num_items(Items.Bamboo) >= 500000000`

### `Leaderboards.Dynamite`
`leaderboard_run(Leaderboards.Dynamite, filename, speedup)`
성공 조건: `num_items(Items.Dynamite) >= 10000000`

### `Leaderboards.Mushrooms`
`leaderboard_run(Leaderboards.Mushrooms, filename, speedup)`
성공 조건: `num_items(Items.Mushroom) >= 240000`

### `Leaderboards.Pyramids`
`leaderboard_run(Leaderboards.Pyramids, filename, speedup)`
성공 조건: `num_items(Items.Power) >= 150000`

## 단일 드론 지하 리더보드
싱글 드론으로 농사짓는 리더보드도 있어요. 드론 하나와 8x8 농장만 주어지며, 정해진 양의 자원을 가능한 한 빨리 모아야 해요.

### `Leaderboards.Rice_Single`
`leaderboard_run(Leaderboards.Rice_Single, filename, speedup)`
성공 조건: `num_items(Items.Rice) >= 100000`

### `Leaderboards.Ores_Single`
`leaderboard_run(Leaderboards.Ores_Single, filename, speedup)`
성공 조건: `num_items(Items.Quartz) >= 4000`

### `Leaderboards.Bamboo_Single`
`leaderboard_run(Leaderboards.Bamboo_Single, filename, speedup)`
성공 조건: `num_items(Items.Bamboo) >= 25000000`

### `Leaderboards.Dynamite_Single`
`leaderboard_run(Leaderboards.Dynamite_Single, filename, speedup)`
성공 조건: `num_items(Items.Dynamite) >= 100000`

### `Leaderboards.Mushrooms_Single`
`leaderboard_run(Leaderboards.Mushrooms_Single, filename, speedup)`
성공 조건: `num_items(Items.Mushroom) >= 30000`

### `Leaderboards.Pyramids_Single`
`leaderboard_run(Leaderboards.Pyramids_Single, filename, speedup)`
성공 조건: `num_items(Items.Power) >= 30000`

