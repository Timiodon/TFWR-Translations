# Dýně
[Dýně](objects/pumpkin) rostou jako mrkve na zorané půdě. Jejich sázení stojí mrkve.

Když jsou všechny dýně ve čtverci plně vzrostlé, srostou dohromady a vytvoří obří dýni. Bohužel dýně mají 20% šanci, že uhynou, jakmile jsou plně vzrostlé, takže budete muset ty mrtvé znovu zasadit, pokud chcete, aby se spojily.

Když dýně uhyne, zanechá po sobě mrtvou dýni, ze které při sklizni nic nevypadne. Zasazení nové rostliny na její místo automaticky odstraní mrtvou dýni, takže není třeba ji sklízet. `can_harvest()` na mrtvých dýních vždy vrací `False`.

Výnos obří dýně závisí na velikosti dýně.

Dýně 1x1 vynese `1*1*1 = 1` dýni.
Dýně 2x2 vynese `2*2*2 = 8` dýní místo `4`.
Dýně 3x3 vynese `3*3*3 = 27` dýní místo `9`.
Dýně 4x4 vynese `4*4*4 = 64` dýní místo `16`.
Dýně 5x5 vynese `5*5*5 = 125` dýní místo `25`.
Dýně `n`x`n` vynese `n*n*6` dýní pro `n >= 6`.

Je dobrý nápad získat dýně o velikosti alespoň 6x6, abyste získali plný násobitel.

To znamená, že i když zasadíte dýni na každé políčko ve čtverci, jedna z dýní může uhynout a zabránit růstu mega dýně.
