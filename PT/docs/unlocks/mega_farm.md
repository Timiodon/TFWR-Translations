# Mega Fazenda
Este desbloqueio incrivelmente poderoso aumenta significativamente o tamanho da fazenda e te dá acesso a múltiplos drones.

Para facilitar as coisas, você sempre recebe exatamente 36 novos blocos para cada novo drone. A proporção de drones para blocos permanece constante.

## Múltiplos Drones
Como antes, você ainda começa com apenas um drone. Drones adicionais devem primeiro ser gerados e desaparecerão após o término do programa.
Cada drone executa sua própria instância de programa separada. Drones podem gerar novos drones usando
`new_drone_id = spawn_drone("filename")`

Isso gera um novo drone na mesma posição do drone que executou o comando `spawn_drone("filename")`. O novo drone começará a executar o programa no arquivo chamado `filename`, então substitua `"filename"` pelo nome do arquivo que você deseja executar.

Você pode pensar nisso como se dissesse ao seu drone para ir até o arquivo chamado `filename` e clicar no botão de execução para o próximo drone.

Drones não colidem uns com os outros.

Use `max_drones()` para obter o número máximo de drones que podem ser gerados.
Use `num_drones()` para obter o número de drones que já estão na fazenda.
Use `get_drone_id()` para descobrir qual drone está executando o código.

Exemplo:

Em um arquivo chamado `farming routine`:
`if get_drone_id() == 0:
    # Apenas o primeiro drone executará isso
    while num_drones() < max_drones():
        spawn_drone("farming routine")
        move(East)`

while True:
    if can_harvest():
        harvest()
    move(North)`

Isso fará com que o seu primeiro drone se mova horizontalmente e gere mais drones. Os drones gerados então se moverão verticalmente e colherão tudo em seu caminho.

<spoiler=mostrar dica>A maneira mais fácil de usar múltiplos drones é dividir sua fazenda entre eles. Os upgrades são projetados para que cada drone possa sempre ter um campo de 6x6.
</spoiler>

### Tudo abaixo aqui é bem avançado e não é necessário para agricultura básica

## Condições de Corrida
Múltiplos drones podem interagir com o mesmo bloco da fazenda ao mesmo tempo. Se dois drones interagirem com o mesmo bloco durante o mesmo tick, a ação do drone com o ID menor ocorrerá primeiro.

Por exemplo, imagine que os drones `0` e `1` estão sobre a mesma árvore que está quase totalmente crescida.
Drone `0` chama
`use_item(Items.Fertilizer)`
Drone `1` chama
`harvest()`

Se essas ações ocorrerem ao mesmo tempo, a árvore será primeiro fertilizada e depois colhida. Nesse caso, você receberá madeira dela. No entanto, se o Drone `1` for ligeiramente mais rápido, a árvore será colhida antes de ser fertilizada, e você não receberá a madeira.
Isso é chamado de "condição de corrida". É um problema comum na programação paralela, onde o resultado depende da ordem em que as operações são realizadas.

Aqui está outra situação problemática que pode acontecer quando múltiplos drones executam o mesmo código simultaneamente na mesma posição.
`if get_water() < 0.5:
    use_item(Items.Water)`

Se múltiplos drones executarem isso simultaneamente, todos eles executarão a primeira linha, que os coloca no bloco `if`. Então, todos usarão água, desperdiçando uma grande quantidade dela.
Quando um drone chegar à segunda linha, `get_water()` pode já não ser menor que `0.5` porque outro drone já irrigou o bloco nesse meio tempo.

## Comunicação entre Drones
Se você estiver interessado em estratégias mais avançadas, pode querer que seus drones se comuniquem entre si usando funções de passagem de mensagem.

Envie qualquer valor para outro drone:
`send(data, receiver_drone_id)`

Receba o próximo valor enviado por qualquer drone:
`data = receive()`

Receba o próximo valor enviado por um drone específico:
`data = receive(sender_drone_id)`

O tempo de execução de `send()` depende do tamanho dos dados enviados. Por exemplo, enviar um grande dictionary requer cópia, o que pode demorar um pouco.

`receive()` não espera por uma mensagem chegar. Se nenhuma mensagem tiver sido enviada ainda, retornará `None`.

Você pode criar uma função que espera por uma mensagem assim:
`def blocking_receive(sender_drone_id = -1):
    while True:
        data = receive(sender_drone_id)
        if data != None:
            return data`

Uma aplicação útil de passar mensagens é ter uma função que gera um drone e envia-lhe uma função para executar.
Em um arquivo chamado `drone_spawning`:
`def run_on_new_drone(f):
    id = spawn_drone("drone_spawning")
    send(f, id)

if __name__ == "__main__":
    f = blocking_receive()
    f()`

Enviar funções assim pode ser muito lento porque todo o estado capturado da função, incluindo todas as variáveis globais, deve ser copiado.