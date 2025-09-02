# Girasoli
I [girasoli](objects/sunflower) raccolgono l'energia del sole. Puoi raccogliere quell'energia. 

Piantarli funziona esattamente come piantare carote o zucche. 

La raccolta di un girasole cresciuto produce energia.
Se ci sono almeno 10 girasoli nella fattoria e raccogli quello con il maggior numero di petali, ottieni `5` volte più energia!

`measure()` restituisce il numero di petali del girasole sotto il drone.
I girasoli hanno almeno `7` e al massimo `15` petali.
Possono essere misurati anche prima di essere completamente cresciuti.

Diversi girasoli possono avere lo stesso numero di petali, quindi possono esserci anche diversi girasoli con il maggior numero di petali. In questo caso, non importa quale di essi raccogli.

Finché hai energia, il drone la userà per andare due volte più veloce. 
Consuma 1 energia ogni 30 azioni (come movimenti, raccolti, piantagioni...)
Anche l'esecuzione di altre istruzioni di codice può usare energia, ma molta meno delle azioni del drone.

In generale, tutto ciò che è accelerato dai potenziamenti di velocità è anche accelerato dall'energia.
Qualsiasi cosa accelerata dall'energia consuma anche energia in proporzione al tempo necessario per eseguirla, ignorando i potenziamenti di velocità.
