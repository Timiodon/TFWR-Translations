# La versione 1.0 è finalmente arrivata!
Dopo oltre tre anni e mezzo di sviluppo costante, più di 20 aggiornamenti e il vostro fantastico feedback, l'Accesso Anticipato è finalmente giunto al termine.

## Cosa c'è di nuovo nella 1.0?
- Droni multipli per massimizzare la tua agricoltura
- Un albero degli sblocchi rivisto con una progressione più esponenziale
- 60 achievement per mettere alla prova le tue abilità
- Sbloccare determinati achievement darà al tuo drone dei cappelli speciali
- Un comparto sonoro completamente rinnovato
- Una nuova traccia musicale
- Miglioramenti alla qualità della vita e varie correzioni
- Cambiamenti che rompono la compatibilità: i potenziamenti saranno parzialmente resettati. Riutilizzare i labirinti funziona in modo leggermente diverso.

Grazie mille a tutti per aver supportato The Farmer Was Replaced dall'Accesso Anticipato fino alla versione completa. 
Non vedo l'ora di vedere come userete i droni multipli in modi creativi e intelligenti!
-Timon

Inoltre, assicurati di unirti a noi su Discord: 
[Discord](https://discord.com/invite/kj33cJkeJn)

## Note della Patch Complete
Cambiamenti che rompono la compatibilità:
-A causa della revisione dell'albero tecnologico, i numeri dei potenziamenti dei vecchi salvataggi non saranno più validi. Il gioco resetterà tutti i potenziamenti a un livello ragionevole quando aprirai un vecchio salvataggio.
-Se stai riutilizzando i labirinti, ora devi prima riposizionare il tesoro e poi misurare la posizione, invece di misurare prima e poi riposizionare.

Gameplay:
-Aggiunti tooltip con informazioni utili quando passi il mouse sopra le caselle della fattoria.
-Usare `measure()` in qualsiasi punto del labirinto ora restituisce sempre la posizione del tesoro corrente. Non è più necessario misurare specificamente il tesoro.
-Ora c'è una funzione `can_move()` per il labirinto.
-Le zucche ora crescono fino a 6x6 invece che 5x5.
-Il comportamento di asciugatura del terreno è leggermente cambiato. Invece di asciugarsi dell'1% ogni 0.8-1.2 secondi, ogni casella di terreno ora ha una probabilità del 10% di asciugarsi ogni 0.1 secondi.
-Il tempo di crescita dei cactus è ora sempre esattamente di 1 secondo.
-Le zucche ora lasciano dietro di sé una zucca morta per indicare che sono morte.
-Aggiunta `pet_the_piggy()`.
-`num_unlocked()` ora viene sbloccato già con Sensi.

Audio:
-L'audio è stato completamente rifatto.
-Ora c'è la musica quando avvii il gioco!

Grafica:
-La grafica dell'albero tecnologico è stata completamente rivista.
-Il pannello dell'inventario nell'angolo in alto a sinistra dello schermo ora ha un bell'effetto visivo quando raccogli un oggetto.
-I cactus ora sono marroni quando non sono ordinati correttamente per renderlo più visibile.
-Le piante sono ora visibili subito dopo essere state piantate, anche se non sono ancora cresciute.

Editor del Codice:
-Facendo doppio clic su identificatori con underscore ora viene selezionato l'intero identificatore.
-Se l'opzione "tab in spazi" è disattivata, gli spazi di indentazione vengono ora convertiti in tab.
-Lo zoom è ora molto più fluido.
-Il completamento automatico del codice ora gestisce correttamente gli import e può dare suggerimenti da altri file.
-Aggiunti cursori diversi per la modifica del testo e il ridimensionamento delle finestre.
-I passi del debugger sono ora basati sulla riga di codice invece che sui tick di simulazione.

Altro:
-Ora puoi concatenare gli operatori di confronto come in Python.
-`get_cost(Entities.Hedge)` e `get_cost(Entities.Treasure)` ora restituiscono il costo di un labirinto 1x1.
-Aggiunta un'impostazione per la risoluzione.
-Aggiunta un'impostazione per disattivare le evidenziazioni lampeggianti quando il codice è in esecuzione.
-L'esecuzione del codice è stata ulteriormente ottimizzata, permettendo al gioco di girare più fluidamente mentre il codice è in esecuzione.
-Aggiunto un tasto per "Attiva/Disattiva HUD".

Correzioni:
-Risolti alcuni dei casi più comuni in cui le evidenziazioni del codice erano visibili attraverso altre finestre.
-Azioni come arare non possono più influenzare il comportamento di asciugatura dell'acqua.
-Risolti problemi di assegnazione dei tasti su tastiere non US.
-Risolto il problema del salvadanaio a porcellino che a volte si allontanava molto dalla fattoria.
-Risolto il fertilizzante che non infettava le piante completamente cresciute.
-Risolto `set_world_size(get_world_size())` che reimpostava la posizione del drone.
-Risolta un'interazione tra simulazione e dinosauro che causava l'abbandono di molte mele.
-Risolto il bug che faceva spostare i messaggi di errore quando si cliccava su minimizza e poi si apriva il menu.
-Risolto il problema dei messaggi di errore che apparivano mentre si stava ancora scrivendo.

Cambiamenti che rompono la compatibilità da patch precedenti che potresti esserti perso:
-Le funzioni definite in altri file (finestre nel gioco) non vengono più importate implicitamente. Ora devi sbloccare e usare istruzioni di import esplicite come in Python (Vedi lo sblocco import).
-`Items.Bones` è stato rinominato in `Items.Bone` così tutti gli oggetti sono al singolare.
-`Entities.Carrots` è stato rinominato in `Entities.Carrot` così tutte le entità sono al singolare.
-`Grounds.Turf` è stato rinominato in `Grounds.Grassland` per renderlo più facile da capire.
-`Items.Water_Tank` è stato rinominato in `Items.Water` perché la funzione di ricarica del serbatoio è stata rimossa.
-`Unlocks.Benchmark` è stato sostituito con `Unlocks.Timing`.
-`get_op_count()` è stato rinominato in `get_tick_count()`.
-`set_farm_size()` è stato rinominato in `set_world_size()` per essere coerente con `get_world_size()`.
-`get_companion()` ora restituisce una tupla della forma (entità, (x, y)) invece di una lista.
-`trade()` è stato rimosso dal gioco.