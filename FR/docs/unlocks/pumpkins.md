# Citrouilles
[Citrouilles](objects/pumpkin) poussent comme des carottes sur un sol labouré. Les planter coûte des carottes.

Lorsque toutes les citrouilles d'un carré sont entièrement mûres, elles se regroupent pour former une citrouille géante. Malheureusement, les citrouilles ont 20% de chances de mourir une fois qu'elles sont complètement mûres, donc vous devrez replanter celles qui sont mortes si vous voulez qu'elles fusionnent.

Le rendement d'une citrouille géante dépend de la taille de la citrouille.

Une citrouille 1x1 donne `1*1*1 = 1` citrouilles.
Une citrouille 2x2 donne `2*2*2 = 8` citrouilles au lieu de `4`.
Une citrouille 3x3 donne `3*3*3 = 27` citrouilles au lieu de `9`.
Une citrouille 4x4 donne `4*4*4 = 64` citrouilles au lieu de `16`.
Une citrouille 5x5 donne `5*5*5 = 125` citrouilles au lieu de `25`.
Une citrouille `n`x`n` donne `n*n*6` citrouilles pour `n >= 6`.

C'est une bonne idée d'avoir des citrouilles d'une taille d'au moins 6x6 pour obtenir le multiplicateur complet.

Cela signifie que même si vous plantez une citrouille sur chaque parcelle d'un carré, l'une des citrouilles peut mourir et empêcher la citrouille géante de pousser.