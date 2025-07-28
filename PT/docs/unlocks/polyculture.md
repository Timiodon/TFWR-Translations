# Policultura
Já deves ter reparado que por vezes as plantas rendem mais quando plantadas juntas.
Relva, arbustos, árvores e cenouras rendem mais quando têm a planta companheira certa. A preferência de companheiro é diferente para cada planta individual e não pode ser prevista. Felizmente, a preferência de companheiro da planta debaixo do drone pode ser medida usando `get_companion()`. Retorna um tuple onde o primeiro elemento é o tipo de planta que quer como companheira e o segundo elemento é a posição onde quer a sua companheira.

`plant_type, (x, y) = get_companion()`

Por exemplo, se plantares um arbusto e depois chamares `get_companion()`, retornará algo como `(Entities.Carrot, (3, 5))`. Isto significa que este arbusto gostaria de ter cenouras na posição `(3,5)`. Portanto, se plantares cenouras em `(3,5)` e depois colheres o arbusto, ele renderá mais madeira. O estágio de crescimento da cenoura não importa.

A preferência de companheiro de uma planta pode ser `Entities.Grass`, `Entities.Bush`, `Entities.Tree` ou `Entities.Carrot`. Cada planta escolhe isto aleatoriamente, mas escolherá sempre uma planta diferente de si mesma. A posição também pode ser qualquer posição a até 3 movimentos da planta, exceto a posição da própria planta.

Se não houver nenhuma planta debaixo do drone que tenha uma preferência de companheiro, `get_companion()` retornará `None`.

Antes de a policultura ser desbloqueada, o multiplicador de rendimento é `5`. Duplica cada vez que a melhoras.