# Girasoli
[Girasoli](objects/sunflower) raccolgono l'energia del sole. Puoi raccogliere quella potenza.

Piantare funziona esattamente come piantare carote o zucche.

La raccolta di un girasole maturo produce energia. Se ci sono almeno 10 girasoli nella fattoria e raccogli quello con il maggior numero di petali, ottieni `5` volte più energia!

`measure()` restituisce il numero di petali del girasole sotto il drone. I girasoli hanno almeno `7` e al massimo `15` petali. Possono essere già misurati prima di essere completamente cresciuti.

Diversi girasoli possono avere lo stesso numero di petali, quindi possono esserci anche diversi girasoli con il maggior numero di petali. In questo caso, non importa quale di loro raccogli.

Finché hai energia, il drone la userà per funzionare il doppio della velocità. Consuma 1 energia ogni 30 azioni (come mosse, raccolte, piantamenti...) L'esecuzione di altre istruzioni di codice può anche utilizzare energia ma molto meno rispetto alle azioni del drone.

In generale, tutto ciò che viene accelerato dagli upgrade di velocità viene accelerato anche dall'energia. Qualsiasi cosa velocizzata dall'energia utilizza anche energia in proporzione al tempo necessario per eseguirla, ignorando gli upgrade di velocità.