# Cactus
Como otras plantas, los [cactus](objects/cactus) se pueden cultivar en tierra y cosechar como de costumbre.

Sin embargo, vienen en varios tamaños y tienen un extraño sentido del orden.

Si cosechas un cactus completamente crecido y todos los cactus vecinos están en orden, también cosechará todos los cactus vecinos de forma recursiva.

Se considera que un cactus está en orden si todos los cactus vecinos al `North` y `East` están completamente crecidos y son de tamaño mayor o igual, y todos los cactus vecinos al `South` y `West` están completamente crecidos y son de tamaño menor o igual.

La cosecha solo se extenderá si todos los cactus adyacentes están completamente crecidos y en orden.
Esto significa que si un cuadrado de cactus crecidos está ordenado por tamaño y cosechas un cactus, cosechará todo el cuadrado.

Un cactus completamente crecido aparecerá marrón si no está ordenado. Una vez ordenado, volverá a ser verde.

Recibirás cactus igual al número de cactus cosechados al cuadrado. Así que si cosechas `n` cactus simultáneamente, recibirás `n**2` `Items.Cactus`.

El tamaño de un cactus se puede medir con `measure()`.
Siempre es uno de estos números: `0,1,2,3,4,5,6,7,8,9`.

También puedes pasar una dirección a `measure(direction)` para medir la casilla vecina en esa dirección del dron.

Puedes intercambiar un cactus con su vecino en cualquier dirección usando el comando `swap()`.
`swap(direction)` intercambia el objeto debajo del dron con el objeto una casilla en la `direction` del dron.

## Ejemplos
En cada una de estas cuadrículas, todos los cactus están en orden y la cosecha se extenderá por todo el campo:
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

En esta cuadrícula, solo el cactus inferior izquierdo está en orden, lo cual no es suficiente para que se extienda:
`1 5 3
4 9 7
3 3 2`

<spoiler=mostrar pista 1>
Si las filas ya están ordenadas, ordenar las columnas no desordenará las filas.
</spoiler>
<spoiler=mostrar pista 2>
Si no estás familiarizado con los algoritmos de ordenación, quizás quieras buscarlos en línea y pensar cuáles podrían adaptarse a este problema. Ten en cuenta que no todos funcionan porque solo puedes intercambiar cactus vecinos.
</spoiler>