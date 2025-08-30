# Dinossauros
Dinossauros são criaturas antigas e majestosas que podem ser cultivadas para obter ossos antigos.

Infelizmente, os dinossauros foram extintos há muito tempo, então o melhor que podemos fazer agora é nos vestir como um.
Para este propósito, você recebeu o novo chapéu de dinossauro.

O chapéu pode ser equipado com
`change_hat(Hats.Dinosaur_Hat)`

Infelizmente, ele não se parece muito com o da propaganda...

Se você equipar o chapéu de dinossauro e tiver abóboras suficientes, uma [maçã](objects/apple) será automaticamente comprada e colocada debaixo do drone.
Quando o drone está sobre uma maçã e se move novamente, ele come a maçã e sua cauda cresce em um. Se você puder pagar, uma nova maçã será comprada e colocada em um local aleatório.
A maçã não pode surgir se outra coisa estiver plantada onde ela quer estar.

A cauda do dinossauro será arrastada atrás do drone, preenchendo as casas anteriores por onde o drone passou. Se um drone tentar se mover para cima da cauda, `move()` falhará e retornará `False`.
O último segmento da cauda sairá do caminho durante o movimento, então você pode se mover para cima dele. No entanto, se a cobra preencher toda a fazenda, você não conseguirá mais se mover. Então, você pode verificar se a cobra está totalmente crescida verificando se não consegue mais se mover.

Usar `measure()` em uma maçã retornará a posição da próxima maçã como um tuple.

`next_x, next_y = measure()`

Quando o chapéu é desequipado novamente, equipando um chapéu diferente, a cauda será colhida.
Você receberá ossos em quantidade igual ao comprimento da cauda ao quadrado. Então, para uma cauda de comprimento `n`, você receberá `n**2` `Items.Bone`.
Por Exemplo:
comprimento 1 => 1 osso
comprimento 2 => 4 ossos
comprimento 3 => 9 ossos
comprimento 4 => 16 ossos
comprimento 16 => 256 ossos
comprimento 100 => 10000 ossos

O Chapéu de Dinossauro é muito pesado, então se você o equipar, fará com que `move()` leve 400 ticks em vez de 200. No entanto, cada vez que você pega uma maçã, o número de ticks usados por `move()` é reduzido em 3% (arredondado para baixo), porque uma cauda mais longa pode ajudá-lo a se mover.

O loop a seguir imprime o número de ticks usados por `move()` após qualquer número de maçãs:

`ticks = 400
for i in range(100):
    print("ticks after ", i, " apples: ", ticks)
    ticks -= ticks * 0.03 // 1`

Você só tem um chapéu de dinossauro, então apenas um drone pode usá-lo.

<spoiler=mostrar dica 1>Se você continuar se movendo pelo mesmo caminho que cobre todo o campo, poderá facilmente obter uma cobra que cobre todo o campo todas as vezes. Não é muito eficiente, mas funciona.
Atravessar completamente uma fazenda muito grande pode levar muito tempo e você pode não precisar de tantos ossos. Sinta-se à vontade para usar `set_world_size()` para alterar o tamanho da fazenda para algo mais conveniente.</spoiler>