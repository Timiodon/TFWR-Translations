# Simulación

Las simulaciones te permiten probar rápidamente código sin cambiar el estado de la granja real. El estado inicial de la simulación se puede elegir libremente, y cuando la simulación termina, la granja real estará exactamente en el mismo estado en el que estaba antes de que comenzara la simulación.

La función `simulate()` se usa para iniciar una simulación.

el archivo en el que debería comenzar la ejecución
`filename = "f1"`

comenzar con todo desbloqueado y completamente mejorado
`sim_unlocks = Unlocks`

comenzar con 10000 zanahorias y 50 heno
`sim_items = {Items.Carrot : 10000, Items.Hay : 50}`

comenzar con una variable global "a" con un valor de 13
`sim_globals = {"a" : 13}`

usar una semilla de aleatoriedad fija
`seed = 0`

acelerar la simulación por un factor de 64
`speedup = 64`

correr la simulación
`run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)`

La función `simulate()` devuelve el tiempo, en segundos, que tomó simular el archivo de inicio dado.

### Nombre de Archivo
El primer argumento de la función simulate es el nombre del archivo. Este es el nombre que se muestra en la parte superior de la ventana de código. La simulación ejecutará el archivo especificado como si hubieras clicado el botón Ejecutar en él.

### Desbloqueos Iniciales
Todas las características de programación como bucles, sentencias if, listas, dicts,... siempre permanecerán desbloqueadas.

El segundo argumento te permite especificar con qué desbloqueos/mejoras debería comenzar la simulación además de las características de programación. Esto debería ser una secuencia de desbloqueos. La simulación comenzará con todos los desbloqueos en la secuencia mejorados a su nivel máximo.

Si deseas especificar un nivel de mejora diferente al máximo, puedes pasar un dictionary que asigne los desbloqueos a niveles de desbloqueo. En este caso, los valores negativos corresponden al nivel máximo de desbloqueo.

### Objetos Iniciales
El tercer argumento te permite pasar un dictionary que asigna objetos a números. Especifica los objetos con los que comenzar la simulación.

### Variables Globales Iniciales
Debido a que la simulación inicia una ejecución de programa completamente nueva, no puedes acceder a variables del programa que inicia la simulación. Sin embargo, es posible pasar valores a la simulación usando el cuarto argumento. Este es un dict que asigna nombres de variables en forma de cadenas a valores. Estas variables se añaden al scope global de la ejecución dentro de la simulación.

Ten en cuenta que esto copia todos los valores, por lo que mutarlos dentro de la simulación no afectará a los valores originales fuera de la simulación. No es posible devolver valores de la simulación aparte del tiempo que tomó ejecutarla.

### Semilla Aleatoria
El quinto argumento te permite especificar la semilla de aleatoriedad usada en la simulación. Debe ser un entero positivo. Los valores negativos causarán que se use una semilla aleatoria.

La semilla aleatoria afecta todo, desde los tiempos de crecimiento de las plantas hasta los diseños de laberintos y los tiempos de decadencia del agua. Si comienzas la misma simulación varias veces con la misma semilla aleatoria y las mismas condiciones iniciales, el resultado debería ser siempre el mismo.

### Aceleración
El sexto argumento es la aceleración inicial de la simulación. Esto te permite probar cosas rápidamente. Si el juego no puede mantenerse al ritmo de la velocidad establecida, se ralentizará automáticamente.

La aceleración no afecta el resultado de la simulación de ninguna manera. Existe solo para reducir el tiempo de espera.