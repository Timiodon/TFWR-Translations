# Labirintos
`Items.Weird_Substance`, que é obtida ao [fertilizar](docs/unlocks/fertilizer.md) plantas, tem um efeito estranho em arbustos. Se o drone estiver sobre um arbusto e você chamar `use_item(Items.Weird_Substance, amount)`, o arbusto crescerá em um labirinto de sebes. O tamanho do labirinto depende da quantidade de `Items.Weird_Substance` usada (o segundo argumento da chamada `use_item()`).
Sem upgrades de labirinto, usar `n` `Items.Weird_Substance` resultará em um labirinto de `n`x`n`. Cada nível de upgrade do labirinto dobra o tesouro, mas também dobra a quantidade de `Items.Weird_Substance` necessária.
Então, para fazer um labirinto de campo completo:

`plant(Entities.Bush)
n_substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, n_substance)`

Por algum motivo, o drone não consegue voar sobre as sebes, apesar de elas não parecerem tão altas.

Há um tesouro escondido em algum lugar no labirinto. Use `harvest()` no tesouro para receber ouro igual à área do labirinto. (Por exemplo, um labirinto de 5x5 renderá 25 de ouro.)

Se você usar `harvest()` em qualquer outro lugar, o labirinto simplesmente desaparecerá.

`get_entity_type()` é igual a `Entities.Treasure` se o drone estiver sobre o tesouro e `Entities.Hedge` em qualquer outro lugar no labirinto.

Labirintos não contêm loops, a menos que você reutilize o labirinto (veja abaixo como reutilizar um labirinto). Assim, não há maneira do drone acabar na mesma posição novamente sem voltar.

Você pode verificar se há uma parede tentando passar por ela.
`move()` retorna `True` se conseguiu e `False` caso contrário.

Se você não tem ideia de como chegar ao tesouro, dê uma olhada na Dica 1. Ela mostra como abordar um problema como este.

Para um desafio extra, você também pode reutilizar o labirinto usando a mesma quantidade de `Items.Weird_Substance` no tesouro novamente.
Isso aumentará a quantidade de ouro no tesouro por um labirinto inteiro e o moverá para uma posição aleatória no labirinto.

Usar `measure()` em um tesouro retorna a posição para a qual ele se moverá, como uma tupla.
`next_x, next_y = measure()`

Cada vez que o tesouro é movido, uma parede aleatória pode ser removida do labirinto. Então labirintos reutilizados podem conter loops.

Observe que loops no labirinto tornam muito mais difícil porque significa que você pode chegar ao mesmo local novamente sem voltar.
Reutilizar um labirinto não lhe dá mais ouro do que simplesmente colher e criar um novo labirinto.
É 100% um desafio extra que você pode simplesmente pular.
Só vale a pena se a informação extra e os atalhos ajudarem você a resolver o labirinto mais rápido.

O mesmo labirinto pode ser resolvido no máximo 300 vezes. Isso corresponde a 299 relocações. Após isso, usar substância estranha no tesouro não aumentará mais o ouro nele e `measure()` retornará `None`.

<spoiler=mostre a dica 1>Aqui está uma abordagem geral para resolver o problema:

Crie um labirinto e imagine que você é o drone.

Pense em como você tentaria encontrar o tesouro se estivesse no labirinto.

Anote sua estratégia passo a passo para que alguém possa segui-la sem pensar.

Agora tente traduzir seus passos em código.
</spoiler>
<spoiler=mostre a dica 2>Enquanto não houver loops: Todas as paredes são realmente apenas uma grande parede conectada. Se você seguir a parede, ela o levará através do labirinto inteiro.
Essa abordagem requer muito pouco código e você não precisa acompanhar onde já esteve. Cerca de 10 linhas de código é tudo o que você precisa.</spoiler>
<spoiler=mostre a dica 3>Em vez de mover o drone em direções absolutas como leste ou oeste, pode ser muito útil movê-lo em direções relativas como "virar à direita" ou "virar à esquerda". Para fazer isso, você precisa acompanhar para onde o drone está se movendo atualmente. O drone nunca realmente gira, mas você ainda pode manter uma rotação "virtual" no código.
O seguinte truque de índice é útil para isso:

`directions = [North, East, South, West]
index = 0`

Use `% 4` para permitir que ele gire "em torno do círculo", de modo que depois de `West` ele retorne para `North`.
`# virar à direita
index = (index + 1) % 4`

`# virar à esquerda
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=mostre a dica 4>Se você não conseguir resolver, você sempre pode facilitar sua vida e fazer menos eficientemente.
Resolver um labirinto de `1`x`1` é trivial.</spoiler>