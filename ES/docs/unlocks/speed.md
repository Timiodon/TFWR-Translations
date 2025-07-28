# Mejora de Velocidad
La velocidad de ejecución se ha duplicado. El problema es que el dron ahora cosecha más rápido de lo que la hierba puede crecer, lo que resulta en que no se cosecha nada en absoluto. Para lidiar con esto, ahora están desbloqueadas las ramas [if](docs/scripting/if.md) y la función [can_harvest](functions/can_harvest).

## Comprobar Antes de Cosechar
Hasta ahora solo teníamos `True` y `False` como condiciones, lo que por supuesto no es muy útil con `if`.

La nueva función can_harvest() proporciona una mejor condición. `can_harvest()` devuelve `True` si la planta debajo del dron se puede cosechar y `False` en caso contrario.

`if can_harvest():
	#hacer algo`

La razón por la que puedes usar esta función como condición de esta manera es porque devuelve un valor booleano.

Un valor de retorno esencialmente significa que después de que se ejecuta la funcionalidad, la expresión de llamada a la función se evalúa al valor devuelto.

Qué sucede cuando se ejecuta el código anterior:
	-el if se ejecuta
	-se llama a `can_harvest()`
	-`can_harvest()` hace lo suyo
	-`can_harvest()` devuelve `True` o `False`
	-la sentencia ahora es `if True:` o `if False:`
	-el bloque de código solo se ejecuta si se puede cosechar

Ahora podemos usar `if` para evitar que el dron coseche demasiado pronto.