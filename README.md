# teste-topaz

$ cd teste-topaz
$ python main.py input.txt

input.txt:

    4
    2
    1
    3
    0
    1
    0
    1

output.txt:

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