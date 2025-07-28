# Bucle While
Has desbloqueado el bucle `while` y los valores `True` y `False`. El bucle `while` sigue ejecutando el cuerpo del bucle mientras la condición sea `True`.

`while condition:
	#cuerpo del bucle`

No te preocupes por crear bucles infinitos. los retardos en la ejecución evitarán que el programa se congele.

## Para Principiantes
Quizás ya has intentado poner varias llamadas a `harvest()` seguidas:

`harvest()
harvest()
harvest()`

Esto te permite cosechar varias veces en una sola ejecución del programa.
Sin embargo, sería bueno cosechar más de tres veces, y escribir el mismo código varias veces es una mala práctica.
La solución es un bucle.
Un bucle te permite ejecutar el mismo código varias veces.

El bucle while toma una condición, que es un valor lógico que solo puede estar en uno de dos estados: `True` o `False`.
Dicho valor se llama valor booleano.

El bucle luego ejecuta el código dentro del bucle hasta que la condición es False.
El bucle while se ve así:

`while condition:
	#cuerpo del bucle
	#cuerpo del bucle
	#...`
	
Donde tienes que reemplazar "condition" con un valor booleano y `#cuerpo del bucle` con lo que quieras hacer en el bucle.

Hay dos valores booleanos constantes disponibles. Las constantes son valores que nunca cambian durante el programa.

Para crear un valor booleano constante que siempre es `True`, puedes simplemente escribir `True`. Escribe `False` como un valor booleano constante que siempre será `False`.
Así que podrías escribir

`while False:
	do_a_flip()`

o

`while True:
	do_a_flip()`

El primero nunca hará una voltereta y el segundo hará volteretas para siempre (un bucle infinito).

Normalmente, crear un bucle infinito es una mala idea porque congelará el programa, pero en este juego hay retardos entre cada iteración del bucle, por lo que hará que el dron siga haciendo una voltereta hasta que lo detengas manualmente presionando nuevamente el botón de ejecutar.

Observa cómo la línea después de los dos puntos está sangrada. La sangría como esta se usa para separar bloques de código.
Simplemente presiona Tab para agregar sangría y Shift + Tab (o Retroceso) para quitarla.

El bucle repetirá todas las sentencias sangradas después de los dos puntos.
Las sentencias después del bloque sangrado se ejecutarán después de que el bucle haya terminado.
