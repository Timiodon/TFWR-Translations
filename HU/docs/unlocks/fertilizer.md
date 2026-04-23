# Fertilizer
At some point, waiting for the plants to grow is just not efficient enough anymore. 
Similar to water, you will automatically receive 1 fertilizer every 10 seconds, doubling with each upgrade.

Fertilizer can make plants grow instantly. `use_item(Items.Fertilizer)` reduces the remaining growing time of the plant under the drone by 2 seconds.

This has some side effects.
Plants grown with fertilizer will be infected.

When a plant is infected, half of its yield is turned into `Items.Weird_Substance` when it is harvested.
Weird Substance can also be used on plants, which has the effect of toggling the infected status of the plant and all adjacent plants.

So if you call `use_item(Items.Weird_Substance)` on an infected plant it will cure it, but if you use it on a healthy plant it will infect it.

If you use it on an infected plant that has healthy neighbors, it will cure the plant but infect the neighbors and vice versa.