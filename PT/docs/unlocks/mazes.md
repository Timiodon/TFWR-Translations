# Labirintos
`Items.Weird_Substance`, que é obtido ao [fertilizar](docs/unlocks/fertilizer.md) plantas, tem um efeito estranho nos arbustos. Se o drone estiver sobre um arbusto e chamares `use_item(Items.Weird_Substance, amount)`, o arbusto crescerá e tornar-se-á um labirinto de sebes.
O tamanho do labirinto depende da quantidade de `Items.Weird_Substance` usada (o segundo argumento da chamada `use_item()`).
Sem melhorias de labirinto, usar `n` `Items.Weird_Substance` resultará num labirinto de `n`x`n`. Cada nível de melhoria do labirinto duplica o tesouro, mas também duplica a quantidade de `Items.Weird_Substance` necessária.
Então, para fazer um labirinto de campo inteiro:

`plant(Entities.Bush)
n_substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, n_substance)`


Por alguma razão, o drone não consegue voar sobre as sebes, embora não pareçam assim tão altas.

Há um tesouro escondido algures na sebe. Usa `harvest()` no tesouro para receberes ouro igual à área do labirinto. (Por exemplo, um labirinto 5x5 renderá 25 de ouro.)

Se usares `harvest()` em qualquer outro lugar, o labirinto simplesmente desaparecerá.

`get_entity_type()` é igual a `Entities.Treasure` se o drone estiver sobre o tesouro e `Entities.Hedge` em todo o resto do labirinto.

Os labirintos não contêm ciclos, a menos que reutilizes o labirinto (vê abaixo como reutilizar um labirinto). Portanto, não há como o drone acabar na mesma posição novamente sem voltar para trás.

Podes verificar se há uma parede tentando passar por ela.
`move()` retorna `True` se for bem-sucedido e `False` caso contrário.

Se não tens ideia de como chegar ao tesouro, dá uma olhada na Dica 1. Ela mostra como abordar um problema como este.


Para um desafio extra, também podes reutilizar o labirinto usando a mesma quantidade de `Items.Weird_Substance` no tesouro novamente.
Isto aumentará a quantidade de ouro no tesouro em um labirinto completo e movê-lo-á para uma posição aleatória no labirinto.

Usar `measure()` num tesouro retorna a posição para a qual ele se moverá, como um tuple.
`next_x, next_y = measure()`

Cada vez que o tesouro é movido, uma parede aleatória pode ser removida do labirinto. Portanto, labirintos reutilizados podem conter ciclos.

Nota que os ciclos no labirinto tornam-no muito mais difícil, porque significa que podes chegar ao mesmo local novamente sem ter de recuar.
Reutilizar um labirinto não te dá mais ouro do que simplesmente colher e gerar um novo labirinto.
Isto é 100% um desafio extra que podes simplesmente ignorar.
Só vale a pena se a informação extra e os atalhos te ajudarem a resolver o labirinto mais rapidamente.

O mesmo labirinto pode ser resolvido no máximo 300 vezes. Isto corresponde a 299 relocalizações. Depois disso, usar substância estranha no tesouro não aumentará mais o ouro nele e `measure()` retornará `None`.

<spoiler=mostrar dica 1>Aqui está uma abordagem geral para resolver o problema:

Cria um labirinto e imagina que és o drone.

Pensa em como tentarias encontrar o tesouro se estivesses no labirinto.

Escreve a tua estratégia passo a passo para que outra pessoa a possa seguir sem pensar.

Agora tenta traduzir os teus passos em código.
</spoiler>
<spoiler=mostrar dica 2>Enquanto não houver ciclos: Todas as paredes são, na verdade, uma única parede grande e conectada. Se seguires a parede, ela levar-te-á por todo o labirinto.
Esta abordagem requer muito pouco código e não precisas de registar onde já estiveste. Cerca de 10 linhas de código é tudo o que precisas.</spoiler>
<spoiler=mostrar dica 3>Em vez de mover o drone em direções absolutas como leste ou oeste, pode ser muito útil mover o drone em direções relativas como "virar à direita" ou "virar à esquerda". Para fazer isso, precisas de registar para que lado o drone está atualmente a mover-se. O drone nunca roda de facto, mas ainda podes manter uma rotação "virtual" em código.
O seguinte truque de índice é útil para isso:

`directions = [North, East, South, West]
index = 0`

Usa `% 4` para permitir que ele rode "em círculo", de modo que após `West` ele volte para `North`.
`# virar à direita
index = (index + 1) % 4`

`# virar à esquerda
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=mostrar dica 4>Se não conseguires resolver, podes sempre facilitar a tua vida e fazê-lo de forma menos eficiente.
Resolver um labirinto `1`x`1` é trivial.</spoiler>