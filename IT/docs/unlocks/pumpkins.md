# Zucche
[Zucche](objects/pumpkin) crescono come le carote su terreno coltivato. Piantarle costa carote.

Quando tutte le zucche in un quadrato sono completamente cresciute, si uniranno per formare una zucca gigante. Sfortunatamente, le zucche hanno il 20% di probabilità di morire quando sono completamente cresciute, quindi dovrai ripiantare quelle morte se vuoi che si uniscano.

Il raccolto di una zucca gigante dipende dalla dimensione della zucca.

Una zucca 1x1 produce `1*1*1 = 1` zucche.
Una zucca 2x2 produce `2*2*2 = 8` zucche invece di `4`.
Una zucca 3x3 produce `3*3*3 = 27` zucche invece di `9`.
Una zucca 4x4 produce `4*4*4 = 64` zucche invece di `16`.
Una zucca 5x5 produce `5*5*5 = 125` zucche invece di `25`.
Una zucca `n`x`n` produce `n*n*6` zucche per `n >= 6`.

È una buona idea ottenere zucche di almeno 6x6 per ottenere il moltiplicatore completo.

Questo significa che anche se pianti una zucca su ogni casella di un quadrato, una delle zucche potrebbe morire e impedire la crescita della mega zucca.