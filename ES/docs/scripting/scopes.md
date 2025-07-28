# Scopes de Nombres
Los scopes determinan qué variables se pueden acceder y desde dónde. Un scope es básicamente un mapeo de nombres a valores.
Funcionan básicamente igual que en Python.

Hay un scope global, y cada función tiene un scope local.
Cuando defines una variable, se añade al scope actual.
Cualquier cosa fuera de una definición de función se considera parte del scope global.

`x = 1`
Asigna un valor de `1` al nombre `x` en el scope global.

Esta sentencia `def` asigna una función al nombre `f` en el scope global.
`def f():
    `Asigna un valor de `1` al nombre `y` en el scope local de `f`.`
    y = 1

    `Asigna una función al nombre `g` en el scope local de `f`.`
    def g():
        pass`

`f()`
Recupera la función guardada en `f` del scope global y la llama.

`print(y)`
Esta sentencia print en el scope global lanza un error porque `y` nunca fue declarada en el scope global, así que no podemos leerla aquí.
Solo existía en el scope local de `f`.

## La palabra clave global
Por default, todas las variables en las funciones se vinculan al scope local, incluso si existe una variable con el mismo nombre en el scope global.

`x = 0

def f():
    x = 1
f()
print(x)`

Este código imprime `0` porque la `x` local dentro de `f` no es la misma variable que la `x` global, por lo que la `x` global no cambia. Esto es importante porque, de lo contrario, una llamada a función podría sobrescribir accidentalmente una variable global que casualmente tiene el mismo nombre que una variable local de esa función.

Si quieres escribir en una variable global, debes hacerlo explícitamente usando la palabra clave `global`.

`x = 0

def f():
    global x
    x = 1
f()
print(x)`

En este ejemplo, `global x` vincula `x` a la variable global `x` definida arriba. Esto ahora imprimirá `1`.
Ten en cuenta que cambiar variables globales suele ser el primer paso hacia el "código espagueti", donde cada parte del programa afecta a todas las demás, así que no abuses de ello.

## Bucles y condicionales
Los bucles y los condicionales no crean sus propios scopes, así que cualquier cosa declarada dentro de ellos se puede seguir usando fuera.

`for i in range(3):
    pass
print(i)`

Esto imprimirá `2` porque la última iteración del bucle `for` asignó `2` a `i`.