# Labirinti
`Items.Weird_Substance`, che si ottiene [concimando](docs/unlocks/fertilizer.md) le piante, ha un effetto strano sui cespugli. Se il drone si trova sopra un cespuglio e chiami `use_item(Items.Weird_Substance, amount)`, il cespuglio crescerà trasformandosi in un labirinto di siepi. La dimensione del labirinto dipende dalla quantità di `Items.Weird_Substance` utilizzata (il secondo argomento della chiamata `use_item()`). Senza miglioramenti del labirinto, utilizzando `n` `Items.Weird_Substance`, ottieni un labirinto `n`x`n`. Ogni livello di miglioramento del labirinto raddoppia il tesoro, ma raddoppia anche la quantità di `Items.Weird_Substance` necessaria. Quindi, per creare un labirinto su tutto il campo:

`plant(Entities.Bush)
n_substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, n_substance)`

Per qualche motivo, il drone non può volare sopra le siepi, anche se non sembrano così alte.

C'è un tesoro nascosto da qualche parte nella siepe. Usa `harvest()` sul tesoro per ricevere oro pari all'area del labirinto. (Per esempio, un labirinto 5x5 frutterà 25 oro.)

Se usi `harvest()` in un altro punto, il labirinto semplicemente scomparirà.

`get_entity_type()` è uguale a `Entities.Treasure` se il drone si trova sopra il tesoro e a `Entities.Hedge` ovunque nel labirinto.

I labirinti non contengono loop a meno che non si riutilizzi il labirinto (vedi sotto come riutilizzare un labirinto). Quindi non c'è modo che il drone finisca nella stessa posizione senza tornare indietro.

Puoi verificare se c'è un muro provando a passarci attraverso. `move()` restituisce `True` se ha successo e `False` altrimenti.

Se non hai idea di come raggiungere il tesoro, dai un'occhiata al Suggerimento 1. Ti mostra come affrontare un problema di questo tipo.

Per una sfida extra, puoi anche riutilizzare il labirinto usando la stessa quantità di `Items.Weird_Substance` nuovamente sul tesoro. Questo aumenterà la quantità di oro nel tesoro di un intero labirinto e lo sposterà in una posizione casuale nel labirinto.

Usare `measure()` su un tesoro restituisce la posizione a cui verrà spostato, sotto forma di una tupla. 
`next_x, next_y = measure()`

Ogni volta che il tesoro viene spostato, un muro casuale potrebbe essere rimosso dal labirinto. Quindi i labirinti riutilizzati possono contenere loop.

Note che i loop nel labirinto lo rendono molto più difficile perché significa che puoi ritornare nella stessa posizione senza tornare indietro. Riutilizzare un labirinto non ti dà più oro rispetto a raccoglierlo e creare un nuovo labirinto. È al 100% una sfida extra che puoi semplicemente ignorare. Vale la pena solo se le informazioni extra e le scorciatoie ti aiutano a risolvere il labirinto più velocemente.

Lo stesso labirinto può essere risolto un massimo di 300 volte. Questo corrisponde a 299 rilocazioni. Dopo di ciò, usare la sostanza strana sul tesoro non aumenterà più l'oro in esso contenuto e `measure()` restituirà `None`.

<spoiler=mostra suggerimento 1>Ecco un approccio generale per risolvere il problema:

Crea un labirinto e immagina di essere il drone.

Pensa a come cercheresti di trovare il tesoro se fossi nel labirinto.

Scrivi la tua strategia passo dopo passo, così qualcun altro potrebbe seguirla senza pensarci.

Ora prova a tradurre i tuoi passi in codice.
</spoiler>
<spoiler=mostra suggerimento 2>Finché non ci sono loop: Tutti i muri sono in realtà un unico grande muro connesso. Se segui il muro, ti condurrà attraverso tutto il labirinto. Questo approccio richiede pochissimo codice e non devi tenere traccia di dove sei già stato. Circa 10 righe di codice sono tutto ciò di cui hai bisogno.</spoiler>
<spoiler=mostra suggerimento 3>Invece di muovere il drone in direzioni assolute come est o ovest, può essere molto utile muovere il drone in direzioni relative come "gira a destra" o "gira a sinistra". Per fare questo devi tenere traccia della direzione verso cui il drone si sta muovendo attualmente. Il drone in realtà non ruota mai, ma puoi ancora mantenere una "rotazione virtuale" nel codice.
Il seguente trucco dell'indice è utile per questo:

`directions = [North, East, South, West]
index = 0`

Usa `% 4` per permettergli di ruotare "attorno al cerchio", così che dopo `West` torni a `North`.
`# gira a destra
index = (index + 1) % 4`

`# gira a sinistra
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=mostra suggerimento 4>Se non riesci a risolverlo, puoi sempre facilitarti la vita e farlo in modo meno efficiente. Risolvere un labirinto `1`x`1` è banale. </spoiler>