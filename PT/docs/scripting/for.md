# Loop For
O loop `for` funciona como em Python. (Chamado de loop foreach em algumas linguagens, não confundir com o loop for ao estilo C, que é uma coisa diferente).

`for i in sequence:
	#faz algo com i`

Semelhante ao loop `while`, o loop `for` também chama repetidamente um bloco de código. Em vez de fazer um loop com base numa condição, ele executa o corpo do loop uma vez para cada elemento numa sequência.

## Sintaxe
Um loop for tem este aspeto:

`for variable_name in sequence:
	#bloco de código`

`variable_name` pode ser qualquer nome que escolhas. É uma variável que armazena o elemento atual na sequência. `sequence` precisa de ser algum valor que possa ser iterado, como um range ou números. O bloco de código é executado para cada elemento com a variável do loop atribuída a esse elemento.

## Sequências
[Ranges](functions/range)      <unlock=lists>[Listas](docs/scripting/lists.md)      </unlock><unlock=functions>[Tuples](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Dictionaries](docs/scripting/dicts.md)      </unlock><unlock=sets>[Sets](docs/scripting/sets.md)</unlock>

## Exemplo
`for i in range(5):
    harvest()`

Este loop executa o corpo um número fixo de vezes. É essencialmente o mesmo que escrever

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

Então, ele chama `harvest()` 5 vezes.

Vê também [Break](docs/scripting/break.md) e [Continue](docs/scripting/continue.md)