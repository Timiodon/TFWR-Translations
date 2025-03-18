# Tiempo
Si realmente quieres optimizar tus métodos, necesitas entender cómo se mide el tiempo en este juego. Este desbloqueo trata de eso.

## Nuevas Funciones
Hay dos funciones útiles para medir cuánto tiempo tardan las cosas:

`get_time()` devuelve el tiempo en segundos desde el inicio del juego.

`get_tick_count()` devuelve el número de ticks realizados desde el comienzo de la ejecución.

Estas dos funciones así como `quick_print()`, son completamente gratis. Incluso la operación de llamada es gratis para ellas.

## Detalles de Ejecución

### Aviso
Esto no es cómo funciona el rendimiento en el mundo real. Estas son solo reglas inventadas para que este juego tenga un modelo de tiempo consistente y comprensible.
Probablemente solo te preocuparás por esto si quieres hiper-optimizar tu código.

La unidad básica de tiempo para la ejecución de código se llama "tick". Sin mejoras de velocidad y energía, la ejecución procede a una tasa de `400` ticks por segundo.

En general, las operaciones que combinan dos valores como `+, -, *, /, //, %, and, or, ...` tardan un tick en ejecutarse.
El valor único `-` y `not` son gratis.
Una rama `if` también toma un tick para ejecutarse (además del tiempo que lleva evaluar la expresión de la condición).
Las llamadas a funciones y las lecturas y escrituras de variables son gratis, pero las definiciones de funciones toman 1 tick.
Las declaraciones `import` son gratis.
Acceder a un módulo importado con el operador `.` es gratis.
Si una función o módulo ha sido pasada mediante argumentos o asignaciones de variables, usarla costará 1 tick en lugar de 0.
Los bucles `for` y `while` toman un tick para comenzar, pero las iteraciones son gratis (sin contar el tiempo para evaluar las expresiones de condición/secuencia).
`return`, `break` y `continue` son gratis.
`pass` toma un tick, por lo que se puede usar para crear demoras precisas.
Indexar en una estructura de datos toma un tick para el operador de índice y, en el caso de un dictionary o set, ticks adicionales dependiendo del tamaño de la clave.

El número de ticks que las funciones builtin tardan en ejecutarse se documenta en la documentación de cada función de manera individual.