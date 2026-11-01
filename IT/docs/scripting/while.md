[<- Primo Programma](docs/first_program.md) <right>[Potenziamento Velocità ->](docs/unlocks/speed.md)
---
# Ciclo While
Hai sbloccato il ciclo `while` e i valori `True` e `False`. Il ciclo `while` continua a eseguire il corpo del ciclo finché la condizione è `True`.

`while condition:
	#corpo del ciclo`

Non preoccuparti di creare cicli infiniti. I ritardi nell'esecuzione impediranno al programma di bloccarsi.

## Per Principianti
Forse hai già provato a mettere diverse chiamate `harvest()` di seguito:

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
harvest()
harvest()
harvest()
}}
Questo ti permette di raccogliere più volte durante una singola esecuzione del programma.
Sarebbe però utile raccogliere più di tre volte, e ripetere lo stesso codice non è una buona pratica.
La soluzione è un ciclo.
Un ciclo ti permette di eseguire lo stesso codice più volte.

Il ciclo while prende una condizione, che è un valore logico che può trovarsi solo in uno di due stati: `True` o `False`. 
Un valore di questo tipo è chiamato valore Booleano.

Il ciclo quindi esegue il codice al suo interno finché la condizione non è Falsa.
Il ciclo while si presenta così:

`while condition:
	#corpo del ciclo
	#corpo del ciclo
	#...`

Dove devi sostituire "condition" con un valore booleano e `#corpo del ciclo` con quello che vuoi fare nel ciclo.

Ci sono due valori booleani costanti disponibili. Le costanti sono valori che non cambiano mai durante il programma.

Per creare un valore booleano costante, basta scrivere `True` o `False`.
Quindi potresti scrivere o

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while False:
	do_a_flip()
}}
o

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	do_a_flip()
}}
Il primo non eseguirà mai un flip, mentre il secondo continuerà a eseguirne per sempre (un ciclo infinito).

Di norma creare un ciclo infinito è una cattiva idea perché blocca il programma. In questo gioco, però, ci sono dei ritardi tra le iterazioni, quindi il drone continuerà a eseguire flip finché non lo fermerai manualmente premendo di nuovo il pulsante Esegui.

Nota come la riga dopo i due punti sia indentata. L'indentazione come questa viene usata per separare i blocchi di codice.
Premi Tab per aggiungere l'indentazione e Shift + Tab (o Backspace) per rimuoverla. Se sono selezionate più righe, Tab e Shift + Tab verranno applicati a tutte.

Nota: se giochi tramite Steam, premendo Shift + Tab si aprirà invece l'overlay di Steam. Puoi riassegnare la scorciatoia per rimuovere l'indentazione nelle opzioni del gioco oppure quella dell'overlay nelle opzioni di Steam.

Qui `do_a_flip()` e `pet_the_piggy()` vengono chiamate ripetutamente perché si trovano nel blocco `while` indentato. `harvest()`, invece, non viene mai eseguita perché si trova dopo quel blocco.
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	do_a_flip()
	pet_the_piggy()
harvest()
}}

---

[Ciclo For](docs/scripting/for.md)      [If](docs/scripting/if.md)      [Break](docs/scripting/break.md)      [Continue](docs/scripting/continue.md)      [Editor Esterno](docs/external_editor.md)
