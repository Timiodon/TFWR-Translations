# Bucle While
Has desbloqueado el bucle `while` y los valores `True` y `False`. El bucle `while` sigue ejecutando el cuerpo del bucle mientras la condición sea `True`.

`while condition:
	#loop body`

No te preocupes por crear bucles infinitos. Los retrasos en la ejecución evitarán que el programa se congele.

## Para Principiantes
Tal vez ya has intentado poner varias llamadas de `harvest()` una tras otra:

`harvest()
harvest()
harvest()`

Esto te permite cosechar varias veces en una ejecución del programa.
Sin embargo, sería genial cosechar más de tres veces, y escribir el mismo código varias veces es una mala práctica.
La solución es un bucle.
Un bucle te permite ejecutar el mismo código múltiples veces.

El bucle while toma una condición, que es un valor lógico que solo puede estar en uno de dos estados: `True` o `False`.
Dicho valor se llama valor booleano.

Luego, el bucle ejecuta el código dentro del bucle hasta que la condición sea False.
El bucle while se ve así:

`while condition:
	#loop body
	#loop body
	#...`

Donde debes reemplazar "condition" con un valor booleano y `#loop body` con lo que quieras hacer en el bucle.

Hay dos valores booleanos constantes disponibles. Las constantes son valores que nunca cambian durante el programa.

Para crear un valor booleano constante que siempre sea `True`, simplemente puedes escribir `True`. Escribe `False` como un valor booleano constante que siempre será `False`.
Así que podrías escribir

`while False:
	do_a_flip()`

o

`while True:
	do_a_flip()`

El primero nunca hará un giro y el segundo hará giros para siempre (un bucle infinito).

Normalmente, crear un bucle infinito es una mala idea porque congelará el programa, pero en este juego hay retrasos entre cada iteración del bucle, así que hará que el dron siga haciendo un giro hasta que lo detengas manualmente presionando el botón de ejecución nuevamente.

Fíjate cómo la línea después de los dos puntos está indentada. La indentación como esta se usa para separar bloques de código.
Solo presiona Tab para añadir indentación y Shift + Tab (o Backspace) para quitarla.

El bucle repetirá todas las instrucciones indentadas después de los dos puntos.
Las instrucciones después del bloque indentado se ejecutarán una vez que el bucle haya terminado.