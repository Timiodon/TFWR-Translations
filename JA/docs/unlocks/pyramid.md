[<- 竹](docs/unlocks/bamboo.md)
---
# ピラミッド

地下に古代のピラミッド型の建造物が現れました。ここからエネルギーを収穫できます！

ピラミッドは砂のブロック（`Grounds.Sand`）でできています。その下には石灰岩（`Grounds.Limestone`）の土台の層があります。古くなって風化しているため、見つかるのは一部が崩れた状態です。土台の層は必ず残っていますが、砂には穴があります。掘り出したピラミッドはこのように見えます：

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
    "items": [{"item": "hay", "n": 100}, {"item": "block", "n": 100}],
    "world_size": {"x": 6, "y": 6},
    "execution_speed": 32,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 7,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "dynamite", "quartz"]
}
#SETUP
jump(Unlocks.Pyramid)
move(North)
#CODE
while get_ground_type() != Grounds.Limestone:
    dig()
do_a_flip()
z = get_pos_z()
for i in range(6):
    for j in range(6):
        while (get_ground_type() != Grounds.Limestone
                and get_ground_type() != Grounds.Sand
                and get_pos_z() > z):
            dig()
        move(North)
    move(East)
}}

ピラミッドの上にあるブロックは必ず土です。上のコードより効率よく掘り出すなら、この性質を利用できます。

見てのとおり、砂には埋める必要のある穴がいくつかあります。穴を埋めてピラミッドを元の形に修復すると、ピラミッドは崩壊し、報酬としてパワーを得られます。

`place(Grounds.Sand)`コマンドでブロックを配置すると、ピラミッドを修復できます。砂は特殊なブロックで、適切に支えられていないとすぐに落盤します。砂のブロックを置くときは、石灰岩の真上か、3x3の砂のブロックの上に配置する必要があります。次の小さな手作りピラミッドを見てください。もちろん、自分で建ててもパワーはもらえません：

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
    "items": [{"item": "hay", "n": 100}, {"item": "block", "n": 100}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 4,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz"]
}
#CODE
for i in range(3):
    for j in range(3):
        place(Grounds.Limestone)
        move(North)
    move(East)
    
for i in range(3):
    for j in range(3):
        place(Grounds.Sand)
        move(North)
    move(East)
    
move(North)
move(East)
place(Grounds.Sand)
}}

正しく修復されたピラミッドは、一辺が奇数の正方形の石灰岩の土台（たとえば5x5）で構成されます。その上には同じサイズの砂のブロックの層（5x5）があり、さらに上に向かって3x3、1x1と小さくなる層が続きます。

ピラミッドが完成すると崩れ落ち、中央に大きなヒマワリが生成されます。これを収穫するとパワーを得られます。完成させたピラミッドが大きいほど、得られるパワーも増えます。

---

[統計](docs/stats.md)      [地下の感覚](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [use_item()](functions/use_item)      [place()](functions/place)
