[<- 철](docs/unlocks/iron.md)
---
# 철 탐사

철 광맥을 찾기가 어려울 때가 있다는 걸 눈치채셨을 겁니다. 운에 맡기고 주변을 파볼 수도 있지만, 더 좋은 방법이 있죠. 철은 자성을 띠므로 멀리서도 찾을 수 있습니다.

바로 `prospect_iron()` 명령으로 가능합니다. `prospect_iron()`은 가장 가까운 철광석으로 한 걸음 다가가기 위해 드론이 이동해야 하는 방위(`North`, `East`, `South`, `West`)를 반환합니다. 명령을 실행하면 석탄 1개를 소모합니다.

드론이 이미 가장 가까운 철광석 바로 위에 있거나, 명령을 실행할 석탄이 부족하거나, 범위 내에 철이 없으면 `prospect_iron()`은 `None`을 반환합니다.

다음 코드를 사용하면 다음 철광석으로 한 걸음 다가갈 수 있습니다.

`if prospect_iron() != None:
    move(prospect_iron())
`

이 코드는 현재 `prospect_iron()`을 두 번 호출해 석탄 2개를 소모하므로 변수를 사용해 최적화하는 것이 좋습니다.

가장 가까운 철광석은 드론이 이동해야 하는 걸음 수로 계산합니다. 드론에서 동쪽으로 2블록, 북쪽으로 3블록 떨어진 곳에 철광석이 있다면, 드론이 그곳까지 다섯 걸음만큼 이동해야 하므로 거리는 5로 계산됩니다.

굴착도 한 걸음으로 계산됩니다. 철이 추가로 지하 7블록 깊이에 묻혀 있다면, 철 위로 이동하는 데 다섯 걸음, 이후 철에 도달하는 데 일곱 번을 굴착해야 하므로 거리는 12죠.

---

[철](docs/unlocks/iron.md)      [지하 감지](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [prospect_iron()](functions/prospect_iron)
