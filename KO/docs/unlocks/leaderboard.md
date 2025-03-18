# 리더보드

여기까지 오셨다면, 많은 도전을 극복하셨습니다. 하지만 효율적으로 해결하셨나요?
가장 효율적인 농법을 위해 다양한 리더보드에서 다른 플레이어들과 경쟁할 수 있습니다.

`leaderboard_run(leaderboard, filename, speedup)`을 호출하여 리더보드 실행을 시작할 수 있습니다. 이는 `simulate()`와 유사한 [시뮬레이션](docs/unlocks/simulation.md)을 시작하나 시작 조건이 고정됩니다. 각 리더보드 카테고리는 서로 다른 시작 및 성공 조건을 가지고 있습니다.

리더보드 실행은 시뮬레이션 종료 시 성공 조건이 `True`인 경우 성공합니다. 목표가 달성되더라도 시뮬레이션은 자동으로 끝나지 않습니다. 프로그램이 종료되도록 확실히 해야 합니다. 실행이 성공할 경우, 당신의 시간이 리더보드에 추가됩니다.

변동성을 줄이기 위해, 모든 실행은 최소 2시간 동안 실행되어야 합니다 (속도를 높일 수 있으니 그렇게 오래 걸리진 않습니다). 실행이 더 빨리 완료되면, 총 2시간에 이를 때까지 반복됩니다. 모든 실행의 평균이 점수로 업로드됩니다.

다음은 건초 리더보드에 오르기 위한 예제 설정입니다.
![](LeaderboardSetup400)

## 가장 빠른 리셋
가장 빠른 리셋은 가장 명성 높은 카테고리입니다. 하나의 농장 구획에서 전적으로 게임을 자동화하여 다시 리더보드 잠금을 해제하세요.

모든 것을 해제할 필요는 없고, 최대한 빨리 `Unlocks.Leaderboard`만 해제하도록 노력하세요.

`num_unlocked(unlock) > 0`을 사용하여 무언가가 해제되었는지 확인할 수 있으며, `get_cost()`를 사용하여 자동으로 적절한 아이템을 농사할 수 있도록 비용을 볼 수 있습니다.

함수 호출:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

동등한 시뮬레이션:
`unlocks = {}
items = {}
globals = {}
# 음수의 seed 값은 무작위 seed를 의미합니다
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

성공 조건:
`num_unlocked(Unlocks.Leaderboard) > 0`

## 미로
모든 잠금을 해제한 상태에서 가능한 한 빠르게 `300000` 골드를 농사하세요. 이는 정확히 미로 한 번을 `300`번 풀었을 때 얻을 수 있는 골드 양입니다.

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
모든 잠금을 해제한 상태에서 가능한 한 빠르게 `98010` 뼈를 농사하세요. 이는 10x10 구역을 공룡 꼬리로 채웠을 때 얻을 수 있는 뼈의 양입니다.

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

## 다른 자원 리더보드
각 식물은 해당 식물을 가능한 한 빠르게 농사하는 리더보드를 가지고 있습니다. 모든 잠금을 해제한 상태로 시작하며, 식물을 기르기 위해 필요한 자원과 많은 파워를 얻습니다. 목표는 해당 식물이 생산하는 자원 `100000`개를 농사하는 것입니다.

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

`Leaderboards.Polyculture`는 세 가지 폴리컬쳐 자원을 각각 `100000`개 농사해야 합니다.