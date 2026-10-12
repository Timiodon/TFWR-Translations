[<- 확장 1](docs/unlocks/expand_1.md) <right>[지하 감지 ->](docs/unlocks/underground_senses.md)
<right>[벼 ->](docs/unlocks/rice.md)
<right>[석탄 ->](docs/unlocks/coal.md)
---
# 채광

드론이 원시적인 드릴을 사용할 수 있게 되어 지하의 보물을 찾을 수 있습니다.

`dig()` 명령으로 드론 아래의 블록을 굴착할 수 있습니다.

우선 블록을 몇 개 모아 볼까요?

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "special_soils"]
}
#SETUP
move(North)
move(East)
#CODE
dig()
do_a_flip()
dig()
do_a_flip()
dig()
do_a_flip()
clear()
}}

지표로 돌아가고 싶다면 언제든 `clear()`를 사용하세요. 이렇게 하면 농장도 복원됩니다.

블록 위에 마우스를 올리면 이름, 안정성, 경도가 표시됩니다.

# 드릴

더 깊이 내려갈수록 블록이 더 단단해져 굴착에 더 오랜 시간이 걸립니다. 다행히 드릴을 업그레이드해 이 문제를 줄일 수 있죠!

`get_hardness()`로 아래 블록의 경도를 확인할 수 있습니다. 유난히 단단한 블록들을 만난다면 빙 돌아가는 것이 더 빠르게 전진하는 방법일지도 모릅니다.

`while True:
        if get_hardness() < 5:
                dig()
        else:
                move(East)`

물론 아래로 내려갈수록 블록은 점점 더 단단해지기 때문에, 이 전략이 도움은 되지만 한계가 있습니다.

## 붕괴

아래로 굴착하면 주변 블록이 붕괴합니다. 드론 옆의 블록 네 개는 항상 파괴됩니다. 그다음부터는 땅의 안정성에 따라 확산합니다. 풀밭처럼 안정성이 1인 블록은 높이 차이가 1블록까지 나더라도 버틸 수 있습니다. 즉, 풀밭의 상하좌우에 z 좌표가 2블록 이상 더 깊은 곳에 있는 블록이 있다면 풀밭은 파괴됩니다.

블록의 안정성은 마우스를 올렸을 때 나타나는 툴팁에서 확인할 수 있습니다.

블록이 붕괴하면 그 위의 모든 블록도 사라집니다. 드론이 직접 굴착한 블록에서만 자원을 얻으므로, 붕괴로 파괴된 블록에서는 자원을 얻지 못합니다.

---

[지하 감지](docs/unlocks/underground_senses.md)      [while 루프](docs/scripting/while.md)

[move()](functions/move)      [dig()](functions/dig)
