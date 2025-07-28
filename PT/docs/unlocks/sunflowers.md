# Girassóis
Os [girassóis](objects/sunflower) recolhem a energia do sol. Podes colher essa energia.

Plantá-los funciona exatamente como plantar cenouras ou abóboras.

Colher um girassol crescido rende energia.
Se houver pelo menos 10 girassóis na quinta e colheres aquele com o maior número de pétalas, recebes `5` vezes mais energia!

`measure()` retorna o número de pétalas do girassol debaixo do drone.
Os girassóis têm pelo menos `7` e no máximo `15` pétalas.
Eles já podem ser medidos antes de estarem totalmente crescidos.

Vários girassóis podem ter o mesmo número de pétalas, então também pode haver vários girassóis com o maior número de pétalas. Neste caso, não importa qual deles colhes.

Enquanto tiveres energia, o drone usá-la-á para se mover duas vezes mais rápido.
Ele consome 1 de energia a cada 30 ações (como movimentos, colheitas, plantações...)
Executar outras declarações de código também pode usar energia, mas muito menos do que as ações do drone.

Em geral, tudo o que é acelerado por melhorias de velocidade também é acelerado por energia.
Qualquer coisa acelerada por energia também usa energia proporcional ao tempo que leva para ser executada, ignorando as melhorias de velocidade.