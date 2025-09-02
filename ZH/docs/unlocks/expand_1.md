# 扩张 1
<unlock=for>另请参阅[扩张_2](docs/unlocks/expand_2.md)

</unlock>你的农场变大了！如果你不能移动无人机，这个空间没什么用，所以有一个新的函数 `move()` 可以移动无人机。`move()` 要求你指定无人机要移动的方向。为此有四个新的常量：`North, East, South, West`

例如，`move(North)` 会将无人机向北移动一格。

如果你移出农场边缘，无人机将被移动到农场的另一边。
以下示例代码将使无人机一直向北移动，并在到达农场边缘时绕回到起点：

`while True:
	move(North)`