# 超级农场
这个极其强大的解锁让你能够使用多架无人机。 

和以前一样，你仍然只从一架无人机开始。额外的无人机必须先被生成，并且在程序终止后会消失。
每架无人机运行自己独立的程序。可以使用 `spawn_drone(function)` 函数来生成新的无人机。

`def drone_function():
    move(North)
    do_a_flip()

spawn_drone(drone_function)`

这会在运行 `spawn_drone(function)` 命令的无人机所在位置生成一架新无人机。新的无人机随后开始执行指定的函数。完成后，它将自动消失。

无人机之间不会互相碰撞。 

使用 `max_drones()` 获取可以生成的最大无人机数量。
使用 `num_drones()` 获取农场上已有的无人机数量。


## 示例:
`def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)`

这将使你的第一架无人机水平移动并生成更多无人机。生成的无人机随后将垂直移动并收获其路径上的一切。

如果所有可用的无人机都已生成，`spawn_drone()` 将什么也不做并返回 `None`。

<spoiler=显示提示> 看看这个超级有用的并行 `for_all` 函数，它接受任何函数并在每个农场地块上运行它。它会利用所有可用的无人机来做到这一点。

`def for_all(f):
	def row():
		for _ in range(get_world_size()-1):
			f()
			move(East)
		f()
	for _ in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(North)

forall(harvest)`

一个特别有用的模式是，如果有一架无人机可用就生成它，否则就自己做。

`if not spawn_drone(task):
	task()`
</spoiler>

## 等待另一架无人机
使用 `wait_for(drone)` 函数来等待另一架无人机完成。你在生成无人机时会收到 `drone` handle。
`wait_for(drone)` 返回另一架无人机正在运行的函数的返回值。

`def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

def zero_arg_wrapper():
    return get_entity_type_in_direction(North)
drone = spawn_drone(zero_arg_wrapper)
print(wait_for(drone))`

请注意，生成无人机需要时间，所以为每件小事都生成一架新无人机不是个好主意。

## 无共享内存
每架无人机都有自己的内存，不能直接读取或写入另一架无人机的全局变量。

`x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)`

这将打印 `0`，因为新的无人机递增了它自己的全局 `x` 的副本，这不影响第一架无人机的 `x`。

## Race Conditions
多架无人机可以同时与同一个农场地块互动。如果两架无人机在同一个 tick 内与同一个地块互动，两个互动都会发生，但结果可能会因互动的顺序而异。

例如，想象一下无人机 `0` 和 `1` 都在同一棵快要成熟的树上。
无人机 `0` 调用
`use_item(Items.Fertilizer)`
无人机 `1` 调用
`harvest()`

如果这些动作同时发生，树会先被施肥然后被收获。在这种情况下，你会从中获得木头。然而，如果无人机 `1` 稍快一些，树会在施肥前被收获，你就不会获得木头。
这被称为“race condition”。这是并行编程中的一个常见问题，其结果取决于操作执行的顺序。

这是另一个可能发生的问题情况，当多架无人机在同一位置同时运行相同的代码时。
`if get_water() < 0.5:
    use_item(Items.Water)`

如果多架无人机同时运行这段代码，它们都会运行第一行，这会使它们都进入 `if` 块。然后，它们都会使用水，从而浪费大量的水。
当一架无人机到达第二行时，`get_water()` 可能已经不再小于 `0.5` 了，因为在此期间另一架无人机已经给地块浇了水。