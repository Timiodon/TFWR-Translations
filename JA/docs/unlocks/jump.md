[<- 石炭](docs/unlocks/coal.md)
---
# ジャンプ
ドローンが`jump()`コマンドをアンロックしました。`Unlocks.Iron`などのアンロックを引数として渡して使います。

このコマンドは、地下に隠れた特定の資源を指定し、すぐにその深さまでジャンプできます。デバッグや、通り過ぎた鉱脈の近くまで飛ばすのに特に便利です。

ジャンプ後は、いちばん上のブロックの表面から3ブロック以内に目的の資源があるはずです。`jump()`を使えるのはプログラムの実行ごとに1回だけで、2回目以降はエラーになります。

次の例は[稲](docs/unlocks/rice.md)までジャンプし、粘土の層を探して稲の段々畑を一列作ります：
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
    "items": [{"item": "hay", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms"],
    "starting_chunk": 0
}
#CODE
# 稲の近くまでジャンプする
jump(Unlocks.Rice)

# 稲の段々畑を一列植える
for i in range(get_world_size()):
    # ジャンプは正確ではないので残りを掘る
    while get_ground_type() != Grounds.Clay:
        dig()

    plant(Entities.Rice)

    move(East)
}}

## 対応するアンロック
`jump()`が使えるのは、次の採掘関連のアンロックだけです：
- 石炭
- 鉄
- 石英
- 稲
- 石化したカボチャ
- 特殊な土壌
- ピラミッド
- 宝物の地図
- キノコ
- ダイナマイト

---

[jump()](functions/jump)
