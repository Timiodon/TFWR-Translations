# Mega Farm
这个强大的解锁功能显著增加了农场的规模，并让你能够使用多个drone。

为了让事情更简单，你每获得一个新的drone都会收到准确36块新的地砖。drone与地砖的比例保持不变。

## 多个Drones
和之前一样，你仍然只从一个drone开始。额外的drones必须首先被生成，并且会在程序终止后消失。
每个drone运行它自己的独立程序实例。drones可以使用
`new_drone_id = spawn_drone("filename")`来生成新drone。

这将在运行`spawn_drone("filename")`命令的drone同一位置生成一个新drone。新drone将开始执行名为`filename`的文件中的程序，所以将`"filename"`替换为你想要运行的文件名。

你可以把这想象成你告诉你的drone去文件名为`filename`的地方点击下一个drone的执行按钮。

drones不会彼此碰撞。

使用`max_drones()`来获取可以生成的最大drone数量。
使用`num_drones()`来获取农场上已经有的drone数量。
使用`get_drone_id()`来找出哪个drone正在运行代码。

例子：

在名为`farming routine`的文件中：
`if get_drone_id() == 0:
    # 只有第一个drone会运行这段代码
    while num_drones() < max_drones():
        spawn_drone("farming routine")
        move(East)`

while True:
    if can_harvest():
        harvest()
    move(North)`

这将使你的第一个drone水平移动并生成更多drones。生成的drones将垂直移动并收割路径上的所有作物。

<spoiler=show hint>使用多个drones的最简单方法是将你的农场划分给它们。升级设计成每个drone总是可以有一个6x6的田地。</spoiler>

### 以下内容较为高级且不是基本种植所需

## 竞争条件
多个drones可以同时与同一地砖互动。如果两个drones在完全相同的tick时间与同一地砖互动，drone ID较小的drone的动作会先发生。

例如，假设drones `0` 和 `1` 都在几乎成熟的树上。
drone `0` 调用
`use_item(Items.Fertilizer)`
drone `1` 调用
`harvest()`

如果这些动作同时发生，树会先被施肥然后被收割。在这种情况下，你会得到木材。然而，如果drone `1` 稍微快一点，树会在施肥前被收割，你将得不到木材。
这就叫做“竞争条件”。这是并行编程中的常见问题，结果依赖于操作的执行顺序。

这是另一个问题：多个drones在同一个位置同时运行相同代码。
`if get_water() < 0.5:
    use_item(Items.Water)`

如果多个drones同时运行，这些drones都会进入`if`块，然后都使用水，从而造成浪费。
当一个drone到达第二行时，由于另一个drone已经给地砖浇水，`get_water()`可能不再小于`0.5`。

## Drone 通信
如果你对更高级的策略感兴趣，你可能希望让你的drones使用消息传递函数进行沟通。

发送任何值给其他drone：
`send(data, receiver_drone_id)`

接收任何drone发送的下一个值：
`data = receive()`

接收特定drone发送的下一个值：
`data = receive(sender_drone_id)`

`send()`的执行时间取决于发送数据的大小。比如，发送一个大的dictionary需要复制，可能需要一会儿。

`receive()`不会等待消息到达。如果尚未发送消息，它将返回`None`。

你可以构建一个等待消息的函数：
`def blocking_receive(sender_drone_id = -1):
    while True:
        data = receive(sender_drone_id)
        if data != None:
            return data`

一个传递消息的有用应用是一个生成drone并发送它一个函数去执行的函数。
在名为`drone_spawning`的文件中：
`def run_on_new_drone(f):
    id = spawn_drone("drone_spawning")
    send(f, id)

if __name__ == "__main__":
    f = blocking_receive()
    f()`

以这种方式发送函数可能非常慢，因为函数的所有捕获状态，包括所有全局变量，必须被复制。