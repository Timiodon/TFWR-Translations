# Mega Farm
This incredibly powerful unlock significantly increases the farm size and gives you access to multiple drones. 

To make things easier, you always receive exactly 36 new tiles for each new drone. The ratio of drones to tiles remains constant.

## Multiple Drones
As before, you still start with just one drone. Additional drones must first be spawned and will disappear after the program terminates.
Each drone runs its own separate program instance. Drones can spawn new drones using
`new_drone_id = spawn_drone("filename")`

This spawns a new drone at the same position as the drone that ran the `spawn_drone("filename")` command. The new drone will start executing the program in the file named `filename`, so replace `"filename"` with the name of the file that you want to run.

You can think of this as if you told your drone to go to the file named `filename` and click the execute button for the next drone.

Drones do not collide with each other. 

Use `max_drones()` to get the maximum number of drones that can be spawned.
Use `num_drones()` to get the number of drones that are already on the farm.
Use `get_drone_id()` to find out which drone is running the code.

Example:

In a file named `farming routine`:
`if get_drone_id() == 0:
    # Only the first drone will run this
    while num_drones() < max_drones():
        spawn_drone("farming routine")
        move(East)`

while True:
    if can_harvest():
        harvest()
    move(North)`

This will cause your first drone to move horizontally and spawn more drones. The spawned drones will then move vertically and harvest everything in their path.

<spoiler=show hint>The easiest way to use multiple drones is to divide your farm among them. The upgrades are designed so that each drone can always have a 6x6 field.
</spoiler>

### Everything below here is quite advanced and not required for basic farming

## Race Conditions
Multiple drones can interact with the same farm tile at the same time. If two drones interact with the same tile during the exact same tick, the action of the drone with the lower drone ID will happen first.

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

## Drone Communication
If you're interested in more advanced strategies, you may want your drones to communicate with each other using message-passing functions.

Send any value to another drone:
`send(data, receiver_drone_id)`

Receive the next value sent by any drone:
`data = receive()`

Receive the next value sent by a specific drone:
`data = receive(sender_drone_id)`

The execution time of `send()` depends on the size of the data sent. For example, sending a large dictionary requires copying, which can take a while.

`receive()` doesn't wait for a message to arrive. If no message has been sent yet, it will return `None`.

You can build a function that waits for a message like this:
`def blocking_receive(sender_drone_id = -1):
    while True:
        data = receive(sender_drone_id)
        if data != None:
            return data`

One useful application of passing messages is to have a function that spawns a drone and sends it a function to execute.
In a file named `drone_spawning`:
`def run_on_new_drone(f):
    id = spawn_drone("drone_spawning")
    send(f, id)

if __name__ == "__main__":
    f = blocking_receive()
    f()`

Sending functions like that can be very slow because all of the function's captured state, including all global variables, must be copied.
