# Mega Farm
Questo incredibile potenziamento aumenta notevolmente la dimensione della fattoria e ti dà accesso a più droni.

Per semplificare le cose, ricevi sempre esattamente 36 nuove tessere per ogni nuovo drone. Il rapporto tra droni e tessere rimane costante.

## Più Droni
Come prima, inizi ancora con un solo drone. I droni aggiuntivi devono essere prima generati e scompariranno dopo la fine del programma. Ogni drone esegue la propria istanza di programma separata. I droni possono generare nuovi droni usando
`new_drone_id = spawn_drone("filename")`

Questo genera un nuovo drone nella stessa posizione del drone che ha eseguito il comando `spawn_drone("filename")`. Il nuovo drone inizierà a eseguire il programma nel file chiamato `filename`, quindi sostituisci `"filename"` con il nome del file che vuoi eseguire.

Puoi pensarlo come se avessi detto al tuo drone di andare al file chiamato `filename` e cliccare sul pulsante di esecuzione per il prossimo drone.

I droni non collidono tra loro.

Usa `max_drones()` per ottenere il numero massimo di droni che possono essere generati.
Usa `num_drones()` per ottenere il numero di droni già presenti nella fattoria.
Usa `get_drone_id()` per scoprire quale drone sta eseguendo il codice.

Esempio:

In un file chiamato `farming routine`:
`if get_drone_id() == 0:
    # Solo il primo drone eseguirà questo
    while num_drones() < max_drones():
        spawn_drone("farming routine")
        move(East)`

while True:
    if can_harvest():
        harvest()
    move(North)`

Questo farà sì che il tuo primo drone si muova orizzontalmente e generi più droni. I droni generati si muoveranno poi verticalmente e raccoglieranno tutto sul loro cammino.

<spoiler=mostra suggerimento>Il modo più semplice per usare più droni è dividere la tua fattoria tra loro. Gli upgrade sono progettati in modo tale che ogni drone possa sempre avere un campo di 6x6.
</spoiler>

### Tutto ciò che segue è piuttosto avanzato e non è necessario per la coltivazione di base

## Condizioni di Gara
Molti droni possono interagire con la stessa tessera della fattoria nello stesso momento. Se due droni interagiscono con la stessa tessera durante lo stesso tick, l'azione del drone con l'ID più basso avverrà per prima.

Ad esempio, immagina che i droni `0` e `1` siano entrambi sopra lo stesso albero che è quasi completamente cresciuto.
Il drone `0` chiama
`use_item(Items.Fertilizer)`
Il drone `1` chiama
`harvest()`

Se queste azioni avvengono contemporaneamente, l'albero verrà prima fertilizzato e poi raccolto. In tal caso, riceverai legno da esso. Tuttavia, se il drone `1` è leggermente più veloce, l'albero verrà raccolto prima di essere fertilizzato e non riceverai il legno.
Ciò si chiama "condizione di gara". È un problema comune nella programmazione parallela, dove il risultato dipende dall'ordine in cui le operazioni vengono eseguite.

Ecco un'altra situazione problematica che può verificarsi quando più droni eseguono lo stesso codice contemporaneamente nella stessa posizione.
`if get_water() < 0.5:
    use_item(Items.Water)`

Se più droni eseguono questo contemporaneamente, eseguiranno tutti la prima riga, entrando nel blocco `if`. Poi, useranno tutti l'acqua, sprecandone molta.
Quando un drone raggiunge la seconda riga, `get_water()` potrebbe non essere più inferiore a `0.5` perché un altro drone ha irrigato la tessera nel frattempo.

## Comunicazione tra Droni
Se sei interessato a strategie più avanzate, potresti volere che i tuoi droni comunichino tra loro usando le funzioni di passaggio dei messaggi.

Invia un qualsiasi valore a un altro drone:
`send(data, receiver_drone_id)`

Ricevi il prossimo valore inviato da qualsiasi drone:
`data = receive()`

Ricevi il prossimo valore inviato da un drone specifico:
`data = receive(sender_drone_id)`

Il tempo di esecuzione di `send()` dipende dalla dimensione dei dati inviati. Ad esempio, l'invio di un grande dizionario richiede una copia, che può richiedere del tempo.

`receive()` non aspetta l'arrivo di un messaggio. Se non è ancora stato inviato un messaggio, restituirà `None`.

Puoi costruire una funzione che attenda un messaggio in questo modo:
`def blocking_receive(sender_drone_id = -1):
    while True:
        data = receive(sender_drone_id)
        if data != None:
            return data`

Una applicazione utile del passaggio dei messaggi è avere una funzione che genera un drone e gli invia una funzione da eseguire.
In un file chiamato `drone_spawning`:
`def run_on_new_drone(f):
    id = spawn_drone("drone_spawning")
    send(f, id)

if __name__ == "__main__":
    f = blocking_receive()
    f()`

Inviare funzioni in questo modo può essere molto lento perché tutto lo stato catturato della funzione, comprese tutte le variabili globali, deve essere copiato.