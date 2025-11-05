# Labirinti
`Items.Weird_Substance`, che si ottiene [fertilizzando](docs/unlocks/fertilizer.md) le piante, ha uno strano effetto sui cespugli. Se il drone si trova su un cespuglio e chiami `use_item(Items.Weird_Substance, amount)`, il cespuglio si trasformerà in un labirinto di siepi.
La dimensione del labirinto dipende dalla quantità di `Items.Weird_Substance` utilizzata (il secondo argomento della chiamata `use_item()`).
Senza i potenziamenti del labirinto, l'uso di `n` `Items.Weird_Substance` risulterà in un labirinto `n`x`n`. Ogni livello di potenziamento del labirinto raddoppia il tesoro, ma raddoppia anche la quantità di `Items.Weird_Substance` necessaria. 
Quindi per creare un labirinto a campo intero:

`plant(Entities.Bush)
substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)`


Per qualche motivo il drone non può volare sopra le siepi, anche se non sembrano così alte.

C'è un tesoro nascosto da qualche parte nella siepe. Usa `harvest()` sul tesoro per ricevere oro pari all'area del labirinto. (Ad esempio, un labirinto 5x5 darà 25 oro.)

Se usi `harvest()` in qualsiasi altro punto, il labirinto semplicemente scomparirà.

`get_entity_type()` è uguale a `Entities.Treasure` se il drone si trova sopra il tesoro e `Entities.Hedge` in ogni altro punto del labirinto.

I labirinti non contengono cicli a meno che non riutilizzi il labirinto (vedi sotto come riutilizzare un labirinto). Quindi non c'è modo per il drone di finire di nuovo nella stessa posizione senza tornare indietro.

Puoi controllare se c'è un muro provando a passarci attraverso. 
`move()` restituisce `True` se ha avuto successo e `False` altrimenti.

`can_move()` può essere usato per controllare se c'è un muro senza muoversi.

Se non hai idea di come arrivare al tesoro, dai un'occhiata al Suggerimento 1. Ti mostra come affrontare un problema del genere.

Usare `measure()` in qualsiasi punto del labirinto restituisce la posizione del tesoro.
`x, y = measure()`

Per una sfida extra puoi anche riutilizzare il labirinto usando di nuovo la stessa quantità di `Items.Weird_Substance` sul tesoro. 
Questo aumenterà la quantità di oro nel tesoro di un intero labirinto e lo sposterà in una posizione casuale nel labirinto.
Solo i labirinti di dimensioni 8x8 o superiori possono essere riutilizzati.

Ogni volta che il tesoro viene spostato, alcune delle pareti del labirinto possono essere rimosse casualmente. Quindi i labirinti riutilizzati possono contenere cicli.

Nota che i cicli nel labirinto lo rendono molto più difficile perché significa che puoi arrivare di nuovo alla stessa posizione senza tornare indietro.
Riutilizzare un labirinto non ti dà più oro che semplicemente raccogliere e creare un nuovo labirinto.
Questa è al 100% una sfida extra che puoi semplicemente saltare.
Vale la pena solo se le informazioni extra e le scorciatoie ti aiutano a risolvere il labirinto più velocemente.

Il tesoro può essere riposizionato fino a 300 volte. Dopodiché, usare la sostanza strana sul tesoro non aumenterà più l'oro al suo interno e non si sposterà più.

<spoiler=mostra suggerimento 1>Ecco un approccio generale per risolvere il problema:

Crea un labirinto e immagina di essere il drone.

Pensa a come cercheresti di trovare il tesoro se fossi nel labirinto.

Scrivi la tua strategia passo dopo passo in modo che qualcun altro possa seguirla senza pensare.

Ora prova a tradurre i tuoi passi in codice.
</spoiler>
<spoiler=mostra suggerimento 2>Finché non ci sono cicli: tutti i muri sono in realtà un unico grande muro connesso. Se segui il muro, ti condurrà attraverso l'intero labirinto.
Questo approccio richiede pochissimo codice e non è necessario tenere traccia di dove sei già stato. Bastano circa 10 righe di codice.</spoiler>
<spoiler=mostra suggerimento 3>Invece di muovere il drone in direzioni assolute come est o ovest, può essere molto utile muovere il drone in direzioni relative come "gira a destra" o "gira a sinistra". Per fare ciò, devi tenere traccia della direzione in cui il drone si sta attualmente muovendo. Il drone non ruota mai effettivamente, ma puoi comunque mantenere una rotazione "virtuale" nel codice.
Il seguente trucco con l'indice è utile per questo:

`directions = [North, East, South, West]
index = 0`

Usa `% 4` per permettergli di ruotare "intorno al cerchio", in modo che dopo `West` torni a `North`.
`# gira a destra
index = (index + 1) % 4`

`# gira a sinistra
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=mostra suggerimento 4>Se non riesci a risolverlo, puoi sempre semplificarti la vita e farlo in modo meno efficiente. 
Risolvere un labirinto `1`x`1` è banale.</spoiler>