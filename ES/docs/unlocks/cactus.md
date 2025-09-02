# Cactus
Como otras plantas, los [cactus](objects/cactus) pueden cultivarse en tierra y cosecharse como de costumbre.

Sin embargo, vienen en varios tamaños y tienen un extraño sentido del orden.

Si cosechas un cactus completamente crecido y todos los cactus vecinos están en orden, también cosechará todos los cactus vecinos de forma recursiva.

Un cactus se considera ordenado si todos los cactus vecinos al `North` y `East` están completamente crecidos y son de tamaño mayor o igual, y todos los cactus vecinos al `South` y `West` están completamente crecidos y son de tamaño menor o igual.

La cosecha solo se propagará si todos los cactus adyacentes están completamente crecidos y en orden.
Esto significa que si un cuadrado de cactus crecidos está ordenado por tamaño y cosechas un cactus, se cosechará todo el cuadrado.

Un cactus completamente crecido aparecerá marrón si no está ordenado. Una vez ordenado, se volverá verde de nuevo.

Recibirás una cantidad de cactus igual al número de cactus cosechados al cuadrado. Así que si cosechas `n` cactus simultáneamente, recibirás `n**2` `Items.Cactus`.

El tamaño de un cactus se puede medir con `measure()`.
Siempre es uno de estos números: `0,1,2,3,4,5,6,7,8,9`.

También puedes pasar una dirección a `measure(direction)` para medir la casilla vecina en esa dirección del dron.

Puedes intercambiar un cactus con su vecino en cualquier dirección usando el comando `swap()`.
`swap(direction)` intercambia el objeto debajo del dron con el objeto a una casilla de distancia en la `direction` del dron.

## Ejemplos
En cada una de estas cuadrículas, todos los cactus están ordenados y la cosecha se extenderá por todo el campo:
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

En esta cuadrícula, solo el cactus inferior izquierdo está ordenado, lo que no es suficiente para que se propague:
`1 5 3
4 9 7
3 3 2`

<spoiler=show hint 1>
Si las filas ya están ordenadas, ordenar las columnas no desordenará las filas.
</spoiler>
<spoiler=show hint 2>
Si no estás familiarizado con los algoritmos de ordenamiento, quizás quieras buscarlos en línea y pensar cuáles podrían adaptarse a este problema. Ten en cuenta que no todos funcionan porque solo puedes intercambiar cactus vecinos.
</spoiler>