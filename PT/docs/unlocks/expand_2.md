# Expandir 2
A tua quinta expandiu-se novamente! Agora os quadrados já não estão numa fila bonita, por isso precisas de encontrar uma maneira de atravessar uma grelha quadrada.

Com o loop `while` isto não é possível até que desbloqueies sentidos e operadores.
Está na hora de apresentar o loop `for`.

Podes ler tudo sobre o loop `for` na página [Loop For](docs/scripting/for.md), mas por agora só vais precisar dele para repetir código um número fixo de vezes.

`#faz n pinos
for i in range(5):
	do_a_flip()`

`range(n)` cria um intervalo de números de `0` a `n-1`, que tem `n` elementos. O loop `for` executa o seu corpo uma vez para cada elemento na sequência. Neste exemplo, `do_a_flip()` será chamado `5` vezes.

A função `get_world_size()` também está disponível agora. Ela retorna o comprimento do lado da tua quinta. Desta forma, podes escrever código que não vai quebrar com a próxima melhoria de expansão.

`for i in range(get_world_size()):
	harvest()
	move(North)`

Este exemplo colhe uma coluna da quinta para qualquer tamanho de quinta.

Se estiveres com dificuldades em descobrir como mover o drone pela quinta, vê a dica abaixo.
<spoiler=mostrar dica>Existem, claro, várias maneiras de se mover pela quinta.
O que procuramos é uma maneira sistemática de a atravessar que não se quebre quando a quinta crescer novamente.
Uma maneira sistemática de chegar a todos os lugares da quinta seria repetir os 2 passos seguintes para sempre:

1.Mover para `North` até dar a volta.
2.Mover para `East`

`for i in range(get_world_size()):` pode ser útil para transformar esta ideia em código.
</spoiler>
<spoiler=mostrar possível solução> A travessia básica pode ser assim:

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		#faz um pino em cada quadrado
		do_a_flip()
		move(North)
	move(East)`
</spoiler>