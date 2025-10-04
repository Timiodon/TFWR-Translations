# 리더보드
여기까지 오셨다면, 많은 도전을 극복하셨을 거예요. 하지만 효율적으로 해결하셨나요? 
다양한 리더보드에서 다른 플레이어들과 가장 효율적인 농사 방법으로 경쟁할 수 있어요.

`leaderboard_run(leaderboard, filename, speedup)`을 호출하여 리더보드 런을 시작할 수 있어요.
이것은 시작 조건이 고정되어 있다는 점을 제외하면 `simulate()`와 유사한 [시뮬레이션](docs/unlocks/simulation.md)을 시작해요. 각 리더보드 카테고리는 다른 시작과 성공 조건을 가지고 있어요.

리더보드 런은 시뮬레이션이 끝날 때 성공 조건이 `True`이면 성공해요. 

목표에 도달해도 시뮬레이션은 자동으로 끝나지 않아요. 프로그램이 종료되도록 해야 해요.
런이 성공하면, 여러분의 시간이 리더보드에 추가될 거예요.

편차를 줄이기 위해, 모든 런은 최소 2시간 동안 실행되어야 해요 (속도를 높일 수 있으니 그렇게 오래 걸리지는 않을 거예요). 런이 더 일찍 완료되면, 총 2시간이 될 때까지 반복될 거예요. 그런 다음 모든 런의 평균이 여러분의 점수로 업로드돼요.

건초 리더보드에 오를 수 있는 예시 설정이에요.
![](LeaderboardSetup400)

## 가장 빠른 리셋
가장 빠른 리셋은 가장 권위 있는 카테고리예요. 단 하나의 농지에서 시작하여 리더보드를 다시 해금할 때까지 게임을 완전히 자동화하세요.

모든 것을 해금할 필요는 없으며, 가능한 한 빨리 `Unlocks.Leaderboard`를 해금하려고 노력하세요.

`num_unlocked(unlock) > 0`을 사용하여 무언가가 해금되었는지 확인할 수 있고, 해금에 `get_cost()`를 사용하여 비용을 확인하여 올바른 아이템을 자동으로 수확할 수 있다는 것을 기억하세요.

함수 호출:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

동등한 시뮬레이션:
`unlocks = {}
items = {}
globals = {}
#음수 시드 값은 무작위 시드를 의미해요
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

성공 조건:
`num_unlocked(Unlocks.Leaderboard) > 0`

## 미로
모든 것이 해금된 상태에서 시작하여 가능한 한 빨리 `9863168` 골드를 모으세요. 이것은 32x32 미로 하나를 `300`번 재사용하여 얻는 정확한 금의 양이에요.

함수 호출:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

동등한 시뮬레이션:
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

성공 조건:
`num_items(Items.Gold) >= 9863168`

## 공룡
모든 것이 해금된 상태에서 시작하여 가능한 한 빨리 `33488928`개의 뼈를 모으세요. 이것은 32x32 영역을 공룡 꼬리로 채우면 얻게 될 정확한 뼈의 수예요.

함수 호출:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

동등한 시뮬레이션:
`unlocks = Unlocks
items = {Items.Cactus : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

성공 조건:
`num_items(Items.Bone) >= 33488928`

## 다른 자원 리더보드
각 식물은 해당 식물을 가능한 한 빨리 재배하는 자체 리더보드가 있어요. 모든 해금 요소, 식물을 키우는 데 필요한 자원, 그리고 많은 파워를 가지고 시작해요. 목표는 식물이 생산하는 자원을 정해진 양만큼 모으는 것이에요.

언제나처럼, 목표에 도달하면 프로그램이 종료되도록 해야 해요. 목표에 도달하더라도 프로그램이 끝나기 전까지는 런이 완료된 것이 아니에요.

### `Leaderboards.Cactus`
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
성공 조건: `num_items(Items.Cactus) >= 33554432`

### `Leaderboards.Sunflowers`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
성공 조건: `num_items(Items.Sunflower) >= 100000`

### `Leaderboards.Pumpkins`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
성공 조건: `num_items(Items.Pumpkin) >= 200000000`

### `Leaderboards.Wood`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
성공 조건: `num_items(Items.Wood) >= 10000000000`

### `Leaderboards.Carrots`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
성공 조건: `num_items(Items.Carrot) >= 2000000000`

### `Leaderboards.Hay`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
성공 조건: `num_items(Items.Hay) >= 2000000000`

## 싱글 드론 리더보드
싱글 드론으로 농사짓는 리더보드도 있어요. 드론 하나와 8x8 농장만 주어지며, 정해진 양의 자원을 가능한 한 빨리 모아야 해요.

### `Leaderboards.Maze_Single`
`leaderboard_run(Leaderboards.Maze_Single, filename, speedup)`
성공 조건: `num_items(Items.Gold) >= 616448`

### `Leaderboards.Cactus_Single`
`leaderboard_run(Leaderboards.Cactus_Single, filename, speedup)`
성공 조건: `num_items(Items.Cactus) >= 131072`

### `Leaderboards.Sunflowers_Single`
`leaderboard_run(Leaderboards.Sunflowers_Single, filename, speedup)`
성공 조건: `num_items(Items.Sunflower) >= 10000`

### `Leaderboards.Pumpkins_Single`
`leaderboard_run(Leaderboards.Pumpkins_Single, filename, speedup)`
성공 조건: `num_items(Items.Pumpkin) >= 10000000`

### `Leaderboards.Wood_Single`
`leaderboard_run(Leaderboards.Wood_Single, filename, speedup)`
성공 조건: `num_items(Items.Wood) >= 500000000`

### `Leaderboards.Carrots_Single`
`leaderboard_run(Leaderboards.Carrots_Single, filename, speedup)`
성공 조건: `num_items(Items.Carrot) >= 100000000`

### `Leaderboards.Hay_Single`
`leaderboard_run(Leaderboards.Hay_Single, filename, speedup)`
성공 조건: `num_items(Items.Hay) >= 100000000`