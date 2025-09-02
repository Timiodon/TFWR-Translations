# Ámbitos de Nombres
Los ámbitos determinan qué variables se pueden acceder y desde dónde. Un ámbito es básicamente una correspondencia de nombres a valores.
Funcionan básicamente igual que en Python.

Hay un ámbito global, y cada función tiene un ámbito local.
Cuando defines una variable, se añade al ámbito actual.
Cualquier cosa fuera de la definición de una función se considera parte del ámbito global.

`x = 1`
Asigna un valor de `1` al nombre `x` en el ámbito global.

Esta instrucción `def` asigna una función al nombre `f` en el ámbito global.
`def f():
    `Asigna un valor de `1` al nombre `y` en el ámbito local de `f`.`
    y = 1

    `Asigna una función al nombre `g` en el ámbito local de `f`.`
    def g():
        pass`

`f()`
Recupera la función almacenada en `f` del ámbito global y la llama.

`print(y)`
Esta instrucción `print` en el ámbito global lanza un error porque `y` nunca se declaró en el ámbito global, así que no podemos leerlo aquí.
Solo existía en el ámbito local de `f`.

## La palabra clave global
Por defecto, todas las variables en las funciones se vinculan al ámbito local, incluso si existe una variable con el mismo nombre en el ámbito global.

`x = 0

def f():
    x = 1
f()
print(x)`

Este código imprime `0` porque la `x` local dentro de `f` no es la misma variable que la `x` global, por lo que la `x` global permanece sin cambios. Esto es importante porque, de lo contrario, una llamada a función podría sobrescribir accidentalmente una variable global que simplemente tiene el mismo nombre que una variable local de esa función.

Si quieres escribir en una variable global, debes hacerlo explícitamente usando la palabra clave `global`.

`x = 0

def f():
    global x
    x = 1
f()
print(x)`

En este ejemplo, `global x` vincula `x` a la variable global `x` definida encima de ella. Esto ahora imprimirá `1`.
Ten en cuenta que cambiar variables globales suele ser el primer paso hacia el código espagueti, donde cada parte del programa afecta a todas las demás, así que no abuses de ello.

## Bucles y Ramificaciones
Los bucles y las ramificaciones no crean sus propios ámbitos, por lo que cualquier cosa declarada dentro de ellos todavía se puede usar fuera.

`for i in range(3):
    pass
print(i)`

Esto imprimirá `2` porque la última iteración del bucle `for` asignó `2` a `i`.