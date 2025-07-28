# Import
Poner todo tu código en un solo archivo se vuelve inmanejable rápidamente.
Las sentencias `import` te permiten importar funciones y variables globales de otro archivo.

`import filename`

Esta es la forma más simple de la sentencia import. Te dará acceso a todo lo definido en el archivo llamado `filename`. Cada ventana en el juego es un archivo, y el nombre del archivo es el que se muestra en la parte superior de la ventana.

Aquí tienes un ejemplo con dos archivos:
Archivo llamado helper:
`x = 0

def say_hello():
    print("hola desde helper")`

Otro archivo:
`import helper
helper.say_hello()
helper.x += 1`

Aquí `import helper` ejecuta el archivo llamado `helper` y te da acceso a todas sus variables globales.
Luego puedes acceder a las variables y funciones dentro del módulo importado usando el operador `.`.
Así que en este ejemplo, `helper.say_hello()` llama a `say_hello()` dentro de helper y la última línea incrementa la variable global x.

También puedes mover las variables globales del módulo importado al scope actual donde se ejecuta la sentencia de importación usando la sintaxis `from`.

`from helper import *`
Importa todas las variables globales de helper.

o

`from helper import say_hello`
Importa solo las variables globales especificadas de helper.

Esto también importa el archivo helper, pero en lugar de acceder a él a través de una variable llamada `helper`, desempaqueta las variables globales de `helper` y las asigna directamente en el scope local.

`from helper import say_hello
say_hello()`

Esta forma de importación no suele recomendarse porque no funciona bien cuando dos archivos se importan mutuamente, y podrías sobrescribir accidentalmente variables en el archivo importador debido a colisiones de nombres.

# Cómo funciona realmente

## TLDR
Las importaciones pueden ser poco intuitivas, pero la mayoría de los problemas se pueden evitar usando la sintaxis `import file` en lugar de `from file import`, y envolviendo todo lo que no sea una definición global en
`if __name__ == "__main__":`

## Efectos Secundarios de la Importación
La primera vez que importas un archivo, se ejecutará el archivo completo y luego te dará acceso a todas las variables que se han definido durante la ejecución.
Si importas el mismo archivo de nuevo, simplemente devolverá el módulo cacheado de la primera vez.

Esto significa que las sentencias de importación pueden tener efectos secundarios. Si importas un archivo que llama a `harvest()`, realmente cosechará durante la importación. Pero cuando lo importes de nuevo, no volverá a cosechar porque el archivo solo se ejecuta una vez.

Hay una forma de evitar tales efectos secundarios usando la variable `__name__`. Esta es una variable que se establece automáticamente a `"__main__"` cuando un archivo se ejecuta directamente, y al nombre del archivo cuando se ejecuta a través de `import`.
Se considera una buena práctica poner cualquier código que no quieras que se ejecute cuando el archivo es importado dentro de un bloque `if __name__ == "__main__":`.

Una estructura de archivos común en Python es poner el código que debe ejecutarse cuando se ejecuta el archivo en una función `main()`. De esta manera, tienes una distinción clara entre las variables locales (definidas dentro de `main()`) y las variables globales que se pueden importar (definidas fuera de `main()`).

`a_global_variable = "global"

def main():
    a_local_variable = "local"
    # hacer cosas

if __name__ == "__main__":
    main()`

## Ciclos de Importación
¿Qué pasa si el archivo `a` importa el archivo `b` y el archivo `b` importa el archivo `a`?

archivo `a`:
`import b
x = 0`

archivo `b`:
`import a
def f():
    print(a.x)`

Esto funcionará bien. Digamos que ninguno de los dos archivos está cargado todavía, y alguien más ejecuta `import a`.

-`a` se ejecuta hasta la línea `import b`.
-`b` se ejecuta hasta la línea `import a`.
-El módulo `a` ya existe, pero no contiene `x` porque solo ha llegado hasta la línea `import b`.
-`b` guarda una referencia al módulo `a` a medio cargar en una variable llamada `a`.
-`b` ejecuta la sentencia `def` y guarda la función `f()`.
-`a` continúa ejecutándose e inicializa `x`.

Cuando alguien llama a `b.f()`, imprimirá correctamente `0` porque el módulo `a` al que `b` tiene una referencia ya está completamente cargado.

Ahora considera el mismo código usando la sintaxis `from`.

archivo `a`:
`from b import *
x = 0`

archivo `b`:
`from a import *
def f():
    print(x)`

-`a` se ejecuta hasta la línea `from b import *`.
-`b` se ejecuta hasta la línea `from a import *`.
-El módulo `a` ya existe, pero aún no se ha ejecutado completamente.
-`b` desempaqueta todo lo que está actualmente en `a` en su propio scope global. En este punto, `a` no contiene nada porque aún no ha llegado a la línea `x = 0`, por lo que no se importa nada.
-`b` ejecuta la sentencia `def` y guarda la función `f()`.
-`a` continúa ejecutándose e inicializa `x`.

Si alguien llama ahora a `b.f()`, recibirá un error de que `x` no existe en el scope actual. Esto se debe a que esta vez `b` no tiene una referencia a `a` que todavía se está cargando y no ve las definiciones que se añadieron después de la importación.