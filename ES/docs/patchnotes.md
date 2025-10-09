# ¡La versión 1.0 ya está aquí!
Después de más de tres años y medio de desarrollo constante, más de 20 actualizaciones y vuestros increíbles comentarios, el Acceso Anticipado finalmente ha llegado a su fin.

## ¿Qué hay de nuevo en la 1.0?
- Múltiples drones para maximizar tu agricultura
- Un árbol de desbloqueos rediseñado con una progresión más exponencial
- 60 logros para poner a prueba tus habilidades
- Desbloquear ciertos logros le dará a tu dron sombreros especiales
- Una revisión completa del sonido
- Una nueva pista de música
- Mejoras de calidad de vida y varias correcciones
- Cambios importantes: Las mejoras se restablecerán parcialmente. La reutilización de laberintos funciona de manera ligeramente diferente.

Muchas gracias a todos por apoyar The Farmer Was Replaced desde el Acceso Anticipado hasta el lanzamiento completo. 
¡Estoy deseando ver cómo usáis los múltiples drones de formas creativas e ingeniosas!
-Timon

Asegúrate también de unirte a nosotros en Discord: 
[Discord](https://discord.com/invite/kj33cJkeJn)

## Notas del Parche Completas
Cambios Importantes:
-Debido al rediseño del árbol de tecnologías, los números de mejora de las partidas guardadas antiguas ya no serán válidos. El juego restablecerá todas las mejoras a un nivel razonable cuando abras una partida guardada antigua.
-Si estás reutilizando laberintos, ahora tienes que reposicionar primero el tesoro y luego medir la posición, en lugar de medir primero y luego reposicionar.

Jugabilidad:
-Se han añadido tooltips con información útil al pasar el cursor sobre las casillas de la granja.
-Usar `measure()` en cualquier parte del laberinto ahora siempre devuelve la posición del tesoro actual. Ya no tienes que medir el tesoro específicamente.
-Ahora hay una función `can_move()` para el laberinto.
-Las calabazas ahora escalan hasta 6x6 en lugar de 5x5.
-El comportamiento de secado del suelo ha cambiado ligeramente. En lugar de secarse un 1% cada 0.8 a 1.2 segundos, cada casilla de terreno ahora tiene un 10% de probabilidad de secarse cada 0.1 segundos.
-El tiempo de crecimiento de los cactus ahora es siempre exactamente de 1 segundo.
-Las calabazas ahora dejan una calabaza muerta para indicar que han muerto.
-Se ha añadido `pet_the_piggy()`.
-`num_unlocked()` ahora se desbloquea con Senses.

Audio:
-El audio se ha rehecho por completo.
-¡Ahora hay música cuando empiezas el juego!

Visuales:
-Los visuales del árbol de tecnologías han sido completamente rediseñados.
-El panel de inventario en la esquina superior izquierda de la pantalla ahora tiene un bonito efecto visual de recogida de ítems.
-Los cactus ahora son marrones cuando no están correctamente ordenados para hacerlo más visible.
-Las plantas ahora son visibles inmediatamente después de plantarlas, incluso si aún no han crecido.

Editor de Código:
-Hacer doble clic en identificadores con guiones bajos ahora selecciona el identificador completo.
-Si la opción "tabuladores a espacios" está desactivada, los espacios de sangría ahora se convierten en tabuladores.
-El zoom ahora es mucho más suave.
-El autocompletado de código ahora es consciente de las importaciones y puede dar sugerencias de otros archivos.
-Se han añadido diferentes cursores para editar texto y redimensionar ventanas.
-Los pasos del depurador ahora se basan en la línea de código en lugar de en los ticks de simulación.

Otros:
-Ahora puedes encadenar operadores de comparación como en Python.
-`get_cost(Entities.Hedge)` y `get_cost(Entities.Treasure)` ahora devuelven el coste de un laberinto de 1x1.
-Se ha añadido una opción de resolución.
-Se ha añadido una opción para desactivar los resaltados parpadeantes cuando el código se está ejecutando.
-La ejecución del código se ha optimizado aún más, permitiendo que el juego funcione más fluidamente mientras se ejecuta el código.
-Se ha añadido un atajo de teclado para "Activar/Desactivar HUD".

Correcciones:
-Se han corregido algunos de los casos más comunes de resaltados de código que eran visibles a través de otras ventanas.
-Acciones como arar ya no pueden afectar el comportamiento de secado del agua.
-Se han corregido problemas de asignación de teclas en teclados no estadounidenses.
-Se ha corregido que la hucha a veces se alejara mucho de la granja.
-Se ha corregido que el fertilizante no infectara plantas completamente crecidas.
-Se ha corregido que `set_world_size(get_world_size())` restableciera la posición del dron.
-Se ha corregido una interacción de simulación + dinosaurio que causaba que se dejaran muchas manzanas.
-Se ha corregido el error que causaba que los mensajes de error se movieran al hacer clic en minimizar y luego abrir el menú.
-Se ha corregido que los mensajes de error aparecieran mientras aún se está escribiendo.

Cambios Importantes de Parches Anteriores que podrías haberte perdido:
-Las funciones definidas en otros archivos (ventanas en el juego) ya no se importan implícitamente. Ahora tienes que desbloquear y usar sentencias de importación explícitas como en Python (Ver el desbloqueo de importación).
-`Items.Bones` ha sido renombrado a `Items.Bone` para que todos los ítems estén en singular.
-`Entities.Carrots` ha sido renombrado a `Entities.Carrot` para que todas las entidades estén en singular.
-`Grounds.Turf` ha sido renombrado a `Grounds.Grassland` para que sea más fácil de entender.
-`Items.Water_Tank` ha sido renombrado a `Items.Water` porque la función de rellenar el tanque ha sido eliminada.
-`Unlocks.Benchmark` ha sido reemplazado por `Unlocks.Timing`.
-`get_op_count()` ha sido renombrado a `get_tick_count()`.
-`set_farm_size()` ha sido renombrado a `set_world_size()` para ser consistente con `get_world_size()`.
-`get_companion()` ahora devuelve una tupla de la forma (entidad, (x, y)) en lugar de una lista.
-`trade()` ha sido eliminado del juego.