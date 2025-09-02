# Simulación

Las simulaciones te permiten probar código rápidamente sin cambiar el estado de la granja real.
El estado inicial de la simulación se puede elegir libremente, y cuando la simulación termina, la granja real estará en el estado exacto en el que estaba antes de que comenzara la simulación.

La función `simulate()` se utiliza para iniciar una simulación.

el archivo en el que debe comenzar la ejecución
`filename = "f1"`

empezar con todo desbloqueado y completamente mejorado
`sim_unlocks = Unlocks`

empezar con 10000 zanahorias y 50 de heno
`sim_items = {Items.Carrot : 10000, Items.Hay : 50}`

empezar con una variable global "a" con un valor de 13
`sim_globals = {"a" : 13}`

usar una semilla aleatoria fija
`seed = 0`

acelerar la simulación por un factor de 64
`speedup = 64`

ejecutar la simulación
`run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)`

La función `simulate()` devuelve el tiempo, en segundos, que tardó en simular el archivo de inicio dado.

### Nombre de Archivo
El primer argumento de la función `simulate` es el nombre del archivo. Este es el nombre que se muestra en la parte superior de la ventana de código. La simulación ejecutará el archivo especificado como si hubieras hecho clic en el botón Ejecutar.

### Desbloqueos Iniciales
Todas las características de programación como bucles, sentencias if, listas, diccionarios,... siempre permanecerán desbloqueadas. 

El segundo argumento te permite especificar con qué desbloqueos/mejoras debe comenzar la simulación, además de las características de programación. Esto debe ser una secuencia de desbloqueos. La simulación comenzará con todos los desbloqueos en la secuencia mejorados a su nivel máximo.

Si quieres especificar un nivel de mejora distinto al máximo, puedes pasar un diccionario que asigne los desbloqueos a los niveles de desbloqueo. En este caso, los valores negativos corresponden al nivel máximo de desbloqueo.

### Ítems Iniciales
El tercer argumento te permite pasar un diccionario que asigna ítems a números. Especifica los ítems con los que comenzar la simulación.

### Globales Iniciales
Debido a que la simulación inicia una ejecución de programa completamente nueva, no puedes acceder a las variables del programa que inicia la simulación.
Sin embargo, es posible pasar valores a la simulación usando el cuarto argumento. Este es un diccionario que asigna nombres de variables en forma de strings a valores. Estas variables se añaden luego al ámbito global de la ejecución dentro de la simulación.

Ten en cuenta que esto copia todos los valores, por lo que modificarlos dentro de la simulación no afectará a los valores originales fuera de la simulación. No es posible devolver valores de la simulación que no sean el tiempo que tardó en ejecutarse.

### Semilla Aleatoria
El quinto argumento te permite especificar la semilla aleatoria utilizada en la simulación. Debe ser un entero positivo. Los valores negativos harán que se utilice una semilla aleatoria.

La semilla aleatoria afecta a todo, desde los tiempos de crecimiento de las plantas hasta los diseños de los laberintos y los tiempos de evaporación del agua. Si inicias la misma simulación varias veces con la misma semilla aleatoria y las mismas condiciones iniciales, el resultado siempre debería ser el mismo.

### Aceleración
El sexto argumento es la aceleración inicial de la simulación. Esto te permite probar las cosas rápidamente. Si el juego no puede mantener la velocidad establecida, se ralentizará automáticamente.

La aceleración no afecta el resultado de la simulación de ninguna manera. Solo existe para reducir el tiempo de espera.