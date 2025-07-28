# Importar
Colocar todo o teu código num único ficheiro torna-se rapidamente incontrolável.
As declarações `import` permitem-te importar funções e variáveis globais de outro ficheiro.

`import nome_do_ficheiro`

Esta é a forma mais simples de uma declaração de importação. Dar-te-á acesso a tudo o que está definido no ficheiro chamado `nome_do_ficheiro`. Cada janela no jogo é um ficheiro, e o nome do ficheiro é o nome exibido no topo da janela.

Aqui está um exemplo com dois ficheiros:
Ficheiro chamado helper:
`x = 0

def say_hello():
    print("olá do helper")`

Outro ficheiro qualquer:
`import helper
helper.say_hello()
helper.x += 1`

Aqui, `import helper` executa o ficheiro chamado `helper` e dá-te acesso a todos os seus globais.
Podes então aceder a variáveis e funções dentro do módulo importado usando o operador `.`. 
Neste exemplo, `helper.say_hello()` chama `say_hello()` dentro do helper e a última linha incrementa a variável global x.

Também podes mover os globais do módulo importado para o scope atual onde a declaração de importação é executada, usando a sintaxe `from`.

`from helper import *`
Importa todos os globais do helper.

ou

`from helper import say_hello`
Importa apenas os globais especificados do helper.

Isto também importa o ficheiro helper, mas em vez de aceder a ele através de uma variável chamada `helper`, desempacota os globais de `helper` e atribui-os diretamente no scope local.

`from helper import say_hello
say_hello()`

Esta forma de importação geralmente não é recomendada porque não funciona bem quando dois ficheiros se importam um ao outro, e podes acidentalmente substituir variáveis no ficheiro que importa devido a colisões de nomes.

# Como funciona na realidade

## TLDR
As importações podem ser bastante pouco intuitivas, mas a maioria dos problemas pode ser evitada usando a sintaxe `import ficheiro` em vez de `from ficheiro import`, e envolvendo tudo o que não é uma definição global em
`if __name__ == "__main__":`

## Efeitos Secundários da Importação
A primeira vez que importas um ficheiro, ele executa o ficheiro inteiro e depois dá-te acesso a todas as variáveis que foram definidas durante a execução.
Se importares o mesmo ficheiro novamente, ele apenas retornará o módulo em cache da primeira vez.

Isto significa que as declarações de importação podem ter efeitos secundários. Se importares um ficheiro que chama `harvest()`, ele irá de facto colher durante a importação. Mas quando o importares novamente, não voltará a colher porque o ficheiro só é executado uma vez.

Existe uma forma de evitar tais efeitos secundários usando a variável `__name__`. Esta é uma variável que é automaticamente definida como `"__main__"` quando um ficheiro é executado diretamente, e como o nome do ficheiro quando um ficheiro é executado através de `import`.
É considerado boa prática colocar qualquer código que não queiras que seja executado quando o ficheiro é importado dentro de um bloco `if __name__ == "__main__":`.

Uma estrutura de ficheiros comum em Python é colocar o código que deve ser executado quando o ficheiro é corrido numa função `main()`. Desta forma, tens uma distinção clara entre variáveis locais (definidas dentro de `main()`) e variáveis globais que podem ser importadas (definidas fora de `main()`).

`uma_variavel_global = "global"

def main():
    uma_variavel_local = "local"
    # faz coisas

if __name__ == "__main__":
    main()`

## Ciclos de Importação
O que acontece se o ficheiro `a` importar o ficheiro `b` e o ficheiro `b` importar o ficheiro `a`?

ficheiro `a`:
`import b
x = 0`

ficheiro `b`:
`import a
def f():
    print(a.x)`

Isto funcionará bem. Digamos que nenhum dos dois ficheiros está carregado ainda, e alguém executa `import a`.

-`a` é executado até à linha `import b`.
-`b` é executado até à linha `import a`.
-O módulo `a` já existe, mas não contém `x` porque só chegou à linha `import b`.
-`b` guarda uma referência ao módulo `a` meio carregado numa variável chamada `a`.
-`b` executa a declaração `def` e guarda a função `f()`.
-`a` continua a ser executado e inicializa `x`.

Quando alguém chama `b.f()`, irá imprimir `0` corretamente porque o módulo `a` ao qual `b` tem uma referência está agora totalmente carregado.

Agora considera o mesmo código usando a sintaxe `from`.

ficheiro `a`:
`from b import *
x = 0`

ficheiro `b`:
`from a import *
def f():
    print(x)`

-`a` é executado até à linha `from b import *`.
-`b` é executado até à linha `from a import *`.
-O módulo `a` já existe, mas ainda não foi totalmente executado.
-`b` desempacota tudo o que está atualmente em `a` para o seu próprio scope global. Neste ponto, `a` não contém nada porque ainda não chegou à linha `x = 0`, por isso nada é importado.
-`b` executa a declaração `def` e guarda a função `f()`.
-`a` continua a ser executado e inicializa `x`.

Se alguém chamar agora `b.f()`, receberá um erro a dizer que `x` não existe no scope atual. Isto acontece porque desta vez `b` não tem uma referência ao `a` que ainda está a carregar e não vê as definições que foram adicionadas após a importação.