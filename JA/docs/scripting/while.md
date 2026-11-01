[<- 最初のプログラム](docs/first_program.md) <right>[スピードアップグレード ->](docs/unlocks/speed.md)
---
# Whileループ
`while` ループと `True` と `False` の値をアンロックしました。`while` ループは、条件が `True` である限りループ本体を実行し続けます。

`while condition:
	#ループ本体`

無限ループを作成することを心配しないでください。ドローンが動けなくなることはありますが、ゲーム全体がフリーズすることはありません。実行中のプログラムを停止して、もう一度試せます。

## 初心者向け
すでに行に複数の `harvest()` 呼び出しを並べてみたかもしれません:

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
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
harvest()
harvest()
harvest()
}}
これにより、1回のプログラム実行で複数回収穫できます。
でも、3回より多く収穫したいですよね。同じコードを何度も書くと、すぐにプログラムが読みにくくなってしまいます。
解決策はループです。
ループを使用すると、同じコードを複数回実行できます。

whileループは条件を取ります。これは `True` または `False` の2つの状態のいずれかしか取れない論理値です。
このような値はブール値と呼ばれます。

ループは、条件がFalseになるまでループ内のコードを実行します。
whileループは次のようになります:

`while condition:
	#ループ本体
	#ループ本体
	#...`
	
ここで "condition" をブール値に、`#ループ本体` をループ内で行いたいことに置き換える必要があります。

利用可能な定数のブール値は2つあります。定数はプログラム中に決して変わらない値です。

定数のブール値を作るには、`True` または `False` と書きます。
したがって、次のように書くことができます

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
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while False:
	do_a_flip()
}}
または

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
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	do_a_flip()
}}
最初のものは決してフリップを行わず、2番目のものは永遠にフリップを行います（無限ループ）。

通常、無限ループを作成するのはプログラムがフリーズするため悪い考えですが、このゲームではループの各反復の間に遅延があるため、実行ボタンをもう一度押して手動で停止するまでドローンはフリップを続けます。

コロンの後の行がインデントされていることに注目してください。このようなインデントはコードのブロックを区切るために使用されます。
Tabキーでインデントを追加し、Shift + Tabキー（またはBackspaceキー）で削除できます。複数の行を選択している場合は、そのすべてに適用されます。

注意：Steamでプレイしている場合、Shift + Tabキーを押すとSteamオーバーレイが開きます。ゲームの設定でインデント解除のショートカットを変更するか、Steamオーバーレイの設定でそのショートカットを変更できます。

ここでは、`do_a_flip()` と `pet_the_piggy()` はインデントされた `while` ブロック内にあるため繰り返し呼ばれます。一方、`harvest()` はそのブロックの後にあるため実行されません。
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
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	do_a_flip()
	pet_the_piggy()
harvest()
}}

---

[forループ](docs/scripting/for.md)      [if文](docs/scripting/if.md)      [break](docs/scripting/break.md)      [continue](docs/scripting/continue.md)      [外部エディタ](docs/external_editor.md)
