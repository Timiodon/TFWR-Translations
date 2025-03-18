# Variables
Las variables pueden pensarse como contenedores nombrados que pueden contener un valor. El `=` operador se utiliza para declarar una variable y almacenar un valor en ella.

`variable_name = value`

El lado izquierdo del operador es el nombre de la variable. Puedes darle cualquier nombre que desees. El lado derecho es una expresión cuyo valor resultante se almacenará en la variable.

Declara una variable llamada `a` y almacena el valor `5` en ella: `a = 5`
Declara una variable llamada `b` y almacena el valor de retorno de `can_harvest()` en ella: `b = can_harvest()`

No confundas el operador `=` con el operador `==`. El operador `==` verifica si dos valores son iguales y devuelve `True` o `False`. El operador `=` asigna el valor de la derecha al nombre de la izquierda.

Después de que una variable ha sido asignada, puedes usarla en el código para recuperar el valor que contiene.

`a = 5
for i in range(a):
	do_a_flip()`

El bucle anterior se ejecuta 5 veces porque `a` está establecida en `5`. La `i` en el bucle `for` es también una variable que se asigna automáticamente al valor actual de la secuencia en cada iteración del bucle. (No tiene que llamarse `i`, puedes darle cualquier nombre de variable válido.)

Las variables también te permiten hacer lo mismo con un bucle while:

`a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1`

Esto hace lo mismo que el bucle for anterior. Solo tenemos que incrementar i manualmente. Ten en cuenta que para incrementar i, lo establecemos en su propio valor más `1`. Cambiar el valor de una variable basado en su valor previo es algo muy común. Se puede abreviar usando estos operadores: `+=, -=, *=, /=, %=`

`i = i + 1` es lo mismo que `i += 1` `a = a / 3` es lo mismo que `a /= 3`