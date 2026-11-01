[<- Quarzo](docs/unlocks/quartz.md) <right>[Dinamite ->](docs/unlocks/dynamite.md)
---
# Funghi
Molti tipi di funghi crescono in colonie sotterranee. Mentre scavi, cerca uno strato di `Grounds.Mushroom`. Puoi quindi usare `measure()` sul terreno per ottenere il tipo di fungo come numero da `0` a `5`.

Il codice seguente trova dei funghi e ne stampa il tipo:
{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 6,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}
#SETUP
jump(Unlocks.Mushrooms)
#CODE
# Elabora una fila di funghi
for i in range(get_world_size()):
    # Scava fino al primo blocco di funghi
    while get_ground_type() != Grounds.Mushroom:
        dig()

    # Stampa il numero del tipo di fungo
    print(measure())

    move(East)
}}

## Raccogliere i Funghi
I funghi dello stesso tipo amano stare insieme, ma sono troppo timidi per crescere uno sopra l'altro. Spingi il blocco di funghi sotto il drone con `push(direction)`.

Impila due blocchi di funghi dello stesso tipo: verranno raccolti automaticamente per ottenere i funghi.

Il codice seguente fa spazio e spinge un fungo finché non corrisponde a quello sottostante:
{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 6,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 3,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron", "special_soils"]
}
#SETUP
jump(Unlocks.Mushrooms)
#CODE
while get_ground_type() != Grounds.Mushroom:
    dig()

depth = get_pos_z()
for i in range(2):
    # Fai spazio per spingere il fungo verso est
    move(East)
    while get_pos_z() > depth - 1:
        dig()
    # Torna indietro, spingi e segui il blocco spinto
    move(West)
    push(East) # Spingi il fungo!
    move(East)
}}

# Spingere i Blocchi
Puoi usare `can_push(direction)` per controllare se il blocco sotto il drone può essere spinto e se qualcosa lo ostacola nella direzione indicata.

`push(direction)` spinge il blocco e restituisce se l'operazione è riuscita.

Si possono spingere solo blocchi di funghi. I blocchi non possono essere spinti verso l'alto e l'operazione fallisce se un altro blocco ostacola il percorso. Se vengono spinti nel vuoto, i blocchi cadono e atterrano sul blocco successivo sotto di loro.

# Strategia
<spoiler=suggerimento>
Ricorda che puoi chiamare `place(Grounds.Dirt)` per posizionare blocchi sotto il drone. Può essere utile per riempire le buche e spingervi sopra altri blocchi.
</spoiler>

---

[Statistiche](docs/stats.md)      [Sensi Sotterranei](docs/unlocks/underground_senses.md)      [Dizionari](docs/scripting/dicts.md)

[move()](functions/move)      [measure()](functions/measure)      [can_push()](functions/can_push)      [push()](functions/push)      [place()](functions/place)      [get_ground_type()](functions/get_ground_type)
