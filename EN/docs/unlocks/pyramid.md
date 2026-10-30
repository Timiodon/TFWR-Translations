[<- Bamboo](docs/unlocks/bamboo.md)
---
# Pyramids

The underground now contains ancient pyramidal structures from which you can harvest energy!

Pyramids are made from sand blocks (`Grounds.Sand`). Below the pyramid itself is a foundation layer of limestone (`Grounds.Limestone`). Because they are old and eroded, you will find them only in a partially destroyed state. The foundation layer is always present, but there will be holes in the sand. Here's how a pyramid looks when you dig it up:

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

The blocks above the pyramid are always dirt. If you want to dig up a pyramid more efficiently than the above code, you can use that fact.

As you can see, there are several holes in the sand which will need to be filled. When you fill these holes and restore the pyramid to its previous state, it destroys itself and you receive power as a reward.

You can restore a pyramid by placing blocks with the command `place(Grounds.Sand)`. Sand is a special block that will cave in immediately when it is not supported properly. Whenever you place a sand block, it must either be placed directly on limestone, or on a 3x3 of sand blocks. Here's a small hand-built pyramid to demonstrate. Of course, building it yourself won't give you any power:

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

A correctly restored pyramid consists of a square limestone foundation with odd-numbered side lengths, for example 5x5. Above it is a layer of sand blocks of the same size (5x5), followed by progressively smaller layers: 3x3, then 1x1.

When a pyramid is completed, it crumbles away and a large sunflower is spawned in the middle. You can harvest it to receive power. The larger the pyramid you completed, the more power you receive.

---

[Stats](docs/stats.md)      [Underground Senses](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [use_item()](functions/use_item)      [place()](functions/place)
