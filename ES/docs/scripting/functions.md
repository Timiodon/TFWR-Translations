# Funciones
Usa la palabra clave `def` para definir una nueva función:
`def f(arg1, arg2 = False):
	#código de la función`

Puedes usar el operador de llamada `()` para llamar a la función:
`f(42)`

Consulta también [Scopes](docs/scripting/scopes.md) para aprender sobre variables locales y globales en funciones.

## Introducción
Ya has visto funciones integradas como `harvest()`.
También puedes definir tus propias funciones, lo que permite estructurar tu código de manera modular. Básicamente, te permite darle un nombre a un bloque de código para que puedas llamarlo desde donde quieras.

## Definiciones de Funciones
Por ejemplo, podrías definir una función que mueva el drone varias veces.

`def move_n_dir(n, dir):
	for i in range(n):
		move(dir)`

La palabra clave `def` indica que esto es una definición de función.
`move_n_dir` es el nombre al que se asocia la función. Este puede ser cualquier nombre de variable válido y se usará para llamar a la función.
`n` y `dir` son parámetros. Son variables que contienen los valores que se pasan a la función (Estos valores también se llaman argumentos). Puedes añadir tantos parámetros como desees a la definición de una función.
Después del `:` viene el bloque de código que se ejecutará cuando se llame a la función.

Con la definición anterior, el siguiente código mueve el drone `10` espacios al `North` y `2` espacios al `West`.

`move_n_dir(10, North)
move_n_dir(2, West)`

Cuando ves `def function():` deberías pensar en ello como una asignación de variable, así:
`function = create_new_function_object()`
¡Como con todas las asignaciones, no puedes usar la variable antes de asignarla!
La instrucción `def` debe ejecutarse antes de cualquier llamada a la función.
Este código lanzará un error:

`func()
def func():
	pass`

## Valores de Retorno
Usa la palabra clave `return` para que una función devuelva un valor.
Por ejemplo, la siguiente función define la operación de "or exclusivo". El "or exclusivo" devuelve `True` si un valor es `True` y el otro es `False`:

`def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()`

[Tuples](docs/scripting/tuples.md) permiten retornar múltiples valores.

## Argumentos por Defecto
También puedes asignar valores por defecto que se usarán si no se pasan argumentos.

`def f(a = False):
	if a:
		do_a_flip()

f()

f(True)`

Un argumento que tiene un valor por defecto no puede ser seguido por un argumento que no lo tenga.

## Uso Avanzado de Funciones
Las funciones son valores al igual que cualquier otro valor, y la declaración `def` actúa como una declaración de asignación, asignando la función al nombre que le des.
Esto permite hacer cosas como esta:

`def f():
	def d():
		do_a_flip()
	return d

f()()`

Aquí, `f()` llama a la función `f` que define y retorna una nueva función `d`. Los segundos `()` ejecutan la función retornada y realiza el giro.
(Hacer este tipo de cosas generalmente no es una buena idea porque es difícil ver qué está pasando)

Las funciones que toman otras funciones como argumentos te permiten ser realmente creativo:

`def f(g, arg):
	for _ in range(10):
		g(arg)

f(move, North)
f(use_item, Items.Fertilizer)`

Este código mueve el drone `North` 10 veces y luego usa fertilizante 10 veces.