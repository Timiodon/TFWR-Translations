# Mega Granja
Este desbloqueo increíblemente poderoso aumenta significativamente el tamaño de la granja y te da acceso a múltiples drones.

Para facilitar las cosas, siempre recibes exactamente 36 nuevas casillas por cada nuevo dron. La proporción de drones a casillas permanece constante.

## Múltiples Drones
Como antes, todavía comienzas con un solo dron. Los drones adicionales deben ser generados primero y desaparecerán después de que el programa termine.
Cada dron ejecuta su propia instancia de programa separada. Los drones pueden generar nuevos drones usando
`new_drone_id = spawn_drone("filename")`

Esto genera un nuevo dron en la misma posición que el dron que ejecutó el comando `spawn_drone("filename")`. El nuevo dron comenzará a ejecutar el programa en el archivo llamado `filename`, así que reemplaza `"filename"` con el nombre del archivo que quieres ejecutar.

Puedes pensar en esto como si le hubieras dicho a tu dron que fuera al archivo llamado `filename` y presionara el botón de ejecutar para el siguiente dron.

Los drones no chocan entre sí.

Usa `max_drones()` para obtener el número máximo de drones que se pueden generar.
Usa `num_drones()` para obtener el número de drones que ya están en la granja.
Usa `get_drone_id()` para saber qué dron está ejecutando el código.

Ejemplo:

En un archivo llamado `farming routine`:
`if get_drone_id() == 0:
    # Solo el primer dron ejecutará esto
    while num_drones() < max_drones():
        spawn_drone("farming routine")
        move(East)

while True:
    if can_harvest():
        harvest()
    move(North)`

Esto hará que tu primer dron se mueva horizontalmente y genere más drones. Los drones generados se moverán verticalmente y cosecharán todo a su paso.

<spoiler=mostrar pista>
La forma más fácil de usar múltiples drones es dividir tu granja entre ellos. Las mejoras están diseñadas para que cada dron siempre pueda tener un campo de 6x6.
</spoiler>

Todo lo que sigue es bastante avanzado y no es necesario para la agricultura básica.

## Race Conditions
Múltiples drones pueden interactuar con la misma casilla de la granja al mismo tiempo. Si dos drones interactúan con la misma casilla durante el mismo tick exacto, la acción del dron con el ID de dron más bajo ocurrirá primero.

Por ejemplo, imagina que los drones `0` y `1` están ambos sobre el mismo árbol que está casi completamente crecido.
El dron `0` llama a
`use_item(Items.Fertilizer)`
El dron `1` llama a
`harvest()`

Si estas acciones ocurren al mismo tiempo, el árbol primero será fertilizado y luego cosechado. En ese caso, recibirás madera de él. Sin embargo, si el Dron `1` es ligeramente más rápido, el árbol será cosechado antes de ser fertilizado, y no recibirás la madera.
Esto se llama una "race condition". Es un problema común en la programación paralela, donde el resultado depende del orden en que se realizan las operaciones.

Aquí hay otra situación problemática que puede ocurrir cuando múltiples drones ejecutan el mismo código simultáneamente en la misma posición.
`if get_water() < 0.5:
    use_item(Items.Water)`

Si varios drones ejecutan esto simultáneamente, todos ejecutarán la primera línea, lo que los pondrá en el bloque `if`. Luego, todos usarán agua, desperdiciando mucha.
Para cuando un dron llega a la segunda línea, `get_water()` podría ya no ser menor que `0.5` porque otro dron ha regado la casilla mientras tanto.

## Comunicación entre Drones
Si estás interesado en estrategias más avanzadas, es posible que quieras que tus drones se comuniquen entre sí usando funciones de paso de mensajes.

Envía cualquier valor a otro dron:
`send(data, receiver_drone_id)`

Recibe el siguiente valor enviado por cualquier dron:
`data = receive()`

Recibe el siguiente valor enviado por un dron específico:
`data = receive(sender_drone_id)`

El tiempo de ejecución de `send()` depende del tamaño de los datos enviados. Por ejemplo, enviar un dictionary grande requiere copiar, lo que puede llevar un tiempo.

`receive()` no espera a que llegue un mensaje. Si aún no se ha enviado ningún mensaje, devolverá `None`.

Puedes construir una función que espere un mensaje así:
`def blocking_receive(sender_drone_id = -1):
    while True:
        data = receive(sender_drone_id)
        if data != None:
            return data`

Una aplicación útil del paso de mensajes es tener una función que genere un dron y le envíe una función para ejecutar.
En un archivo llamado `drone_spawning`:
`def run_on_new_drone(f):
    id = spawn_drone("drone_spawning")
    send(f, id)

if __name__ == "__main__":
    f = blocking_receive()
    f()`

Enviar funciones de esa manera puede ser muy lento porque todo el estado capturado de la función, incluidas todas las variables globales, debe copiarse.
