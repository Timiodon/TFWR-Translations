# Zucche
Le [zucche](objects/pumpkin) crescono come le carote sul terreno arato. Piantarle costa carote.

Quando tutte le zucche in un quadrato sono completamente cresciute, cresceranno insieme per formare una zucca gigante. Sfortunatamente, le zucche hanno il 20% di possibilità di morire una volta che sono completamente cresciute, quindi dovrai ripiantare quelle morte se vuoi che si uniscano.

Quando una zucca muore, lascia dietro di sé una zucca morta che non rilascerà nulla quando raccolta. Piantare una nuova pianta al suo posto rimuove automaticamente la zucca morta, quindi non c'è bisogno di raccoglierla. `can_harvest()` restituisce sempre `False` sulle zucche morte.

La resa di una zucca gigante dipende dalla sua dimensione.

Una zucca 1x1 produce `1*1*1 = 1` zucca.
Una zucca 2x2 produce `2*2*2 = 8` zucche invece di `4`.
Una zucca 3x3 produce `3*3*3 = 27` zucche invece di `9`.
Una zucca 4x4 produce `4*4*4 = 64` zucche invece di `16`.
Una zucca 5x5 produce `5*5*5 = 125` zucche invece di `25`.
Una zucca `n`x`n` produce `n*n*6` zucche per `n >= 6`.

È una buona idea ottenere zucche di dimensioni almeno 6x6 per ottenere il moltiplicatore completo.

Questo significa che anche se pianti una zucca su ogni casella di un quadrato, una delle zucche potrebbe morire e impedire alla mega zucca di crescere.
