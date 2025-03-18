# Fertilizzante  
A un certo punto, aspettare che le piante crescano non è più abbastanza efficiente.  
Simile all'acqua, riceverai automaticamente 1 fertilizzante ogni 10 secondi, più uno extra per ogni potenziamento.

Il fertilizzante può far crescere istantaneamente le piante. `use_item(Items.Fertilizer)` riduce il tempo di crescita rimanente della pianta sotto il drone di 2 secondi.

Questo ha alcuni effetti collaterali.  
Le piante cresciute con fertilizzante saranno infettate.

Quando una pianta è infettata, metà del suo raccolto viene trasformata in `Items.Weird_Substance` quando viene raccolta.  
La Sostanza Strana può essere usata anche sulle piante, e ha l'effetto di cambiare lo stato di infezione della pianta e delle piante adiacenti.

Quindi se chiami `use_item(Items.Weird_Substance)` su una pianta infetta, la curerà, ma se la usi su una pianta sana, la infetterà.

Se la usi su una pianta infetta che ha vicini sani, curerà la pianta ma infetterà i vicini e viceversa.