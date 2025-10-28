# Megagranja
Este desbloqueo increíblemente poderoso te da acceso a múltiples drones. 

Como antes, todavía comienzas con un solo dron. Los drones adicionales deben ser generados primero y desaparecerán después de que el programa termine.
Cada dron ejecuta su propio programa por separado. Se pueden generar nuevos drones usando la función `spawn_drone(function)`.

`def drone_function():
    move(North)
    do_a_flip()

spawn_drone(drone_function)`

Esto genera un nuevo dron en la misma posición que el dron que ejecutó el comando `spawn_drone(function)`. El nuevo dron comienza a ejecutar la función especificada. Después de que termina, desaparecerá automáticamente.

Los drones no chocan entre sí. 

Usa `max_drones()` para obtener el número máximo de drones que pueden existir simultáneamente.
Usa `num_drones()` para obtener el número de drones que ya están en la granja.


## Ejemplo:
`def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)`

Esto hará que tu primer dron se mueva horizontalmente y genere más drones. Los drones generados se moverán verticalmente y cosecharán todo a su paso.

Si ya se han generado todos los drones disponibles, `spawn_drone()` no hará nada y devolverá `None`.

Aquí hay otro ejemplo que pasa una dirección diferente a cada dron.
`for dir in [North, East, South, West]:
    def task():
        move(dir)
        do_a_flip()
    spawn_drone(task)`

## Todos los Drones son Iguales
No hay un dron "principal" especial. Todos los drones pueden generar otros drones, y todos cuentan para el límite de drones. Todos los drones desaparecen cuando terminan. Si el primer dron termina su programa antes de tiempo, otro dron se convertirá en aquel cuya ejecución se visualiza con el resaltado de código. Todos los drones pueden activar breakpoints, y cuando un dron activa un breakpoint, el resaltado de código cambia a ese dron.

<spoiler=show hint> Echa un vistazo a esta súper útil función paralela `for_all`, que toma cualquier función y la ejecuta en cada casilla de la granja. Utiliza todos los drones disponibles para hacerlo.

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

Un patrón particularmente útil es generar un dron si hay uno disponible y, de lo contrario, hacerlo tú mismo.

`if not spawn_drone(task):
	task()`
</spoiler>

## Esperar a otro Dron
Usa la función `wait_for(drone)` para esperar a que otro dron termine. Recibes el handle del `drone` cuando lo generas.
`wait_for(drone)` devuelve el valor de retorno de la función que el otro dron estaba ejecutando.

`def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

def zero_arg_wrapper():
    return get_entity_type_in_direction(North)
drone = spawn_drone(zero_arg_wrapper)
print(wait_for(drone))`

Ten en cuenta que generar drones lleva tiempo, así que no es una buena idea generar un nuevo dron para cada pequeña cosa.

Puedes usar `has_finished(drone)` para ver si el dron ya terminó sin tener que esperar.

## Sin Memoria Compartida
Cada dron tiene su propia memoria y no puede leer o escribir directamente las variables globales de otro dron.

`x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)`

Esto imprimirá `0` porque el nuevo dron incrementó su propia copia de la `x` global, lo que no afecta a la `x` del primer dron.

## Condiciones de Carrera
Múltiples drones pueden interactuar con la misma casilla de la granja al mismo tiempo. Si dos drones interactúan con la misma casilla durante el mismo tick, ambas interacciones ocurrirán, pero los resultados pueden diferir según el orden de las interacciones.

Por ejemplo, imagina que los drones `0` y `1` están ambos sobre el mismo árbol que está casi completamente crecido.
El dron `0` llama a
`use_item(Items.Fertilizer)`
El dron `1` llama a
`harvest()`

Si estas acciones ocurren al mismo tiempo, el árbol primero será fertilizado y luego cosechado. En ese caso, recibirás madera de él. Sin embargo, si el dron `1` es ligeramente más rápido, el árbol será cosechado antes de ser fertilizado, y no recibirás la madera.
Esto se llama una "condición de carrera". Es un problema común en la programación paralela, donde el resultado depende del orden en que se realizan las operaciones.

Aquí hay otra situación problemática que puede ocurrir cuando múltiples drones ejecutan el mismo código simultáneamente en la misma posición.
`if get_water() < 0.5:
    use_item(Items.Water)`

Si múltiples drones ejecutan esto simultáneamente, todos ejecutarán la primera línea, lo que los pondrá en el bloque `if`. Luego, todos usarán agua, desperdiciando mucha.
Para cuando un dron llega a la segunda línea, `get_water()` podría ya no ser menor que `0.5` porque otro dron ha regado la casilla mientras tanto.