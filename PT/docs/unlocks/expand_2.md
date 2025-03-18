# Expandir 2
Sua fazenda se expandiu novamente! Agora os tiles não estão mais em uma linha reta, então você precisa encontrar uma maneira de atravessar uma grade quadrada.

Com o `while` loop isso não é possível até você desbloquear sensores e operadores.
É hora de apresentar o `for` loop.

Você pode ler tudo sobre o `for` loop na página [For Loop](docs/scripting/for.md), mas por agora você só precisará dele para repetir o código um número fixo de vezes.

`#faça n flips
for i in range(5):
	do_a_flip()`

`range(n)` cria um intervalo de números de `0` a `n-1`, o qual possui `n` elementos. O `for` loop executa seu corpo uma vez para cada elemento na sequência. Neste exemplo, `do_a_flip()` será chamado `5` vezes.

A função `get_world_size()` também está disponível agora. Ela retorna o comprimento do lado da sua fazenda. Desta forma, você pode escrever código que não vai quebrar com a próxima atualização de expansão.

`for i in range(get_world_size()):
	harvest()
	move(North)`

Este exemplo colhe uma coluna da fazenda para qualquer tamanho de fazenda.

Se você estiver travado tentando descobrir como mover o drone pela fazenda, veja a dica abaixo.
<spoiler=mostrar dica> Existem, claro, várias maneiras de se mover pela fazenda.
O que estamos procurando é uma maneira de percorrê-la de forma sistemática que não quebre quando a fazenda crescer novamente.
Uma maneira sistemática de chegar a todos os lugares na fazenda seria repetir os seguintes passos para sempre:

1. Mover `North` até voltar.
2. Mover `East`

`for i in range(get_world_size()):` pode ser útil para transformar essa ideia em código.
</spoiler>
<spoiler=mostrar solução possível> O percurso básico pode ser assim:

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		#faça um flip em cada tile
		do_a_flip()
		move(North)
	move(East)`
</spoiler>