# Citrouilles
Les [citrouilles](objects/pumpkin) poussent comme des carottes sur un sol labouré. Les planter coûte des carottes.

Lorsque toutes les citrouilles d'un carré sont entièrement développées, elles fusionnent pour former une citrouille géante. Malheureusement, les citrouilles ont 20% de chances de mourir une fois qu'elles sont complètement développées, vous devrez donc replanter celles qui sont mortes si vous voulez qu'elles fusionnent.

Quand une citrouille meurt, elle laisse derrière elle une citrouille morte qui ne donnera rien lors de la récolte. Planter une nouvelle plante à sa place supprime automatiquement la citrouille morte, il n'est donc pas nécessaire de la récolter. `can_harvest()` retourne toujours `False` sur les citrouilles mortes.

Le rendement d'une citrouille géante dépend de sa taille.

Une citrouille de 1x1 rapporte `1*1*1 = 1` citrouilles.
Une citrouille de 2x2 rapporte `2*2*2 = 8` citrouilles au lieu de `4`.
Une citrouille de 3x3 rapporte `3*3*3 = 27` citrouilles au lieu de `9`.
Une citrouille de 4x4 rapporte `4*4*4 = 64` citrouilles au lieu de `16`.
Une citrouille de 5x5 rapporte `5*5*5 = 125` citrouilles au lieu de `25`.
Une citrouille de `n`x`n` rapporte `n*n*6` citrouilles pour `n >= 6`.

C'est une bonne idée d'obtenir des citrouilles d'au moins 6x6 pour obtenir le multiplicateur complet.

Cela signifie que même si vous plantez une citrouille sur chaque case d'un carré, l'une des citrouilles peut mourir et empêcher la méga-citrouille de pousser.