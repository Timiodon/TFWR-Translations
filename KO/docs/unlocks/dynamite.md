[<- 버섯](docs/unlocks/mushroom.md) <right>[폭발 드릴 ->](docs/unlocks/explosive_drill.md)
---
# 다이너마이트
이전의 채광 탐사대가 남긴 획기적인 폭발물입니다. 안타깝게도 드릴은 다이너마이트를 폭발시키기에 딱 좋아서 주변 블록을 모두 날려 버립니다. 모은 다이너마이트는 `use_item(Items.Dynamite)`로 사용할 수 있으며 드론 바로 아래에서 즉시 폭발합니다.

다이너마이트를 안전하게 굴착하려면 `Grounds.Dynamite`와 `Grounds.Soot`의 이중 지층을 찾아야 합니다. 위쪽의 다이너마이트 땅은 조금 오래되었기 때문에 일부 블록은 안전하게 굴착할 수 있습니다. 하지만 다이너마이트 일부는 아직 활성 상태이므로 굴착 시 폭발합니다.

이 예시는 다이너마이트와 첫 굴착 지점 주변을 파서 숫자가 적힌 그을음층을 드러내고 측정값을 출력합니다:
{{codeexample 
{
    "camera_position": {"x": -3, "y": 0, "z": 15},
    "show_image": true,
    "image_size": {"x": 800, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 7, "y": 7},
    "execution_speed": 2,
    "digging_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 6,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz", "petrified_pumpkins"]
}
#SETUP
jump(Unlocks.Dynamite)
for _ in range(3):
    move(East)
    move(North)
#CODE
# 다이너마이트층을 뚫고 그을음층까지 굴착
while get_ground_type() != Grounds.Soot:
    dig()

# 드론을 원형으로 움직이는 방향 목록
circle_directions = [
    East, South, West, West, 
    North, North, East, East
]
for dir in circle_directions:
    move(dir)
    dig()
    print(measure()) # 그을음 블록의 숫자
}}

## 다이너마이트 지뢰 찾기
불발탄 블록을 모두 찾아 굴착하고 활성 블록만 남길 수 있나요? 다른 활성 블록이나 그을음 블록으로만 둘러싸인 활성 블록은 다이너마이트 지층이 사라질 때 추가 다이너마이트를 제공합니다.

다행히 아래의 그을음 블록이 도움이 되겠군요. 이 블록은 인접한 다이너마이트 블록 중 활성 다이너마이트가 있는 블록의 수를 감지할 수 있습니다. 어느 블록이 활성인지는 알려주지 않고 총 몇 개가 있는지만 알려주므로, 여러 그을음 블록의 측정값을 조합해 스스로 추론해야 합니다.

그을음 블록에서 `measure()`를 호출하면 위쪽 다이너마이트 지층의 인접한 여덟 타일에 있는 활성 다이너마이트의 수를 반환합니다. 숫자는 `0`(활성 다이너마이트 없음)부터 `8`(모든 인접 블록에 활성 다이너마이트가 있음)까지입니다.

다이너마이트 지층에서 처음 파내는 블록은 항상 불발탄입니다. 다이너마이트 블록을 굴착할 때마다 다이너마이트를 약간 얻습니다. 모든 불발탄을 굴착하는 데 성공하거나 활성 다이너마이트를 실수로 파서 지층이 파괴되면, 완전히 드러난 활성 블록 수의 제곱만큼 다이너마이트를 추가로 얻습니다.

## 지층 구조
다이너마이트 지층의 활성 다이너마이트 수와 다이너마이트를 찾는 난이도는 깊이에 따라 증가합니다. 농장이 커지면 전체 지뢰 수와 층을 해결했을 때 얻는 최대 수확량도 증가합니다.

다이너마이트를 업그레이드하면 다이너마이트 블록을 굴착하거나 활성 블록을 완전히 드러내서 얻는 수확량이 늘어납니다. 또한 다이너마이트 폭발 에너지가 30% 증가합니다.

## 성공과 실패 감지
활성 다이너마이트를 파면 두 지층이 폭발합니다. `Grounds.Dynamite`를 판 뒤 `get_ground_type()`를 사용해 이를 확인할 수 있습니다. 땅이 `Grounds.Soot`가 아니라면 퍼즐을 풀지 못한 겁니다. 반대로 마지막 비활성 다이너마이트 블록을 굴착하면 모든 다이너마이트 블록이 사라지면서 퍼즐에서 얻을 수 있는 최대 수확량을 받을 수 있습니다. 그을음 지층은 남지만 `measure()`가 `None`을 반환해 퍼즐을 성공적으로 풀었음을 알려줍니다.

`# 다이너마이트 블록을 굴착해 퍼즐 상태 확인
def dig_dynamite():
    dig()
    if get_ground_type() != Grounds.Soot:
        # 활성 다이너마이트를 굴착함, 퍼즐 실패
        return False
    elif measure() == None:
        # 마지막 불발탄 블록을 굴착함, 퍼즐 해결
        return True
    else:
        # 측정값을 얻음, 퍼즐 진행 중
        return None
`

## 전략
<spoiler=힌트>
아래 코드는 다이너마이트층을 파고 측정값이 `0`인 그을음 블록을 찾습니다. 찾을 때마다 주변 다이너마이트 블록을 모두 파냅니다:
{{codeexample 
{
    "camera_position": {"x": -5, "y": 0, "z": 15},
    "show_image": true,
    "image_size": {"x": 800, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 7, "y": 7},
    "execution_speed": 4,
    "digging_speed": 8,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 6,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz", "petrified_pumpkins"]
}
#SETUP
jump(Unlocks.Dynamite)
for _ in range(3):
    move(East)
    move(North)
#CODE
while get_ground_type() != Grounds.Soot:
    dig()

circle_directions = [
    East, South, West, West, North,
    North, East, East, South, West
]
# 처음 파낸 블록 주변을 돌기
for dir in circle_directions:
    # 그을음의 측정값이 0이면,
    # 주변 다이너마이트는 모두 불발탄
    if get_ground_type() == Grounds.Soot and measure() == 0:
        # 주변 블록을 한 바퀴 더 돌기
        for dir2 in circle_directions:
            move(dir2)
            # 불발 다이너마이트 블록 파기
            while get_ground_type() != Grounds.Soot:
                dig()
    move(dir)
}}
</spoiler>

---

[통계](docs/stats.md)      [지하 감지](docs/unlocks/underground_senses.md)      [딕셔너리](docs/scripting/dicts.md)      [세트](docs/scripting/sets.md)

[move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)      [use_item()](functions/use_item)
