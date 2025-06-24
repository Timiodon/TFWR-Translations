# Mega Granja
Este desbloqueo increíblemente poderoso aumenta significativamente el tamaño de la granja y te da acceso a múltiples drones.

Para facilitar las cosas, siempre recibirás exactamente 36 nuevos cuadros por cada nuevo drone. La proporción de drones a cuadros se mantiene constante.

## Múltiples Drones
Como antes, todavía comienzas con solo un drone. Los drones adicionales deben ser creados primero y desaparecerán después de que el programa termine.
Cada drone ejecuta su propia instancia de programa. Los drones pueden crear nuevos drones usando
`new_drone_id = spawn_drone("filename")`

Esto genera un nuevo drone en la misma posición que el drone que ejecutó el comando `spawn_drone("filename")`. El nuevo drone comenzará a ejecutar el programa en el archivo llamado `filename`, así que reemplaza `"filename"` con el nombre del archivo que deseas ejecutar.

Puedes pensar en esto como si le dijeras a tu drone que vaya al archivo llamado `filename` y haga clic en el botón de ejecutar para el próximo drone.

Los drones no chocan entre sí.

Usa `max_drones()` para obtener el número máximo de drones que se pueden crear.
Usa `num_drones()` para obtener el número de drones que ya están en la granja.
Usa `get_drone_id()` para averiguar qué drone está ejecutando el código.

Ejemplo:

En un archivo llamado `farming routine`:
`if get_drone_id() == 0:
    # Solo el primer drone ejecutará esto
    while num_drones() < max_drones():
        spawn_drone("farming routine")
        move(East)`

while True:
    if can_harvest():
        harvest()
    move(North)`

Esto hará que tu primer drone se mueva horizontalmente y genere más drones. Los drones generados se moverán verticalmente y cosecharán todo en su camino.

<spoiler=show hint>La manera más fácil de usar múltiples drones es dividir tu granja entre ellos. Las mejoras están diseñadas para que cada drone siempre pueda tener un campo de 6x6.
</spoiler>

### Todo lo que está abajo es bastante avanzado y no es necesario para la agricultura básica

## Condiciones de Carrera
Múltiples drones pueden interactuar con el mismo cuadro de la granja al mismo tiempo. Si dos drones interactúan con el mismo cuadro durante el mismo tick exacto, la acción del drone con el ID más bajo ocurrirá primero.

Por ejemplo, imagina que los drones `0` y `1` están ambos sobre el mismo árbol que está casi completamente crecido.
El drone `0` llama a
`use_item(Items.Fertilizer)`
El drone `1` llama a
`harvest()`

Si estas acciones ocurren al mismo tiempo, el árbol será fertilizado primero y luego cosechado. En ese caso, recibirás madera de él. Sin embargo, si el Drone `1` es ligeramente más rápido, el árbol será cosechado antes de ser fertilizado, y no recibirás la madera.
A esto se le llama una "condición de carrera". Es un problema común en la programación paralela, donde el resultado depende del orden en que las operaciones se realizan.

Aquí hay otra situación problemática que puede ocurrir cuando múltiples drones ejecutan el mismo código simultáneamente en la misma posición.
`if get_water() < 0.5:
    use_item(Items.Water)`

Si múltiples drones ejecutan esto simultáneamente, todos ejecutarán la primera línea, lo que los coloca en el bloque `if`. Luego, todos usarán agua, desperdiciando mucha de ella.
Para cuando un drone llegue a la segunda línea, `get_water()` podría ya no ser menor a `0.5` porque otro drone ha regado el cuadro en el ínterin.

## Comunicación entre Drones
Si te interesan estrategias más avanzadas, puede que desees que tus drones se comuniquen entre sí usando funciones de paso de mensajes.

Envía cualquier valor a otro drone:
`send(data, receiver_drone_id)`

Recibe el siguiente valor enviado por cualquier drone:
`data = receive()`

Recibe el siguiente valor enviado por un drone específico:
`data = receive(sender_drone_id)`

El tiempo de ejecución de `send()` depende del tamaño de los datos enviados. Por ejemplo, enviar un gran dictionary requiere ser copiado, lo que puede tomar tiempo.

`receive()` no espera a que llegue un mensaje. Si aún no se ha enviado un mensaje, devolverá `None`.

Puedes construir una función que espere un mensaje así:
`def blocking_receive(sender_drone_id = -1):
    while True:
        data = receive(sender_drone_id)
        if data != None:
            return data`

Una aplicación útil de pasar mensajes es tener una función que genere un drone y le envíe una función para ejecutar.
En un archivo llamado `drone_spawning`:
`def run_on_new_drone(f):
    id = spawn_drone("drone_spawning")
    send(f, id)

if __name__ == "__main__":
    f = blocking_receive()
    f()`

Enviar funciones así puede ser muy lento porque todo el estado capturado de la función, incluidas todas las variables globales, deben ser copiadas.