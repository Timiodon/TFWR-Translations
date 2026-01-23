# Sunflowers
[Slunečnice](objects/sunflower) sbírají energii ze slunce. Tu můžeš sklízet. 

Sázení funguje úplně stejně jako u mrkve nebo dýní. 

Sklizeň vyrostlé slunečnice dává „power“ (energii).
Pokud je na farmě alespoň 10 slunečnic a sklidíš tu s největším počtem okvětních lístků, dostaneš `5`× více energie!

`measure()` vrací počet okvětních lístků slunečnice pod dronem.
Slunečnice mají nejméně `7` a nejvýše `15` lístků.
Lze je měřit i před úplným dorůstem.

Více slunečnic může mít stejný počet lístků, takže může existovat i více „největších“. V takovém případě nezáleží na tom, kterou z nich sklidíš.

Dokud máš energii, dron ji využije k běhu dvojnásobnou rychlostí. 
Spotřebuje 1 „power“ každých 30 akcí (pohyb, sklizeň, sázení…).
Provádění jiných programových příkazů může energii také spotřebovávat, ale mnohem méně než akce dronu.

Obecně platí, že vše, co zrychlují vylepšení rychlosti, zrychluje i energie.
Cokoli je zrychlené energií, zároveň spotřebovává energii úměrně času vykonávání, bez ohledu na vylepšení rychlosti.
