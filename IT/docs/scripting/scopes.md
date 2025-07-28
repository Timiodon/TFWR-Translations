# Scope
Gli scope determinano quali variabili possono essere accessibili e da dove. Uno scope è fondamentalmente un'associazione tra nomi e valori.
Funzionano praticamente come in Python.

C'è uno scope globale e ogni funzione ha uno scope locale.
Quando definisci una variabile, viene aggiunta allo scope corrente.
Qualsiasi cosa al di fuori della definizione di una funzione è considerata parte dello scope globale.

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
Questa istruzione print nello scope globale genera un error perché `y` non è mai stato dichiarato nello scope globale, quindi non possiamo leggerlo qui.
Esisteva solo nello scope locale di `f`.

## La parola chiave global
Di default, tutte le variabili nelle funzioni si legano allo scope locale, anche se una variabile con lo stesso nome esiste nello scope globale.

`x = 0

def f():
    x = 1
f()
print(x)`

Questo codice stampa `0` perché la `x` locale dentro `f` non è la stessa variabile della `x` globale, quindi la `x` globale rimane invariata. Questo è importante perché altrimenti una chiamata di funzione potrebbe sovrascrivere accidentalmente una variabile globale che ha casualmente lo stesso nome di una variabile locale di quella funzione.

Se vuoi scrivere in una variabile globale, devi farlo esplicitamente usando la parola chiave `global`.

`x = 0

def f():
    global x
    x = 1
f()
print(x)`

In questo esempio, `global x` lega `x` alla variabile globale `x` definita sopra. Ora stamperà `1`.
Nota che modificare le variabili globali è solitamente il primo passo verso il "codice spaghetti", dove ogni parte del programma influenza ogni altra parte, quindi non abusarne.

## Cicli e diramazioni
Cicli e diramazioni non creano i propri scope, quindi tutto ciò che viene dichiarato al loro interno può ancora essere usato all'esterno.

`for i in range(3):
    pass
print(i)`

Questo stamperà `2` perché l'ultima iterazione del ciclo `for` ha assegnato `2` a `i`.