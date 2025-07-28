# Funciones
Usa la palabra clave `def` para definir una nueva función:
`def f(arg1, arg2 = False):
	#código de la función`

Puedes usar el operador de llamada `()` para llamar a la función:
`f(42)`

Consulta también [Scopes](docs/scripting/scopes.md) para aprender sobre variables locales y globales en funciones.

## Introducción
Ya has visto funciones integradas como `harvest()`.
También puedes definir tus propias funciones, lo que permite estructurar tu código de forma modular. Básicamente, te permite dar un nombre a un bloque de código para que puedas llamarlo desde donde quieras.

## Definiciones de Funciones
Por ejemplo, podrías definir una función que mueva el dron varias veces.

`def move_n_dir(n, dir):
	for i in range(n):
		move(dir)`

La palabra clave `def` indica que se trata de una definición de función.
`move_n_dir` es el nombre al que se asocia la función. Puede ser cualquier nombre de variable válido y se usará para llamar a la función.
`n` y `dir` son parámetros. Son variables que contienen los valores que se pasan a la función (estos valores también se llaman argumentos). Puedes añadir tantos parámetros a una definición de función como quieras.
Después de los `:` viene el bloque de código que se ejecutará cuando se llame a la función.

Con la definición anterior, el siguiente código mueve el dron `10` casillas hacia `North` y `2` casillas hacia `West`.

`move_n_dir(10, North)
move_n_dir(2, West)`

Cuando veas `def function():`, deberías pensar en ello como una asignación de variable como esta:
`function = create_new_function_object()`
Como con todas las asignaciones, ¡no puedes usar la variable antes de que haya sido asignada!
La sentencia `def` tiene que ejecutarse antes de cualquier llamada a la función.
Este código lanzará un error:

`func()
def func():
	pass`

## Valores de Retorno
Usa la palabra clave `return` para hacer que una función devuelva un valor.
Por ejemplo, la siguiente función define la operación "o exclusivo". El "o exclusivo" devuelve `True` si un valor es `True` y el otro es `False`:

`def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()`

Las [Tuplas](docs/scripting/tuples.md) permiten devolver múltiples valores.

## Argumentos por Default
También puedes asignar valores por default que se usarán si no se pasan argumentos.

`def f(a = False):
	if a:
		do_a_flip()

f()

f(True)`

Un argumento que tiene un valor por default no puede ir seguido de un argumento que no lo tenga.

## Uso Avanzado de Funciones
Las funciones son valores como cualquier otro, y la sentencia `def` actúa como una sentencia de asignación, asignando la función al nombre que le des.
Esto permite hacer cosas como esta:

`def f():
	def d():
		do_a_flip()
	return d

f()()`

Aquí `f()` llama a la función `f`, que define y devuelve una nueva función `d`. El segundo `()` ejecuta la función devuelta y realiza una voltereta.
(Hacer este tipo de cosas no suele ser una buena idea porque es difícil ver lo que está pasando)

Las funciones que toman otras funciones como argumentos te permiten ser muy creativo:

`def f(g, arg):
	for _ in range(10):
		g(arg)

f(move, North)
f(use_item, Items.Fertilizer)`

Este código mueve el dron `10` veces hacia `North` y luego usa fertilizante 10 veces.