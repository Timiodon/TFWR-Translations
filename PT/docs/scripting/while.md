[<- Primeiro Programa](docs/first_program.md) <right>[Melhoria de Velocidade ->](docs/unlocks/speed.md)
---
# Loop While
Você desbloqueou o loop `while` e os valores `True` e `False`. O loop `while` continua executando o corpo do loop enquanto a condição for `True`.

`while condition:
	#corpo do loop`

Não se preocupe em criar loops infinitos. O drone pode ficar preso, mas o jogo inteiro não vai travar: basta parar o programa e tentar novamente.

## Para Iniciantes
Talvez você já tenha tentado colocar várias chamadas `harvest()` em sequência:

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
harvest()
harvest()
harvest()
}}
Isso permite que você colha várias vezes em uma única execução do programa. 
No entanto, seria bom colher mais de três vezes, e escrever o mesmo código várias vezes rapidamente deixa o programa uma bagunça.
A solução é um loop. 
Um loop permite que você execute o mesmo código várias vezes.

O loop while recebe uma condição, que é um valor lógico que só pode estar em um de dois estados: `True` ou `False`. 
Tal valor é chamado de valor Booleano.

O loop então executa o código dentro do loop até que a condição seja False.
O loop while se parece com isto:

`while condition:
	#corpo do loop
	#corpo do loop
	#...`
	
Onde você tem que substituir "condition" por um valor booleano e `#corpo do loop` com o que você quiser fazer no loop.

Existem dois valores booleanos constantes disponíveis. Constantes são valores que nunca mudam durante o programa.

Para criar um valor booleano constante, basta escrever `True` ou `False`.
Então você pode escrever

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while False:
	do_a_flip()
}}
ou

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	do_a_flip()
}}
O primeiro nunca dará uma cambalhota, e o segundo dará cambalhotas para sempre (um loop infinito).

Normalmente, criar um loop infinito é uma má ideia porque ele trava o programa. Neste jogo, porém, há pausas entre as iterações, então o drone continuará dando cambalhotas até você interrompê-lo manualmente pressionando o botão Executar outra vez.

Observe que a linha depois dos dois-pontos está recuada. Esse tipo de indentação é usado para separar blocos de código.
Basta pressionar Tab para adicionar indentação e Shift + Tab (ou Backspace) para removê-la. Se várias linhas estiverem selecionadas, Tab e Shift + Tab serão aplicados a todas elas.

Observação: se você estiver jogando pela Steam, pressionar Shift + Tab abrirá a sobreposição da Steam. Você pode redefinir o atalho para remover a indentação nas opções do jogo ou o atalho da sobreposição nas opções da Steam.

Aqui, `do_a_flip()` e `pet_the_piggy()` são chamados repetidamente porque estão dentro do bloco `while` indentado. Porém, `harvest()` nunca é executado porque vem depois desse bloco.
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	do_a_flip()
	pet_the_piggy()
harvest()
}}

---

[Loop For](docs/scripting/for.md)      [If](docs/scripting/if.md)      [Break](docs/scripting/break.md)      [Continue](docs/scripting/continue.md)      [Editor Externo](docs/external_editor.md)
