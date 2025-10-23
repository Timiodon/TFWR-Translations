# Mazes
`Items.Weird_Substance`, kterou získáš [hnojením](docs/unlocks/fertilizer.md) rostlin, má zvláštní účinek na keře. Pokud je dron nad keřem a zavoláš `use_item(Items.Weird_Substance, amount)`, keř vyroste do bludiště z živých plotů.
Velikost bludiště závisí na množství použité `Items.Weird_Substance` (druhý argument volání `use_item()`).
Bez vylepšení bludiště použití `n` kusů `Items.Weird_Substance` vytvoří bludiště `n`×`n`. Každá úroveň vylepšení bludiště zdvojnásobí poklad, ale zároveň zdvojnásobí i potřebné množství `Items.Weird_Substance`. 
Pro vytvoření bludiště přes celou farmu tedy:

`plant(Entities.Bush)
substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)`

Z nějakého důvodu dron nedokáže létat nad živými ploty, i když nevypadají nijak vysoké.

Někde v bludišti je ukryt poklad. Použij `harvest()` na poklad a získáš zlato rovné ploše bludiště. (Například bludiště 5×5 dá 25 zlata.)

Pokud použiješ `harvest()` kdekoliv jinde, bludiště jednoduše zmizí.

`get_entity_type()` je rovno `Entities.Treasure`, pokud je dron nad pokladem, a `Entities.Hedge` všude jinde v bludišti.

Bludiště neobsahují žádné smyčky, pokud je nezačneš znovu používat (viz níže, jak bludiště znovu použít). To znamená, že dron se nemůže dostat na stejné místo znovu, aniž by se vracel.

Můžeš zkontrolovat, zda je před tebou zeď, tak, že se zkusíš pohnout skrz ni.  
`move()` vrátí `True`, pokud se pohyb podařil, jinak `False`.

`can_move()` lze použít k ověření existence zdi bez pohybu.

Pokud netušíš, jak se dostat k pokladu, podívej se na Hint 1. Ukáže ti, jak k takovému problému přistoupit.

Použití `measure()` kdekoliv v bludišti vrátí pozici pokladu.  
`x, y = measure()`

Pro extra výzvu můžeš bludiště znovu použít tak, že na poklad opět použiješ stejné množství `Items.Weird_Substance`.  
Tím se množství zlata v pokladu zvýší o jednu plochu bludiště a poklad se přesune na náhodnou pozici v bludišti.

Pokaždé, když se poklad přesune, mohou být některé zdi bludiště náhodně odstraněny. Znovu použité bludiště tedy může obsahovat smyčky.

Všimni si, že smyčky v bludišti to výrazně ztěžují, protože se můžeš dostat na stejné místo znovu, aniž by ses vracel.  
Znovupoužití bludiště ti nedá více zlata, než kdybys ho prostě sklidil a vytvořil nové.  
Je to na 100 % jen extra výzva, kterou můžeš přeskočit.  
Vyplatí se pouze tehdy, pokud ti dodatečné informace a zkratky pomohou bludiště řešit rychleji.

Poklad lze přemístit až 300×. Poté už použití podivné látky na poklad nezvýší množství zlata a poklad se už nebude hýbat.

<spoiler=show hint 1>Here's a general approach to solving the problem:

Create a maze and imagine that you are the drone.

Think about how you would try to find the treasure if you were in the maze.

Write down your strategy step by step so that someone else could follow it without thinking.

Now try translating your steps into code.
</spoiler>
<spoiler=show hint 2>As long as there are no loops: All the walls are really just one large connected wall. If you follow the wall, it will lead you through the whole maze.
This approach requires very little code and you do not need to keep track of where you have already been. Around 10 lines of code is all you need.</spoiler>
<spoiler=show hint 3>Instead of moving the drone in absolute directions like east or west it can be very useful to move the drone in relative directions like "turn right" or "turn left". To do this you need to keep track of which way the drone is currently moving. The drone never actually rotates, but you can still keep a "virtual" rotation in code.
The following index trick is helpful for this:

`directions = [North, East, South, West]
index = 0`

Use `% 4` to allow it to rotate "around the circle", so that after `West` it wraps back to `North`.
`# turn right
index = (index + 1) % 4`

`# turn left
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=show hint 4>If you can't solve it, you can always make your life easy and do it less efficiently. 
Solving a `1`x`1` maze is trivial.</spoiler>
