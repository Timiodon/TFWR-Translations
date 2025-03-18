# Importar
Colocar todo tu código en un solo archivo rápidamente se vuelve inmanejable. Las declaraciones `import` te permiten importar funciones y variables globales desde otro archivo.

`import filename`

Esta es la forma más sencilla de declaración de importación. Te dará acceso a todo lo definido en el archivo llamado `filename`. Cada ventana en el juego es un archivo, y el nombre del archivo es el nombre mostrado en la parte superior de la ventana.

Aquí tienes un ejemplo con dos archivos:
Archivo llamado helper:
`x = 0

def say_hello():
    print("hello from helper")`

Algún otro archivo:
`import helper
helper.say_hello()
helper.x += 1`

Aquí `import helper` ejecuta el archivo llamado `helper` y te da acceso a todas sus variables globales.
Luego puedes acceder a las variables y funciones dentro del módulo importado usando el operador `.`.
Así que en este ejemplo, `helper.say_hello()` llama a `say_hello()` dentro de helper y la última línea incrementa la variable global x.

También puedes mover las variables globales del módulo importado al ámbito actual donde se ejecuta la declaración de importación usando la sintaxis `from`.

`from helper import *`
Importa todas las variables globales de helper.

o

`from helper import say_hello`
Importa solo las variables globales especificadas de helper.

Esto también importa el archivo helper, pero en lugar de acceder a él a través de una variable llamada `helper`, desempaqueta las variables globales de `helper` y las asigna directamente en el ámbito local.

`from helper import say_hello
say_hello()`

Esta forma de importar generalmente no se recomienda porque no funciona bien cuando dos archivos se importan mutuamente, y puede que accidentalmente sobrescribas variables en el archivo que importa debido a colisiones de nombres.

# Cómo realmente funciona

## Resumen
Los imports pueden ser bastante poco intuitivos, pero la mayoría de los problemas se pueden evitar adhiriéndose a la sintaxis `import file` en lugar de `from file import`, y envolviendo todo lo que no sea una definición global en
`if __name__ == "__main__":`

## Efectos secundarios del import
La primera vez que importas un archivo, ejecutará todo el archivo y luego te dará acceso a todas las variables que se hayan definido durante la ejecución.
Si importas el mismo archivo de nuevo, solo devolverá el módulo almacenado en caché de la primera vez.

Esto significa que las declaraciones de importación pueden tener efectos secundarios. Si importas un archivo que llama a `harvest()`, realmente cosechará durante el import. Pero cuando lo importes de nuevo, no cosechará de nuevo porque el archivo solo se ejecuta una vez.

Hay una manera de evitar tales efectos secundarios usando la variable `__name__`. Esta es una variable que se establece automáticamente a `"__main__"` cuando un archivo se ejecuta directamente, y al nombre del archivo cuando un archivo se ejecuta a través de `import`.
Se considera una buena práctica colocar cualquier código que no quieras que se ejecute cuando el archivo es importado dentro de un bloque `if __name__ == "__main__":`.

Una estructura de archivo común en Python es colocar el código que debe ejecutarse cuando el archivo es ejecutado en una función `main()`. De esta manera, tienes una clara distinción entre las variables locales (definidas dentro de `main()`) y las variables globales que pueden ser importadas (definidas fuera de `main()`).

`a_global_variable = "global"

def main():
    a_local_variable = "local"
    # hacer cosas

if __name__ == "__main__":
    main()`

## Ciclos de importación
¿Qué pasa si el archivo `a` importa el archivo `b` y el archivo `b` importa el archivo `a`?

archivo `a`:
`import b
x = 0`

archivo `b`:
`import a
def f():
    print(a.x)`

Esto funcionará bien. Supongamos que ninguno de los dos archivos está cargado todavía, y alguien más ejecuta `import a`.

-`a` se ejecuta hasta la línea `import b`.
-`b` se ejecuta hasta la línea `import a`.
-El módulo `a` ya existe, pero no contiene `x` porque solo ha llegado a la línea `import b`.
-`b` almacena una referencia al módulo medio cargado `a` en una variable llamada `a`.
-`b` ejecuta la declaración `def` y almacena la función `f()`.
-`a` continúa ejecutándose e inicializa `x`.

Cuando alguien llama a `b.f()` imprimirá correctamente `0` porque el módulo `a` al que `b` tiene una referencia ya está completamente cargado.

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
-El módulo `a` ya existe, pero no se ha ejecutado por completo todavía.
-`b` desempaqueta todo lo que está actualmente en `a` en su propio ámbito global. En este punto, `a` no contiene nada porque no ha llegado a la línea `x = 0` todavía, por lo que no se importa nada.
-`b` ejecuta la declaración `def` y almacena la función `f()`.
-`a` continúa ejecutándose e inicializa `x`.

Si alguien ahora llama a `b.f()`, obtendrán un error porque `x` no existe en el ámbito actual. Esto se debe a que esta vez `b` no tiene una referencia al `a` aún en carga y no ve las definiciones que se agregaron después del import.