[<- 철](docs/unlocks/iron.md)
---
# 보물지도

전설에 따르면 오래전에 죽은 건망증 심한 해적이 찾기 힘든 보물을 숨겼다고 합니다. 뭐, 대충 그런 얘기였던 것 같은데요. 해적이 보물로 가는 길을 지도에 적어 놓고 그 지도를 잃어버린 건 아닐까요? 용암의 강까지 몰렸을 때 지도를 떨어뜨렸고, 그 위에 현무암층이 쌓이면서 보존되었을지도 모르죠. 현무암을 측정하면 뭔가를 더 알아낼 수 있을 겁니다.

<spoiler=자세히 알려주세요>
`Grounds.Basalt`층을 찾아보세요. 현무암을 측정해 무엇을 알려주는지 확인해 보세요. 단서를 따라가면 보물지도를 찾을 수 있을지도 모릅니다. 지도를 측정하면 틀림없이 보물로 가는 길을 알아낼 수 있죠. 지도의 지시를 해독할 수 있는지는 또 다른 문제겠지만요.
</spoiler>

<spoiler=방법만 알려주세요>
알겠어요. `Grounds.Basalt` 지층과 그 바로 아래의 `Grounds.Treasure_Map` 블록을 찾으세요. 현무암에서 `measure()`를 사용하면 아래 지도 블록의 `(x, y)` 위치를 얻을 수 있어요.

지도 블록에서 `measure()`를 호출하면 방향 문자열로 보물로 가는 길을 알아낼 수 있습니다. N, E, S, W는 각각 `North`, `East`, `South`, `West`를, D는 "Down(아래)" 또는 "Dig(굴착)"을 뜻합니다. 이 문자들은 보물로 이어지는 `Grounds.Treasure_Path`블록의 길을 나타내죠.

```
path = measure()
for letter in path:
    do_something(letter)
```

보물지도 블록을 굴착하는 드론이 보물을 찾아야 합니다. 이 드론은 항상 `Grounds.Treasure_Path` 블록 위에 머물러야 합니다. 다른 땅으로 이동하면 길이 끊어지고 보물을 잃습니다.

길 끝에는 `Grounds.Treasure_Goal` 블록이 있습니다. 드론이 길을 벗어나지 않았다면 그 위에 `Entities.Underground_Treasure`가 나타납니다. 드론은 상자를 `harvest()`해 황금을 모을 수 있습니다.

황금의 양은 보물 길의 길이에 비례합니다. 보물지도 해금을 업그레이드하면 보물 길이 더 깊어지고, 확장을 업그레이드하면 좌우로 더 넓게 움직일 수 있습니다. 두 업그레이드 모두 보물 길의 길이와 발견하는 황금의 양을 늘려줍니다.
</spoiler>

---

[통계](docs/stats.md)      [for 루프](docs/scripting/for.md)      [튜플](docs/scripting/tuples.md)      [지하 감지](docs/unlocks/underground_senses.md)

[harvest()](functions/harvest)      [move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)
