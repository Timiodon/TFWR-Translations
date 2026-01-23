# Dinosauři
Dinosauři jsou dávní, majestátní tvorové, které lze farmit pro získání prastarých kostí.

Bohužel dinosauři už dávno vyhynuli, takže to nejlepší, co můžeme udělat, je převléct se za jednoho. K tomuto účelu jsi dostal nový dinosauří klobouk.

Klobouk můžeš nasadit pomocí  
`change_hat(Hats.Dinosaur_Hat)`

Bohužel ale nevypadá úplně tak, jak bylo slíbeno v reklamě...

Pokud máš nasazený dinosauří klobouk a dostatek kaktusů, automaticky se zakoupí [jablko](objects/apple) a umístí pod dron.  
Když se dron nachází nad jablkem a znovu se pohne, jablko sní a jeho ocas se prodlouží o jeden díl. Pokud si to můžeš dovolit, zakoupí se nové jablko a umístí na náhodné místo.  
Jablko se nemůže objevit, pokud je na daném místě něco jiného zasazeno.

Ocas dinosaura se táhne za dronem a vyplňuje pole, po kterých se dron pohyboval. Pokud se dron pokusí pohnout na ocas, `move()` selže a vrátí `False`.  
Poslední segment ocasu se při pohybu posune z cesty, takže na něj můžeš vstoupit. Pokud však had vyplní celou farmu, už se nebudeš moct pohnout.  Můžeš tedy zjistit, že had dosáhl maximální délky, pokud už se nelze nikam pohnout.

Použitím `measure()` na jablko získáš pozici dalšího jablka jako n-tici.

`next_x, next_y = measure()`

Když klobouk sundáš (nasazením jiného klobouku), ocas se sklidí.  
Získáš počet kostí rovnající se druhé mocnině délky ocasu. Takže pro ocas délky `n` získáš `n**2` `Items.Bone`.  
Například:  
délka 1 => 1 kost  
délka 2 => 4 kosti  
délka 3 => 9 kostí  
délka 4 => 16 kostí  
délka 16 => 256 kostí  
délka 100 => 10 000 kostí

Dinosauří klobouk je velmi těžký, takže když ho nasadíš, způsobí, že `move()` trvá 400 tiků místo 200. Každé sebrané jablko ale dobu trvání `move()` sníží o 3 % (zaokrouhleno dolů), protože delší ocas pomáhá s pohybem.

Následující smyčka vypíše počet tiků, které `move()` používá po libovolném počtu jablek:

`ticks = 400
for i in range(100):
    print("ticks after ", i, " apples: ", ticks)
    ticks -= ticks * 0.03 // 1`

Máš pouze jeden dinosauří klobouk, takže ho může nosit jen jeden dron.

<spoiler=show hint 1>
Pokud se budeš pohybovat stále po stejné cestě, která pokrývá celé pole, můžeš snadno vytvořit hada, který vyplní celou farmu. Není to příliš efektivní, ale funguje to.  
Procházení velmi velké farmy může trvat dlouho a pravděpodobně nebudeš potřebovat tolik kostí. Můžeš proto použít `set_world_size()` k úpravě velikosti farmy na praktičtější rozměr.</spoiler>
