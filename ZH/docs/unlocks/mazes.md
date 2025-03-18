# 迷宫
`Items.Weird_Substance` 是通过给植物 [施肥](docs/unlocks/fertilizer.md) 获得的，它对灌木丛有奇怪的效果。如果无人机在灌木上方并调用 `use_item(Items.Weird_Substance, amount)` ，灌木会长成一个篱笆迷宫。
迷宫的大小取决于使用的 `Items.Weird_Substance` 的数量（`use_item()` 调用的第二个参数）。
没有迷宫升级时，使用 `n` 个 `Items.Weird_Substance` 会生成 `n`x`n` 的迷宫。每次升级迷宫，你需要多使用一个 `n` 个 `Items.Weird_Substance` 才能达到相同的效果。
所以要制作一个完整的田地迷宫：

`plant(Entities.Bush)
n_substance = get_world_size() * num_unlocked(Unlocks.Mazes)
use_item(Items.Weird_Substance, n_substance)`

出于某种原因，无人机无法飞越篱笆，即便它们看起来并不高。

在篱笆中某处隐藏着宝藏。使用 `harvest()` 在宝藏上可以获得与迷宫面积相等的金币。（例如，一个 5x5 的迷宫会产生 25 个金币。）

如果在其他地方使用 `harvest()`，迷宫将简单地消失。

如果无人机在宝藏上方，`get_entity_type()` 等于 `Entities.Treasure`，在迷宫其他地方则等于 `Entities.Hedge`。

除非你重复使用迷宫（见下述如何重复使用迷宫），迷宫中通常不会有循环。因此，无人机不会再次回到相同的位置，除非掉头。

你可以通过尝试穿过墙壁来检查是否有墙。`move()` 返回 `True` 表示成功，`False` 则表示失败。

如果你不知道如何到达宝藏，可以查看提示 1，它会告诉你如何解决类似的问题。

如果想要额外的挑战，你可以通过在宝藏上再次使用相同数量的 `Items.Weird_Substance` 来重用迷宫。
这将使宝藏中的金币增加一个完整迷宫，并将其移动到迷宫中的随机位置。

在宝藏上使用 `measure()` 会以元组形式返回它将移到的位置。
`next_x, next_y = measure()`

每次宝藏移动时，迷宫中可能会随机移除一堵墙。因此，重复使用的迷宫可以包含循环。

注意，迷宫中的循环会使问题复杂很多，因为这意味着你可以无需回头就到达相同位置。
重复使用迷宫并不能比单纯收割然后生成新迷宫获得更多的金币。
这100%是个额外的挑战，你完全可以跳过。
只有当额外的信息和捷径能帮助你更快解决迷宫时才值得。

同一个迷宫最多可以被解开 300 次。这相当于 299 次重新定位。此后，在宝藏上使用奇怪物质将不再增加金币，`measure()` 将返回 `None`。

<spoiler=show hint 1>这是一种解决问题的一般方法：

创建一个迷宫，想象你就是无人机。

想一下如果你在迷宫中，你会如何寻找宝藏。

逐步写下你的策略，让其他人无需思考便可遵循。

现在尝试将你的步骤转换成代码。
</spoiler>
<spoiler=show hint 2>只要没有循环：所有的墙实际上只是一个大连通墙。如果你沿着墙走，它会引导你穿过整个迷宫。
这种方法需要的代码很少，你不需要记录已经去过的地方。大约十行代码就足够了。</spoiler>
<spoiler=show hint 3>与其将无人机朝东或西等绝对方向移动，不如使用“向右转”或“向左转”等相对方向。这就需要你记录无人机当前移动的方向。无人机实际上从不旋转，但你可以在代码中保持一个“虚拟”旋转。
以下索引技巧对你很有帮助：

`directions = [North, East, South, West]
index = 0`

使用 `% 4` 使其可以“绕圈旋转”，这样在 `West` 之后会返回到 `North`。
`# 向右转
index = (index + 1) % 4`

`# 向左转
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=show hint 4>如果无法解决问题，你可以选择简单快捷但效率低的方法。
解决一个 `1`x`1` 的迷宫是很简单的。</spoiler>