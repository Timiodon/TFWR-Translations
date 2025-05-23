# Girassóis
[Girassóis](objects/sunflower) coletam a energia do sol. Você pode colher essa energia.

Plantá-los funciona exatamente como plantar cenouras ou abóboras.

Colher um girassol crescido rende energia.
Se houver pelo menos 10 girassóis na fazenda e você colher o que tem o maior número de pétalas, você ganha `5` vezes mais energia!

`measure()` retorna o número de pétalas do girassol sob o drone.
Girassóis têm no mínimo `7` e no máximo `15` pétalas.
Eles podem ser medidos antes de estarem completamente crescidos.

Vários girassóis podem ter o mesmo número de pétalas, então pode haver vários girassóis com o maior número de pétalas. Nesse caso, não importa qual deles você colhe.

Enquanto você tiver energia, o drone a usará para funcionar duas vezes mais rápido.
Ele consome 1 de energia a cada 30 ações (como mover, colher, plantar...)
Executar outras declarações de código também pode usar energia, mas muito menos do que as ações do drone.

Em geral, tudo que é acelerado por atualizações de velocidade também é acelerado pela energia.
Qualquer coisa acelerada pela energia também usa energia proporcional ao tempo que leva para executá-la, ignorando atualizações de velocidade.