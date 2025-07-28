# Variables
Las variables pueden considerarse como contenedores con nombre que pueden almacenar un valor.
El operador `=` se utiliza para declarar una variable y almacenar un valor en ella.

`nombre_variable = valor`

El lado izquierdo del operador es el nombre de la variable. Puedes darle el nombre que quieras.
El lado derecho es una expresión cuyo valor resultante se almacenará en la variable.

Declara una variable llamada `a` y almacena el valor `5` en ella:
`a = 5`
Declara una variable llamada `b` y almacena el valor de retorno de `can_harvest()` en ella:
`b = can_harvest()`

No confundas el operador `=` con el operador `==`.
El operador `==` comprueba si dos valores son iguales y devuelve `True` o `False`.
El operador `=` asigna el valor de la derecha al nombre de la izquierda.

Después de que una variable ha sido asignada, puedes usarla en el código para recuperar el valor que contiene

`a = 5
for i in range(a):
	do_a_flip()`

El bucle anterior se ejecuta 5 veces porque `a` está establecido en `5`.
La `i` en el bucle `for` también es una variable a la que se le asigna automáticamente el valor actual de la secuencia en cada iteración del bucle. (No tiene que llamarse `i`, puedes darle cualquier nombre de variable válido).

Las variables también te permiten hacer lo mismo con un bucle while:

`a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1`

Esto hace lo mismo que el bucle for de arriba. Solo tenemos que incrementar i manualmente.
Ten en cuenta que para incrementar i, lo establecemos a su propio valor más `1`. Cambiar el valor de una variable basándose en su valor anterior es algo muy común.
Se puede abreviar usando estos operadores: `+=, -=, *=, /=, %=`

`i = i + 1` es lo mismo que `i += 1`
`a = a / 3` es lo mismo que `a /= 3`
