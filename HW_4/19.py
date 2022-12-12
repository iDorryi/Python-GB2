# 4'. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# # Пример:
# # k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
# # k=3 => 2*x*3 + 4*x*2 + 4*x + 5 = 0 5'. 

import sympy
import random
# from random import randint as rnd
def get_polinom(k: int, simple: bool = True) -> str:
    polinom = ''
    for i in range(k, -1, -1):
        polinom += f'{random.randrange(0,100)}*x**{i}+'
        if i == 0:
            polinom += f'{random.randrange(0,100)}*x**{i}'
    if simple:
        return str(sympy.simplify(polinom))
    else:
        return str(polinom)

def create_file(polinom: str, filename: str = "file"):
    # f = open('file.txt','w')
    with open('file.txt','w') as f:
        f.write(polinom)
k = int(input("Введите степень: "))

print(f'Сгенерированный полином {get_polinom(k)}')
create_file(get_polinom(k))

