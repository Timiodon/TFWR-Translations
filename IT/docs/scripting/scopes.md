# Name Scopes
Gli scope determinano quali variabili possono essere accedute da dove. Uno scope è fondamentalmente una mappatura da nomi a valori.
Funzionano praticamente come in Python.

C'è uno scope globale, e ogni funzione ha uno scope locale.
Quando definisci una variabile, viene aggiunta allo scope corrente.
Qualsiasi cosa al di fuori di una definizione di funzione è considerata parte dello scope globale.

`x = 1`
Assegna un valore di `1` al nome `x` nello scope globale.

Questa istruzione `def` assegna una funzione al nome `f` nello scope globale.
`def f():
    `Assegna un valore di `1` al nome `y` nello scope locale di `f`.`
    y = 1

    `Assegna una funzione al nome `g` nello scope locale di `f`.`
    def g():
        pass`

`f()`
Recupera la funzione memorizzata in `f` dallo scope globale e la chiama.

`print(y)`
Questa istruzione di print nello scope globale genera un errore perché `y` non è mai stata dichiarata nello scope globale, quindi non possiamo leggerla qui.
È esistita solo nello scope locale di `f`.

## La parola chiave global
Di default tutte le variabili nelle funzioni si legano allo scope locale, anche se una variabile con lo stesso nome esiste nello scope globale.

`x == 0

def f():
    x = 1
f()
print(x)`

Questo codice stampa `0` perché la `x` locale dentro `f` non è la stessa variabile della `x` globale, quindi la `x` globale rimane invariata. Questo è importante perché altrimenti una chiamata di funzione potrebbe accidentalmente sovrascrivere una variabile globale che casualmente ha lo stesso nome di una variabile locale di quella funzione.

Se vuoi scrivere su una variabile globale, devi farlo esplicitamente usando la parola chiave `global`.

`x == 0

def f():
    global x
    x = 1
f()
print(x)`

In questo esempio, `global x` lega `x` alla variabile globale `x` definita sopra. Ora questo stamperà `1`.
Nota che cambiare variabili globali è solitamente il primo passo verso il codice spaghetti, dove ogni parte del programma influisce su ogni altra parte del programma, quindi non abusarne.

## Loop e ramificazioni
I loop e le ramificazioni non creano i propri scope, quindi qualsiasi cosa dichiarata al loro interno può ancora essere usata all'esterno.

`for i in range(3):
    pass
print(i)`

Questo stamperà `2` perché l'ultima iterazione del ciclo `for` ha assegnato `2` a `i`.