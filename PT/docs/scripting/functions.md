# Funções
Usa a palavra-chave `def` para definir uma nova função:
`def f(arg1, arg2 = False):
	#código da função`

Podes usar o operador de chamada `()` para chamar a função:
`f(42)`

Vê também [Scopes](docs/scripting/scopes.md) para aprender sobre variáveis locais e globais em funções.

## Introdução
Já viste funções incorporadas como `harvest()`.
Também podes definir as tuas próprias funções, o que permite estruturar o teu código de forma modular. Basicamente, permite-te dar um nome a um bloco de código para que o possas chamar de onde quiseres.

## Definições de Função
Por exemplo, podes definir uma função que move o drone várias vezes.

`def move_n_dir(n, dir):
	for i in range(n):
		move(dir)`

A palavra-chave `def` sinaliza que isto é uma definição de função.
`move_n_dir` é o nome ao qual a função fica associada. Pode ser qualquer nome de variável válido e será usado para chamar a função.
`n` e `dir` são parâmetros. São variáveis que contêm os valores que são passados para a função (Estes valores também são chamados de argumentos). Podes adicionar quantos parâmetros quiseres a uma definição de função.
Depois dos `:` vem o bloco de código que será executado quando a função for chamada.

Com a definição acima, o código seguinte move o drone `10` quadrados para `North` e `2` quadrados para `West`.

`move_n_dir(10, North)
move_n_dir(2, West)`

Quando vês `def function():`, deves pensar nisso como uma atribuição de variável como esta:
`function = create_new_function_object()`
Como em todas as atribuições, não podes usar a variável antes de ela ser atribuída!
A declaração `def` tem que ser executada antes de qualquer chamada de função.
Este código lançará um erro:

`func()
def func():
	pass`

## Valores de Retorno
Usa a palavra-chave `return` para fazer uma função retornar um valor.
Por exemplo, a função seguinte define a operação "ou exclusivo". O "ou exclusivo" retorna `True` se um valor for `True` e o outro for `False`:

`def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()`

[Tuples](docs/scripting/tuples.md) permitem retornar múltiplos valores.

## Argumentos Padrão
Também podes atribuir valores padrão que serão usados se nenhum argumento for passado.

`def f(a = False):
	if a:
		do_a_flip()

f()

f(True)`

Um argumento que tem um valor padrão não pode ser seguido por um argumento que não tem um valor padrão.

## Uso Avançado de Funções
As funções são valores como qualquer outro valor, e a declaração `def` age como uma declaração de atribuição, atribuindo a função ao nome que lhe deres.
Isto permite fazer coisas como esta:

`def f():
	def d():
		do_a_flip()
	return d

f()()`

Aqui `f()` chama a função `f` que define e retorna uma nova função `d`. O segundo `()` executa então a função retornada e faz o pino.
(Fazer este tipo de coisas geralmente não é uma boa ideia porque é difícil ver o que está a acontecer)

Funções que recebem outras funções como argumentos permitem-te ser muito criativo:

`def f(g, arg):
	for _ in range(10):
		g(arg)

f(move, North)
f(use_item, Items.Fertilizer)`

Este código move o drone `North` 10 vezes e depois usa fertilizante 10 vezes.