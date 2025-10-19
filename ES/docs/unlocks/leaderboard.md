# Tabla de clasificación
Si has llegado hasta aquí, has superado muchos desafíos. Pero, ¿los has resuelto de manera eficiente? 
Puedes competir con otros jugadores en varias tablas de clasificación por los métodos de cultivo más eficientes.

Puedes iniciar una carrera en la tabla de clasificación llamando a `leaderboard_run(leaderboard, filename, speedup)`.
Esto inicia una [simulación](docs/unlocks/simulation.md) similar a `simulate()`, excepto que las condiciones iniciales son fijas. Cada categoría de la tabla de clasificación tiene diferentes condiciones de inicio y éxito.

La carrera de la tabla de clasificación tiene éxito si la condición de éxito es `True` cuando la simulación termina. 

La simulación NO terminará automáticamente cuando se alcance el objetivo. Debes asegurarte de que el programa termine.
Si la carrera es exitosa, tu tiempo se añadirá a la tabla de clasificación.

Para reducir la varianza, todas las carreras deben durar al menos 2 horas (puedes acelerarlo, para que no tarde tanto). Si una carrera se completa antes, se repetirá hasta alcanzar un tiempo total de 2 horas. El promedio de todas las carreras se sube como tu puntuación.

Aquí hay un ejemplo de configuración que te pondrá en la tabla de clasificación del heno.
![](LeaderboardSetup400)

## Reinicio más rápido
El reinicio más rápido es la categoría más prestigiosa. Automatiza completamente el juego desde una sola parcela de granja hasta desbloquear de nuevo las tablas de clasificación.

No tienes que desbloquear todo, solo intenta desbloquear `Unlocks.Leaderboard` lo más rápido posible.

Recuerda que puedes usar `num_unlocked(unlock) > 0` para comprobar si algo está desbloqueado y puedes usar `get_cost()` en los desbloqueos para ver cuánto cuestan y así poder cultivar automáticamente los ítems correctos.

Llamada de función:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Simulación equivalente:
`unlocks = {}
items = {}
globals = {}
#un valor de semilla negativo significa una semilla aleatoria
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condición de éxito:
`num_unlocked(Unlocks.Leaderboard) > 0`

## Laberinto
Comienza con todo desbloqueado y consigue `9863168` de oro lo más rápido que puedas. Esta es exactamente la cantidad de oro que ganarás al reutilizar un laberinto de 32x32 `300` veces.

Llamada de función:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Simulación equivalente:
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condición de éxito:
`num_items(Items.Gold) >= 9863168`

## Dinosaurio
Comienza con todo desbloqueado y consigue `33488928` huesos lo más rápido que puedas. Este es exactamente el número de huesos que obtendrás si llenas un área de 32x32 con la cola del dinosaurio.

Llamada de función:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Simulación equivalente:
`unlocks = Unlocks
items = {Items.Cactus : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condición de éxito:
`num_items(Items.Bone) >= 33488928`

## Otras tablas de clasificación de recursos
Cada planta tiene su propia tabla de clasificación para cultivar esa planta en particular lo más rápido posible. Comienzas con todos los desbloqueos, los recursos que necesitas para cultivar la planta y mucha energía. El objetivo es conseguir una cantidad determinada del recurso producido por la planta.

Como siempre, necesitas asegurarte de que tu programa termine cuando alcances el objetivo. Una carrera no se considera finalizada hasta que el programa termina, incluso si se ha alcanzado el objetivo.

### `Leaderboards.Cactus`
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
Condición de éxito: `num_items(Items.Cactus) >= 33554432`

### `Leaderboards.Sunflowers`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
Condición de éxito: `num_items(Items.Power) >= 100000`

### `Leaderboards.Pumpkins`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
Condición de éxito: `num_items(Items.Pumpkin) >= 200000000`

### `Leaderboards.Wood`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
Condición de éxito: `num_items(Items.Wood) >= 10000000000`

### `Leaderboards.Carrots`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
Condición de éxito: `num_items(Items.Carrot) >= 2000000000`

### `Leaderboards.Hay`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
Condición de éxito: `num_items(Items.Hay) >= 2000000000`

## Tablas de clasificación de un solo dron
También hay tablas de clasificación para cultivar con un solo dron. Solo tienes un dron y una granja de 8x8 y tienes que conseguir una cierta cantidad de recursos lo más rápido posible.

### `Leaderboards.Maze_Single`
`leaderboard_run(Leaderboards.Maze_Single, filename, speedup)`
Condición de éxito: `num_items(Items.Gold) >= 616448`

### `Leaderboards.Cactus_Single`
`leaderboard_run(Leaderboards.Cactus_Single, filename, speedup)`
Condición de éxito: `num_items(Items.Cactus) >= 131072`

### `Leaderboards.Sunflowers_Single`
`leaderboard_run(Leaderboards.Sunflowers_Single, filename, speedup)`
Condición de éxito: `num_items(Items.Power) >= 10000`

### `Leaderboards.Pumpkins_Single`
`leaderboard_run(Leaderboards.Pumpkins_Single, filename, speedup)`
Condición de éxito: `num_items(Items.Pumpkin) >= 10000000`

### `Leaderboards.Wood_Single`
`leaderboard_run(Leaderboards.Wood_Single, filename, speedup)`
Condición de éxito: `num_items(Items.Wood) >= 500000000`

### `Leaderboards.Carrots_Single`
`leaderboard_run(Leaderboards.Carrots_Single, filename, speedup)`
Condición de éxito: `num_items(Items.Carrot) >= 100000000`

### `Leaderboards.Hay_Single`
`leaderboard_run(Leaderboards.Hay_Single, filename, speedup)`
Condición de éxito: `num_items(Items.Hay) >= 100000000`