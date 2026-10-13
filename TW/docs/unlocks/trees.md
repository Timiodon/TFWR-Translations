[<- 胡蘿蔔](docs/unlocks/carrots.md) <right>[南瓜 ->](docs/unlocks/pumpkins.md)
---
# 樹
[樹](objects/tree)是比灌木取得的木材效率更高。每棵樹能提供 5 份木材。它們和灌木一樣，可以種植在草地或耕過的土地上。

樹喜歡保持一定的空間，相鄰的兩棵樹生長速度會減慢。每在其正北、正東、正西或正南方向地塊上種植一棵樹，都會使其生長時間翻倍。所以如果在每個地塊上都種上樹，它們的生長時間將是原來的 `2*2*2*2 = 16` 倍。

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 10,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
for i in range(get_world_size()):
	for j in range(get_world_size()):
		plant(Entities.Tree)
		move(North)
	move(East)
}}

<spoiler=顯示>此時 `%` 運算子或許可以派上用場。記住，`%` 運算子會回傳除法的餘數。偶數除以 `2` 的餘數是 `0`，奇數除以 `2` 的餘數是 `1`。
所以你可以像這樣檢查一個數是否是偶數：

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": false,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
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
def is_even(n):
	return n % 2 == 0

print("is_even(0): ", is_even(0))
print("is_even(1): ", is_even(1))
print("is_even(2): ", is_even(2))
print("is_even(5): ", is_even(5))
print("is_even(-1): ", is_even(-1))
print("is_even(x): ", is_even(get_pos_x()))
}}
</spoiler>

---

[統計資料](docs/stats.md)      [運算子](docs/scripting/operators.md)      [If 陳述式](docs/scripting/if.md)      [For 迴圈](docs/scripting/for.md)      [混合種植](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)
