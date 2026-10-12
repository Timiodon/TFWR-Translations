[<- 石炭](docs/unlocks/coal.md)
---
# ジャンプ

ドローンが`jump()`コマンドをアンロックしました。

このコマンドを使うと、特定のアンロックを指定して、その場所へ飛び進むことができます。これはデバッグや、さっき見逃した鉱石の鉱脈まで移動するときに特に便利で、`Unlocks.Iron`のようなアンロックを引数として渡すと使うことができます。

`jump()`は`jump(Unlocks.Rice)`や`jump(Unlocks.Iron)`のように、地下に現れるアンロックに対してのみ使えます。

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 3,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms"],
    "starting_chunk": 0
}
#CODE
dig()
dig()
dig()
jump(Unlocks.Iron)
do_a_flip()
}}

ジャンプ先が必ず対象のアンロックの真上になることは保証されていません。そのため、周りを少し見渡す必要があるかもしれません。ただし、対象が近くにあることは保証されています。

`jump()`を使えるのは、プログラムの実行ごとに1回だけです。

---

[jump()](functions/jump)
