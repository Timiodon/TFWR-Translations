# Medición de Tiempo
Si de verdad quieres optimizar tus métodos, necesitas entender cómo se mide el tiempo en este juego. Este desbloqueo trata sobre eso.

## Nuevas Funciones
Hay dos funciones útiles para medir cuánto tardan las cosas:

`get_time()` devuelve el tiempo en segundos desde el inicio del juego.

`get_tick_count()` devuelve el número de ticks realizados desde el inicio de la ejecución.

Estas dos funciones, así como `quick_print()`, son completamente gratuitas. Incluso la operación de llamada es gratuita para ellas.

## Detalles de Ejecución

### Aviso
Así no es como funciona el rendimiento en el mundo real. Estas son solo reglas creadas para este juego para tener un modelo de tiempo consistente y comprensible.
Probablemente solo te importe esto si quieres hiperoptimizar tu código.


La unidad básica de tiempo para la ejecución de código se llama "tick". Sin mejoras de velocidad y energía, la ejecución procede a una velocidad de `400` ticks por segundo.

En general, las operaciones que combinan dos valores como `+, -, *, /, //, %, and, or, ...` tardan un tick en ejecutarse.
Los operadores unarios `-` y `not` son gratuitos.
Una ramificación `if` también tarda un tick en ejecutarse (además del tiempo que tarda en evaluar la expresión de la condición).
Las llamadas a funciones y las lecturas y escrituras de variables son gratuitas, pero las definiciones de funciones tardan 1 tick.
Las instrucciones `import` son gratuitas.
Acceder a un módulo importado con el operador `.` es gratuito.
Si una función o módulo se ha pasado a través de argumentos o asignaciones de variables, usarlo costará 1 tick en lugar de 0.
Los bucles `for` y `while` tardan un tick en empezar, pero las iteraciones son gratuitas (sin contar el tiempo para evaluar las expresiones de condición/secuencia).
`return`, `break` y `continue` son todos gratuitos.
`pass` tarda un tick, por lo que se puede usar para crear retrasos precisos.
Indexar en una estructura de datos tarda un tick para el operador de índice y, en el caso de un diccionario o conjunto, ticks adicionales dependiendo del tamaño de la clave.

El número de ticks que tardan en ejecutarse las funciones integradas está documentado en la documentación de cada función de forma individual.