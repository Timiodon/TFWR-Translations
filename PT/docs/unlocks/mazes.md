# Labirintos
`Items.Weird_Substance`, que é obtida [fertilizando](docs/unlocks/fertilizer.md) plantas, tem um efeito estranho em arbustos. Se o drone estiver sobre um arbusto e você chamar `use_item(Items.Weird_Substance, amount)`, o arbusto se transformará em um labirinto de sebes.
O tamanho do labirinto depende da quantidade de `Items.Weird_Substance` usada (o segundo argumento da chamada `use_item()`).
Sem melhorias de labirinto, usar `n` `Items.Weird_Substance` resultará em um labirinto `n`x`n`. Cada nível de melhoria do labirinto dobra o tesouro, mas também dobra a quantidade de `Items.Weird_Substance` necessária. 
Então, para fazer um labirinto de campo inteiro:

`plant(Entities.Bush)
substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)`


Por alguma razão, o drone não consegue voar sobre as sebes, embora não pareçam tão altas.

Há um tesouro escondido em algum lugar na sebe. Use `harvest()` no tesouro para receber ouro igual à área do labirinto. (Por exemplo, um labirinto 5x5 renderá 25 de ouro.)

Se você usar `harvest()` em qualquer outro lugar, o labirinto simplesmente desaparecerá.

`get_entity_type()` é igual a `Entities.Treasure` se o drone estiver sobre o tesouro e `Entities.Hedge` em qualquer outro lugar no labirinto.

Labirintos não contêm loops, a menos que você reutilize o labirinto (veja abaixo como reutilizar um labirinto). Portanto, não há como o drone acabar na mesma posição novamente sem voltar.

Você pode verificar se há uma parede tentando se mover através dela. 
`move()` retorna `True` se teve sucesso e `False` caso contrário.

`can_move()` pode ser usado para verificar se há uma parede sem se mover.

Se você não tem ideia de como chegar ao tesouro, dê uma olhada na Dica 1. Ela mostra como abordar um problema como este.

Usar `measure()` em qualquer lugar no labirinto retorna a posição do tesouro.
`x, y = measure()`

Para um desafio extra, você também pode reutilizar o labirinto usando a mesma quantidade de `Items.Weird_Substance` no tesouro novamente. 
Isso aumentará a quantidade de ouro no tesouro em um labirinto completo e o moverá para uma posição aleatória no labirinto.

Cada vez que o tesouro é movido, algumas das paredes do labirinto podem ser removidas aleatoriamente. Portanto, labirintos reutilizados podem conter loops.

Note que loops no labirinto o tornam muito mais difícil, porque significa que você pode chegar ao mesmo local novamente sem voltar.
Reutilizar um labirinto não lhe dá mais ouro do que apenas colher e gerar um novo labirinto.
Este é 100% um desafio extra que você pode simplesmente pular.
Só vale a pena se as informações extras e os atalhos o ajudarem a resolver o labirinto mais rápido.

O mesmo labirinto pode ser resolvido no máximo 300 vezes. Isso corresponde a 299 realocações. Depois disso, usar substância estranha no tesouro não aumentará mais o ouro nele e `measure()` retornará `None`.

<spoiler=show hint 1>Aqui está uma abordagem geral para resolver o problema:

Crie um labirinto e imagine que você é o drone.

Pense em como você tentaria encontrar o tesouro se estivesse no labirinto.

Anote sua estratégia passo a passo para que outra pessoa possa segui-la sem pensar.

Agora tente traduzir seus passos em código.
</spoiler>
<spoiler=show hint 2>Enquanto não houver loops: todas as paredes são, na verdade, uma grande parede conectada. Se você seguir a parede, ela o levará por todo o labirinto.
Esta abordagem requer muito pouco código e você não precisa acompanhar onde já esteve. Cerca de 10 linhas de código é tudo o que você precisa.</spoiler>
<spoiler=show hint 3>Em vez de mover o drone em direções absolutas como leste ou oeste, pode ser muito útil mover o drone em direções relativas como "virar à direita" ou "virar à esquerda". Para fazer isso, você precisa acompanhar para qual lado o drone está se movendo atualmente. O drone nunca gira de fato, mas você ainda pode manter uma rotação "virtual" no código.
O seguinte truque de índice é útil для isso:

`directions = [North, East, South, West]
index = 0`

Use `% 4` para permitir que ele gire "em círculo", de modo que após `West` ele volte para `North`.
`# vire à direita
index = (index + 1) % 4`

`# vire à esquerda
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=show hint 4>Se você não conseguir resolver, pode sempre facilitar sua vida e fazer de forma menos eficiente. 
Resolver um labirinto `1`x`1` é trivial.</spoiler>