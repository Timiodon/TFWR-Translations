# Depuración
A veces tu código simplemente no funciona y necesitas averiguar por qué. Hay un par de herramientas para ayudarte a hacerlo.

La primera es ejecutar el programa paso a paso. 
Puedes entrar en el modo paso a paso con el botón junto al botón Ejecutar o estableciendo un punto de interrupción.

Los puntos de interrupción se pueden añadir haciendo clic en el panel de puntos de interrupción a la izquierda del código.
![](Breakpoints227)
Cuando la ejecución llega a la línea donde está el punto de interrupción, cambiará automáticamente al modo paso a paso.

Cuando mueves el ratón sobre una variable, se muestra su valor actual.

La función `print()` también puede ser muy útil. Escribirá cualquier valor que se le pase directamente en el aire.

Ejemplos:

Imprime "0.24".
`print(0.24)`

Imprime "True" o "False".
`print(can_harvest())`

Imprime la posición actual.
`print(get_pos_x(), get_pos_y())`

La función `print` imprime el valor directamente en el aire y en la página de [Salida](docs/output.md).

Escribir en el aire a veces puede ser un poco lento si quieres imprimir muchos valores.
En este caso, puedes usar la función `quick_print()`, que imprime solo en la ventana de salida.

La ventana de salida también registra advertencias y errores, por lo que si algo no funciona como se esperaba, puede ser útil revisarla.

Cuando la ejecución se detiene, la salida también se escribe en el archivo output.txt en la carpeta del juego. [output.txt](persistent_data_path/output.txt).