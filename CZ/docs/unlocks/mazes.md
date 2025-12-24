# Bludiště
`Items.Weird_Substance` (podivná látka), která se získává [hnojením](docs/unlocks/fertilizer.md) rostlin, má zvláštní účinek na keře. Pokud je dron nad keřem a zavoláte `use_item(Items.Weird_Substance, amount)`, keř vyroste do bludiště živých plotů.
Velikost bludiště závisí na množství použité `Items.Weird_Substance` (druhý argument volání `use_item()`).
Bez vylepšení bludiště bude použití `n` `Items.Weird_Substance` mít za následek bludiště `n`x`n`. Každá úroveň vylepšení bludiště zdvojnásobuje poklad, ale také zdvojnásobuje množství potřebné `Items.Weird_Substance`.
Takže pro vytvoření bludiště přes celé pole:

`plant(Entities.Bush)
substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)`


Z nějakého důvodu dron nemůže létat přes živé ploty, i když nevypadají tak vysoko.

Někde v živém plotě je ukrytý poklad. Použijte `harvest()` na poklad, abyste získali zlato rovné ploše bludiště. (Například bludiště 5x5 vynese 25 zlata.)

Pokud použijete `harvest()` kdekoli jinde, bludiště jednoduše zmizí.

`get_entity_type()` je rovno `Entities.Treasure`, pokud je dron nad pokladem, a `Entities.Hedge` všude jinde v bludišti.

Bludiště neobsahují žádné smyčky, pokud bludiště znovu nepoužijete (viz níže, jak znovu použít bludiště). Takže neexistuje způsob, jak by se dron ocitl na stejné pozici znovu, aniž by se vrátil zpět.

Zda je tam zeď, můžete zkontrolovat pokusem o průchod skrz ni.
`move()` vrací `True`, pokud uspěl, a `False` v opačném případě.

`can_move()` lze použít ke kontrole, zda je tam zeď, bez pohybu.

Pokud nemáte tušení, jak se dostat k pokladu, podívejte se na Nápovědu 1. Ukazuje, jak přistupovat k problému, jako je tento.

Použití `measure()` kdekoli v bludišti vrátí pozici pokladu.
`x, y = measure()`

Pro extra výzvu můžete bludiště také znovu použít použitím stejného množství `Items.Weird_Substance` na poklad znovu.
Tím se poklad sebere a objeví se nový poklad na náhodné pozici v bludišti.

Pokaždé, když se poklad přesune, mohou být některé zdi bludiště náhodně odstraněny. Takže znovu použitá bludiště mohou obsahovat smyčky.

Všimněte si, že smyčky v bludišti to dělají mnohem obtížnější, protože to znamená, že se můžete dostat na stejné místo znovu, aniž byste se vraceli zpět.
Opětovné použití bludiště vám nedá více zlata než jen sklizeň a vytvoření nového bludiště.
Toto je 100% extra výzva, kterou můžete prostě přeskočit.
Stojí to za to pouze tehdy, pokud vám extra informace a zkratky pomohou vyřešit bludiště rychleji.

Poklad lze přemístit až 300krát. Poté už použití podivné látky na poklad nezvýší zlato v něm a už se nebude pohybovat.

<spoiler=zobrazit nápovědu 1>Zde je obecný přístup k řešení problému:

Vytvořte bludiště a představte si, že jste dron.

Přemýšlejte o tom, jak byste se pokusili najít poklad, kdybyste byli v bludišti.

Zapište si svou strategii krok za krokem, aby ji mohl někdo jiný následovat bez přemýšlení.

Nyní zkuste přeložit své kroky do kódu.
</spoiler>
<spoiler=zobrazit nápovědu 2>Dokud nejsou žádné smyčky: Všechny zdi jsou ve skutečnosti jen jedna velká spojená zeď. Pokud budete sledovat zeď, provede vás celým bludištěm.
Tento přístup vyžaduje velmi málo kódu a nemusíte sledovat, kde jste již byli. Asi 10 řádků kódu je vše, co potřebujete.</spoiler>
<spoiler=zobrazit nápovědu 3>Místo pohybu dronem v absolutních směrech, jako je východ nebo západ, může být velmi užitečné pohybovat dronem v relativních směrech, jako je "zahni doprava" nebo "zahni doleva". K tomu musíte sledovat, kterým směrem se dron aktuálně pohybuje. Dron se ve skutečnosti nikdy neotáčí, ale stále můžete v kódu udržovat "virtuální" rotaci.
Následující trik s indexem je pro to užitečný:

`directions = [North, East, South, West]
index = 0`

Použijte `% 4`, abyste umožnili rotaci "kolem kruhu", takže po `West` (západ) se vrátí zpět na `North` (sever).
`# zahni doprava
index = (index + 1) % 4`

`# zahni doleva
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=zobrazit nápovědu 4>Pokud to nemůžete vyřešit, můžete si vždy usnadnit život a udělat to méně efektivně.
Vyřešení bludiště `1`x`1` je triviální.</spoiler>