# Pumpkins
[Dýně](objects/pumpkin) rostou podobně jako mrkev na zorané půdě. Jejich zasazení stojí několik mrkví.

Když všechny dýně v určitém čtverci plně dorostou, spojí se dohromady a vytvoří obří dýni. Bohužel má každá dýně 20% šanci, že po úplném dorůstu zemře, takže pokud chceš, aby se spojily, budeš muset ty mrtvé znovu zasadit.

Když dýně zemře, zůstane po ní „mrtvá dýně“, která při sklizni nic nedá. Zasazení nové rostliny na její místo automaticky mrtvou dýni odstraní, takže ji není třeba sklízet ručně. `can_harvest()` vždy vrátí `False` u mrtvých dýní.

Výnos obří dýně závisí na její velikosti:

Dýně 1×1 dává `1*1*1 = 1` dýni.  
Dýně 2×2 dává `2*2*2 = 8` dýní místo `4`.  
Dýně 3×3 dává `3*3*3 = 27` dýní místo `9`.  
Dýně 4×4 dává `4*4*4 = 64` dýní místo `16`.  
Dýně 5×5 dává `5*5*5 = 125` dýní místo `25`.  
Dýně `n`×`n` dává `n*n*6` dýní pro `n >= 6`.

Je tedy dobré pěstovat alespoň dýně velikosti 6×6, abys získal plný multiplikátor.  

To také znamená, že i když zasadíš dýni na každé políčko čtverce, jedna z nich může zemřít a zabránit tak růstu megadýně.