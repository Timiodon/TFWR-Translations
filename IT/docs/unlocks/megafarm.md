# Mega Farm
Questo sblocco incredibilmente potente ti dà accesso a più droni.

Come prima, inizi sempre con un solo drone. I droni aggiuntivi devono prima essere creati e scompariranno al termine del programma.
Ogni drone esegue il proprio programma separato. Nuovi droni possono essere creati usando la funzione `spawn_drone(function)`.

`def drone_function():
    move(North)
    do_a_flip()

spawn_drone(drone_function)`

Questo crea un nuovo drone nella stessa posizione del drone che ha eseguito il comando `spawn_drone(function)`. Il nuovo drone inizia quindi a eseguire la funzione specificata. Una volta terminato, scomparirà automaticamente.

I droni non si scontrano tra loro.

Usa `max_drones()` per ottenere il numero massimo di droni che possono essere creati.
Usa `num_drones()` per ottenere il numero di droni che sono già nella fattoria.


## Esempio:
`def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)`

Questo farà sì che il tuo primo drone si muova orizzontalmente e crei altri droni. I droni creati si muoveranno quindi verticalmente e raccoglieranno tutto ciò che si trova sul loro percorso.

Se tutti i droni disponibili sono già stati creati, `spawn_drone()` non farà nulla e restituirà `None`.

<spoiler=mostra suggerimento> Dai un'occhiata a questa utilissima funzione parallela `for_all`, che prende una qualsiasi funzione e la esegue su ogni casella della fattoria. Utilizza tutti i droni disponibili per farlo.

`def for_all(f):
	def row():
		for _ in range(get_world_size()-1):
			f()
			move(East)
		f()
	for _ in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(North)

for_all(harvest)`

Un pattern particolarmente utile è creare un drone se ce n'è uno disponibile, altrimenti fare il lavoro da soli.

`if not spawn_drone(task):
	task()`
</spoiler>

## Attendere un Altro Drone
Usa la funzione `wait_for(drone)` per attendere che un altro drone finisca. Ricevi l'handle `drone` quando crei il drone.
`wait_for(drone)` restituisce il valore di ritorno della funzione che l'altro drone stava eseguendo.

`def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

def zero_arg_wrapper():
    return get_entity_type_in_direction(North)
drone = spawn_drone(zero_arg_wrapper)
print(wait_for(drone))`

Nota che creare droni richiede tempo, quindi non è una buona idea creare un nuovo drone per ogni piccola cosa.

## Nessuna Memoria Condivisa
Ogni drone ha la sua memoria e non può leggere o scrivere direttamente le variabili globali di un altro drone.

`x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)`

Questo stamperà `0` perché il nuovo drone ha incrementato la propria copia della variabile globale `x`, il che non influisce sulla `x` del primo drone.

## Race Condition
Più droni possono interagire con la stessa casella della fattoria contemporaneamente. Se due droni interagiscono con la stessa casella durante lo stesso tick, entrambe le interazioni avverranno, ma i risultati potrebbero differire in base all'ordine delle interazioni.

Ad esempio, immagina che i droni `0` e `1` si trovino entrambi sopra lo stesso albero quasi completamente cresciuto.
Il drone `0` chiama
`use_item(Items.Fertilizer)`
Il drone `1` chiama
`harvest()`

Se queste azioni avvengono contemporaneamente, l'albero verrà prima fertilizzato e poi raccolto. In tal caso, riceverai del legno. Tuttavia, se il drone `1` è leggermente più veloce, l'albero verrà raccolto prima di essere fertilizzato e non riceverai il legno.
Questa è chiamata "race condition". È un problema comune nella programmazione parallela, in cui il risultato dipende dall'ordine in cui vengono eseguite le operazioni.

Ecco un'altra situazione problematica che può verificarsi quando più droni eseguono lo stesso codice simultaneamente nella stessa posizione.
`if get_water() < 0.5:
    use_item(Items.Water)`

Se più droni eseguono questo codice simultaneamente, eseguiranno tutti la prima riga, che li inserisce nel blocco `if`. Poi, useranno tutti l'acqua, sprecandone molta.
Quando un drone raggiunge la seconda riga, `get_water()` potrebbe non essere più inferiore a `0.5` perché un altro drone ha annaffiato la casella nel frattempo.