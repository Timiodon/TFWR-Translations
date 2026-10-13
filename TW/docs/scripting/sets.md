[<- 字典](docs/scripting/dicts.md)
---
# 集合
集合就像[字典](docs/scripting/dicts.md)，但是沒有值，僅由一組無序的鍵構成。

它的建立方式類似字典，只是沒有值。
`set = {North, East, West}`

呼叫 `set()` 函式建立一個空集合。注意，`{}` 建立的是一個空字典。

呼叫 `set.add(elem)` 函式向集合新增 1 個新元素。

呼叫 `set.remove(elem)` 函式從集合中刪除 1 個元素。

呼叫 `if elem in set:` 函式判斷集合是否包含某個元素。

呼叫 `for elem in set:` 函式迭代集合中的所有元素。
對於較大的集合，`in` 運算子的執行速度比在串列上快得多。

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
my_set = set()
print(my_set)
my_set.add(1)
my_set.add(North)
print(my_set)
my_set.remove(North)
print(my_set)
if North in my_set:
    print("North 在集合中")
else:
    print("North 不在集合中")
for element in my_set:
    print(element)
}}

集合與字典一樣是無序的，所以無法保證元素迭代的順序。

此外，集合中的元素是唯一的，所以新增一個已存在於集合中的元素不會改變集合。

---

[字典](docs/scripting/dicts.md)      [串列](docs/scripting/lists.md)      [For 迴圈](docs/scripting/for.md)

[len()](functions/len)
