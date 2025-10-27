# Megafazenda
Este desbloqueio incrivelmente poderoso lhe dá acesso a vários drones. 

Como antes, você ainda começa com apenas um drone. Drones adicionais devem primeiro ser gerados e desaparecerão após o término do programa.
Cada drone executa seu próprio programa separado. Novos drones podem ser gerados usando a função `spawn_drone(function)`.

`def drone_function():
    move(North)
    do_a_flip()

spawn_drone(drone_function)`

Isso gera um novo drone na mesma posição que o drone que executou o comando `spawn_drone(function)`. O novo drone então começa a executar a função especificada. Depois de terminar, ele desaparecerá automaticamente.

Drones não colidem entre si. 

Use `max_drones()` para obter o número máximo de drones que podem existir simultaneamente.
Use `num_drones()` para obter o número de drones que já estão na fazenda.


## Exemplo:
`def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)`

Isso fará com que seu primeiro drone se mova horizontalmente e gere mais drones. Os drones gerados se moverão verticalmente e colherão tudo em seu caminho.

Se todos os drones disponíveis já tiverem sido gerados, `spawn_drone()` não fará nada e retornará `None`.

Aqui está outro exemplo que passa uma direção diferente para cada drone.
`for dir in [North, East, South, West]:
    def task():
        move(dir)
        do_a_flip()
    spawn_drone(task)`

<spoiler=show hint> Confira esta função paralela super útil `for_all`, que pega qualquer função e a executa em cada casa da fazenda. Ela utiliza todos os drones disponíveis para fazer isso.

`def for_all(f):
	def row():
		for _ in range(get_world_size()-1):
			f()
			move(East)
		f()
	for _ in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(North)

for_all(harvest)`

Um padrão particularmente útil é gerar um drone se houver um disponível e, caso contrário, fazer você mesmo.

`if not spawn_drone(task):
	task()`
</spoiler>

## Aguardando Outro Drone
Use a função `wait_for(drone)` para esperar que outro drone termine. Você recebe o handle `drone` quando gera o drone.
`wait_for(drone)` retorna o valor de retorno da função que o outro drone estava executando.

`def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

def zero_arg_wrapper():
    return get_entity_type_in_direction(North)
drone = spawn_drone(zero_arg_wrapper)
print(wait_for(drone))`

Note que gerar drones leva tempo, então não é uma boa ideia gerar um novo drone para cada pequena coisa.

Você pode usar `has_finished(drone)` para ver se o drone terminou sem precisar esperar.

## Sem Memória Compartilhada
Cada drone tem sua própria memória e não pode ler ou escrever diretamente as variáveis globais de outro drone.

`x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)`

Isso imprimirá `0` porque o novo drone incrementou sua própria cópia do `x` global, o que não afeta o `x` do primeiro drone.

## Condições de Corrida
Vários drones podem interagir com a mesma casa da fazenda ao mesmo tempo. Se dois drones interagirem com a mesma casa durante o mesmo tick, ambas as interações ocorrerão, mas os resultados podem diferir com base na ordem das interações.

Por exemplo, imagine que os drones `0` e `1` estão ambos sobre a mesma árvore que está quase totalmente crescida.
O drone `0` chama
`use_item(Items.Fertilizer)`
O drone `1` chama
`harvest()`

Se essas ações ocorrerem ao mesmo tempo, a árvore será primeiro fertilizada e depois colhida. Nesse caso, você receberá madeira dela. No entanto, se o Drone `1` for um pouco mais rápido, a árvore será colhida antes de ser fertilizada, e você não receberá a madeira.
Isso é chamado de "condição de corrida". É um problema comum em programação paralela, onde o resultado depende da ordem em que as operações são realizadas.

Aqui está outra situação problemática que pode acontecer quando vários drones executam o mesmo código simultaneamente na mesma posição.
`if get_water() < 0.5:
    use_item(Items.Water)`

Se vários drones executarem isso simultaneamente, todos eles executarão a primeira linha, o que os coloca no bloco `if`. Então, todos eles usarão água, desperdiçando muita dela.
No momento em que um drone chega à segunda linha, `get_water()` pode não ser mais menor que `0.5` porque outro drone já regou a casa nesse meio tempo.