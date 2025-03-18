# Cacto
Como outras plantas, [cactos](objects/cactus) podem ser cultivados na terra e colhidos normalmente.

No entanto, eles vêm em vários tamanhos e têm um estranho senso de ordem.

Se você colher um cacto totalmente crescido e todos os cactos vizinhos estiverem em ordem, ele também irá colher todos os cactos vizinhos de forma recursiva.

Um cacto é considerado em ordem se todos os cactos vizinhos ao `North` e `East` estiverem totalmente crescidos e forem maiores ou iguais em tamanho e todos os cactos vizinhos ao `South` e `West` estiverem totalmente crescidos e forem menores ou iguais em tamanho.

A colheita só se espalha se todos os cactos adjacentes estiverem totalmente crescidos e em ordem. Isso significa que se um quadrado de cactos crescidos estiver ordenado por tamanho e você colher um cacto, ele irá colher o quadrado inteiro.

Você receberá cactos igual ao número de cactos colhidos ao quadrado. Então, se você colher `n` cactos simultaneamente, você receberá `n**2` `Items.Cactus`.

O tamanho de um cacto pode ser medido com `measure()`.
Ele sempre será um destes números: `0,1,2,3,4,5,6,7,8,9`.

Você também pode passar uma direção para `measure(direction)` para medir o azulejo vizinho naquela direção do drone.

Você pode trocar um cacto com seu vizinho em qualquer direção usando o comando `swap()`. `swap(direction)` troca o objeto sob o drone com o objeto uma casa na `direction` do drone.

## Exemplos
Em cada uma dessas grades, todos os cactos estão em ordem e a colheita se espalhará por todo o campo:
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

Nesta grade, apenas o cacto no canto inferior esquerdo está em ordem, o que não é suficiente para se espalhar:
`1 5 3
4 9 7
3 3 2`

<spoiler=mostrar dica 1>
Se cada coluna e cada linha do campo estiverem ordenadas, então o campo inteiro está ordenado.
</spoiler>
<spoiler=mostrar dica 2>
Se você não estiver familiarizado com algoritmos de ordenação, pode querer pesquisá-los online e pensar em quais poderiam ser adaptados para este problema.
</spoiler>