# Citrouilles
[Citrouilles](objects/pumpkin) poussent comme des carottes sur un sol labouré. Les planter coûte des carottes.

Quand toutes les citrouilles dans un carré sont complètement mûres, elles se regroupent pour former une citrouille géante. Malheureusement, les citrouilles ont 20% de chances de mourir une fois mûres, donc tu devras replanter celles qui sont mortes si tu veux qu'elles fusionnent.

Le rendement d'une citrouille géante dépend de sa taille.

Une citrouille de 1x1 donne `1*1*1 = 1` citrouille.
Une citrouille de 2x2 donne `2*2*2 = 8` citrouilles au lieu de `4`.
Une citrouille de 3x3 donne `3*3*3 = 27` citrouilles au lieu de `9`.
Une citrouille de 4x4 donne `4*4*4 = 64` citrouilles au lieu de `16`.
Une citrouille de `n`x`n` donne `n*n*5` citrouilles pour `n >= 5`.

C’est une bonne idée d’avoir des citrouilles d’au moins 5x5 en taille pour obtenir le multiplicateur complet.

Cela signifie que même si tu plantes une citrouille sur chaque case d'un carré, une des citrouilles peut mourir et empêcher la méga citrouille de pousser.