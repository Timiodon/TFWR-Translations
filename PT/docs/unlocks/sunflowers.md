# Girassóis
[Girassóis](objects/sunflower) coletam a energia do sol. Você pode colher essa energia. 

Plantá-los funciona exatamente como plantar cenouras ou abóboras. 

Colher um girassol crescido rende energia.
Se houver pelo menos 10 girassóis na fazenda e você colher aquele com o maior número de pétalas, você ganha `5` vezes mais energia!

`measure()` retorna o número de pétalas do girassol sob o drone.
Girassóis têm pelo menos `7` e no máximo `15` pétalas.
Eles já podem ser medidos antes de estarem totalmente crescidos.

Vários girassóis podem ter o mesmo número de pétalas, então também pode haver vários girassóis com o maior número de pétalas. Nesse caso, não importa qual deles você colhe.

Enquanto você tiver energia, o drone a usará para funcionar duas vezes mais rápido. 
Ele consome 1 de energia a cada 30 ações (como movimentos, colheitas, plantios...)
Executar outras instruções de código também pode usar energia, mas muito menos do que as ações do drone.

Em geral, tudo que é acelerado por melhorias de velocidade também é acelerado por energia.
Qualquer coisa acelerada por energia também usa energia proporcional ao tempo que leva para executá-la, ignorando as melhorias de velocidade.
