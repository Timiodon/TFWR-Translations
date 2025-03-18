# Importação
Colocar todo o seu código em um único arquivo rapidamente se torna caótico.
As instruções `import` permitem que você importe funções e variáveis globais de outro arquivo.

`import filename`

Esta é a forma mais simples de instrução de importação. Ela te dará acesso a tudo que está definido no arquivo chamado `filename`. Cada janela no jogo é um arquivo, e o nome do arquivo é o nome exibido no topo da janela.

Aqui está um exemplo com dois arquivos:
Arquivo chamado helper:
`x = 0

def say_hello():
    print("hello from helper")`

Algum outro arquivo:
`import helper
helper.say_hello()
helper.x += 1`

Aqui `import helper` executa o arquivo chamado `helper` e te dá acesso a todas as suas globais.
Você pode então acessar variáveis e funções no módulo importado usando o operador `.`.
Então, neste exemplo, `helper.say_hello()` chama `say_hello()` dentro do helper e a última linha incrementa a variável global x.

Você também pode mover as globais do módulo importado para o escopo atual onde o comando de importação é executado usando a sintaxe `from`.

`from helper import *`
Importa todas as globais do helper.

ou

`from helper import say_hello`
Importa apenas as globais especificadas de helper.

Isso também importa o arquivo helper, mas em vez de acessá-lo através de uma variável chamada `helper`, ele desempacota as globais de `helper` e as atribui diretamente no escopo local.

`from helper import say_hello
say_hello()`

Essa forma de importação geralmente não é recomendada porque não funciona bem quando dois arquivos se importam mutuamente, e você pode acidentalmente sobrescrever variáveis no arquivo que está importando devido a colisões de nomes.

# Como realmente funciona

## TLDR
Importações podem ser bem não intuitivas, mas a maioria dos problemas pode ser evitada seguindo a sintaxe `import file` em vez de `from file import`, e envolvendo tudo que não é uma definição global em
`if __name__ == "__main__":`

## Efeitos colaterais de Import
Na primeira vez que você importa um arquivo, ele executará o arquivo inteiro e então te dará acesso a todas as variáveis que foram definidas durante a execução.
Se você importar o mesmo arquivo novamente, ele apenas retornará o módulo armazenado em cache da primeira vez.

Isso significa que as instruções de importação podem ter efeitos colaterais. Se você importar um arquivo que chama `harvest()`, ele realmente irá colher durante a importação. Mas quando você o importa novamente, ele não irá colher novamente porque o arquivo é executado apenas uma vez.

Há uma maneira de evitar esses efeitos colaterais usando a variável `__name__`. Esta é uma variável que é automaticamente definida como "__main__" quando um arquivo é executado diretamente e para o nome do arquivo quando ele é executado através do `import`.
É considerado uma boa prática colocar qualquer código que você não quer que seja executado quando o arquivo é importado dentro de um bloco `if __name__ == "__main__":`.

Uma estrutura comum de arquivos em Python é colocar o código que deve ser executado quando o arquivo é executado em uma função `main()`. Dessa forma, você tem uma distinção clara entre variáveis locais (definidas dentro de `main()`) e variáveis globais que podem ser importadas (definidas fora de `main()`).

`a_global_variable = "global"

def main():
    a_local_variable = "local"
    # fazer coisas

if __name__ == "__main__":
    main()`

## Ciclos de Importação
O que acontece se o arquivo `a` importa o arquivo `b` e o arquivo `b` importa o arquivo `a`?

arquivo `a`:
`import b
x = 0`

arquivo `b`:
`import a
def f():
    print(a.x)`

Isso funcionará bem. Digamos que nenhum dos dois arquivos estejam carregados ainda, e alguém executa `import a`.

-`a` executa até a linha `import b`.
-`b` executa até a linha `import a`.
-O módulo `a` já existe, mas não contém `x` porque só chegou até a linha `import b`.
-`b` armazena uma referência para o módulo meio carregado `a` em uma variável chamada `a`.
-`b` executa a declaração `def` e armazena a função `f()`.
-`a` continua a execução e inicializa `x`.

Quando alguém chama `b.f()`, ele imprimirá corretamente `0` porque o módulo `a` para o qual `b` tem uma referência agora está totalmente carregado.

Agora considere o mesmo código usando a sintaxe `from`.

arquivo `a`:
`from b import *
x = 0`

arquivo `b`:
`from a import *
def f():
    print(x)`

-`a` executa até a linha `from b import *`.
-`b` executa até a linha `from a import *`.
-O módulo `a` já existe, mas ainda não foi totalmente executado.
-`b` desempacota tudo que está atualmente em `a` em seu próprio escopo global. Neste ponto, `a` não contém nada porque ainda não chegou na linha `x = 0`, então nada é importado.
-`b` executa a declaração `def` e armazena a função `f()`.
-`a` continua a execução e inicializa `x`.

Se alguém agora chamar `b.f()`, eles receberão um erro que `x` não existe no escopo atual. Isso porque desta vez `b` não tem uma referência para o ainda carregando `a` e não vê definições que foram adicionadas após a importação.