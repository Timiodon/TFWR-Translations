# Ámbitos de Nombres
Los ámbitos determinan qué variables pueden ser accedidas desde dónde. Un ámbito es básicamente un mapeo de nombres a valores. Funcionan básicamente igual que en Python.

Hay un ámbito global, y cada función tiene un ámbito local. 
Cuando defines una variable, se añade al ámbito actual. 
Cualquier cosa fuera de una definición de función se considera parte del ámbito global.

`x = 1`
Asigna un valor de `1` al nombre `x` en el ámbito global.

Esta declaración `def` asigna una función al nombre `f` en el ámbito global. 
`def f():
    `Asigna un valor de `1` al nombre `y` en el ámbito local de `f`.`
    y = 1

    `Asigna una función al nombre `g` en el ámbito local de `f`.`
    def g():
        pass`

`f()`
Recupera la función almacenada en `f` desde el ámbito global y la llama.

`print(y)`
Esta declaración de impresión en el ámbito global lanza un error porque `y` nunca fue declarada en el ámbito global, por lo que no podemos leerla aquí. Solo existió en el ámbito local de `f`.

## La palabra clave global
Por defecto, todas las variables en funciones se enlazan al ámbito local, incluso si una variable con el mismo nombre existe en el ámbito global.

`x == 0

def f():
    x = 1
f()
print(x)`

Este código imprime `0` porque el `x` local dentro de `f` no es la misma variable que el `x` global, por lo que el `x` global permanece sin cambios. Esto es importante porque, de lo contrario, una llamada a función podría sobrescribir accidentalmente una variable global que casualmente tiene el mismo nombre que una variable local de esa función.

Si deseas escribir en una variable global, debes hacerlo explícitamente usando la palabra clave `global`.

`x == 0

def f():
    global x
    x = 1
f()
print(x)`

En este ejemplo, `global x` enlaza `x` a la variable global `x` definida anteriormente. Esto ahora imprimirá `1`. Ten en cuenta que cambiar las variables globales suele ser el primer paso hacia un código desordenado, donde todas las partes del programa afectan a todas las demás, así que no lo uses en exceso.

## Bucles y ramas
Los bucles y las ramas no crean sus propios ámbitos, por lo que cualquier cosa declarada dentro de ellos puede seguir siendo utilizada fuera.

`for i in range(3):
    pass
print(i)`

Esto imprimirá `2` porque la última iteración del bucle `for` asignó `2` a `i`.