# Fertilizzante
A un certo punto, aspettare che le piante crescano non è più abbastanza efficiente. 
Similmente all'acqua, riceverai automaticamente 1 fertilizzante ogni 10 secondi, più uno extra per ogni potenziamento.

Il fertilizzante può far crescere le piante istantaneamente. `use_item(Items.Fertilizer)` riduce il tempo di crescita rimanente della pianta sotto il drone di 2 secondi.

Questo ha alcuni effetti collaterali.
Le piante coltivate con fertilizzante saranno infette.

Quando una pianta è infetta, metà del suo raccolto viene trasformata in `Items.Weird_Substance` quando viene raccolta.
La Sostanza Strana può anche essere usata sulle piante, il che ha l'effetto di alternare lo stato di infezione della pianta e di tutte le piante adiacenti.

Quindi se chiami `use_item(Items.Weird_Substance)` su una pianta infetta, la curerà, ma se la usi su una pianta sana, la infetterà.

Se la usi su una pianta infetta che ha vicini sani, curerà la pianta ma infetterà i vicini e viceversa.
