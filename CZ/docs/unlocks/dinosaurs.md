# Dinosauři
Dinosauři jsou prastará, majestátní stvoření, která lze chovat pro starověké kosti.

Bohužel dinosauři již dávno vyhynuli, takže to nejlepší, co můžeme udělat, je převléknout se za jednoho z nich.
Za tímto účelem jste obdrželi nový dinosauří klobouk.

Klobouk lze nasadit pomocí
`change_hat(Hats.Dinosaur_Hat)`

Bohužel nevypadá úplně jako v reklamě...

Pokud si nasadíte dinosauří klobouk a máte dostatek kaktusů, automaticky se zakoupí [jablko](objects/apple) a umístí se pod drona.
Když je dron nad jablkem a znovu se pohne, sní jablko a jeho ocas se zvětší o jedna. Pokud si to můžete dovolit, zakoupí se nové jablko a umístí se na náhodné místo.
Jablko se nemůže objevit, pokud je na místě, kde chce být, zasazeno něco jiného.

Ocas dinosaura se potáhne za dronem a zaplní předchozí políčka, přes která se dron pohyboval. Pokud se dron pokusí pohnout na ocas, `move()` selže a vrátí `False`.
Poslední segment ocasu se během pohybu uhne z cesty, takže se na něj můžete přesunout. Pokud však had zaplní celou farmu, nebudete se moci dále pohybovat. Můžete tedy zkontrolovat, zda je had plně vzrostlý, kontrolou, zda se již nemůžete pohnout.
Při nošení dinosauřího klobouku se dron nemůže pohybovat přes hranici farmy na druhou stranu.

Použití `measure()` na jablko vrátí pozici dalšího jablka jako n-tici (tuple).

`next_x, next_y = measure()`

Když se klobouk znovu sundá nasazením jiného klobouku, ocas se sklidí.
Získáte kosti rovné délce ocasu na druhou. Takže za ocas o délce `n` získáte `n**2` `Items.Bone`.
Například:
délka 1 => 1 kost
délka 2 => 4 kosti
délka 3 => 9 kostí
délka 4 => 16 kostí
délka 16 => 256 kostí
délka 100 => 10000 kostí

Dinosauří klobouk je velmi těžký, takže pokud si ho nasadíte, `move()` bude trvat 400 tiků místo 200. Nicméně pokaždé, když seberete jablko, počet tiků použitých funkcí `move()` se sníží o 3 % (zaokrouhleno dolů), protože delší ocas vám může pomoci v pohybu.

Následující smyčka vypíše počet tiků použitých funkcí `move()` po libovolném počtu jablek:

`ticks = 400
for i in range(100):
    print("ticks after ", i, " apples: ", ticks)
    ticks -= ticks * 0.03 // 1`

Máte pouze jeden dinosauří klobouk, takže ho může nosit pouze jeden dron.

<spoiler=zobrazit nápovědu 1>Pokud se budete pohybovat po stejné cestě, která pokrývá celé pole, můžete snadno získat hada, který pokaždé pokryje celé pole. Není to příliš efektivní, ale funguje to.
Úplné projití velmi velké farmy může trvat dlouho a možná ve skutečnosti nepotřebujete tolik kostí. Nebojte se použít `set_world_size()` ke změně velikosti farmy na něco pohodlnějšího.</spoiler>