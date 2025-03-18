# Polycultura
Você já deve ter notado que, às vezes, as plantas produzem mais quando plantadas juntas.
Grama, arbustos, árvores e cenouras rendem mais quando têm a companhia certa. A preferência de companhia é diferente para cada planta individual e não pode ser prevista. Felizmente, a preferência de companhia da planta sob o drone pode ser medida usando `get_companion()`. Ele retorna uma tupla onde o primeiro elemento é o tipo de planta que ela quer como companheira e o segundo elemento é a posição onde ela quer sua companheira.

`plant, (x, y) = get_companion()`

Por exemplo, se você plantar um arbusto e então chamar `get_companion()`, ele retornará algo como `(Entities.Carrot, (3, 5))`. Isso significa que esse arbusto gostaria de ter cenouras na posição `(3,5)`. Então, se você plantar cenouras em `(3,5)` e depois colher o arbusto, ele renderá mais madeira. O estágio de crescimento da cenoura não importa.

A preferência de companhia de uma planta pode ser `Entities.Grass`, `Entities.Bush`, `Entities.Tree` ou `Entities.Carrot`. Cada planta escolhe isso aleatoriamente, mas sempre escolherá uma planta diferente de si mesma. A posição pode ser qualquer posição dentro de 3 movimentos da planta, exceto a posição da própria planta.

Se não houver uma planta sob o drone que tenha uma preferência de companhia, `get_companion()` retornará `None`.

O multiplicador de rendimento é `5` mais o número de melhorias de polycultura.