# Dinossauros
Dinossauros são criaturas antigas e majestosas que podem ser cultivadas para obter ossos antigos.

Infelizmente, os dinossauros foram extintos há muito tempo, então o melhor que podemos fazer agora é nos vestir como um. Para isso, você recebeu o novo chapéu de dinossauro.

O chapéu pode ser equipado com
`change_hat(Hats.Dinosaur_Hat)`

Infelizmente, ele não parece exatamente como no anúncio...

Se você equipar o chapéu de dinossauro e tiver abóboras suficientes, uma [apple](objects/apple) será automaticamente comprada e colocada sob o drone. Quando o drone estiver sobre uma maçã e se mover novamente, ele comerá a maçã e aumentará seu rabo em um segmento. Se você puder pagar, uma nova maçã será comprada e colocada em um local aleatório. A maçã não pode nascer se algo já estiver plantado onde ela deseja estar.

O rabo do dinossauro será arrastado atrás do drone, preenchendo os quadrados anteriores por onde o drone passou. Se um drone tentar se mover sobre o rabo `move()` falhará e retornará `False`. 
O último segmento do rabo sairá do caminho durante o movimento, assim você poderá se mover sobre ele. No entanto, se a cobra preencher toda a fazenda, você não poderá se mover mais. Então, você pode verificar se a cobra está totalmente crescida verificando se não consegue mais se mover.

Usar `measure()` em uma maçã retornará a posição da próxima maçã como uma tupla.

`next_x, next_y = measure()`

Quando o chapéu é desequipado ao equipar um chapéu diferente, o rabo será colhido.
Você receberá ossos equivalentes ao comprimento do rabo ao quadrado. Então, para um rabo de comprimento `n` você receberá `n**2` `Items.Bone`. 
Por exemplo:
comprimento 1 => 1 osso
comprimento 2 => 4 ossos
comprimento 3 => 9 ossos
comprimento 4 => 16 ossos
comprimento 16 => 256 ossos
comprimento 100 => 10000 ossos

O Chapéu de Dinossauro é muito pesado, então se você o equipar, fará com que `move()` leve 800 ticks em vez de 200. No entanto, cada vez que você pegar uma maçã, o número de ticks usado por `move()` será reduzido em 3% (arredondado para baixo), porque um rabo mais longo pode ajudar você a se mover.

O loop a seguir imprime o número de ticks usado por `move()` após qualquer número de maçãs:

`ticks = 800
for i in range(100):
    print("ticks após ", i, " maçãs: ", ticks)
    ticks -= ticks * 0.03 // 1`

<spoiler=mostrar dica 1>Se você continuar se movendo ao longo do mesmo caminho que cobre todo o campo, pode facilmente conseguir uma cobra que cobre todo o campo todas as vezes, porque você cobrirá cada espaço livre antes de voltar para onde está seu rabo. Não é muito eficiente, mas funciona. Campos ímpares podem ser mais difíceis. Se você tiver `Unlocks.Debug2` desbloqueado, pode alterar o tamanho do campo para algo mais conveniente.</spoiler>