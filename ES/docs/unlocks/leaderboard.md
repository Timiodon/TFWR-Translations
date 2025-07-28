# Leaderboard
Si has llegado hasta aquí, has superado muchos desafíos. ¿Pero los has resuelto eficientemente?
Puedes competir con otros jugadores en varios leaderboards por los métodos de cultivo más eficientes.

Puedes iniciar una carrera de leaderboard llamando a `leaderboard_run(leaderboard, filename, speedup)`.
Esto inicia una [simulación](docs/unlocks/simulation.md) similar a `simulate()` excepto que las condiciones de inicio son fijas. Cada categoría del leaderboard tiene diferentes condiciones de inicio y de éxito.

La carrera del leaderboard tiene éxito si la condición de éxito es `True` cuando termina la simulación. La simulación no terminará automáticamente cuando se alcance el objetivo. Debes asegurarte de que el programa termine.
Si la carrera es exitosa, tu tiempo se añadirá al leaderboard.

Para reducir la varianza, se requiere que todas las carreras duren al menos 2 horas (puedes acelerarlo, para que no tarde tanto). Si una carrera se completa antes, se repetirá hasta alcanzar un tiempo total de 2 horas. El promedio de todas las carreras se sube como tu puntuación.

Aquí tienes una configuración de ejemplo que te pondrá en el leaderboard de heno.
![](LeaderboardSetup400)

## Reinicio Más Rápido
El reinicio más rápido es la categoría más prestigiosa. Automatiza completamente el juego desde una sola parcela de granja hasta desbloquear los leaderboards de nuevo.

No tienes que desbloquear todo, solo intenta desbloquear `Unlocks.Leaderboard` lo más rápido posible.

Recuerda que puedes usar `num_unlocked(unlock) > 0` para comprobar si algo está desbloqueado y puedes usar `get_cost()` en los desbloqueos para ver lo que cuestan y así poder cultivar automáticamente los items correctos.

Llamada a la Función:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Simulación Equivalente:
`unlocks = {}
items = {}
globals = {}
#un valor de semilla negativo significa una semilla aleatoria
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condición de Éxito:
`num_unlocked(Unlocks.Leaderboard) > 0`

## Laberinto
Comienza con todo desbloqueado y consigue `300000` de oro lo más rápido que puedas. Esta es exactamente la cantidad de oro que ganarás resolviendo un laberinto `300` veces.

Llamada a la Función:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Simulación Equivalente:
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condición de Éxito:
`num_items(Items.Gold) >= 300000`

## Dinosaurio
Comienza con todo desbloqueado y consigue `98010` huesos lo más rápido que puedas. Este es exactamente el número de huesos que obtendrás si llenas un área de 10x10 con la cola del dinosaurio.

Llamada a la Función:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Simulación Equivalente:
`unlocks = Unlocks
items = {Items.Pumpkin : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condición de Éxito:
`num_items(Items.Bone) >= 98010`

## Otros Leaderboards de Recursos
Cada planta tiene su propio leaderboard para cultivar esa planta en particular lo más rápido posible. Comienzas con todos los desbloqueos, los recursos que necesitas para cultivar la planta y mucha energía. El objetivo es conseguir `100000` del recurso producido por la planta.

Llamadas a Funciones:
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
`leaderboard_run(Leaderboards.Polyculture, filename, speedup)`

Condición de Éxito:
`num_items(resource) >= 100000`

`Leaderboards.Polyculture` requiere conseguir `100000` de los tres recursos del policultivo.