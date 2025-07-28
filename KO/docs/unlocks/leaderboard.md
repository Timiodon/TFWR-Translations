# Leaderboard
여기까지 오셨다면 많은 도전을 극복하셨을 겁니다. 하지만 효율적으로 해결하셨나요?
다양한 leaderboard에서 가장 효율적인 농사 방법으로 다른 플레이어와 경쟁할 수 있습니다.

`leaderboard_run(leaderboard, filename, speedup)`을 호출하여 leaderboard 실행을 시작할 수 있습니다.
이것은 시작 조건이 고정되어 있다는 점을 제외하고 `simulate()`와 유사한 [시뮬레이션](docs/unlocks/simulation.md)을 시작합니다. 각 leaderboard 카테고리마다 다른 시작 조건과 성공 조건이 있습니다.

시뮬레이션이 끝날 때 성공 조건이 `True`이면 leaderboard 실행은 성공합니다. 목표에 도달해도 시뮬레이션은 자동으로 끝나지 않습니다. 프로그램이 종료되도록 해야 합니다.
실행이 성공적이면, 여러분의 시간이 leaderboard에 추가됩니다.

편차를 줄이기 위해 모든 실행은 최소 2시간 동안 실행되어야 합니다(속도를 높일 수 있으므로 그렇게 오래 걸리지는 않습니다). 실행이 더 일찍 완료되면 총 2시간이 될 때까지 반복됩니다. 그런 다음 모든 실행의 평균이 점수로 업로드됩니다.

여기 건초 leaderboard에 오를 수 있는 예시 설정입니다.
![](LeaderboardSetup400)

## 가장 빠른 초기화
가장 빠른 초기화는 가장 권위 있는 카테고리입니다. 단일 농지에서 시작하여 다시 leaderboard를 해금할 때까지 게임을 완전히 자동화하세요.

모든 것을 해금할 필요는 없으며, `Unlocks.Leaderboard`를 가능한 한 빨리 해금하려고 노력하세요.

`num_unlocked(unlock) > 0`을 사용하여 무언가가 해금되었는지 확인할 수 있고, `get_cost()`를 해금에 사용하여 비용을 확인하고 자동으로 올바른 아이템을 수확할 수 있다는 것을 기억하세요.

함수 호출:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

동등한 시뮬레이션:
`unlocks = {}
items = {}
globals = {}
#음수 seed 값은 무작위 seed를 의미합니다
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

성공 조건:
`num_unlocked(Unlocks.Leaderboard) > 0`

## 미로
모든 것이 해금된 상태에서 시작하여 가능한 한 빨리 `300000` 금을 수확하세요. 이것은 하나의 미로를 `300`번 해결하여 얻게 될 금의 정확한 양입니다.

함수 호출:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

동등한 시뮬레이션:
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

성공 조건:
`num_items(Items.Gold) >= 300000`

## 공룡
모든 것이 해금된 상태에서 시작하여 가능한 한 빨리 `98010` 뼈를 수확하세요. 이것은 10x10 영역을 공룡 꼬리로 채우면 얻게 될 뼈의 정확한 수입니다.

함수 호출:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

동등한 시뮬레이션:
`unlocks = Unlocks
items = {Items.Pumpkin : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

성공 조건:
`num_items(Items.Bone) >= 98010`

## 기타 자원 Leaderboard
각 식물은 해당 식물을 가능한 한 빨리 수확하기 위한 자체 leaderboard를 가지고 있습니다. 모든 해금, 식물을 키우는 데 필요한 자원, 그리고 많은 파워를 가지고 시작합니다. 목표는 식물이 생산하는 자원을 `100000`개 수확하는 것입니다.

함수 호출:
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
`leaderboard_run(Leaderboards.Polyculture, filename, speedup)`

성공 조건:
`num_items(resource) >= 100000`

`Leaderboards.Polyculture`는 세 가지 모든 복합재배 자원을 `100000`개씩 수확해야 합니다.