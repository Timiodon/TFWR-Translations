# Labirinti
`Items.Weird_Substance`, che si ottiene [concimando](docs/unlocks/fertilizer.md) le piante, ha un effetto strano sui cespugli. Se il drone si trova sopra un cespuglio e chiami `use_item(Items.Weird_Substance, amount)`, il cespuglio crescerà trasformandosi in un labirinto di siepi. La dimensione del labirinto dipende dalla quantità di `Items.Weird_Substance` utilizzata (il secondo argomento della chiamata `use_item()`). Senza miglioramenti del labirinto, utilizzando `n` `Items.Weird_Substance`, ottieni un labirinto `n`x`n`. Per ogni livello di miglioramento del labirinto, devi usare un ulteriore `n` `Items.Weird_Substance` per ottenere lo stesso effetto. Quindi, per creare un labirinto a campo pieno:

`plant(Entities.Bush)
n_substance = get_world_size() * num_unlocked(Unlocks.Mazes)
use_item(Items.Weird_Substance, n_substance)`

Per qualche motivo, il drone non può volare sopra le siepi, anche se non sembrano così alte.

C'è un tesoro nascosto da qualche parte nel labirinto. Usa `harvest()` sul tesoro per ricevere oro pari all'area del labirinto. (Ad esempio, un labirinto 5x5 darà 25 oro.)

Se usi `harvest()` in un altro punto, il labirinto scomparirà semplicemente.

`get_entity_type()` è uguale a `Entities.Treasure` se il drone è sopra il tesoro e `Entities.Hedge` ovunque nel labirinto.

I labirinti non contengono loop a meno che non riutilizzi il labirinto (vedi sotto come riutilizzare un labirinto). Quindi non c'è modo che il drone finisca nella stessa posizione senza tornare indietro.

Puoi controllare se c'è un muro cercando di attraversarlo. `move()` restituisce `True` se ha successo e `False` altrimenti.

Se non hai idea di come raggiungere il tesoro, dai un'occhiata al Suggerimento 1. Ti mostra come affrontare un problema come questo.

Per una sfida extra, puoi anche riutilizzare il labirinto usando di nuovo la stessa quantità di `Items.Weird_Substance` sul tesoro. Questo aumenterà la quantità d'oro nel tesoro di un intero labirinto e lo sposterà in una posizione casuale nel labirinto.

Usare `measure()` su un tesoro restituisce la posizione a cui si sposterà, come una tupla. `next_x, next_y = measure()`

Ogni volta che il tesoro viene spostato, potrebbe essere rimossa una parete casuale dal labirinto. Quindi i labirinti riutilizzati possono contenere loop.

Nota che i loop nel labirinto lo rendono molto più difficile perché significa che puoi tornare alla stessa posizione senza tornare indietro. Riutilizzare un labirinto non ti dà più oro rispetto a raccoglierlo e crearne uno nuovo. Questa è una sfida extra al 100% che puoi semplicemente saltare. Vale la pena solo se le informazioni aggiuntive e le scorciatoie ti aiutano a risolvere il labirinto più velocemente.

Lo stesso labirinto può essere risolto un massimo di 300 volte. Questo corrisponde a 299 rilocazioni. Dopo di ciò, l'uso della sostanza strana sul tesoro non aumenterà più l'oro in esso e `measure()` restituirà `None`.

<spoiler=mostra suggerimento 1>Ecco un approccio generale per risolvere il problema:

Crea un labirinto e immagina di essere il drone.

Pensa a come cercheresti di trovare il tesoro se fossi nel labirinto.

Scrivi la tua strategia passo dopo passo in modo che qualcun altro possa seguirla senza pensare.

Ora prova a tradurre i tuoi passaggi in codice.
</spoiler>
<spoiler=mostra suggerimento 2>Finché non ci sono loop: Tutte le pareti sono davvero un solo grande muro connesso. Se segui la parete, ti condurrà attraverso tutto il labirinto.
Questo approccio richiede pochissimo codice e non è necessario tenere traccia di dove sei già stato. Circa 10 righe di codice sono tutto ciò di cui hai bisogno.</spoiler>
<spoiler=mostra suggerimento 3>Invece di muovere il drone in direzioni assolute come est o ovest, può essere molto utile muovere il drone in direzioni relative come "gira a destra" o "gira a sinistra". Per fare questo, devi tener traccia di quale direzione sta attualmente muovendo il drone. Il drone in realtà non ruota mai, ma puoi comunque mantenere una rotazione "virtuale" nel codice. Il seguente trucco dell'indice è utile per questo:

`directions = [North, East, South, West]
index = 0`

Usa `% 4` per permettere di ruotare "intorno al cerchio", in modo che dopo `West` ritorni a `North`.
`# gira a destra
index = (index + 1) % 4`

`# gira a sinistra
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=mostra suggerimento 4>Se non riesci a risolverlo, puoi sempre facilitarti la vita e farlo in modo meno efficiente.
Risolvere un labirinto `1`x`1` è banale.</spoiler>