[<- Estrazione](docs/unlocks/mining.md) <right>[Ferro ->](docs/unlocks/iron.md)
<right>[Salto ->](docs/unlocks/jump.md)
---
# Carbone
Nel sottosuolo si nascondono diversi minerali, in attesa di essere trovati ed estratti. Se attraversi la superficie e scavi in `Grounds.Dirt`, il primo minerale che trovi è il carbone.

Per estrarre carbone non serve nulla di speciale: esegui `dig()` quando il drone è direttamente sopra un blocco di `Grounds.Coal`. Usa `get_ground_type()` per controllare cosa c'è sotto il drone e `get_ground_type(direction)` per controllare i quattro blocchi adiacenti.

Il programma seguente è un buon punto di partenza per trovare il carbone. Scava verso il basso alla ricerca di uno strato di carbone.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 4,
    "digging_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 2,
    "exclude_unlocks": ["watering", "fertilizer"]
}
#SETUP
move(North)
move(East)
move(East)
#CODE
# Scava finché non appare un blocco di carbone
while get_ground_type() != Grounds.Coal:
    dig()

# Estrai il carbone
dig()
}}

## Nota sui Crolli
Ottieni carbone solo dai blocchi che scavi direttamente, non da quelli che crollano intorno al drone. Tienilo presente per estrarre più carbone possibile e perderne il meno possibile nei crolli.

## Struttura delle Vene
Le vene formano strati orizzontali spessi 1 blocco, che devi trovare per caso scavando nella terra. La maggior parte dei blocchi di carbone di uno strato è direttamente adiacente, ma alcuni sono collegati solo in diagonale.

I giacimenti di carbone crescono in proporzione alla fattoria: potenzia ancora [Espandi](unlocks/expand) per estrarre più carbone.

## Strategia
<spoiler=mostra suggerimento> 
Una strategia semplice, soprattutto nelle fattorie piccole, è scavare tutti i blocchi alla profondità in cui hai trovato carbone. Per aumentare l'efficienza, puoi tenere traccia del carbone visto con `get_ground_type(direction)` ed evitare di perdere tempo passando sopra la terra. Fai attenzione alle connessioni diagonali, che ti sfuggiranno se ti muovi solo sopra i blocchi di carbone.
</spoiler>

---

[Statistiche](docs/stats.md)      [Estrazione](docs/unlocks/mining.md)      [Sensi Sotterranei](docs/unlocks/underground_senses.md)

[move()](functions/move)      [get_ground_type()](functions/get_ground_type)      [dig()](functions/dig)
