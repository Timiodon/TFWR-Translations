[<- Fertilizante](docs/unlocks/fertilizer.md) <right>[Megafazenda ->](docs/unlocks/megafarm.md)

---

# Labirintos

`Items.Weird_Substance` tem um efeito estranho nos arbustos. Se o drone estiver sobre um arbusto e você chamar `use_item(Items.Weird_Substance, amount)`, o arbusto se transformará em um labirinto de sebes.
O tamanho do labirinto depende da quantidade de `Items.Weird_Substance` usada (o segundo argumento da chamada `use_item()`).
Sem melhorias de labirinto, usar `n` `Items.Weird_Substance` criará um labirinto de `n`x`n`. Cada nível de melhoria do labirinto dobra o tesouro, mas também dobra a quantidade necessária de `Items.Weird_Substance`.
Portanto, para criar um labirinto que ocupe o campo inteiro:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": -1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
}}

Por alguma razão, o drone não consegue voar sobre as sebes, embora não pareçam tão altas.

Há um tesouro escondido em algum lugar do labirinto. Use `harvest()` no tesouro para receber uma quantidade de ouro igual à área do labirinto. Por exemplo, um labirinto 5x5 renderá 25 de ouro.

Se você usar `harvest()` em qualquer outro lugar, o labirinto simplesmente desaparecerá.

`get_entity_type()` é igual a `Entities.Treasure` se o drone estiver sobre o tesouro e `Entities.Hedge` em qualquer outro lugar no labirinto.

Os labirintos não contêm ciclos, a menos que sejam reutilizados (veja abaixo). Portanto, o drone não pode voltar à mesma posição sem refazer o caminho.

Você pode verificar se há uma parede tentando se mover através dela. 
`move()` retorna `True` se teve sucesso e `False` caso contrário.

`can_move()` pode ser usado para verificar se há uma parede sem se mover.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(East)
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
#CODE
quick_print(
    can_move(North), 
    can_move(East), 
    can_move(South), 
    can_move(West)
)
if move(North) and get_entity_type() == Entities.Treasure:
    harvest()
}}

Se você não tem ideia de como chegar ao tesouro, dê uma olhada na Dica 1. Ela mostra como abordar um problema como este.

Usar `measure()` em qualquer lugar no labirinto retorna a posição do tesouro.
`x, y = measure()`

Para um desafio extra, você pode reutilizar o labirinto aplicando novamente a mesma quantidade de `Items.Weird_Substance` no tesouro.
Isso coletará o tesouro e fará surgir outro em uma posição aleatória do labirinto.

Cada vez que o tesouro é movido, algumas das paredes do labirinto podem ser removidas aleatoriamente. Portanto, labirintos reutilizados podem conter loops.

Note que loops no labirinto o tornam muito mais difícil, porque significa que você pode chegar ao mesmo local novamente sem voltar.
Reutilizar um labirinto não lhe dá mais ouro do que apenas colher e gerar um novo labirinto.
Este é 100% um desafio extra que você pode simplesmente pular.
Só vale a pena se as informações extras e os atalhos o ajudarem a resolver o labirinto mais rápido.

O tesouro pode ser realocado até 300 vezes. Depois disso, usar a Substância Estranha nele não dará mais ouro nem moverá o tesouro.

<spoiler=mostrar dica 1>
Aqui está uma abordagem geral para resolver o problema:

Crie um labirinto e imagine que você é o drone.

Pense em como você tentaria encontrar o tesouro se estivesse no labirinto.

Anote sua estratégia passo a passo para que outra pessoa possa segui-la sem pensar.

Agora tente transformar seus passos em código.
</spoiler>
<spoiler=mostrar dica 2>
Enquanto não houver ciclos, todas as paredes formarão uma única grande parede conectada. Se você colocar a mão esquerda na parede e segui-la, ela o conduzirá por todo o labirinto.
Essa abordagem exige pouquíssimo código, e você não precisa controlar por onde já passou. Cerca de 10 linhas de código são suficientes.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": true,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": -1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
#CODE
directions = [North, East, South, West]
index = 0
while get_entity_type() != Entities.Treasure:
    index = (index - 1) % 4
    for _ in range(4):
        if move(directions[index]):
            break
        index = (index + 1) % 4
do_a_flip()
harvest()
}}

</spoiler>
<spoiler=mostrar dica 3>
Em vez de mover o drone em direções absolutas, como leste ou oeste, pode ser útil movê-lo em direções relativas, como "virar à direita" ou "virar à esquerda". Para isso, você precisa acompanhar a direção em que o drone está se movendo. O drone nunca gira de fato, mas ainda é possível manter uma rotação "virtual" no código.
O seguinte truque com índices ajuda nisso:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
directions = [North, East, South, West]
index = 0
move(directions[index])

#virar à direita
index = (index + 1) % 4
move(directions[index])

#virar à esquerda
index = (index - 1) % 4
move(directions[index])
}}

`% 4` é usado para permitir que a rotação "dê a volta no círculo", fazendo com que `3 (West) + 1` volte a ser `0 (North)`, pois `4 % 4 == 0` e `-1 % 4 == 3`.</spoiler>
<spoiler=mostrar dica 4>
Se não conseguir resolver, você sempre pode simplificar o problema usando uma abordagem menos eficiente.
Resolver um labirinto de `1`x`1` é trivial.</spoiler>

---

[Estatísticas](docs/stats.md)      [Listas](docs/scripting/lists.md)      [Dicionários](docs/scripting/dicts.md)      [Tuplas](docs/scripting/tuples.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [can_move()](functions/can_move)      [move()](functions/move)      [use_item()](functions/use_item)
