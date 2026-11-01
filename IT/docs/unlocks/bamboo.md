[<- Riso](docs/unlocks/rice.md) <right>[Blocchi Colorati ->](docs/unlocks/debug_place.md)
<right>[Piramidi ->](docs/unlocks/pyramid.md)
---
# Bambù
Il bambù è una pianta che cresce verso l'alto. Il drone dovrà staccare regolarmente i suoi frutti marroni perché continui a crescere. Possiamo farlo con il comando `hover` appena sbloccato.

Il bambù va piantato sul terreno arato (`Grounds.Soil`) e piantarlo costa riso.

Il codice seguente pianta il bambù e aspetta che cresca fino al primo frutto.
{{codeexample
{
"camera_position": {"x": -1, "y": 0, "z": 10},
"show_image": true,
"image_size": {"x": 800, "y": 500},
"show_code": true,
"show_inventory": true,
"show_output": false,
"collapsing": true,
"autoplay": false,
"items": [{"item": "rice", "n": 100}],
"world_size": {"x": 4, "y": 4},
"execution_speed": 2,
"action_ticks": 200,
"operation_ticks": 200,
"seed": 1,
"exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
move(East) # allontanati per lasciare crescere il bambù
}}

## Frutti
Il bambù cresce esattamente di 1 blocco al secondo.

Il bambù produce frutti ogni pochi blocchi. Quando succede, smette di crescere e devi entrarci con il drone per distruggere il frutto. Il bambù può crescere fino al terzo frutto. Da quel momento non crescerà più in altezza, anche se lo stacchi.

Per staccare i frutti, devi prima usare `hover` per raggiungere l'altezza giusta. Poi usa `move` per entrare nel frutto e staccarlo, e ancora `move` per allontanarti e lasciare crescere il bambù.

Puoi usare `measure()` sul bambù per sapere a quale altezza apparirà il prossimo frutto. `measure()` conta da `0`, quindi `hover(measure())` porterà il drone all'altezza del frutto.

{{codeexample
{
"camera_position": {"x": -1, "y": 0, "z": 10},
"show_image": true,
"image_size": {"x": 800, "y": 500},
"show_code": true,
"show_inventory": true,
"show_output": false,
"collapsing": true,
"autoplay": false,
"items": [{"item": "rice", "n": 100}],
"world_size": {"x": 4, "y": 4},
"execution_speed": 2,
"action_ticks": 200,
"operation_ticks": 200,
"seed": 1,
"exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
hover(measure()) # vola all'altezza del frutto

move(East) # allontanati e aspetta che cresca
for i in range(3):
    do_a_flip()

move(West) # stacca il frutto
move(East) # allontanati di nuovo
}}

## Volo Stazionario
Il comando `hover` accetta un argomento: l'altezza di volo, un numero da `0` a `18`. L'altezza di volo predefinita del drone è `1`. `hover` non può far scendere il drone dentro entità solide: se è già sopra il bambù, non puoi farlo entrare eseguendo `hover(0)`.

`hover` restituisce `True` se il drone ha raggiunto l'altezza indicata, altrimenti `False`.

Esiste anche il comando `get_hover`, che restituisce l'altezza di volo attuale del drone.

Se usi `dig`, `harvest` o `plant` mentre il drone è in volo stazionario, tornerà alla sua altezza predefinita (`1`).

Infine, l'altezza di volo non influisce su `get_pos_z()`. Restituisce sempre la posizione z del blocco sotto il drone.

## Raccogliere il Bambù
Puoi usare `harvest()`, ma il metodo consigliato per raccogliere il bambù è entrarci con il drone a un'altezza di volo di `0` (`hover(0)`). In questo modo raccogli tutta la pianta in una volta.

Se vuoi raccogliere il bambù senza distruggerlo, puoi entrarci con `move` a qualsiasi altezza, per esempio con `hover(3)`. Raccoglierai tutti i segmenti da quell'altezza in su, ma il bambù resterà vivo. Un bambù raccolto parzialmente in questo modo produrrà di nuovo i frutti, che dovrai quindi staccare ancora.

In entrambi i casi, la resa è uguale al quadrato del numero di segmenti di bambù distrutti: più alta è la pianta, maggiore è la resa.

---

[Statistiche](docs/stats.md)      [Ciclo For](docs/scripting/for.md)      [Variabili](docs/scripting/variables.md)      [If](docs/scripting/if.md)      [Funzioni](docs/scripting/functions.md)      [Riso](docs/unlocks/rice.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [measure()](functions/measure)
