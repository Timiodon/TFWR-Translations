# 扩展 1
<unlock=for>另请参见 [Expand_2](docs/unlocks/expand_2.md)

</unlock>你的农场扩大了！如果你不能移动无人机，这个空间就没什么用了，所以有一个新函数`move()`可以移动无人机。`move()`需要你指定希望无人机移动的方向。有四个新的常量可以使用：`North, East, South, West`

例如，`move(North)`会把无人机向北移动一个格子。

如果你移动到农场边缘，无人机会被移动到农场的另一边。以下示例代码将持续把无人机向北移动，并在到达农场边缘时返回起点：

`while True:
	move(North)`