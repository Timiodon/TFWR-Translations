# Import
Colocar todo o seu código em um único arquivo rapidamente se torna incontrolável. 
As declarações `import` permitem que você importe funções e variáveis globais de outro arquivo.

`import filename`

Esta é a forma mais simples de declaração de importação. Ela lhe dará acesso a tudo o que for definido no arquivo chamado `filename`. Cada janela no jogo é um arquivo, e o nome do arquivo é o nome exibido no topo da janela.

Aqui está um exemplo com dois arquivos:
Arquivo chamado helper:
`x = 0

def say_hello():
    print("olá do helper")`

Algum outro arquivo:
`import helper
helper.say_hello()
helper.x += 1`

Aqui `import helper` executa o arquivo chamado `helper` e lhe dá acesso a todas as suas variáveis globais.
Você pode então acessar variáveis e funções dentro do módulo importado usando o operador `.`. 
Então, neste exemplo, `helper.say_hello()` chama `say_hello()` dentro do helper e a última linha incrementa a variável global x.

Você também pode mover as variáveis globais do módulo importado para o escopo atual onde a declaração de importação é executada usando a sintaxe `from`.

`from helper import *`
Importa todas as variáveis globais de helper.

ou

`from helper import say_hello`
Importa apenas as variáveis globais especificadas de helper.

Isso também importa o arquivo helper, mas em vez de acessá-lo através de uma variável chamada `helper`, ele desempacota as variáveis globais de `helper` e as atribui diretamente no escopo local.

`from helper import say_hello
say_hello()`

Esta forma de importação geralmente não é recomendada porque não funciona bem quando dois arquivos se importam mutuamente, e você pode acidentalmente sobrescrever variáveis no arquivo importador devido a colisões de nomes.

# Como realmente funciona

## TLDR
Importações podem ser bastante contraintuitivas, mas a maioria dos problemas pode ser evitada usando a sintaxe `import file` em vez de `from file import`, e envolvendo tudo o que não é uma definição global em
`if __name__ == "__main__":`

## Efeitos Colaterais da Importação
A primeira vez que você importa um arquivo, ele executará o arquivo inteiro e então lhe dará acesso a todas as variáveis que foram definidas durante a execução.
Se você importar o mesmo arquivo novamente, ele apenas retornará o módulo em cache da primeira vez.

Isso significa que as declarações de importação podem ter efeitos colaterais. Se você importar um arquivo que chama `harvest()`, ele realmente colherá durante a importação. Mas quando você o importar novamente, ele não colherá novamente porque o arquivo é executado apenas uma vez.

Existe uma maneira de evitar tais efeitos colaterais usando a variável `__name__`. Esta é uma variável que é automaticamente definida como `"__main__"` quando um arquivo é executado diretamente, и para o nome do arquivo quando um arquivo é executado através de `import`.
É considerado uma boa prática colocar qualquer código que você não queira que seja executado quando o arquivo é importado dentro de um bloco `if __name__ == "__main__":`.

Uma estrutura de arquivo comum em Python é colocar o código que deve ser executado quando o arquivo é executado em uma função `main()`. Desta forma, você tem uma distinção clara entre variáveis locais (definidas dentro de `main()`) e variáveis globais que podem ser importadas (definidas fora de `main()`).

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

Isso funcionará bem. Digamos que nenhum dos dois arquivos esteja carregado ainda, e alguém executa `import a`.

-`a` executa até a linha `import b`.
-`b` executa até a linha `import a`.
-O módulo `a` já existe, mas não contém `x` porque só atingiu a linha `import b`.
-`b` armazena uma referência ao módulo `a` meio carregado em uma variável chamada `a`.
-`b` executa a declaração `def` e armazena a função `f()`.
-`a` continua a executar e inicializa `x`.

Quando alguém chama `b.f()`, ele imprimirá corretamente `0` porque o módulo `a` ao qual `b` tem uma referência agora está totalmente carregado.

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
-`b` desempacota tudo o que está atualmente em `a` para seu próprio escopo global. Neste ponto, `a` não contém nada porque ainda não atingiu a linha `x = 0`, então nada é importado.
-`b` executa a declaração `def` e armazena a função `f()`.
-`a` continua a executar e inicializa `x`.

Se alguém agora chamar `b.f()`, receberá um erro de que `x` não existe no escopo atual. Isso ocorre porque desta vez `b` não tem uma referência ao `a` ainda em carregamento e não vê as definições que foram adicionadas após a importação.