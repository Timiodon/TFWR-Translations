# Import
Poner todo tu código en un solo archivo se vuelve inmanejable rápidamente. 
Las sentencias `import` te permiten importar funciones y variables globales de otro archivo.
Cómo funciona en una captura de pantalla:
![](ImportsInOnePicture400)

Aquí, `import module2` ejecuta el archivo llamado `module2` y te da acceso a todas sus variables globales.
Luego puedes acceder a las variables y funciones dentro del módulo importado usando el operador `.`.
Así que en este ejemplo, `module2.print_x()` llama a `print_x()` en `module2`.

### No es necesario seguir leyendo

También puedes mover las variables globales del módulo importado al ámbito actual donde se ejecuta la sentencia de importación usando la sintaxis `from`.

`from module2 import print_x
print_x()`
Importa solo las variables globales especificadas de `module2`.

o

`from module2 import *
print_x()`
Importa todas las variables globales de `module2`.

Esto también importa el archivo `module2`, pero en lugar de acceder a él a través de una variable llamada `module2`, desempaqueta las variables globales de `module2` y las asigna directamente en el ámbito local.

Esta forma de importar no suele recomendarse porque no funciona bien cuando dos archivos se importan mutuamente, y podrías sobrescribir accidentalmente variables en el archivo que importa debido a colisiones de nombres. Es más seguro evitar la sintaxis `from` si no sabes lo que estás haciendo.

# Cómo funciona realmente

## En resumen
Las importaciones pueden ser poco intuitivas, pero la mayoría de los problemas se pueden evitar usando la sintaxis `import archivo` en lugar de `from archivo import`, y envolviendo todo lo que no sea una definición global en
`if __name__ == "__main__":`

## Efectos Secundarios de la Importación
La primera vez que importas un archivo, se ejecutará el archivo completo y luego te dará acceso a todas las variables que se hayan definido durante la ejecución.
Si importas el mismo archivo de nuevo, simplemente devolverá el módulo guardado en caché de la primera vez.

Esto significa que las sentencias de importación pueden tener efectos secundarios. Si importas un archivo que llama a `harvest()`, realmente cosechará durante la importación. Pero cuando lo importes de nuevo, no volverá a cosechar porque el archivo solo se ejecuta una vez.

Hay una forma de evitar tales efectos secundarios usando la variable `__name__`. Esta es una variable que se establece automáticamente a `"__main__"` cuando un archivo se ejecuta directamente, y al nombre del archivo cuando se ejecuta a través de `import`.
Se considera una buena práctica poner cualquier código que no quieras que se ejecute cuando se importa el archivo dentro de un bloque `if __name__ == "__main__":`.

Una estructura de archivo común en Python es poner el código que debe ejecutarse cuando se ejecuta el archivo en una función `main()`. De esta manera tienes una distinción clara entre las variables locales (definidas dentro de `main()`) y las variables globales que se pueden importar (definidas fuera de `main()`).

`una_variable_global = "global"

def main():
    una_variable_local = "local"
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

Cuando alguien llama a `b.f()`, imprimirá `0` correctamente porque el módulo `a` al que `b` tiene una referencia ya está completamente cargado.

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
-`b` desempaqueta todo lo que está actualmente en `a` en su propio ámbito global. En este punto, `a` no contiene nada porque aún no ha llegado a la línea `x = 0`, por lo que no se importa nada.
-`b` ejecuta la sentencia `def` y guarda la función `f()`.
-`a` continúa ejecutándose e inicializa `x`.

Si alguien llama ahora a `b.f()`, obtendrá un error de que `x` no existe en el ámbito actual. Esto se debe a que esta vez `b` no tiene una referencia a `a` que todavía se está cargando y no ve las definiciones que se añadieron después de la importación.