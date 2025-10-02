@warning_not_enough_items_to_trade = 尝试购买 {0}，但没有所需资源。
@warning_no_space_to_plant = 尝试种植 {0}，但地块上已有植物。
@warning_cant_plant_on_ground = 不能在 {1} 上种植 {0}。
@warning_missing_seed = 没有种植 {0} 所需的物品。
@warning_no_item_to_use = 尝试使用 {0} 但数量不足。
@warning_failed_swap_wrap = 尝试跨过农场边界进行交换，但这是不允许的。
@warning_failed_swap_unswappable = 尝试交换 {0}，但这是不可交换的。
@warning_weird_substance_not_divisible = 你使用的奇异物质数量与创建迷宫所需的数量不完全一致。别忘了，所需的奇异物质数量会随着迷宫升级而增加。

若要生成一个全尺寸的迷宫，请执行：
`plant(Entities.Bush)
substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)`
@warning_recursive_simulation = 模拟和排行榜运行不能在其他模拟和排行榜运行中启动。