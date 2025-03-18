# Mejora de Velocidad
La velocidad de ejecución se ha duplicado. El problema es que ahora el dron cosecha más rápido de lo que la hierba puede crecer, lo que resulta en ninguna cosecha en absoluto. Para solucionar esto, las ramas [if](docs/scripting/if.md) y la función [can_harvest](functions/can_harvest) ahora están desbloqueadas.

## Comprobando Antes de Cosechar
Hasta ahora solo teníamos `True` y `False` como condiciones, lo cual no es muy útil con `if`.

La nueva función can_harvest() proporciona una mejor condición. `can_harvest()` devuelve `True` si la planta bajo el dron puede ser cosechada y `False` en caso contrario.

`if can_harvest():
	#do something`

La razón por la que puedes usar esta función como una condición de esta manera es porque devuelve un valor booleano.

Un valor de retorno esencialmente significa que después de que se ejecuta la funcionalidad, la expresión de llamada de la función se evalúa al valor devuelto.

Lo que ocurre cuando se ejecuta el código anterior:
	-el if se ejecuta
	-se llama a `can_harvest()`
	-`can_harvest()` hace su trabajo
	-`can_harvest()` devuelve `True` o `False`
	-la declaración ahora es `if True:` o `if False:`
	el bloque de código solo se ejecuta si se puede cosechar

Ahora podemos usar `if` para evitar que el dron coseche demasiado pronto.