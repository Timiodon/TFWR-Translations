# Mega Quinta
Este unlock incrivelmente poderoso aumenta significativamente o tamanho da quinta e dá-te acesso a múltiplos drones.

Para facilitar as coisas, recebes sempre exatamente 36 novos quadrados para cada novo drone. A proporção de drones para quadrados permanece constante.

## Múltiplos Drones
Como antes, ainda começas com apenas um drone. Drones adicionais devem primeiro ser criados e desaparecerão após o programa terminar.
Cada drone executa a sua própria instância de programa separada. Os drones podem criar novos drones usando
`new_drone_id = spawn_drone("filename")`

Isto cria um novo drone na mesma posição do drone que executou o comando `spawn_drone("filename")`. O novo drone começará a executar o programa no ficheiro chamado `filename`, então substitui `"filename"` pelo nome do ficheiro que queres executar.

Podes pensar nisto como se tivesses dito ao teu drone para ir ao ficheiro chamado `filename` e premir o botão de execução para o próximo drone.

Os drones não colidem uns com os outros.

Usa `max_drones()` para obter o número máximo de drones que podem ser criados.
Usa `num_drones()` para obter o número de drones que já estão na quinta.
Usa `get_drone_id()` para descobrir qual drone está a executar o código.

Exemplo:

Num ficheiro chamado `rotina de cultivo`:
`if get_drone_id() == 0:
    # Apenas o primeiro drone executará isto
    while num_drones() < max_drones():
        spawn_drone("rotina de cultivo")
        move(East)

while True:
    if can_harvest():
        harvest()
    move(North)`

Isto fará com que o teu primeiro drone se mova horizontalmente e crie mais drones. Os drones criados mover-se-ão então verticalmente e colherão tudo no seu caminho.

<spoiler=mostrar dica>
A maneira mais fácil de usar múltiplos drones é dividir a tua quinta entre eles. As melhorias são projetadas para que cada drone possa ter sempre um campo de 6x6.
</spoiler>

Tudo o que se segue é bastante avançado e não é necessário para o cultivo básico

## Race Conditions
Múltiplos drones podem interagir com o mesmo quadrado da quinta ao mesmo tempo. Se dois drones interagirem com o mesmo quadrado durante o mesmo tick, a ação do drone com o ID de drone mais baixo acontecerá primeiro.

Por exemplo, imagina que os drones `0` e `1` estão ambos sobre a mesma árvore que está quase totalmente crescida.
O Drone `0` chama
`use_item(Items.Fertilizer)`
O Drone `1` chama
`harvest()`

Se estas ações ocorrerem ao mesmo tempo, a árvore será primeiro fertilizada e depois colhida. Nesse caso, receberás madeira dela. No entanto, se o Drone `1` for ligeiramente mais rápido, a árvore será colhida antes de ser fertilizada, e não receberás a madeira.
Isto chama-se uma "race condition". É um problema comum na programação paralela, onde o resultado depende da ordem em que as operações são realizadas.

Aqui está outra situação problemática que pode acontecer quando múltiplos drones executam o mesmo código simultaneamente na mesma posição.
`if get_water() < 0.5:
    use_item(Items.Water)`

Se múltiplos drones executarem isto simultaneamente, todos eles executarão a primeira linha, o que os coloca no bloco `if`. Depois, todos eles usarão água, desperdiçando muita dela.
Quando um drone chega à segunda linha, `get_water()` pode já não ser inferior a `0.5` porque outro drone regou o quadrado entretanto.

## Comunicação entre Drones
Se estiveres interessado em estratégias mais avançadas, talvez queiras que os teus drones comuniquem entre si usando funções de passagem de mensagens.

Envia qualquer valor para outro drone:
`send(data, receiver_drone_id)`

Recebe o próximo valor enviado por qualquer drone:
`data = receive()`

Recebe o próximo valor enviado por um drone específico:
`data = receive(sender_drone_id)`

O tempo de execução de `send()` depende do tamanho dos dados enviados. Por exemplo, enviar um dictionary grande requer cópia, o que pode demorar um pouco.

`receive()` não espera que uma mensagem chegue. Se nenhuma mensagem tiver sido enviada ainda, retornará `None`.

Podes construir uma função que espera por uma mensagem assim:
`def blocking_receive(sender_drone_id = -1):
    while True:
        data = receive(sender_drone_id)
        if data != None:
            return data`

Uma aplicação útil da passagem de mensagens é ter uma função que cria um drone e lhe envia uma função para executar.
Num ficheiro chamado `drone_spawning`:
`def run_on_new_drone(f):
    id = spawn_drone("drone_spawning")
    send(f, id)

if __name__ == "__main__":
    f = blocking_receive()
    f()`

Enviar funções assim pode ser muito lento porque todo o estado capturado da função, incluindo todas as variáveis globais, tem de ser copiado.
