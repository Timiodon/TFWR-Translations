# Laço For
O laço `for` funciona como em Python. (Chamado de foreach em algumas linguagens, não confunda com o laço estilo C, que é diferente).

`for i in sequence:
	#do something with i`

Semelhante ao laço `while`, o laço `for` também chama repetidamente um bloco de código. Em vez de iterar com base em uma condição, ele executa o corpo do laço uma vez para cada elemento em uma sequência.

## Sintaxe
Um laço for se parece com isso:

`for variable_name in sequence:
	#code block`

`variable_name` pode ser qualquer nome que você escolher. É uma variável que armazena o elemento atual na sequência. `sequence` precisa ser algum valor que possa ser iterado como um range ou números. O bloco de código é executado para cada elemento com a variável do laço atribuída a esse elemento.

## Sequências
[Ranges](functions/range)      <unlock=lists>[Listas](docs/scripting/lists.md)      </unlock><unlock=functions>[Tuplas](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Dictionaries](docs/scripting/dicts.md)      </unlock><unlock=sets>[Sets](docs/scripting/sets.md)</unlock>

## Exemplo
`for i in range(5):
    harvest()`

Este laço executa o corpo um número fixo de vezes. É essencialmente o mesmo que escrever

`i = 0
harvest()
i = 1
harvest()
i = 2
harvest()
i = 3
harvest()
i = 4
harvest()`

Portanto, ele chama `harvest()` 5 vezes.

Veja também [Break](docs/scripting/break.md) e [Continue](docs/scripting/continue.md)