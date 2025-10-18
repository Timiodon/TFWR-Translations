# Expansão 2
Sua fazenda expandiu novamente! Agora as casas não estão mais em uma bela fila, então você precisa encontrar uma maneira de percorrer uma grade quadrada.

Com o loop `while` isso não é possível até que você desbloqueie sensores e operadores.
É hora de apresentar o loop `for`.

Você pode ler tudo sobre o loop `for` na página [Loop For](docs/scripting/for.md), mas por enquanto você só precisará dele para repetir código um número fixo de vezes.

`#dê n piruetas
for i in range(5):
	do_a_flip()`

`range(n)` cria um intervalo de números de `0` a `n-1` que tem `n` elementos. O loop `for` executa o corpo do loop uma vez para cada elemento na sequência. Neste exemplo, `do_a_flip()` será chamado `5` vezes.

A função `get_world_size()` também está disponível agora. Ela retorna o comprimento do lado da sua fazenda. Desta forma, você pode escrever código que não quebrará com a próxima melhoria de expansão.

`for i in range(get_world_size()):
	harvest()
	move(North)`

Este exemplo colhe uma coluna da fazenda para qualquer tamanho de fazenda.

Se você está com dificuldades para descobrir como mover o drone pela fazenda, veja a dica abaixo.
<spoiler=show hint>Existem, é claro, várias maneiras de se mover pela fazenda.
O que estamos procurando é uma maneira de percorrê-la de forma sistemática que não quebre quando a fazenda crescer novamente.
Uma maneira sistemática de chegar a todos os lugares da fazenda seria repetir os 2 passos a seguir para sempre:

1.Mova `North` até voltar ao início.
2.Mova `East`

`for i in range(get_world_size()):` pode ser útil para transformar esta ideia em código.
</spoiler>
<spoiler=show possible solution> A travessia básica pode se parecer com isto:

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		#dê uma pirueta em cada casa
		do_a_flip()
		move(North)
	move(East)`
</spoiler>