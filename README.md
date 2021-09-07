# teste-topaz

Para executar, após clonar o diretório como o comando _git clone https://github.com/dg-veiga/teste-topaz.git_ basta entrar na pasta e executar o python com o nome do script .py e passar como argumento o nome do arquivo de input presente no mesmo diretório (input.txt):

    $ git clone https://github.com/dg-veiga/teste-topaz.git
    $ cd teste-topaz
    $ python main.py input.txt

Arquivo de input, input.txt:

    4
    2
    1
    3
    0
    1
    0
    1

Arquivo de saída, output.txt:

    1
    2,2
    2,2
    2,2,1
    1,2,1
    2
    2
    1
    1
    0
    15

Prints da execução do script:

    {'Tick': 1, 'Input': 1, 'Ttasks': [[4]]}
    {'Tick': 2, 'Input': 3, 'Ttasks': [[3, 4], [4, 4]]}
    {'Tick': 3, 'Input': 0, 'Ttasks': [[2, 3], [3, 3]]}
    {'Tick': 4, 'Input': 1, 'Ttasks': [[1, 2], [2, 2], [4]]}
    {'Tick': 5, 'Input': 0, 'Ttasks': [[1], [1, 1], [3]]}
    {'Tick': 6, 'Input': 1, 'Ttasks': [[2, 4]]}
    {'Tick': 7, 'Input': '-', 'Ttasks': [[1, 3]]}
    {'Tick': 8, 'Input': '-', 'Ttasks': [[2]]}
    {'Tick': 9, 'Input': '-', 'Ttasks': [[1]]}
    {'Tick': 10, 'Input': '-', 'Ttasks': []}

Representação dos valores dos dicts acima:

- Tick: momento da execução
- Input: novos usuários entrando no exato momento
- Ttasks: cada array dentro do array mestre representa um server, e dentro de cada server estão os valores em ticks restantes para a conclusão das tarefas de cada usuário presente no server.