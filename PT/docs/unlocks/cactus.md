# Cacto
Como outras plantas, os [catos](objects/cactus) podem ser cultivados em solo e colhidos como de costume.

No entanto, eles vêm em vários tamanhos e têm um estranho sentido de ordem.

Se colheres um cato totalmente crescido e todos os catos vizinhos estiverem em ordem, ele também colherá todos os catos vizinhos recursivamente.

Um cato é considerado em ordem se todos os catos vizinhos a `North` e `East` estiverem totalmente crescidos e forem de tamanho igual ou maior, e todos os catos vizinhos a `South` e `West` estiverem totalmente crescidos e forem de tamanho igual ou menor.

A colheita só se espalhará se todos os catos adjacentes estiverem totalmente crescidos e em ordem.
Isto significa que se um quadrado de catos crescidos estiver ordenado por tamanho e tu colheres um cato, ele colherá o quadrado inteiro.

Um cato totalmente crescido aparecerá castanho se não estiver ordenado. Uma vez ordenado, voltará a ficar verde.

Receberás catos em quantidade igual ao número de catos colhidos ao quadrado. Portanto, se colheres `n` catos simultaneamente, receberás `n**2` `Items.Cactus`.

O tamanho de um cato pode ser medido com `measure()`.
É sempre um destes números: `0,1,2,3,4,5,6,7,8,9`.

Podes também passar uma direção para `measure(direction)` para medir o quadrado vizinho nessa direção do drone.

Podes trocar um cato com o seu vizinho em qualquer direção usando o comando `swap()`.
`swap(direction)` troca o objeto debaixo do drone com o objeto um quadrado na `direction` do drone.

## Exemplos
Em cada uma destas grelhas, todos os catos estão em ordem e a colheita espalhar-se-á por todo o campo:
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

Nesta grelha, apenas o cato inferior esquerdo está em ordem, o que não é suficiente para que se espalhe:
`1 5 3
4 9 7
3 3 2`

<spoiler=mostrar dica 1>
Se as linhas já estiverem ordenadas, ordenar as colunas não desordenará as linhas.
</spoiler>
<spoiler=mostrar dica 2>
Se não estás familiarizado com algoritmos de ordenação, talvez queiras pesquisá-los online e pensar em quais poderiam ser adaptados a este problema. Tem em mente que nem todos funcionam porque só podes trocar catos vizinhos.
</spoiler>