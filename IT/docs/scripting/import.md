# Import
Mettere tutto il codice in un unico file diventa rapidamente ingestibile.
Le istruzioni `import` ti permettono di importare funzioni e variabili globali da un altro file.

`import nomefile`

Questa è la forma più semplice di istruzione di import. Ti darà accesso a tutto ciò che è definito nel file chiamato `nomefile`. Ogni finestra nel gioco è un file, e il nome del file è il nome visualizzato in cima alla finestra.

Ecco un esempio con due file:
File chiamato helper:
`x = 0

def say_hello():
    print("hello from helper")`

Un altro file:
`import helper
helper.say_hello()
helper.x += 1`

Qui `import helper` esegue il file chiamato `helper` e ti dà accesso a tutte le sue variabili globali.
Puoi quindi accedere a variabili e funzioni all'interno del modulo importato usando l'operatore `.`.
Quindi in questo esempio, `helper.say_hello()` chiama `say_hello()` all'interno di helper e l'ultima riga incrementa la variabile globale x.

Puoi anche spostare le variabili globali dal modulo importato nello scope corrente in cui viene eseguita l'istruzione di import usando la sintassi `from`.

`from helper import *`
Importa tutte le variabili globali da helper.

oppure

`from helper import say_hello`
Importa solo le variabili globali specificate da helper.

Questo importa anche il file helper, ma invece di accedervi tramite una variabile chiamata `helper`, scompatta le variabili globali da `helper` e le assegna direttamente nello scope locale.

`from helper import say_hello
say_hello()`

Questa forma di import di solito non è raccomandata perché non funziona bene quando due file si importano a vicenda, e potresti sovrascrivere accidentalmente variabili nel file che importa a causa di conflitti di nomi.

# Come funziona davvero

## Riassumendo
Gli import possono essere poco intuitivi, ma la maggior parte dei problemi può essere evitata attenendosi alla sintassi `import file` invece di `from file import`, e racchiudendo tutto ciò che non è una definizione globale in
`if __name__ == "__main__":`

## Effetti collaterali dell'import
La prima volta che importi un file, verrà eseguito l'intero file e poi ti verrà dato accesso a tutte le variabili che sono state definite durante l'esecuzione.
Se importi lo stesso file di nuovo, restituirà semplicemente il modulo memorizzato nella cache dalla prima volta.

Ciò significa che le istruzioni di import possono avere effetti collaterali. Se importi un file che chiama `harvest()`, raccoglierà effettivamente durante l'import. Ma quando lo importi di nuovo, non raccoglierà di nuovo perché il file viene eseguito solo una volta.

C'è un modo per evitare tali effetti collaterali usando la variabile `__name__`. Questa è una variabile che viene impostata automaticamente a `"__main__"` quando un file viene eseguito direttamente, e al nome del file quando un file viene eseguito tramite `import`.
È considerata una buona pratica mettere qualsiasi codice che non vuoi che venga eseguito quando il file viene importato all'interno di un blocco `if __name__ == "__main__":`.

Una struttura di file comune in Python è mettere il codice che dovrebbe essere eseguito quando il file viene eseguito in una funzione `main()`. In questo modo hai una chiara distinzione tra variabili locali (definite all'interno di `main()`) e variabili globali che possono essere importate (definite al di fuori di `main()`).

`a_global_variable = "global"

def main():
    a_local_variable = "local"
    # fai cose

if __name__ == "__main__":
    main()`

## Cicli di importazione
Cosa succede se il file `a` importa il file `b` e il file `b` importa il file `a`?

file `a`:
`import b
x = 0`

file `b`:
`import a
def f():
    print(a.x)`

Questo funzionerà bene. Supponiamo che nessuno dei due file sia ancora stato caricato, e qualcun altro esegua `import a`.

-`a` viene eseguito fino alla riga `import b`.
-`b` viene eseguito fino alla riga `import a`.
-Il modulo `a` esiste già, ma non contiene `x` perché ha raggiunto solo la riga `import b`.
-`b` memorizza un riferimento al modulo `a` parzialmente caricato in una variabile chiamata `a`.
-`b` esegue l'istruzione `def` e memorizza la funzione `f()`.
-`a` continua l'esecuzione e inizializza `x`.

Quando qualcuno chiama `b.f()` stamperà correttamente `0` perché il modulo `a` a cui `b` ha un riferimento è ora completamente caricato.

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
-Il modulo `a` esiste già, ma non è stato ancora eseguito completamente.
-`b` scompatta tutto ciò che è attualmente in `a` nel suo scope globale. A questo punto, `a` non contiene nulla perché non ha ancora raggiunto la riga `x = 0`, quindi non viene importato nulla.
-`b` esegue l'istruzione `def` e memorizza la funzione `f()`.
-`a` continua l'esecuzione e inizializza `x`.

Se qualcuno ora chiama `b.f()`, riceverà un errore che `x` non esiste nello scope corrente. Questo perché questa volta `b` non ha un riferimento all'`a` ancora in fase di caricamento e non vede le definizioni che sono state aggiunte dopo l'import.