[<- 速度升級](docs/unlocks/speed.md) <right>[胡蘿蔔 ->](docs/unlocks/carrots.md)
<right>[偵錯 ->](docs/scripting/debug.md)
<right>[運算子 ->](docs/scripting/operators.md)
---
# 種植
草會自動生長，這很好。所有其他植物都需要呼叫 `plant()` 函式進行種植。你現在唯一能種的植物是灌木。
你可以像這樣把你想種的植物類型傳遞給函式：

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Bush)
}}

這會在無人機下方的地塊上種植 1 叢灌木。

呼叫 `clear()` 函式可以將農場重設為整片草地，並重設無人機回到 (0,0) 的位置。

當農場上同時生長著多種植物時，可能會提高產量。你需要研究混合種植以了解更多資訊。

---

[統計資料](docs/stats.md)      [If 陳述式](docs/scripting/if.md)      [感官](docs/unlocks/senses.md)      [混合種植](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)
