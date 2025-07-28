# Dinossauros
Os dinossauros são criaturas antigas e majestosas que podem ser cultivadas para obter ossos antigos.

Infelizmente, os dinossauros foram extintos há muito tempo, por isso o melhor que podemos fazer agora é vestir-nos como um.
Para este propósito, recebeste o novo chapéu de dinossauro.

O chapéu pode ser equipado com
`change_hat(Hats.Dinosaur_Hat)`

Infelizmente, não se parece bem com o do anúncio...

Se equipares o chapéu de dinossauro e tiveres abóboras suficientes, uma [maçã](objects/apple) será automaticamente comprada e colocada debaixo do drone.
Quando o drone está sobre uma maçã e se move novamente, ele come a maçã e a sua cauda cresce em um. Se puderes pagar, uma nova maçã será comprada e colocada numa localização aleatória.
A maçã não pode aparecer se outra coisa estiver plantada onde ela quer estar.

A cauda do dinossauro será arrastada atrás do drone, preenchendo os quadrados anteriores por onde o drone se moveu. Se um drone tentar mover-se para cima da cauda, `move()` falhará e retornará `False`.
O último segmento da cauda sairá do caminho durante o movimento, para que possas mover-te para cima dele. No entanto, se a cobra preencher toda a quinta, não poderás mais mover-te. Portanto, podes verificar se a cobra está totalmente crescida, verificando se não te podes mais mover.

Usar `measure()` numa maçã retornará a posição da próxima maçã como um tuple.

`next_x, next_y = measure()`

Quando o chapéu é desequipado novamente, equipando um chapéu diferente, a cauda será colhida.
Receberás ossos em quantidade igual ao comprimento da cauda ao quadrado. Assim, para uma cauda de comprimento `n`, receberás `n**2` `Items.Bone`.
Por Exemplo:
comprimento 1 => 1 osso
comprimento 2 => 4 ossos
comprimento 3 => 9 ossos
comprimento 4 => 16 ossos
comprimento 16 => 256 ossos
comprimento 100 => 10000 ossos

O Chapéu de Dinossauro é muito pesado, por isso, se o equipares, fará com que `move()` leve 800 ticks em vez de 200. No entanto, cada vez que apanhas uma maçã, o número de ticks usados por `move()` é reduzido em 3% (arredondado para baixo), porque uma cauda mais longa pode ajudar-te a mover.

O loop seguinte imprime o número de ticks usados por `move()` após qualquer número de maçãs:

`ticks = 800
for i in range(100):
    print("ticks após ", i, " maçãs: ", ticks)
    ticks -= ticks * 0.03 // 1`

<spoiler=mostrar dica 1>Se continuares a mover-te pelo mesmo caminho que cobre todo o campo, podes facilmente obter uma cobra que cobre todo o campo sempre, porque cobrirás todos os espaços livres antes de voltares para onde está a tua cauda. Não é muito eficiente, mas funciona.
Campos de tamanho ímpar podem ser mais difíceis. Se tiveres `Unlocks.Debug2` desbloqueado, podes mudar o tamanho do campo para algo mais conveniente.</spoiler>