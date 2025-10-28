# Mega Farm
This incredibly powerful unlock gives you access to multiple drones. 

As before, you still start with just one drone. Additional drones must first be spawned and will disappear after the program terminates.
Each drone runs its own separate program. New drones can be spawned using the `spawn_drone(function)` function.

`def drone_function():
    move(North)
    do_a_flip()

spawn_drone(drone_function)`

This spawns a new drone in the same position as the drone that ran the `spawn_drone(function)` command. The new drone then begins executing the specified function. After it is done, it will disappear automatically.

Drones do not collide with each other. 

Use `max_drones()` to get the maximum number of drones that can exist simultaneously.
Use `num_drones()` to get the number of drones that are already on the farm.


## Example:
`def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)`

This will cause your first drone to move horizontally and spawn more drones. The spawned drones will then move vertically and harvest everything in their path.

If all available drones have already been spawned, `spawn_drone()` will do nothing and return `None`.

Here's another example that passes a different direction to each drone.
`for dir in [North, East, South, West]:
    def task():
        move(dir)
        do_a_flip()
    spawn_drone(task)`

## All Drones Are Equal
There is no special "main" drone. All drones can spawn other drones, and they all count toward the drone limit. All drones disappear when they terminate. If the first drone finishes its program early, another drone will become the one whose execution is visualized with code highlights. All drones can trigger breakpoints, and when a drone triggers a breakpoint, the code highlighting switches to that drone.

<spoiler=show hint> Check out this super useful parallel `for_all` function, which takes any function and runs it on every farm tile. It makes use of all available drones to do so.

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

One particularly useful pattern is to spawn a drone if one is available and otherwise do it yourself.

`if not spawn_drone(task):
	task()`
</spoiler>

## Awaiting Another Drone
Use the `wait_for(drone)` function to wait for another drone to finish. You receive the `drone` handle when you spawn the drone.
`wait_for(drone)` returns the return value of the function that the other drone was running.

`def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

def zero_arg_wrapper():
    return get_entity_type_in_direction(North)
drone = spawn_drone(zero_arg_wrapper)
print(wait_for(drone))`

Note that spawning drones takes time, so it's not a good idea to spawn a new drone for every little thing.

You can use `has_finished(drone)` to check if the drone has finished without waiting for it.

## No Shared Memory
Each drone has its own memory and cannot directly read or write another drone's globals.

`x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)`

This will print `0` because the new drone incremented its own copy of the global `x`, which does not affect the first drone's `x`.

## Race Conditions
Multiple drones can interact with the same farm tile at the same time. If two drones interact with the same tile during the same tick, both interactions will occur, but the results may differ based on the order of the interactions.

For example, imagine that drones `0` and `1` are both over the same tree that is almost fully grown.
Drone `0` calls
`use_item(Items.Fertilizer)`
Drone `1` calls
`harvest()`

If these actions occur at the same time, the tree will first be fertilized and then harvested. In that case, you will receive wood from it. However, if Drone `1` is slightly faster, the tree will be harvested before it is fertilized, and you will not receive the wood.
This is called a "race condition." It is a common issue in parallel programming, where the result depends on the order in which operations are performed.

Here's another problematic situation that can happen when multiple drones run the same code simultaneously at the same position.
`if get_water() < 0.5:
    use_item(Items.Water)`

If multiple drones run this simultaneously, they will all run the first line, which puts them into the `if` block. Then, they will all use water, wasting a lot of it.
By the time a drone reaches the second line, `get_water()` might no longer be less than `0.5` because another drone has watered the tile in the meantime.