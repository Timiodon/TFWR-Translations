# Slunečnice
[Slunečnice](objects/sunflower) sbírají sílu slunce. Tuto sílu můžete sklízet.

Jejich sázení funguje přesně jako sázení mrkví nebo dýní.

Sklizeň vzrostlé slunečnice dává energii.
Pokud je na farmě alespoň 10 slunečnic a sklidíte tu s největším počtem okvětních lístků, získáte `8`krát více energie!
Pokud sklidíte slunečnici, zatímco existuje jiná slunečnice s více okvětními lístky, další slunečnice, kterou sklidíte, vám také dá pouze normální množství energie (ne 8x bonus).

`measure()` vrací počet okvětních lístků slunečnice pod dronem.
Slunečnice mají alespoň `7` a nejvíce `15` okvětních lístků.
Lze je změřit již předtím, než jsou plně vzrostlé.

Několik slunečnic může mít stejný počet okvětních lístků, takže může existovat i několik slunečnic s největším počtem okvětních lístků. V tomto případě nezáleží na tom, kterou z nich sklidíte.

Dokud máte energii, dron ji bude využívat k tomu, aby běžel dvakrát rychleji.
Spotřebuje 1 energii každých 30 akcí (jako pohyby, sklizně, sázení...).
Provádění jiných příkazů kódu může také spotřebovávat energii, ale mnohem méně než akce dronu.

Obecně platí, že vše, co je zrychleno vylepšeními rychlosti, je také zrychleno energií.
Cokoli zrychlené energií také spotřebovává energii úměrně času, který trvá její provedení, bez ohledu na vylepšení rychlosti.
