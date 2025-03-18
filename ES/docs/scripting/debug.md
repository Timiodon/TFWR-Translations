# Depuración
A veces tu código simplemente no funciona y necesitas averiguar por qué. Hay un par de herramientas que pueden ayudarte a hacer eso.

La primera es ejecutar el programa paso a paso. 
Puedes entrar al modo paso a paso con el botón al lado del botón de Ejecutar o configurando un breakpoint.

Se pueden añadir breakpoints haciendo clic en el panel de breakpoints a la izquierda del código.
![](Breakpoints227)
Cuando la ejecución llega a la línea donde está el breakpoint, automáticamente cambiará al modo paso a paso.

Cuando pasas el ratón sobre una variable, se muestra su valor actual.

La función `print()` también puede ser muy útil. Escribirá cualquier valor que le pases directamente en el aire.

Ejemplos:

Imprimir "0.24".
`print(0.24)`

Imprimir "True" o "False".
`print(can_harvest())`

Imprimir la posición actual.
`print(get_pos_x(), get_pos_y())`

La función print imprime el valor directamente en el aire y en la página de [Salida](docs/output.md).

Escribir en el aire a veces puede ser un poco lento si quieres imprimir muchos valores.
En este caso puedes usar la función `quick_print()` que imprime solo en la ventana de salida.

La ventana de salida también registra advertencias y errores, por lo que si algo no funciona como se espera, puede ser útil revisar eso.

Cuando la ejecución se detiene, la salida también se escribe en el archivo output.txt en la carpeta del juego. [output.txt](persistent_data_path/output.txt).