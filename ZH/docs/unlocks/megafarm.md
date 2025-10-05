# 巨型农场
这个极其强大的解锁项让你能够使用多架无人机。

和以前一样，一开始只有一架无人机。额外的无人机必须先被生成，且程序终止后便会消失。
每架无人机运行的都是自己独立的程序。新无人机可以使用 `spawn_drone(function)` 函数生成。

`def drone_function():
    move(North)
    do_a_flip()

spawn_drone(drone_function)`

以上代码会在运行 `spawn_drone(function)` 命令的无人机所在位置生成一架新的无人机。新无人机随后开始执行指定的函数，完成后便会自动消失。

无人机之间不会相互碰撞。

使用 `max_drones()` 获取可生成的无人机数量上限。
使用 `num_drones()` 获取农场上已有的无人机数量。


## 示例：
`def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)`

这段代码会让你的第一架无人机水平移动，并生成更多的无人机。生成的无人机将垂直移动并收获其路径上的一切资源。

如果生成的无人机数量已达上限，`spawn_drone()` 将什么也不做并返回 `None`。

以下是另一个为每架无人机传递不同方向的示例。
`for dir in [North, East, South, West]:
    def task():
        move(dir)
        do_a_flip()
    spawn_drone(task)`

<spoiler=显示提示>这个并行 `for_all` 函数超级实用，可接受任何函数并在每个农场地块上运行。它会利用所有可用的无人机来做到这一点。

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

for_all(harvest)`

一个特别有用的模式是，如果有可用的无人机就生成一架，没有就自己执行。

`if not spawn_drone(task):
	task()`
</spoiler>

## 等待另一架无人机
使用 `wait_for(drone)` 函数来等待另一架无人机完成。你在生成无人机时会收到 `drone` 句柄。
`wait_for(drone)` 返回另一架无人机正在运行的函数的返回值。

`def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

def zero_arg_wrapper():
    return get_entity_type_in_direction(North)
drone = spawn_drone(zero_arg_wrapper)
print(wait_for(drone))`

请注意，生成无人机需要时间，所以不建议为每件小事都生成一架新的无人机。

你可以用 `has_finished(drone)` 来看看无人机是不是已经完成了，不用等。

## 无共享内存
每架无人机都有自己的内存，不能直接读取或写入另一架无人机的全局变量。

`x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)`

这段代码将打印 `0`，因为新的无人机增加了它自己的全局 `x` 副本的值，但不影响第一架无人机的 `x`。

## 竞态条件
多架无人机可以同时与同一个农场地块交互。如果两架无人机在同一个 tick 内与同一个地块交互，两个交互都会发生，但结果可能会因交互的顺序而异。

例如，想象无人机 `0` 和 `1` 都在同一棵即将完全成熟的树上方。
无人机 `0` 调用
`use_item(Items.Fertilizer)`
无人机 `1` 调用
`harvest()`

如果两个操作同时发生，树将先被施肥再被收获。在这种情况下，你将从中获得木材。但是，如果无人机 `1` 稍微快一点，就会在给树施肥前执行收获，也因此不会得到木材。
这就是所谓的“竞态条件”，属于并行编程中的一个常见问题，结果取决于操作执行的顺序。

多架无人机同时在同一位置运行相同代码时，还有可能发生以下问题。
`if get_water() < 0.5:
    use_item(Items.Water)`

如果多架无人机同时运行这段代码，则会都运行第一行，从而进入 `if` 块，接着又都会使用水，导致浪费大量的水。
当一架无人机执行到第二行时，`get_water()` 可能不再小于 `0.5`，因为另一架无人机在此期间已经给地块浇了水。