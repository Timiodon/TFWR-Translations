# Import
Mettere tutto il codice in un unico file diventa rapidamente ingestibile. 
Le istruzioni `import` ti permettono di importare funzioni e variabili globali da un altro file.
Come funziona in un'immagine:
![](ImportsInOnePicture400)

Qui `import module2` esegue il file chiamato `module2` e ti dà accesso a tutte le sue variabili globali.
Puoi quindi accedere a variabili e funzioni all'interno del modulo importato usando l'operatore `.`.
Quindi in questo esempio, `module2.print_x()` chiama `print_x()` in `module2`.

### Non è necessario leggere oltre

Puoi anche spostare le variabili globali dal modulo importato nello scope corrente dove viene eseguita l'istruzione di import, usando la sintassi `from`.

`from module2 import print_x
print_x()`
Importa solo le variabili globali specificate da `module2`.

o

`from module2 import *
print_x()`
Importa tutte le variabili globali da `module2`.

Anche questo importa il file `module2`, ma invece di accedervi tramite una variabile chiamata `module2`, spacchetta le variabili globali da `module2` e le assegna direttamente nello scope locale.

Questa forma di import di solito non è raccomandata perché non funziona bene quando due file si importano a vicenda, e potresti sovrascrivere accidentalmente delle variabili nel file che importa a causa di conflitti di nomi. È più sicuro evitare la sintassi `from` se non sai cosa stai facendo.

# Come funziona veramente

## TL;DR
Gli import possono essere poco intuitivi, ma la maggior parte dei problemi può essere evitata attenendosi alla sintassi `import file` invece di `from file import`, e racchiudendo tutto ciò che non è una definizione globale in
`if __name__ == "__main__":`

## Effetti Collaterali dell'Import
La prima volta che importi un file, questo eseguirà l'intero file e poi ti darà accesso a tutte le variabili che sono state definite durante l'esecuzione.
Se importi di nuovo lo stesso file, restituirà semplicemente il modulo memorizzato nella cache dalla prima volta.

Questo significa che le istruzioni di import possono avere effetti collaterali. Se importi un file che chiama `harvest()`, eseguirà effettivamente la raccolta durante l'import. Ma quando lo importi di nuovo, non raccoglierà di nuovo perché il file viene eseguito solo una volta.

C'è un modo per evitare tali effetti collaterali usando la variabile `__name__`. Questa è una variabile che viene impostata automaticamente a `"__main__"` quando un file viene eseguito direttamente, e al nome del file quando un file viene eseguito tramite `import`.
È considerata una buona pratica mettere qualsiasi codice che non vuoi eseguire quando il file viene importato all'interno di un blocco `if __name__ == "__main__":`.

Una struttura di file comune in Python è mettere il codice che deve essere eseguito quando il file viene avviato in una funzione `main()`. In questo modo hai una chiara distinzione tra le variabili locali (definite all'interno di `main()`) e le variabili globali che possono essere importate (definite al di fuori di `main()`).

`a_global_variable = "global"

def main():
    a_local_variable = "local"
    # fai delle cose

if __name__ == "__main__":
    main()`

## Cicli di Importazione
Cosa succede se il file `a` importa il file `b` e il file `b` importa il file `a`?

file `a`:
`import b
x = 0`

file `b`:
`import a
def f():
    print(a.x)`

Questo funzionerà senza problemi. Diciamo che nessuno dei due file è ancora stato caricato, e qualcun altro esegue `import a`.

-`a` viene eseguito fino alla riga `import b`.
-`b` viene eseguito fino alla riga `import a`.
-Il modulo `a` esiste già, ma non contiene `x` perché ha raggiunto solo la riga `import b`.
-`b` memorizza un riferimento al modulo `a` parzialmente caricato in una variabile chiamata `a`.
-`b` esegue l'istruzione `def` e memorizza la funzione `f()`.
-`a` continua l'esecuzione e inizializza `x`.

Quando qualcuno chiama `b.f()`, stamperà correttamente `0` perché il modulo `a` a cui `b` ha un riferimento è ora completamente caricato.

Ora considera lo stesso codice usando la sintassi `from`.

file `a`:
`from b import *
x = 0`

file `b`:
`from a import *
def f():
    print(x)`

-`a` viene eseguito fino alla riga `from b import *`.
-`b` viene eseguito fino alla riga `from a import *`.
-Il modulo `a` esiste già, ma non è stato ancora completamente eseguito.
-`b` spacchetta tutto ciò che è attualmente in `a` nel proprio scope globale. A questo punto, `a` non contiene nulla perché non ha ancora raggiunto la riga `x = 0`, quindi non viene importato nulla.
-`b` esegue l'istruzione `def` e memorizza la funzione `f()`.
-`a` continua l'esecuzione e inizializza `x`.

Se qualcuno ora chiama `b.f()`, riceverà un errore che `x` non esiste nello scope corrente. Questo perché questa volta `b` non ha un riferimento ad `a` che si sta ancora caricando e non vede le definizioni che sono state aggiunte dopo l'importazione.